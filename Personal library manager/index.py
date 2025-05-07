import streamlit as st


if 'books' not in st.session_state:
    st.session_state.books = []

def add_book():
    st.write("Add a Book")
    title = st.text_input("Enter the book title:")
    author = st.text_input("Enter the author:")
    year = st.text_input("Enter the publication year:")
    genre = st.text_input("Enter the genre:")
    read_status = st.text_input("Have you read this book? (yes/no):")
    if st.button("Add Book"):
        if title and author and year and genre:
            st.session_state.books.append({"title": title, "author": author, "year": year, "genre": genre, "read_status": read_status})
            st.success(f"Book '{title}' added successfully!")
        else:
            st.error("Please fill in all fields.")

def remove_book():
    st.write("Remove Book")
    title = st.text_input("Enter the title of the book to remove:")
    if st.button("Remove Book"):
        for book in st.session_state.books:
            if book["title"] == title:
                st.session_state.books.remove(book)
                st.warning(f"Book '{title}' removed successfully!")
                break
        else:
            st.error(f"Book '{title}' not found.")

def display_books():
    st.write("Displaying all books:")
    if not st.session_state.books:
        st.write("No books available.")
    else:
        for i, book in enumerate(st.session_state.books, 1):
            st.write(f"{i}. Title: {book['title']} , Author: {book['author']} , Year: {book['year']} , Genre: {book['genre']} , Read: {book['read_status']}")

def statistics ():
     st.write("Displaying Statistics:")
     total_books = len(st.session_state.books)
     st.write(f"Total number of books in your library: {total_books}")



def main():
    st.title("Welcome to your Personal Library Manager!")
    st.subheader("1. Add a book")
    st.subheader("2. Remove a book")
    st.subheader("3. Display all books")
    st.subheader("4. Display statistics")
    st.subheader("5. Exit")

    choice = st.number_input("Enter your choice (1-5):", value=0, key="user_choice")

    
    if choice == 1:
        add_book()
    elif choice == 2:
        remove_book()
    elif choice == 3:
        display_books()
    elif choice == 4:
        statistics()
    elif choice == 5:
        st.write("Library saved to file. Goodbye!")
        st.stop()
    else:
        st.write("Please enter a valid choice (1-6).")

main()