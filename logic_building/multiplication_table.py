def multiplication_table():
    """Generate  a multiplication table."""
    table_for=int(input("Enter the number for which you want the multiplication table: "))
    range_for_table=int(input("Enter the range for the multiplication table: "))
    for i in range(1,range_for_table+1):
        print(f"{table_for} x {i} = {table_for*i}")
#example usage :
multiplication_table()
