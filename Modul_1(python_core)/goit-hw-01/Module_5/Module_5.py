def count(start):
    while start > 0:
        yield start
        start = start - 1

for numbers in count(10):
    print(numbers)

    
print("good by")