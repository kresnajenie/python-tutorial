import random

angka_tebakan = random.randint(1,11)

while True:
    jawaban = int(input("Jawab: "))

    if jawaban == angka_tebakan:
        print("Selamat")
        break
    elif jawaban > 9:
        print("hanya 1 ampe 9 doang")
    elif jawaban < angka_tebakan:
        print("kekecilan")
    elif jawaban > angka_tebakan:
        print("kebesaran")

print("keluar dari loop")