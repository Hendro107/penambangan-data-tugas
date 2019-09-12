## Distribusi Data

Distribusi data yang paling dikenal adalah distribusi normal atau Gaussian. Distribusi ini ditemukan pada sistem fisik dimana data dibangkitkan secara acak. Distribusi data terbagi menjadi dua, yaitu distribusi tunggal dan distribusi frekuensi.

Distribusi tunggal adalah distribusi dilakukan jika data penelitian bersifat sederhana dan jumlah data yang sedikit. 

Distribusi frekuensi adalah suatu yang menjelaskan frekuensi anggota populasi yang didistribusikan menurut nilai variabel yang diambilnya. Distribusi frekuensi digunakan apabila dipeboleh sekelompok data penelitian yang tidak memugkinkan ;disusun dalam bentuk distribusi tunggal.

### Rata-rata (Mean)

Mean merupakan nilai yang diperoleh dengan menjumlahkan semua nilai data dan membaginya dengan jumlah data. Rumus nilai rata-rata (Mean) adalah :
$$
\mu = \frac{∑X}{N} = \frac{x_1+x_2+...+x_n}{N}
$$
Keterangan :
μ = rata-rata hitung populasi
X = nilai data yang ada dalam populasi
N = jumlah data populasi
∑X = jumlah dari seluruh nilai X

### Median

Median adalah nilai yang letaknya ditengah data yang telah diurutkan, namun datanya belu dikelompokkan ke dalam kelas/ketegori atau belum dalam bentuk distribusi frekuensi. Rumus median adalah :
$$
Me=x_{ij}+\big(\frac{n/2-f_{kij}}{f_i}\big)p
$$
Me = median 
xij = batas bawah median 
n = jumlah data 
fkij = frekuensi kumulatif data di bawah kelas median 
fi = frekuensi data pada kelas median
p = panjang interval kelas

### Modus

Modus adalah suatu nilai pengamat yang paling sering muncul. Rumus meodus adalah :
$$
Modus = tb + \big(\frac{ΔF1}{ΔF1+ΔF2}\big)p
$$
tb = tepi bawah
ΔF1 = frekuensi tertinggi dikurangi frekuensi diatasnya
ΔF2 = frekuensi tertinggi dikurangi frekuensi dibawahnya
p = interval

### Untuk melakukan implementasi menggunakan coding, hasilnya seperti ini :

```
import pandas as pd
from scipy import stats
df=pd.read_csv("Berat.csv",usecols=[0])

print("jumlah data  ",df['NilaiPreTest'].count())
print("rata-rata   ",df['NilaiPreTest'].mean())
print("nilai minimal ",df['NilaiPreTest'].min())
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
```

- "pandas" adalah bahasa pemrograman Python menganalisis data terstruktur.
- "scipy" berfungsi untuk komputasi ilmiah dan komputasi teknik.
- "count()" ini untuk menghitung jumlah data.
- "mean()" ini untuk menghitung nilai rata-rata. 
- "min()" ini untuk menghitung nilai minimal.
- "quantile()" ini untuk menilai titik potong yang membagi rentang distribusi probabilitas ke dalam interval berkesinambungan dengan probabilitas yang sama.
- "max()" ini untuk menghitung nilai maksimal.
- "skew()" ini untuk mengukur asimetri distribusi probabilitas dari variabel acak bernilai riil.