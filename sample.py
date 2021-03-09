def print_multiplication_table(table, start,end):
    for i in range(start, end + 1):
        print(f"{table} * {i} = {table * i}")

print_multiplication_table(9, 1, 20)