#!/usr/bin/env python3

import argparse
from gatc.version import __version__
from gatc.gatc import GATC
import os

def main():
    description=f"""
    GATC: Genotype Array To Cervus. A parsing software to convert 50k reports into a format for cervus \n
    Version: {__version__}"""
    parser = argparse.ArgumentParser(description=description,formatter_class=argparse.RawTextHelpFormatter, add_help=False)

    required = parser.add_argument_group('Required Arguments')
    required.add_argument("-i", "--input", help="50k Final Report input file")
    required.add_argument("-v", "--vcf", help="VCF of loci to extract from 50k")
    optional = parser.add_argument_group('Optional Arguments')
    optional.add_argument("-h", "--help", action="help", help="show this help message and exit")

    args=parser.parse_args()
    input=args.input
    vcf=args.vcf

    job=GATC(input,vcf)
    job.gatc_run()

if __name__ == '__main__':
	main()
