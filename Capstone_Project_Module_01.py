# Import library
import pandas as pd
import numpy as np
import mysql.connector

# Membuat dictionary barang lengkap dengan nama, harga jual, harga beli, dan satuan
barang = {
    "BP001": {"Nama": "Beras", "Harga_Jual": 15000, "Harga_Beli": 12500, "Satuan": "kg"},
    "BP002": {"Nama": "Tepung Terigu", "Harga_Jual": 11000, "Harga_Beli": 9000, "Satuan": "kg"},
    "BP003": {"Nama": "Minyak Goreng", "Harga_Jual": 19500, "Harga_Beli": 18000, "Satuan": "liter"},
    "BP004": {"Nama": "Kentang", "Harga_Jual": 21000, "Harga_Beli": 17000, "Satuan": "kg"},
    "BP005": {"Nama": "Jagung", "Harga_Jual": 5500, "Harga_Beli": 3500, "Satuan": "kg"},
    "BD001": {"Nama": "Garam", "Harga_Jual": 10000, "Harga_Beli": 8000, "Satuan": "kg"},
    "BD002": {"Nama": "Gula", "Harga_Jual": 17500, "Harga_Beli": 16000, "Satuan": "kg"},
    "BD003": {"Nama": "Merica", "Harga_Jual": 1600, "Harga_Beli": 1400, "Satuan": "sachet"},
    "BD004": {"Nama": "Bawang Putih", "Harga_Jual": 42000, "Harga_Beli": 40000, "Satuan": "kg"},
    "BD005": {"Nama": "Bawang Merah", "Harga_Jual": 50000, "Harga_Beli": 47000, "Satuan": "kg"},
    "MK001": {"Nama": "Le Minerale", "Harga_Jual": 3000, "Harga_Beli": 2500, "Satuan": "botol"},
    "MK002": {"Nama": "Teh Pucuk", "Harga_Jual": 4000, "Harga_Beli": 3500, "Satuan": "botol"},
    "MK003": {"Nama": "Kopi Kapal Api", "Harga_Jual": 5800, "Harga_Beli": 5000, "Satuan": "botol"},
    "MK004": {"Nama": "Ultra Milk Coklat", "Harga_Jual": 6500, "Harga_Beli": 6000, "Satuan": "pack"},
    "MK005": {"Nama": "You C-1000", "Harga_Jual": 9000, "Harga_Beli": 8000, "Satuan": "botol"}
}

# List toko cabang
toko_cabang = ["Jakarta", "Bandung", "Surabaya"]

# Menentukan kategori barang dengan menggunakan conditional statement
def kategori_barang(kode):
    if kode.startswith("BP"):
        return "Bahan Pokok"
    elif kode.startswith("BD"):
        return "Bumbu Dapur"
    elif kode.startswith("MK"):
        return "Minuman Kemasan"
    else:
        return "Lainnya"

# Membuat data list dari dictionary barang dan cabang dengan menggunakan looping
data = []
for cabang in toko_cabang:
    for kode, info in barang.items():
        data.append((
            cabang,
            kode,
            info["Nama"],
            kategori_barang(kode),
            info["Harga_Jual"],
            info["Harga_Beli"],
            info["Satuan"]
        ))

# Membuat DataFrame
df = pd.DataFrame(data, columns=["Cabang", "Kode_Barang", "Nama_Barang", "Kategori_Barang", "Harga_Jual", "Harga_Beli", "Satuan"])

# Menambahkan kolom Penjualan secara random
np.random.seed(25)
df["Penjualan"] = np.random.randint(10, 50, size=len(df))

print(df)

# Koneksi ke MySQL
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Purwadhika.2025',
    database='toko'
)
cursor = mydb.cursor()
if mydb.is_connected():
    print("Koneksi ke database SQL berhasil!")

# Query INSERT
sql = """
INSERT INTO laporan_penjualan_barang_toko
(Cabang, Kode_Barang, Nama_Barang, Kategori_Barang, Harga_Jual, Harga_Beli, Satuan, Penjualan)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
"""

# Ubah DataFrame menjadi list of tuples
data_to_insert = [tuple(x) for x in df.to_numpy()]

# Eksekusi query
cursor.executemany(sql, data_to_insert)
mydb.commit()

print(cursor.rowcount, "data berhasil ditambahkan ke tabel laporan_penjualan_barang_toko")

cursor.close()
mydb.close()
