def is_prime (num):
    if num<=1:
    return False
for i in range(2,int(num**0.5)+1):
    if num% i==0:
        return False
    return True
number=int(input("enter a number:"))
if is_prime(number):
    print(f"{number}is a prime nnumber.")
else:
    print(f"{number}is not a prime number.")    