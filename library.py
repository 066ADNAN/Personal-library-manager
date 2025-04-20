import json
import os

def display_menu():
    """Display the main menu options"""
    print("\nWelcome to your Personal Library Manager!")
    print("1. Add a book")
    print("2. Remove a book")
    print("3. Search for a book")
    print("4. Display all books")
    print("5. Display statistics")
    print("6. Exit")

def add_book(library):
    """Add a new book to the library"""
    print("\nAdd a new book:")
    title = input("Enter the book title: ").strip()
    author = input("Enter the author: ").strip()
    
    # Validate publication year
    while True:
        try:
            year = int(input("Enter the publication year: "))
            if year < 0:
                print("Please enter a valid year.")
                continue
            break
        except ValueError:
            print("Please enter a valid year number.")
    
    genre = input("Enter the genre: ").strip()
    
    # Validate read status
    while True:
        read_status = input("Have you read this book? (yes/no): ").lower().strip()
        if read_status in ('yes', 'y'):
            read = True
            break
        elif read_status in ('no', 'n'):
            read = False
            break
        else:
            print("Please enter 'yes' or 'no'.")
    
    # Create book dictionary
    book = {
        'title': title,
        'author': author,
        'year': year,
        'genre': genre,
        'read': read
    }
    
    library.append(book)
    print("Book added successfully!")

def remove_book(library):
    """Remove a book from the library by title"""
    if not library:
        print("Your library is empty!")
        return
    
    title = input("\nEnter the title of the book to remove: ").strip()
    found = False
    
    for i, book in enumerate(library[:]):
        if book['title'].lower() == title.lower():
            library.remove(book)
            found = True
            print("Book removed successfully!")
            break
    
    if not found:
        print("Book not found in your library.")

def search_books(library):
    """Search for books by title or author"""
    if not library:
        print("Your library is empty!")
        return
    
    print("\nSearch by:")
    print("1. Title")
    print("2. Author")
    
    while True:
        try:
            choice = int(input("Enter your choice (1-2): "))
            if choice not in (1, 2):
                print("Please enter 1 or 2.")
                continue
            break
        except ValueError:
            print("Please enter a number.")
    
    search_term = input("Enter the search term: ").strip().lower()
    matches = []
    
    if choice == 1:
        matches = [book for book in library if search_term in book['title'].lower()]
    else:
        matches = [book for book in library if search_term in book['author'].lower()]
    
    if not matches:
        print("No matching books found.")
    else:
        print(f"\nFound {len(matches)} matching book(s):")
        for i, book in enumerate(matches, 1):
            status = "Read" if book['read'] else "Unread"
            print(f"{i}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {status}")

def display_all_books(library):
    """Display all books in the library"""
    if not library:
        print("Your library is empty!")
        return
    
    print("\nYour Library:")
    for i, book in enumerate(library, 1):
        status = "Read" if book['read'] else "Unread"
        print(f"{i}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {status}")

def display_statistics(library):
    """Display library statistics"""
    if not library:
        print("Your library is empty!")
        return
    
    total_books = len(library)
    read_books = sum(1 for book in library if book['read'])
    percentage_read = (read_books / total_books) * 100 if total_books > 0 else 0
    
    print("\nLibrary Statistics:")
    print(f"Total books: {total_books}")
    print(f"Percentage read: {percentage_read:.1f}%")

def save_library(library, filename='library.json'):
    """Save the library to a JSON file"""
    try:
        with open(filename, 'w') as f:
            json.dump(library, f)
        print("Library saved to file.")
    except Exception as e:
        print(f"Error saving library: {e}")

def load_library(filename='library.json'):
    """Load the library from a JSON file if it exists"""
    if os.path.exists(filename):
        try:
            with open(filename, 'r') as f:
                return json.load(f)
        except Exception as e:
            print(f"Error loading library: {e}")
            return []
    return []

def main():
    """Main program loop"""
    # Load library from file if it exists
    library = load_library()
    
    while True:
        display_menu()
        
        try:
            choice = int(input("Enter your choice (1-6): "))
        except ValueError:
            print("Please enter a number between 1 and 6.")
            continue
        
        if choice == 1:
            add_book(library)
        elif choice == 2:
            remove_book(library)
        elif choice == 3:
            search_books(library)
        elif choice == 4:
            display_all_books(library)
        elif choice == 5:
            display_statistics(library)
        elif choice == 6:
            save_library(library)
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()