#!/usr/bin/env python3

import argparse, os

from gatc.version import __version__
from gatc.gatc import gatc_run,read_vcf
# from gatc.cervus_parse_tb import run_cp

def main():
    description=f"""
    GATC: Genotype Array To Cervus. A parsing software to convert 50k reports into a format for cervus \n
    Version: {__version__}"""
    parser = argparse.ArgumentParser(description=description,formatter_class=argparse.RawTextHelpFormatter, add_help=False)

    required = parser.add_argument_group('Required Arguments')
    required.add_argument("-i", "--input", help="50k Final Report input file")
    required.add_argument("-v", "--vcf", help="VCF of loci to extract from 50k")

    optional = parser.add_argument_group('Optional Arguments')
    optional.add_argument("-c", "--cervus_parse", help="if a previous cervus_parse output is given, GATC will add the 50k results to it")
    optional.add_argument("-h", "--help", action="help", help="show this help message and exit")
    args=parser.parse_args()
    input=args.input
    vcf=args.vcf
    cp=args.cervus_parse

    d=read_vcf(vcf)
    gatc_run(d,input,cp)

if __name__ == '__main__':
	main()
