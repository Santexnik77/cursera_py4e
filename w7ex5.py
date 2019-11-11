largest = None
smallest = None
while True:
    num = input("Enter a number: ")

    if num == "done" :
        break
    try:
        tmp = int(num)
    except:
        print("Invalid input")
        continue

    if largest is None:
        largest = tmp

    if largest < tmp:
        largest = tmp

    if smallest is None:
        smallest = tmp

    if smallest > tmp:
        smallest = tmp

print("Maximum is", largest)
print("Minimum is", smallest)
