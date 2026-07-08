
def book_table(tables):
    table_no = int(input("Enter table number: "))

    if tables[table_no] == "Available":
        name = input("Enter customer name: ")
        tables[table_no] = name
        print("Table booked successfully")
    else:
        print("Table not available")


def cancel_table(tables):
    table_no = int(input("Enter table number to cancel: "))

    if tables[table_no] != "Available":
        tables[table_no] = "Available"
        print("Booking cancelled")
    else:
        print("Table already available")
