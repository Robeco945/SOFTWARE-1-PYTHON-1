from typing import List

print("exercise 3")
numbers: list[float] = []
num = input("enter a number: ")
while num !="":
    number = float(num)
    numbers.append(number)
    num = input("enter a number: ")

small = min(numbers)
big = max(numbers)
print(f"the smallest number is: {small}")
print(f"the largest number is: {big}")