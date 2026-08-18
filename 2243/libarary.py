
n = int(input("Enter the number of books: "))
books = []
for i in range(n):
    print("\nEnter details of Book", i + 1)
    title = input("Book Title: ")
    borrowed = int(input("Number of times borrowed: "))
    members = int(input("Number of members who borrowed this book: "))

    books.append({
        "title": title,
        "borrowed": borrowed,
        "members": members
    })

total_borrowed = sum(book["borrowed"] for book in books)
total_members = sum(book["members"] for book in books)

if total_members > 0:
    average = total_borrowed / total_members
else:
    average = 0

print("\n1. Average number of books borrowed per member =", round(average, 2))
highest = max(books, key=lambda x: x["borrowed"])
lowest = min(books, key=lambda x: x["borrowed"])

print("\n2. Book with Highest Borrowing:")
print(highest["title"], "-", highest["borrowed"], "times")

print("Book with Lowest Borrowing:")
print(lowest["title"], "-", lowest["borrowed"], "times")
no_borrow = int(input("\nEnter the number of members who have not borrowed any book: "))
print("3. Members who have not borrowed any book =", no_borrow)
most_frequent = max(books, key=lambda x: x["borrowed"])

print("\n4. Most Frequently Borrowed Book:")
print(most_frequent["title"], "-", most_frequent["borrowed"], "times")
print("\n5. Library Borrowing Records")
print("---------------------------------------")
for book in books:
    print("Book Title :", book["title"])
    print("Times Borrowed :", book["borrowed"])
    print("Members Borrowed :", book["members"])
    print("---------------------------------------")