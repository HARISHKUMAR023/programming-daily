#Write a function to return True if the first and
# last number of a given list is same.
# If numbers are different then return False.

number=[10,20,30,10]
first=number[0]
second=number[-1]
if first == second:
    print(second)
    print(first)
    print("the both the first and last number is same")
else:
    print("number in list is not equal")