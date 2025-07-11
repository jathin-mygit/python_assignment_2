num = int(input("Enter a number: "))

if num % 2 == 0 :
    print(str(num) + " is an even number.")
elif num % 2 != 0 :
    print(str(num) + " is an odd number.")
else :
    print("Invalid input.")