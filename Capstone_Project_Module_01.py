# Import library
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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
        return None

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

#Menambahkan kolom Nilai Penjualan dan Profit
df["Nilai_Penjualan"] = df["Penjualan"] * df["Harga_Jual"]
df["Profit"] = (df["Harga_Jual"] - df["Harga_Beli"]) * df["Penjualan"]

# Membuat fungsi untuk menampilkan tabel laporan penjualan barang toko
def tampilkan_tabel():
    print("\n=== TABEL LAPORAN PENJUALAN BARANG TOKO ===")
    print(df)

# Membuat fungsi untuk menambahkan data baru pada tabel laporan penjualan toko
def tambah_data():
    cabang = input("Masukkan nama cabang: ")
    kode = input("Masukkan kode barang: ")
    if kode not in barang:
        print("Kode barang tidak ditemukan!")
        return
    jumlah = int(input("Masukkan jumlah terjual: "))
    df.loc[len(df)] = [
        cabang,
        kode,
        barang[kode]["Nama"],
        kategori_barang(kode),
        barang[kode]["Harga_Jual"],
        barang[kode]["Harga_Beli"],
        barang[kode]["Satuan"],
        jumlah,
        jumlah * barang[kode]["Harga_Jual"],
        (barang[kode]["Harga_Jual"] - barang[kode]["Harga_Beli"]) * jumlah
    ]
    print("Data berhasil ditambahkan!")

# Membuat fungsi untuk menghapus data pada tabel laporan penjualan toko 
def hapus_data():
    kode = input("Masukkan kode barang yang ingin dihapus: ")
    cabang = input("Masukkan nama cabang: ")
    idx = df[(df["Kode_Barang"] == kode) & (df["Cabang"] == cabang)].index
    if len(idx) > 0:
        df.drop(idx, inplace=True)
        print("Data berhasil dihapus!")
    else:
        print("Data tidak ditemukan!")

# Membuat fungsi untuk menampilkan tabel laporan penjualan toko berdasarkan cabang
def laporan_per_cabang():
    cabang = input("Masukkan nama cabang: ")
    data_cabang = df[df["Cabang"] == cabang]
    if data_cabang.empty:
        print("Tidak ada data untuk cabang ini.")
    else:
        print(data_cabang)

# Membuat fungsi untuk menampilkan tabel laporan penjualan toko berdasarkan kode barang
def laporan_per_kode():
    kode = input("Masukkan kode barang: ")
    data_kode = df[df["Kode_Barang"] == kode]
    if data_kode.empty:
        print("Tidak ada data untuk kode ini.")
    else:
        print(data_kode)

# Membuat fungsi untuk menampilkan profit penjualan berdasarkan cabang
def profit_per_cabang():
    print("\n=== PROFIT PER CABANG ===")
    print(df.groupby("Cabang")["Profit"].sum())

# Membuat fungsi untuk menampilkan profit penjualan berdasarkan kode barang
def profit_per_kode():
    print("\n=== PROFIT PER KODE BARANG ===")
    print(df.groupby("Kode_Barang")["Profit"].sum())

# Membuat fungsi untuk menampilkan rata-rata penjualan berdasarkan cabang
def mean_per_cabang():
    print("\n=== RATA-RATA PENJUALAN PER CABANG ===")
    print(df.groupby("Cabang")["Penjualan"].mean().round(2))

# Membuat fungsi untuk menampilkan rata-rata penjualan berdasarkan kode barang
def mean_per_kode():
    print("\n=== RATA-RATA PENJUALAN PER KODE BARANG ===")
    print(df.groupby("Kode_Barang")["Penjualan"].mean().round(2))

# Membuat grafik total penjualan per cabang
def grafik_total_penjualan_per_cabang():
    plt.figure(figsize=(10,5))
    total = df.groupby("Cabang")["Penjualan"].sum()
    plt.bar(total.index, total.values, color=["blue", "green", "red"])
    plt.xlabel("Cabang")
    plt.ylabel("Jumlah Penjualan")
    plt.title("Grafik Total Penjualan Per Cabang")
    plt.show(block=False)
    input("\n Tekan ENTER untuk kembali ke menu")
    plt.close()

# Membuat grafik persentase penjualan berdasarkan kategori barang
def grafik_persentase_penjualan_kategori_barang():
    plt.figure(figsize=(10,5))
    penjualan_kategori_barang = df.groupby("Kategori_Barang")["Penjualan"].sum()
    persentase = penjualan_kategori_barang / penjualan_kategori_barang.sum() * 100
    plt.pie(persentase, labels=persentase.index, autopct = "%1.2f%%", colors=["blue", "green", "red"])
    plt.title("Grafik Persentase Penjualan Berdasarkan Kategori Barang")
    plt.show(block=False)
    input("\n Tekan ENTER untuk kembali ke menu")
    plt.close()
    
while True:
    print("""
========= LAPORAN PENJUALAN BARANG TOKO =========
Silakan pilih menu:
1. Menampilkan tabel laporan penjualan barang toko
2. Menambahkan data penjualan barang
3. Menghapus data penjualan barang
4. Menampilkan laporan penjualan berdasarkan cabang
5. Menampilkan laporan penjualan berdasarkan kode barang
6. Menghitung profit penjualan berdasarkan cabang
7. Menghitung profit penjualan berdasarkan kode barang
8. Menampilkan nilai mean penjualan berdasarkan cabang
9. Menampilkan nilai mean penjualan berdasarkan kode barang
10. Menampilkan grafik total penjualan per cabang
11. Menampilkan grafik persentase penjualan berdasarkan kategori barang
12. Keluar dari program
""")

    pilihan = input("Masukkan pilihan (1-12): ")
    if pilihan == "1":
        tampilkan_tabel()
    elif pilihan == "2":
        tambah_data()
    elif pilihan == "3":
        hapus_data()
    elif pilihan == "4":
        laporan_per_cabang()
    elif pilihan == "5":
        laporan_per_kode()
    elif pilihan == "6":
        profit_per_cabang()
    elif pilihan == "7":
        profit_per_kode()
    elif pilihan == "8":
        mean_per_cabang()
    elif pilihan == "9":
        mean_per_kode()
    elif pilihan == "10":
        grafik_total_penjualan_per_cabang()
    elif pilihan == "11":
        grafik_persentase_penjualan_kategori_barang()
    elif pilihan == "12":
        df.to_csv("data_penjualan.csv", index=False)
        print("Terima kasih! Program selesai.")
        break
    else:
        print("Pilihan tidak valid, silakan coba lagi.")


