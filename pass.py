users = [
    {
        "user": "kresna",
        "pass": "auloh"
    },
    {
        "user": "bons",
        "pass": "spida"
    }
]

def tambah(x, y):
    return x + y

def check_user(user):
    data = {
        "val": False
    }

    for use in users:
        if use["user"] == user:
            data["val"] = True
            data["user"] = use
            break
    
    return data


while True:
    user_input = input("Masukkan user: ")
    data = check_user(user_input)
    if data["val"]:
        pass_input = input("Masukkan password: ")
        if pass_input == data["user"]["pass"]:
            print("Access Granted")
            break
        else: 
            print("====WARNING=====")
            print("Access Denied")
    else:
        print("====WARNING=====")
        print("User doesn't exist")
    