# WAP to compute sum of first n natural numbers

n = int(input("Enter a number: "))
sum = 0
for i in range(1, n+1):
    sum += i
print("Sum of first", n, "natural numbers:", sum)
