#print("Hello World")
## print("We are checking")
   # print("Checking Done")
##

# n = 0
# where = input("Go left or right? ")
# while where == "right":
#     n +=1 
#     if n > 2 :
#         print("You are out")
#     where = input("Go left or right? ")
# print("You are out! ")

# n = 0
# while n < 5:
#     print(n)
#     n = n+1 

x = input("Enter a number to find its factorial: ")
x = int(x)  # Convert input to integer
i = 1
factorial = 1
while i <= x:
    factorial = factorial * i
    i = i + 1
print("Factorial of", x, "is", factorial)
