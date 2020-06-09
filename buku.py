class Buku:
    def __init__(self, nama, harga, isi):
        self.nama = nama
        self.harga = harga
        self.isi = isi

    def print_data(self, isi=False):
        if (isi):
            print(f'Nama: {self.nama}\n Harga: {self.harga}\n Isi: {self.isi}\n============')
        else:
            print(f'Nama: {self.nama}\n Harga: {self.harga}\n ============')

class Reader:
    def __init__(self, nama, balance = 0):
        self.nama = nama
        self.purchased = []
        self.balance = balance

    def buy_book(self):
        book = self.list_books()
        
        print(book.nama)
        if (self.balance < book.harga):
            print("BALANCE NOT ENOUGH")
        else:
            self.balance -= book.harga
            self.purchased.append(book)
            print("Thank you for buying %s" % book.nama)
            print("Your balance is %s" % self.balance)

    def read_book(self):
        book = self.list_books(self.purchased)  
        book.print_data(isi=True)

    @staticmethod
    def list_books(bukus=None):
        if (bukus == None):
            bukus = books
        print(bukus)
        print("Book List")
        print("=====================")
        counter = 1
        for (book) in bukus:
            print(counter)
            book.print_data()
            counter += 1
        user_input = input("Which book do you want to buy? (Please input the number): \n")
        return bukus[int(user_input)-1]


books = []
books.append(Buku("Sapiens", 600000, "sapi sapi sapi"))  
books.append(Buku("Robin Hood", 100000, "Robin hood mencuri"))  
books.append(Buku("Into the night", 300000, "pesawat hijacked"))  
books.append(Buku("Nickel Boys", 600000, "Elwood Curtis"))  

kresna = Reader("kresna", 700000)

while True:
    print("Menu =====================")
    print("Hello %s" % kresna.nama)
    print("Please select an action")
    print("0 to leave")
    print("1 to buy a book")
    print("2 to read a book")
    user_input = int(input())
    if (user_input == 0):
        break
    elif (user_input == 1):
        kresna.buy_book()
    elif (user_input == 2):
        kresna.read_book()
    else: 
        print("Please input a valid number")