# Import library
import pandas as pd
import mysql.connector

# Membaca file csv
df = pd.read_csv("data_penjualan.csv") 

# Koneksi ke MySQL
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Purwadhika.2025',
    database='toko')
cursor = mydb.cursor()
if mydb.is_connected():
    print("Koneksi ke database SQL berhasil!")

# Query INSERT
sql = """
INSERT INTO laporan_penjualan_barang_toko
(Cabang, Kode_Barang, Nama_Barang, Kategori_Barang, Harga_Jual, Harga_Beli, Satuan, Penjualan, Nilai_Penjualan, Profit)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
"""

# Ubah DataFrame menjadi list of tuples
data_to_insert = [tuple(x) for x in df.to_numpy()]

# Eksekusi query
cursor.executemany(sql, data_to_insert)
mydb.commit()
print(cursor.rowcount, "data berhasil ditambahkan ke tabel laporan_penjualan_barang_toko")
cursor.close()
mydb.close()