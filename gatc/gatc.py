#!/usr/bin/env python3
import os,csv
import pandas as pd

class GATC():
        def __init__(self, input, vcf):
                self.input=input
                self.vcf=vcf

        def read_vcf(self, vcf):
            df=pd.read_csv(vcf, sep='\t')
            d=dict(zip(df['Allele Name'].str.lower(), df.Position))
            return(d)

        def read_50k(self,input,d):
            df2=pd.read_csv(input,sep='\t',skiprows=9)
            ID=df2.iloc[1,1]
            data=[]
            for index, row in df2.iterrows():
                try:
                    data.append([d[row['SNP Name'].lower()],row['Allele1 - AB'],row['Allele2 - AB']])
                except KeyError:
                    continue
            return(data,ID)


        def create_output(self,data,ID):
            positions = ["Sample"]
            calls=[ID]
            for item in data:
                positions.append(item[0])
                positions.append(item[0])
            for item in data:
                calls.append(item[1])
                calls.append(item[2])
            with open('output.tsv', 'w') as fh_out:
                tsv_output=csv.writer(fh_out,delimiter="\t")
                tsv_output.writerow(positions)
                tsv_output.writerow(calls)


        def gatc_run(self):
            d=self.read_vcf(self.vcf)
            data,ID=self.read_50k(self.input,d)
            self.create_output(data,ID)

def main():
    gatc_run()

if __name__ == '__main__':
	main()
