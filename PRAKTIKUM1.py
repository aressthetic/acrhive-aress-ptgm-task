def kalkulator_simple():
    while True:
        print("\npilih operasi:")
        print("1. tambah (+)")
        print("2. kurang (-)")
        print("3. kali   (*)")
        print("4. bagi   (/)")
        print("5. keluar")

        pilihan = input("pilihan (1/2/3/4/5): ")

        if pilihan == '5':
            print("selesai.")
            break

        elif pilihan in ('1', '2', '3', '4'):
            try:
                a = float(input("angka pertama: "))
                b = float(input("angka kedua: "))
            except ValueError:
                print("input tidak valid.")
                continue

            if pilihan == '1':
                hasil = a + b
                op = '+'
            elif pilihan == '2':
                hasil = a - b
                op = '-'
            elif pilihan == '3':
                hasil = a * b
                op = '*'
            elif pilihan == '4':
                if b != 0:
                    hasil = a / b
                    op = '/'
                else:
                    print("error pembagian nol.")
                    continue

            print(f"hasil: {a} {op} {b} = {hasil}")

        else:
            print("pilihan tidak dikenal.")

kalkulator_simple()
