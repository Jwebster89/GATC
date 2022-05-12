#!/usr/bin/env python3

import argparse, csv, os
import pandas as pd

from version import __versioncp__
from gatc import read_vcf

pd.options.mode.chained_assignment = None

def tb_it_parse(input,d):
    df=pd.read_csv(input, sep='\t')
    dft=df.T
    dft.rename(columns=dft.iloc[0], inplace = True)
    dft.drop(dft.index[0], inplace = True)
    dft.columns= dft.columns.str.lower()
    keys=list(d.keys())
    data=dft[dft.columns.intersection(keys)]
    data.rename(columns=d, inplace = True)
    data.replace('./.','00', inplace = True)
    data.dropna(inplace = True)
    return(data)

def tb_conv(df):
    positions=["ID"]
    tb=[]
    for column in df.columns:
        positions.append(column)
        positions.append(column)
    for index, row in df.iterrows():
        calls=[]
        calls.append(index)
        for item in row.tolist():
            for l in str(item):
                if l == 'A':
                    calls.append(1)
                elif l == 'B':
                    calls.append(2)
                else:
                    calls.append(0)
        tb.append(calls)
    with open('output_cp.csv', 'w') as fh_out:
        tsv_output=csv.writer(fh_out)
        tsv_output.writerow(positions)
        tsv_output.writerows(tb)

def merge_with_cp(cp):
    if cp:
        cp_res=pd.read_csv(cp)
        tb_df=pd.read_csv('output_cp.csv')
        result=pd.concat([tb_df,cp_res])
        result.to_csv('cp_concat.csv',index=False)

def run_cp(input,vcf,cp):
    d=read_vcf(vcf)
    df=tb_it_parse(input,d)
    tb=tb_conv(df)
    merge_with_cp(cp)

def main():
    description=f"""
    GATC: Ion Torrent Topbot data for GATC. \n
    Version: {__versioncp__}"""
    parser = argparse.ArgumentParser(description=description,formatter_class=argparse.RawTextHelpFormatter, add_help=False)

    required = parser.add_argument_group('Required Arguments')
    required.add_argument("-i", "--input", help="Input data from IonTorrent in topbot format")
    required.add_argument("-v", "--vcf", help="VCF of loci to extract from 50k")

    optional = parser.add_argument_group('Optional Arguments')
    optional.add_argument("-c", "--cervus_parse", help="if a previous cervus_parse output is given, GATC will add the 50k results to it")
    optional.add_argument("-h", "--help", action="help", help="show this help message and exit")

    args=parser.parse_args()
    input=args.input
    vcf=args.vcf
    cp=args.cervus_parse

    run_cp(input,vcf,cp)

if __name__ == '__main__':
    main()
