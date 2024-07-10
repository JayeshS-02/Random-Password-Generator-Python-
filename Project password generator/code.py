import random

print("Welcome to your password Generator")
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@!$#^*%&,.?1234567890"
numbers = input("Amount of password to generate : ")
numbers = int(numbers)
length = input("Input your password length : ")
length = int(length)

print('\nhere are your passwords:')

for pwd in range(numbers):
  passwords = ''
  for c in range(length):
    passwords += random.choice(chars)
  print(passwords)
