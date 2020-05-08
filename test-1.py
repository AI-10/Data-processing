import requests
import csv

f = open('数据.csv', 'a+', encoding='utf-8', newline='')

csv_writer = csv.writer(f)
csv_writer.writerow(
    ["chrom", "pos", "ref", "alt", "rsids", "nearest_genes", "pval", "beta", "sebeta", "af", "ac", "tstat",
     "num_significant_in_peak", "peak"])

url = 'http://pheweb.sph.umich.edu/SAIGE-UKB/api/manhattan/pheno/427.2.json'

result = requests.get(url).json()
for ii in result['unbinned_variants']:
    print(ii)
    try:
        num_significant_in_peak = ii['num_significant_in_peak']
    except:
        num_significant_in_peak = ""
    try:
        peak = ii['peak']
    except:
        peak = ""
    csv_writer.writerow(
        [ii["chrom"], ii["pos"], ii["ref"], ii["alt"], ii["rsids"], ii["nearest_genes"], ii["pval"], ii["beta"],
         ii["sebeta"], ii["af"], ii["ac"], ii["tstat"], num_significant_in_peak, peak])
