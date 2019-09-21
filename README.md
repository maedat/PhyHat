# PhyHat; A pipeline for ML-tree analysis with multiple gene set

====

PhyHat is a pipeline for the ML-tree construction with Mafft aligenment, Prequel ambigouse base masking and Iq-tree tree construction. 

## Requirement
Python 3.7. (Biopython, pandas, argparse, bcbio-gff)

## Usage
```sh
usage: GFF2MSS.py [-h] -f FASTA -g GFF -a ANN -l LOC -n NAM [-s STN] -o OUT
[-m MOL]

optional arguments:
-h, --help            show this help message and exit
-f FASTA, --fasta FASTA
File path to a genome sequence file
-g GFF, --gff GFF     gff3 file for gene modeling
-a ANN, --ann ANN     txt file for gene annotation (header = ID,
Description)
-l LOC, --loc LOC     locus_tag prefix
-n NAM, --nam NAM     organism name
-s STN, --stn STN     strain
-o OUT, --out OUT     output MSS file path
-m MOL, --mol MOL     mol_type value (default = genomic DNA)
```

## Demo
```sh
python3 GFF2MSS.py \
-f example/Lj3.0_Chloroplastl.fna \
-g example/Lj3.0_cp_gene_models.gff3  \
-a example/Lj3.0_anno.txt \
-l "PRE_TEST_" \
-n "Lotus japonicus" \
-s "MG-20" \
-o mss.out.txt 

```
