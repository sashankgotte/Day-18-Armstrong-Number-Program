
n = int(input("Enter number: "))

digits = str(n)
total = sum(int(d) ** len(digits) for d in digits)

if total == n:
    print("Armstrong Number")
else:
    print("Not Armstrong")
