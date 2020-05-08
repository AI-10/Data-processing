import numpy as np
import pandas as pd 
import requests

url = input()
result = requests.get(url).json()

print(len(result),result.keys())
result_variant_bins = pd.DataFrame(result['variant_bins'])
result_unbinned_variants = pd.DataFrame(result['unbinned_variants'])

with pd.ExcelWriter(r"C:\Users\acer\Desktop\result.xlsx") as writer:
    result_variant_bins.to_excel(writer,sheet_name = "result_variant_bins")
    result_unbinned_variants.to_excel(writer,sheet_name ="result_unbinned_variants")