# import os
# def automation(task):
#     if task == "restart":
#         print("Restarting the server...")
#         os.system("sudo reboot")
#     else:
#         print("Unknown task.")

# automation("restart")

# def diff(n):
#     if n <= 17:
#         return 17 -n
#     else :
#         return (n-17) *2

# n = int(input("Enter a number"))
# print(diff(n))

# def near_thousand(n):
#     # Check if the absolute difference between 1000 and n is less than or equal to 100
#     # OR check if the absolute difference between 2000 and n is less than or equal to 100
#     return ((abs(1000 - n) <= 100) or (abs(2000 - n) <= 100))

# # Call the "near_thousand" function with the argument 1000 and print the result
# print(near_thousand(1000))

# # Call the "near_thousand" function with the argument 900 and print the result
# print(near_thousand(900))

# # Call the "near_thousand" function with the argument 800 and print the result
# print(near_thousand(800))

# # Call the "near_thousand" function with the argument 2200 and print the result
# print(near_thousand(2200))


# num = int(input("Enter a Number :"))
# mod = num % 2
# if mod > 0:
#     print("this is odd number")
# else:
#     print("this is even number")

# # Step 1: Take input from the user and convert it to an integer
# num = int(input("Enter a number: "))

# # Step 2: Handle the special case — numbers less than or equal to 1 are not prime
# if num <= 1:
#     print("Not a prime number")

# else:
#     # Step 3: Assume it's a prime unless we find a factor
#     is_prime = True
#     # Step 4: Check for factors from 2 up to (and including) the square root of the number
#     for i in range(2, int(num ** 0.5) + 1):
#         # If num is divisible by i, it's not prime
#         if num % i == 0:
#             is_prime = False
#             break  # No need to check further, we already found a factor
#     # Step 5: Print the result based on whether we found a factor
#     if is_prime:
#         print("Prime number")
#     else:
#         print("Not a prime number")


