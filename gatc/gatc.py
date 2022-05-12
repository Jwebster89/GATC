#!/usr/bin/env python3

import argparse, csv, os
import pandas as pd

def read_vcf(vcf):
    df=pd.read_csv(vcf, sep='\t')
    d=dict(zip(df['Allele Name'].str.lower(), df.Position))
    return(d)

def read_50k(input,d):
    df2=pd.read_csv(input,sep='\t',skiprows=9)
    ID=df2.iloc[1,1]
    data=[]
    for index, row in df2.iterrows():
        try:
            data.append([d[row['SNP Name'].lower()],row['Allele1 - AB'],row['Allele2 - AB']])
        except KeyError:
            continue
    return(data,ID)

def create_output(data,ID,cp):
    positions = ["ID"]
    calls=[ID]
    for item in data:
        positions.append(item[0])
        positions.append(item[0])
    for item in data:
        if item[1]=='A':
            calls.append('1')
        elif item[1]=='B':
            calls.append('2')
        else:
            calls.append('0')
        if item[2]=='A':
            calls.append('1')
        elif item[2]=='B':
            calls.append('2')
        else:
            calls.append('0')
    with open('output.tsv', 'w') as fh_out:
        tsv_output=csv.writer(fh_out,delimiter="\t")
        tsv_output.writerow(positions)
        tsv_output.writerow(calls)

def merge_with_cp(cp):
    if cp:
        array_res=pd.read_csv('output.tsv',sep='\t')
        cp_res=pd.read_csv(cp)
        result=pd.concat([array_res,cp_res])
        result.to_csv('gatc_parse.csv',index=False)

def gatc_run(d,input,cp):
    data,ID=read_50k(input,d)
    create_output(data,ID,cp)
    merge_with_cp(cp)
