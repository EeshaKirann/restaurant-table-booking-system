
def create_tables():
    tables = {
        1: "Available",
        2: "Available",
        3: "Available",
        4: "Available",
        5: "Available"
    }
    return tables


def show_tables(tables):
    print("\nTables Status:")
    for table in tables:
        print("Table", table, "-", tables[table])
