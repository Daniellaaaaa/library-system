# Library system

library=["python for beginners", "data structures in c", "ai basics"]
student_id=1
borrowed_books={}
def start ():
	while True:
		print('''
1. Display all books
2. Add books
3. Borrow book
4. Return book
5. Borrowed books
6. Students that borrowed books
7. Exit

''')
		user_choice=int(input("Enter choice: "))
		call_function(user_choice)

def call_function(user_choice):
	if user_choice == 1:
		display_books()
	elif user_choice == 2:
		book_name=input("Book to add: ").lower()
		add_book(book_name)
	elif user_choice == 3:
		book_name= input("Book to Borrow: ").lower()
		borrow_book(book_name)
			

def display_books():
	if len(library) != 0:
		for book in library:
			print(book)
	else:
		print("No books in the library")

def add_book(book_name):
	if book_name in library:
		print("Book already exist")
	else:
		library.append(book_name)	
		print(f"{book_name} added successfully")

def borrow_book(book_name):
	global student_id
	if book_name in library:
		library.remove(book_name)
		borrowed_books[student_id] = book_name
		student_id += 1	
		print(library)
		print(borrowed_books)
	else:
		print("Book not found")		
							
start()
