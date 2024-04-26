# WAP to compute compound Interest
print("name-dev,rollno-2210997068")
principal = int(input("Enter the principal amount: "))
rate = int(input("Enter rate of interest: "))
time = int(input("Enter time in years: " ))
Amount = principal * (pow((1 + rate / 100), time))
CI = Amount - principal
print("Compound interest is", CI)