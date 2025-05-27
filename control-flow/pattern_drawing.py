from turtle import pos


positive_number = int(input("Enter the size of the pattern: "))


while positive_number > 0:
    for _ in range(positive_number):
        for _ in range(positive_number):
            print("*", end="")
        print()
    break