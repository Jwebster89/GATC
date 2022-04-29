# GATC: Genotype Array To Cervus

converts 50k data to input for cervus

## Requirements
* Python3
* pandas

## Installation
git clone https://github.com/Jwebster89/GATC.git

## Quick Usage
GATC can be run as follows using the final report from a 50k Array and a VCF file that describes your panel for a single sample
`./gatc_runner -v VCF_FILE -i GENO_ARRAY_REPORT -c CERVUS_PARSE_TABLE`

## Options and Usage
```
usage: gatc_runner.py [-i INPUT] [-v VCF] [-c CERVUS_PARSE] [-h]

    GATC: Genotype Array To Cervus. A parsing software to convert 50k reports into a format for cervus

    Version: 1.0.0

Required Arguments:
  -i INPUT, --input INPUT
                        50k Final Report input file
  -v VCF, --vcf VCF     VCF of loci to extract from 50k

Optional Arguments:
  -c CERVUS_PARSE, --cervus_parse CERVUS_PARSE
                        if a previous cervus_parse output is given, GATC will add the 50k results to it
  -h, --help            show this help message and exit
```
