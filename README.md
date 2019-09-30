# PhyHat; A pipeline for ML-tree analysis with multiple gene set

====

PhyHat is a pipeline for the ML-tree construction with Mafft aligenment, Prequel ambigouse base masking and Iq-tree tree construction. 

## Requirement
Python 3.7. (Biopython, pandas, argparse)

## Usage
-phyhat.py (for species tree construction from multiple gene set)

- [iptree](http://www.iqtree.org)

- [mafft](https://mafft.cbrc.jp/alignment/software/)

- [PREQUAL](https://github.com/simonwhelan/prequal)

- [trimal](http://trimal.cgenomics.org)

```sh
usage: phyhat.py [-h] -f FASTA -d GROUP -n NAME

optional arguments:
  -h, --help            show this help message and exit
  -f FASTA, --fasta FASTA
                        File path to a fasta including all species sequence
  -d GROUP, --group GROUP
                        Ortholog grouping file
  -n NAME, --name NAME  Species name in order (Space-separated)
```

phyhat_gene.py (for gene tree construction for each homolog group)

```sh
usage: phyhat_gene.py [-h] -f FASTA -d GROUP [-n NAME]

optional arguments:
  -h, --help            show this help message and exit
  -f FASTA, --fasta FASTA
                        File path to a fasta including all species sequence
  -d GROUP, --group GROUP
                        Ortholog grouping file
  -n NAME, --name NAME  Species names in order (Space-separated)
```



## Demo

phyhat.py

```sh
cd ../example 
../phyhat.py -f ex_species.fa -d ex_species.db -n "SpA SpB SpC SpD SpE"

```

phyhat_gene.py

```sh
cd ../example 
../phyhat_gene.py -f ex_gene.fa -d ex_gene.db -n "SpA SpB SpC SpD SpE"

```

## Licence

[MIT License](http://opensource.org/licenses/mit-license.php)

## Author

[Taro Maeda](https://github.com/maedat)
