def tampil_menu():
    print("\n=== KALKULATOR SEDERHANA ===")
    print("Pilih operasi:")
    print("1) Tambah (+)")
    print("2) Kurang (-)")
    print("3) Kali (*)")
    print("4) Bagi (/)")
    print("5) Modulus (%)")
    print("6) Pangkat (**)")
    print("7) Lihat riwayat")
    print("0) Keluar")

def ambil_angka(prompt):
    while True:  # loop sampai user masukkan angka valid
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Input bukan angka. Coba lagi.")

def hitung(a, b, pilihan):
    # percabangan untuk memilih operasi
    if pilihan == "1":
        return a + b
    elif pilihan == "2":
        return a - b
    elif pilihan == "3":
        return a * b
    elif pilihan == "4":
        # jaga pembagian dengan 0
        if b == 0:
            return "Error: pembagian dengan 0"
        return a / b
    elif pilihan == "5":
        if b == 0:
            return "Error: modulus dengan 0"
        return a % b
    elif pilihan == "6":
        return a ** b
    else:
        return None

def main():
    riwayat = []  # akan menyimpan tuple (expr, result)
    while True:  # loop utama program, berhenti kalau user pilih 0
        tampil_menu()
        pilihan = input("Masukkan pilihan (0-7): ").strip()

        # percabangan untuk kontrol pilihan menu
        if pilihan == "0":
            print("Keluar. Sampai jumpa!")
            break
        elif pilihan == "7":
            if not riwayat:
                print("Belum ada riwayat.")
            else:
                print("\n--- Riwayat Perhitungan ---")
                # contoh penggunaan for untuk menampilkan riwayat
                for i, (expr, res) in enumerate(riwayat, start=1):
                    print(f"{i}. {expr} = {res}")
                print("---------------------------")
            continue
        elif pilihan in {"1","2","3","4","5","6"}:
            a = ambil_angka("Masukkan angka pertama: ")
            b = ambil_angka("Masukkan angka kedua: ")
            result = hitung(a, b, pilihan)
            # tampilkan hasil dan simpan ke riwayat
            # untuk membuat ekspresi yang enak dibaca:
            ops = {"1":"+","2":"-","3":"*","4":"/","5":"%","6":"**"}
            expr = f"{a} {ops[pilihan]} {b}"
            print(f"Hasil: {result}")
            riwayat.append((expr, result))
        else:
            print("Pilihan tidak dikenali. Masukkan 0-7.")

    # saat keluar, kita bisa menanyakan mau simpan riwayat ke file
    simpan = input("Simpan riwayat ke file? (y/n): ").strip().lower()
    if simpan == "y":
        nama_file = input("Nama file (contoh: riwayat.txt): ").strip()
        try:
            with open(nama_file, "w", encoding="utf-8") as f:
                f.write("Riwayat Kalkulator\n")
                f.write("==================\n")
                for expr, res in riwayat:
                    f.write(f"{expr} = {res}\n")
            print(f"Riwayat tersimpan di {nama_file}")
        except Exception as e:
            print("Gagal menyimpan:", e)

if __name__ == "__main__":
    main()