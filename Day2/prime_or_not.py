num = 29

# To take input from the user
#num = int(input("Enter a number: "))

flag = False

if num > 1:
    # check for factors
    for i in range(2, num):
        if (num % i) == 0:
            flag = True
            break
if flag:
    print(num, "is not a prime number")
else:
    print(num, "is a prime number")

# Output 29 is a prime number