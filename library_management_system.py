class Library:
    def __init__(self,books):
        self.books=books
        self.issued_books={}
    def display_books(self):
        print("\nAvailable Books:")
        if len(self.books)==0:
            print("No books available")
        else:
            for book in self.books:
                print("-",book)
    def issue_book(self,book_name,student):
        if book_name in self.books:
            self.books.remove(book_name)
            self.issued_books[book_name]=student
            print(f"{book_name} is issued to {student}")
        else:
            print("Book not available")
    def return_book(self,book_name):
        if book_name in self.issued_books:
            student=self.issued_books.pop(book_name)
            self.books.append(book_name)
            print(f"{book_name} is returned by {student}")
        else:
            print("This book was not issued")
    def show_issued_book(self):
        print("\nIssued Books:")
        if len(self.issued_books)==0:
            print("No books are issued")
        else:
            for book,student in self.issued_books.items():
                print(f"{book} -> {student}")
    def search_book(self,book_name):
        if book_name in self.books:
            print(f"{book_name} is available in library")
        elif book_name in self.issued_books:
            print(f"{book_name} is issued to {self.issued_books[book_name]}")
        else:
            print("Book not found in library")
    def add_book(self,book_name):
        self.books.append(book_name)
        print(f"{book_name} added to library")

    def total_books(self):
        print("Available books:",len(self.books))
        print("Issued books:",len(self.issued_books))

library=Library(["Python","C Programming","Java","Data Structures"])

while True:
    print("\n===== Library Management System =====")
    print("1.Display Books")
    print("2.Issue Book")
    print("3.Return Book")
    print("4.Show Issued Books")
    print("5.Search Book")
    print("6.Add Book")
    print("7.Count Books")
    print("8.Exit")

    try:
        choice=int(input("Enter your choice: "))
    except ValueError:
        print("Please enter a valid number")
        continue

    if choice==1:
        library.display_books()

    elif choice==2:
        book=input("Enter book name:")
        student=input("Enter student name:")
        library.issue_book(book,student)
    
    elif choice==3:
        book=input("Enter book name to return:")
        library.return_book(book)

    elif choice==4:
        library.show_issued_book()
    
    elif choice==5:
        book=input("Enter book name to seach:")
        library.search_book(book)
    
    elif choice==6:
        book=input("Enter new book name:")
        library.add_book(book)

    elif choice==7:
        library.total_books()
    
    elif choice==8:
        print("Thank you for using Library system")
        break
    else:
        print("Invalid choice")
