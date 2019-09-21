#!/usr/bin/env python
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
    return parser.parse_args()



if __name__ == '__main__':
    args = GET_ARGS()
    fasta_in = args.fasta
    query_in = args.group


    print(fasta_in)
    print(query_in)


    for q in open(query_in, "r"):
        query = re.split('[\t ,]',q)
        os.mkdir(query[0])
        os.chdir("./"+query[0])
        
        f = open(query[0] +".fa", 'w')
        print("<" + query[0]+ ">")
        for record in SeqIO.parse("../" + fasta_in, 'fasta'):
            id_part = record.id
            desc_part = record.description
            seq = record.seq
            for i in range(len(query)):
                if desc_part == query[i] :
                    seq_m=str(seq).replace("*", "")
                    seq_m=seq_m.replace(".", "")
                    fasta_seq = '>' + desc_part + '\n' + seq_m + '\n'
                    print(desc_part)
                    f.write(str(fasta_seq))
        f.close()
        subprocess.run("prequal "+query[0] + ".fa", shell=True)
        subprocess.run("mafft --auto " +query[0]+".fa.filtered"+" > "+query[0]+".fa.filtered.maffted.fa", shell=True) 
        subprocess.run("mafft --auto " +query[0]+".fa" + " > "+query[0]+".trimal.fa", shell=True)
        subprocess.run("trimal -in " +query[0]+".trimal.fa -out " +  query[0]+".trimal.maffted.fa -htmlout " + query[0]+".trimal.maffted.html  -automated1", shell=True)
        subprocess.run("iqtree -nt AUTO -bb 1000  -pre \"prequel\" -s " + query[0]+".fa.filtered.maffted.fa", shell=True)
        subprocess.run("iqtree -nt AUTO -bb 1000  -pre \"trimal\" -s " + query[0]+".trimal.maffted.fa", shell=True)
        os.chdir("../")
