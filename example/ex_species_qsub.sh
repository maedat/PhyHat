#!/bin/bash
#PBS -S /bin/bash
#PBS -V
#PBS -l ncpus=40


cd ${PBS_O_WORKDIR}   ## instead of "#$ -cwd" 



../phyhat.py -f ex_species.fa -d ex_species.db -n "SpA SpB SpC SpD SpE"