#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#python >3.5

import argparse
from Bio import SeqIO
import subprocess
import re
import os

def GET_ARGS():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f','--fasta',  help="File path to a fasta including all species sequence", required=True)
    parser.add_argument('-d','--group', help="Ortholog grouping file", required=True)
    parser.add_argument('-n','--name',help="Species names in order (Space-separated)", type=str, required=False)
    parser.set_defaults(name='NoFile')
    return parser.parse_args()
    
if __name__ == '__main__':
    args = GET_ARGS()
    fasta_in = args.fasta
    query_in = args.group
    sp = args.name
    sp_list = sp.split()
    print("Input fasta; " +fasta_in)
    print("Input data set file; " + query_in)
    print("Spcies name list; " +sp)
    with open(query_in, "r") as fq:
        for q in fq:
            query = re.split('\t',q)        
            QUERY = query[0].replace("|", "_")
            if not os.path.exists(QUERY):
                os.mkdir(QUERY)
            os.chdir("./"+QUERY)
            if sp!="NoFile":
                with open(QUERY +".fa", "w") as f:
                    print("<" + QUERY+ ">")
                    for record in SeqIO.parse("../" + fasta_in, 'fasta'):
                        id_part = record.id
                        desc_part = record.description
                        seq = record.seq
                        for i in range(len(query)-1):
                            sp_name = sp_list[i]
                            query_each = query[i+1].split(',')
                            if len(query_each) !=0:
                                for j in range(len(query_each)):                
                                    if desc_part == query_each[j].rstrip():
                                        seq_m=str(seq).replace("*", "")
                                        seq_m=seq_m.replace(".", "")
                                        fasta_seq = '>' + desc_part + "_("+sp_name+")"+ '\n' + seq_m + '\n'
                                        print(desc_part)
                                        f.write(str(fasta_seq))
            elif sp=="NoFile":
                with open(QUERY +".fa", "w") as f:
                    print("<" + QUERY+ ">")
                    for record in SeqIO.parse("../" + fasta_in, 'fasta'):
                        id_part = record.id
                        desc_part = record.description
                        seq = record.seq
                        for i in range(len(query)+1):
                            query_each = query[i].split(',')
                            for j in range(len(query_each)):                
                                if desc_part == query_each[j]:
                                    seq_m=str(seq).replace("*", "")
                                    seq_m=seq_m.replace(".", "")
                                    fasta_seq = '>' + desc_part + '\n' + seq_m + '\n'
                                    print(desc_part)
                                    f.write(str(fasta_seq))
                            
            subprocess.run("prequal "+QUERY + ".fa", shell=True)
            subprocess.run("mafft --auto " +QUERY+".fa.filtered"+" > "+QUERY+".fa.filtered.maffted.fa", shell=True)
            subprocess.run("mafft --auto " +QUERY+".fa"+ " > "+QUERY+".trimal.fa", shell=True)
            subprocess.run("trimal -in " +QUERY+".trimal.fa -out " +  QUERY+".trimal.maffted.fa -htmlout " + QUERY+".trimal.maffted.html  -automated1", shell=True)
            subprocess.run("iqtree -nt AUTO -bb 1000  -pre \"prequel\" -s " + QUERY+".fa.filtered.maffted.fa", shell=True)
            subprocess.run("iqtree -nt AUTO -bb 1000  -pre \"trimal\" -s " + QUERY+".trimal.maffted.fa", shell=True)
            os.chdir("../")
