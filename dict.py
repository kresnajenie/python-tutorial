import random

print(random.randint(1,101))

people = [{"nama": "Leo", "umur": 16, "alamat":"Bogor"}]
a = 0

def list_contacts():
    for person in people:
        for key, value in person.items():
            print(f'{key}: {value}')
        print('')

def add_contact():
    print("add contact")
    nama = input("Please enter name: ")
    umur = input("Please enter umur: ")
    alamat = input("Please enter alamat: ")
    person = {
        "nama": nama,
        "umur": umur,
        "alamat": alamat,
    }
    people.append(person)
    
a = 10
while a > 0:
    print("0 to exit")
    print("1 to list")
    print("2 to add contact")
    user_input = int(input("Masukkan input: "))
    if user_input == 0:
        break 
    elif user_input == 1:
        list_contacts()
    elif user_input == 2:
        add_contact()
    else:
        continue
