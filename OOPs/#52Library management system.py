class library:
    lst = ["Harry potter", "Atomic habit", "Talk with computer", "My song", "Your pet", "This or that", "bas have", "aatali bov bov"]
    def add(self, str):
        self.lst.append(str)
    def rent(self, str):
        self.lst.pop(str)

a = library()
while True:
    print("Do want to talk about books?")
    c = input("Y for yes and N for no and ? for list of avalible books.")
    if(c=="N"):
        break
    if c=="Y":
        print("Write exact name:")
        print("Do you want to rent a book or give a book?")
        ch = input("R fot rent and G for give:")
        if(ch=="R"):
            print("Ok sir, which book do you want?")
            book = input("Name of book:")
            if book in a.lst:
                print("Yes sir we have it here is your book, thank you sir")
                a.rent(a.lst.index(book))
        if ch=="G":
            print("Ok sir which book do you want to give?")
            bookname = input("Enter the name of book:")
            a.add(bookname)
    if c=="?":
        print(len(a.lst))
        for i in a.lst:
            print(i)