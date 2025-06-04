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

# x = input("Enter a number to find its factorial: ")
# x = int(x)  # Convert input to integer
# i = 1
# factorial = 1
# while i <= x:
#     factorial = factorial * i
#     i = i + 1
# print("Factorial of", x, "is", factorial)

# for i in range(1,10):
#     if i % 2 == 0:
#         print(i, "is even")
#     else:
#         print(i, "is odd")   

# for i in range (1,4,1): #start, stop, step
#     print("i is " , i)
# for j in range(1,4,2): #start, stop, step
#     print("j is ",j*2)
# for me in range(4,0,-1): #start, stop, step
#     print("me is ", me)
#     print("$"*me)

# rows = 5  # Number of rows
# for i in range(1, rows + 1):
#     print("*" * i)

# n = int(input("Enter the number of rows: "))
# # Upper half of the diamond
# for i in range(1, n + 1):
#     print(" " * (n - i) + "* " * i)
# # Lower half of the diamond
# for i in range(n - 1, 0, -1):
#     print(" " * (n - i) + "* " * i)


# for i in range (4):
#     for j in range(4):
#         if i == 0 or i == 3 or j == 0 or j == 3:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()  # Move to the next line after each row


# mysum = 0
# for i in range (10):
#     mysum += i
# print("Sum of first 10 numbers is", mysum)

mysum = 0
start = 3
end = 5

for i in range (start, end + 1): #start, stop
    mysum += i
print("Sum of numbers from", start, "to", end, "is", mysum)
