
from tables import create_tables, show_tables
from booking import book_table, cancel_table

tables = create_tables()

print("Restaurant Table Booking System")

while True:
    print("\n1. View Tables")
    print("2. Book Table")
    print("3. Cancel Booking")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        show_tables(tables)

    elif choice == "2":
        book_table(tables)

    elif choice == "3":
        cancel_table(tables)

    elif choice == "4":
        print("System Closed")
        break

    else:
        print("Invalid choice")
