size_in_bytes = 1.44 * 1024 * 1024

books_size_in_bytes = 100 * 50 * 25 * 4

res = size_in_bytes // books_size_in_bytes

print("Количество книг, помещающихся на дискету:", int(res))
