#!/usr/bin/env python3
# coding: UTF-8

# 
# ======================================================================
# Project Name    : PhyHat
# File Name       : phyhat.py
# Version       : 1.0.0
# Encoding        : python
# Creation Date   : 2019/09/1
# Author : Taro Maeda 
# license     MIT License (http://opensource.org/licenses/mit-license.php)
# Copyright (c) 2019 Taro Maeda
# ======================================================================
# 





import argparse
from Bio import SeqIO
import subprocess
import re
import os


def GET_ARGS():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f','--fasta',  help="File path to a fasta including all species sequence", required=True)
    parser.add_argument('-d','--group', help="Ortholog grouping file", required=True)
    parser.add_argument('-n','--name',help="Species name in order (Space-separated)", type=str, required=True)
    return parser.parse_args()



if __name__ == '__main__':
    args = GET_ARGS()
    fasta_in = args.fasta
    query_in = args.group
    sp = args.name
    sp_list = sp.split()

    print(fasta_in)
    print(query_in)
    print(sp_list)

    fnex = open("iqtree.run.nex", 'w')
    fnex.write("#nexus \n begin sets;\n")

    for q in open(query_in, "r"):
        query = q.split()
        QUERY = query[0].replace("|", "_")
        if not os.path.exists(QUERY):
            os.mkdir(QUERY)
        os.chdir("./"+QUERY)
        f = open(QUERY + ".fa", 'w')
        print("<" + QUERY+ ">")
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
        print("<OTU rename>")
        fsp = open(QUERY+ ".sp.fa", 'w')
        for record in SeqIO.parse("../" +fasta_in, 'fasta'):
            id_part = record.id
            desc_part = record.description
            seq = record.seq
            for i in range(len(query)):
                if desc_part == query[i] :
                    print(sp_list[i-1])
                    fasta_seq = '>' + sp_list[i-1] + '\n' + seq.rstrip("*") + '\n'
                    fsp.write(str(fasta_seq))
        fsp.close()
        subprocess.run("prequal "+QUERY + ".sp.fa", shell=True)
        subprocess.run("mafft --auto "+QUERY+".sp.fa.filtered"+" > "+QUERY+".sp.fa.filtered.maffted.fa", shell=True)
        os.chdir("../")
        fnex.write("charset "+QUERY+" = "+ QUERY +"/" + QUERY+".sp.fa.filtered.maffted.fa: ; \n ")
    fnex.write("end;")
    fnex.close()

    subprocess.run("iqtree -sp iqtree.run.nex -nt AUTO -bb 1000", shell=True)