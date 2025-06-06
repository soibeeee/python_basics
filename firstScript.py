# print("Hello World")
# # print("We are checking")
#    print("Checking Done")
# #

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

# mysum = 0
# start = 3
# end = 5

# for i in range (start, end + 1): #start, stop
#     mysum += i
# print("Sum of numbers from", start, "to", end, "is", mysum)
# print("Hello World")
# # print("We are checking")
#    print("Checking Done")
# #

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

# mysum = 0
# start = 3
# end = 5

# for i in range (start, end + 1): #start, stop
#     mysum += i
# print("Sum of numbers from", start, "to", end, "is", mysum)

# mysum = 0
# for i in range ( 5 , 11 , 2 ):
#     mysum += i
#     if mysum == 5:
#         break
#         mysum += 1
# print( mysum)
# even_num = 0
# for i in range(5):
#     if i%2 == 0:
#         even_num += 1

# print(even_num)

# s = "demo loops - fruit loops"    
# for index in range(len(s)):
#     if s[index] == "O" or s[index] == "i":
#         print("Found 'o' at index", index)


# def check_even_odd(num):
#     if num % 2 == 0:
#         return "Even"
#     else:
#         return "Odd"
    

# num = int(input("Enter a number: "))
# result = check_even_odd(num)
# print(f"The number {num} is {result}.") 

# def check_prime(num):
#     if num < 2:
#         return False
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             return False
#     return True     

# num = int(input("Enter a number: "))
# if check_prime(num):
#     print(f"The number {num} is prime.")
# else:
#     print(f"The number {num} is not prime.")  

# def check_palindrome(s):
#     s = s.lower()  # Convert to lowercase for case-insensitive comparison
#     return s == s[::-1]  # Check if the string is equal to its reverse       

# s = input("Enter a string: ")
# if check_palindrome(s):
#     print(f"The string '{s}' is a palindrome.")
# else:
#     print(f"The string '{s}' is not a palindrome.")     


# def fibonacci(n):
#     fib_sequence = []
#     a, b = 0, 1
#     for i in range(n):
#         fib_sequence.append(a)
#         a, b = b, a + b
#     return fib_sequence     

# n = int(input("Enter the number of terms in the Fibonacci sequence: "))
# fib_sequence = fibonacci(n)
# print("Fibonacci sequence:", fib_sequence)  

# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)     
    
# n = int(input("Enter a number to find its factorial: "))
# result = factorial(n)
# print(f"The factorial of {n} is {result}.") 

# def sum_of_squares(n):
#     return sum(i**2 for i in range(1, n + 1))       

# sum_n = int(input("Enter a number to find the sum of squares: "))
# result = sum_of_squares(sum_n)      

# def ReverseString(string):
#     reversed_string = ""
#     for char in string:
#         reversed_string = char + reversed_string
#     return reversed_string  

# string = input("Enter a string to reverse: ")
# reversed_string = ReverseString(string)     
# print("Reversed string:", reversed_string)  

# def bubble_sort(lst):
#     n = len(lst)
#     for i in range(n):  
#         for j in range(0, n - i - 1):  
#             if lst[j] > lst[j + 1]:  
#                 lst[j], lst[j + 1] = lst[j + 1], lst[j]  # Swap elements

# # Example usage
# numbers = input("Enter numbers separated by spaces: ").split()
# numbers = [int(num) for num in numbers]  # Convert input strings to integers
# print("Original List:", numbers)                
# bubble_sort(numbers)
# print("Sorted List:", numbers)

# def two_sum(nums, target):
#     num_map = {}
#     for i, num in enumerate(nums):
#         complement = target - num
#         if complement in num_map:
#             return [num_map[complement], i]
#         num_map[num] = i
#     return None 

# # Example usage
# ints = input("Enter numbers separated by spaces: ").split()
# ints = [int(num) for num in ints]  # Convert input strings to integers
# target = int(input("Enter the target sum: "))
# result = two_sum(ints, target)      
# print(result if result else "No two numbers found that add up to the target.")

