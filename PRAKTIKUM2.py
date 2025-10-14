print("--- Kalkulator Sederhana ---")
print("Pilih Operasi:")
print("1. Penjumlahan (+)")
print("2. Pengurangan (-)")
print("3. Perkalian (*)")
print("4. Pembagian (/)")

# Input pilihan
pilihan = input("Masukkan pilihan (1/2/3/4): ")

# Input angka
try:
    angka1 = float(input("Masukkan angka pertama: "))
    angka2 = float(input("Masukkan angka kedua: "))
except ValueError:
    print("Error: Harap masukkan input berupa angka.")
    exit()

# Logika Percabangan Inti
if pilihan == '1':
    hasil = angka1 + angka2
    operator = '+'
elif pilihan == '2':
    hasil = angka1 - angka2
    operator = '-'
elif pilihan == '3':
    hasil = angka1 * angka2
    operator = '*'
elif pilihan == '4':
    # Percabangan internal untuk Pembagian
    if angka2 != 0:
        hasil = angka1 / angka2
        operator = '/'
    else:
        # Menampilkan error dan menghentikan proses
        print("Error: Tidak bisa membagi dengan nol!")
        exit()
else:
    print("Error: Pilihan operasi tidak valid.")
    exit()

# Menampilkan hasil
print(f"\nHasil dari {angka1} {operator} {angka2} = {hasil}")
