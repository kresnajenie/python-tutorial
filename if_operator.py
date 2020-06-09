username = "enryl"
password = "einhard"
guess_username = input("Masukkan username: ")
guess_password = input("Masukkan password: ")
while guess_username != username and guess_password != password:
    print("Coba lagi")  
    guess_username = input("Masukkan username: ")
    guess_password = input("Masukkan password: ")

print("Berhasil")