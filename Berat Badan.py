import pandas as pd
from scipy import stats
df=pd.read_csv("Berat.csv",usecols=[0])

print("jumlah data  ",df['NilaiPreTest'].count())
print("rata-rata   ",df['NilaiPreTest'].mean())
print("nila minimal ",df['NilaiPreTest'].min())
print("Q1       ",df['NilaiPreTest'].quantile(0.25))
print("Q2          ",df['NilaiPreTest'].quantile(0.5))
print("Q3          ",df['NilaiPreTest'].quantile(0.75))
print("Nilai Max   ",df['NilaiPreTest'].max())
print("kemencengan","{0:.2f}".format(round(df['NilaiPreTest'].skew(),2)))
mode=stats.mode(df)
print("Nilai modus {} dengan jumlah {}".format(mode.mode[0], mode.count[0]))
print("kemencengan          " ,"{0:.6f}".format(round(df['NilaiPreTest'].skew(),6)))
print("Standar Deviasi   ","{0:.2f}".format(round(df['NilaiPreTest'].std(),2)))
print("Variansi         ","{0:.2f}".format(round(df['NilaiPreTest'].var(),2)))