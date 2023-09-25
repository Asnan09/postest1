# nama : Asnan Fadjri Wahyudi
# nim  : 2309116094

# Informasi login
nama = input("Masukkan nama Anda: ")
nim = input("Masukkan NIM Anda: ")

# Cek informasi login
if nama == "contoh_nama" and nim == "contoh_nim":
    print("Login berhasil!")
    # Tempatkan kode yang ingin dijalankan setelah login berhasil di sini
else:
    print("Login berhasil ")

# masukan input nilai dalam kilogram
kilogram = float(input("Masukkan nilai dalam kilogram: "))

# Menampilkan menu pilihan satuan massa
print("Pilih satuan massa yang ingin di konversikan:")
print("1. Pounds (lb)")
print("2. Ounce (ons)")
print("3. Gram (g)")

# Meminta pengguna untuk memilih satuan
pilihan = int(input("Masukkan nomor pilihan (1,2,3): "))

# Inisialisasi variabel hasil
hasil = 0

# konversi yang di pilihan
if pilihan == 1:
    # Konversi ke pounds (lb)
    hasil = kilogram * 2.20462
    satuan = "pounds (lb)"
elif pilihan == 2:
    # Konversi ke ounce (ons)
    hasil = kilogram * 35.274
    satuan = "ounce (ons)"
elif pilihan == 3:
    # Konversi ke gram (g)
    hasil = kilogram * 1000
    satuan = "gram (g)"
else:
    print("Pilihan tidak valid. Silakan pilih nomor 1, 2, atau 3.")

# Menampilkan hasil konversi jika pilihan valid
if pilihan in [1, 2, 3]:
    print(f"{kilogram} kilogram sama dengan {hasil} {satuan}")












