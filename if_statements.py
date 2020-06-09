username1 = 'Kresna'
password1 = 'python'

# username2 = 'Juan'
# password2 = 'Bons'


print("CIA DATABASE LOGIN")
print("==============")
print("Please input user")
user = input()
print("Please input password")
password_user = input()
if user == username1 and password_user == password1:
    print("Access Granted")
# elif user == username2 and password_user == password2:
#     print("Access Granted")
else:
    print("Access Denied")
