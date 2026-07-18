class Book:
    def __init__(self, book_id, title, author, year):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year
    
    def __str__(self):
        return f"ID: {self.book_id} | Title: {self.title} | Author: {self.author} | Year: {self.year}"
    
    def __repr__(self):
        return self.__str__()


class LibraryManagementSystem:
    
    def __init__(self):
        self.books = []
        self.next_id = 1
    
    def add_book(self, title, author, year):
        book = Book(self.next_id, title, author, year)
        self.books.append(book)
        self.next_id += 1
        print(f"✓ Book '{title}' added successfully! (ID: {book.book_id})")
        return book
    
    def remove_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                self.books.remove(book)
                print(f"✓ Book '{book.title}' removed successfully!")
                return True
        print(f"✗ Book with ID {book_id} not found.")
        return False
    
    def search_by_title(self, title):
        results = [book for book in self.books if title.lower() in book.title.lower()]
        return results
    
    def search_by_author(self, author):
        results = [book for book in self.books if author.lower() in book.author.lower()]
        return results
    
    def search(self, query):
        title_results = self.search_by_title(query)
        author_results = self.search_by_author(query)
        results = list(set(title_results + author_results))
        return results
    
    def display_all_books(self):
        if not self.books:
            print("✗ The library is empty.")
            return
        
        print("\n" + "="*80)
        print("LIBRARY CATALOG - ALL AVAILABLE BOOKS")
        print("="*80)
        for book in self.books:
            print(book)
        print("="*80)
        print(f"Total books: {len(self.books)}\n")
    
    def display_search_results(self, results, query):
        if not results:
            print(f"\n✗ No books found matching '{query}'.\n")
            return
        
        print(f"\n{'='*80}")
        print(f"SEARCH RESULTS FOR '{query}' ({len(results)} book(s) found)")
        print(f"{'='*80}")
        for book in results:
            print(book)
        print(f"{'='*80}\n")


def display_menu():
    print("\n" + "="*80)
    print("LIBRARY MANAGEMENT SYSTEM")
    print("="*80)
    print("1. Add a new book")
    print("2. Remove a book")
    print("3. Search for a book")
    print("4. Display all books")
    print("5. Exit")
    print("="*80)


def main():
    library = LibraryManagementSystem()
    
    print("Loading sample books...\n")
    library.add_book("To Kill a Mockingbird", "Harper Lee", 1960)
    library.add_book("1984", "George Orwell", 1949)
    library.add_book("The Great Gatsby", "F. Scott Fitzgerald", 1925)
    library.add_book("Pride and Prejudice", "Jane Austen", 1813)
    library.add_book("The Catcher in the Rye", "J.D. Salinger", 1951)
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ").strip()
        
        if choice == "1":
            print("\n--- Add New Book ---")
            title = input("Enter book title: ").strip()
            author = input("Enter author name: ").strip()
            try:
                year = int(input("Enter publication year: ").strip())
                library.add_book(title, author, year)
            except ValueError:
                print("✗ Invalid year. Please enter a valid number.")
        
        elif choice == "2":
            print("\n--- Remove Book ---")
            library.display_all_books()
            try:
                book_id = int(input("Enter book ID to remove: ").strip())
                library.remove_book(book_id)
            except ValueError:
                print("✗ Invalid ID. Please enter a valid number.")
        
        elif choice == "3":
            print("\n--- Search Book ---")
            query = input("Enter title or author name to search: ").strip()
            if query:
                results = library.search(query)
                library.display_search_results(results, query)
            else:
                print("✗ Search query cannot be empty.")
        
        elif choice == "4":
            library.display_all_books()
        
        elif choice == "5":
            print("\n✓ Thank you for using Library Management System. Goodbye!")
            break
        
        else:
            print("✗ Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()
