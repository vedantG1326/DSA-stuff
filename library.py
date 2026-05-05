books = {"A": 5, "B": 2, "C": 0, "D": 7, "E": 2}

values = list(books.values())

avg = sum(values) / len(values)
max_book = max(books, key=books.get)
min_book = min(books, key=books.get)
zero_count = values.count(0)

# mode
mode = max(set(values), key=values.count)

print("Average:", avg)
print("Max:", max_book)
print("Min:", min_book)
print("Zero borrow:", zero_count)
print("Most frequent:", mode)
