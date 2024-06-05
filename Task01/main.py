import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sbn

data1 = pd.read_csv("./world-bank-data/API_SP.POP.TOTL_DS2_en_csv_v2_144171.csv", skiprows=4)
# data2 = pd.read_csv("./world-bank-data/Metadata_Country_API_SP.POP.TOTL_DS2_en_csv_v2_144171.csv")

x = data2['IncomeGroup']
y = data2['Region']

plt.title("Regionwise Income Group")
plt.xlabel("Income Group")
plt.ylabel("Region")

plt.bar(x, y)