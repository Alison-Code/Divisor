n = int(input("How many apples are there with Harry: "))
mn = int(input("Minimum numbers of students: "))
if mn > mx:
    print("This is not a range")

if mn == mx:
    print("This is not a range. Minimum and Maximum are same")

else:
    for i in range(mn, mx + 1):
        if n % i == 0:
            print(f"{i} is a divisor of {n}")
