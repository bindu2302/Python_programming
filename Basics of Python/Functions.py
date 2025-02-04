# Without input and without a return statement

def add():
    a=10
    b=20
    print("Addition is:",a+b)


# With input and without return statement

def sub(a,b):
    print("Subtrcation is:",a-b)

# Without input and with return statement:
def mul():
    return 10*20

# with Inout and with return statements
def div(a,b):
    return a/b

add()
sub(100,50)
print(mul())
print(div(200,10))


 
def checkout_book(book_title, available_books):
    if book_title in available_books:
        available_books.remove(book_title)

def return_book(book_title, available_books):
    available_books.append(book_title)

def view_books(available_books):
    print("Available books:", available_books)

available_books = ['Harry Potter', '1984', 'Pride and Prejudice']

view_books(available_books)
checkout_book('Harry Potter', available_books)
view_books(available_books)
return_book('Harry Potter', available_books)
view_books(available_books)



def add_book(book_title, available_books):
    if book_title not in available_books:
        available_books.append(book_title)

def search_book(book_title, available_books):
    if book_title in available_books:
        print(f"'{book_title}' is available in the library.")
    else:
        print(f"Sorry, '{book_title}' is not available in the library.")

def view_books(available_books):
    print("Available books:", available_books)


available_books = ['Harry Potter', '1984', 'Pride and Prejudice']

view_books(available_books)

add_book('The Great Gatsby', available_books)
view_books(available_books)

search_book('1984', available_books)
search_book('The Catcher in the Rye', available_books)




def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def celsius_to_kelvin(celsius):
    return celsius + 273.15

celsius_temp = float(input().strip())

fahrenheit_temp = celsius_to_fahrenheit(celsius_temp)
kelvin_temp = celsius_to_kelvin(celsius_temp)

print(f"Temperature in Fahrenheit: {fahrenheit_temp}")
print(f"Temperature in Kelvin: {kelvin_temp}")

