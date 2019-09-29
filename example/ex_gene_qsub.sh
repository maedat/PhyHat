#!/bin/bash
#PBS -S /bin/bash
#PBS -V
#PBS -l ncpus=40


cd ${PBS_O_WORKDIR}   ## instead of "#$ -cwd" 



../phyhat_gene.py -f ex_gene.fa -d ex_gene.db -n "SpA SpB SpC SpD SpE"