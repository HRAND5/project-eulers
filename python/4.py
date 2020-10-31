current_largest = 0
for i in range(1, 1000):
    for j in range(1, 1000):
        if str(i*j) == str(i*j)[::-1]:
            if i*j > current_largest:
                current_largest = i*j
print(current_largest)