print()
print("CS112: COMPUTER PROGRAMMING 1 - PRE-FINAL EXAM")
print("created by: James Ira A. Tagalog")
print()
print("Problem: Create python program that displays all prime numbers within a range.")
print()
print("RULES TO CONSIDER:")
print("[1] If number [start] is a negative number. The program will promtp a message: \"Enter a non-negative number\"")
print("[2] If number [end] is less than number [start]. The program will prompt a message: \"Enter a number greater than number [start]\" ")
print("[3] If the user enter the number \"0\", the program will terminate.")
print()
print()

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


while True:
    print()
    start = int(input("Enter the start number: "))

    if start == 0:
        print()
        print("Program terminated.")
        print("___________________")
        break

    if start < 0:
        print()
        print("Enter a non-negative number.")
        print("____________________________")
        continue

    end = int(input("Enter the end number: "))

    if end <= start:
        print()
        print("Enter a number greater than", start)
        print("_____________________________")
        continue

    print("Prime numbers between", start, "to", end, "are:")
    for num in range(start, end + 1):
        if is_prime(num):
            print(num, end=' ')
            print()
    print("__________________________________")

