def tambah(x, y):
    return x + y

while True:
    try:
        angka1 = int(input("Masukkan angka pertama: "))
        angka2 = int(input("Masukkan angka kedua: "))
        print(tambah(angka1, angka2))

        break
    except ValueError:
        print("Please input a number")
    except:
        print("Error")

