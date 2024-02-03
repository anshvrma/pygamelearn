""" calculator """
# a= int(input("First number: "))
# s= str(input("symbol: "))
# b= int(input("second number: "))
# add= "+"
# sub="-"
# div="/"
# multiply="*"

# if s is add:
#     print("your answer is",a+b)

# elif s is sub:
#     print("your answer is",a-b)

# elif s is div:
#     print("your answer is",a/b)

# elif s is multiply:
#     print("your answer is",a*b)

# else:
#     print("Error!")


"""time greeting"""
# import time
# name= input("What is your name? ")
# timestamp = int(time.strftime('%H'))
# R_name= name.capitalize()
# if (5<= timestamp<12):
#     print("Good morning,",R_name)
# elif (12<= timestamp<18):
#     print("Good afternoon,",R_name)
# elif (18<= timestamp<22):
#     print("Good evening,",R_name)
# else:
#     print("Good night,",R_name)


"""Quiz show"""
# que= ["what is the color of milk?", "how many edge a triangle have?", "how many color traffic light have?"]
# opsn= ["black", "white", "Red", "blue", "2", "4", "3", "5"]

# x=0
# for x in que:
#     print(x)
#     if x == que[0]:
#         print(opsn[:4])
#         ans= input("Write your answer here:- ")
#         if ans == opsn[1]:
#             print("you have won Rs. 10,000")
#         else:
#             print("you have won Rs. 0, Better luck next time!")
#             break
#     elif x == que[1]:
#         print(opsn[4:])
#         ans= input("Write your answer here:- ")
#         if ans == opsn[6]:
#             print("you have won Rs. 20,000")
#         else:
#             print("you have won Rs. 10,000, Better luck next time!")
#             break
#     elif x == que [2]:
#         print(opsn[4:])
#         ans= input("Write your answer here:- ")
#         if ans == opsn[6]:
#             print("you have won Rs. 30,000")
#         else:
#             print("you have won Rs. 20,000, Better luck next time!")
#             break

"""recursion - fibonacci effect"""
# def fibonacci(n):
#     if (n == 0):
#         return 0
#     elif (n == 1):
#         return 1
#     else:
#         return int(fibonacci(n-1) + fibonacci(n-2))

# print(fibonacci(9))
# print(fibonacci(8))
# print(fibonacci(7))
# print(fibonacci(6))
# print(fibonacci(5))
# print(fibonacci(4))
# print(fibonacci(3))
# print(fibonacci(2))
# print(fibonacci(1))
# print(fibonacci(0))

"""secret code language"""
# write a python program to translate a massage into secret code language. use the rule below to translate normal english into secret code language

# # coding: 
# if the word contains atleast 3 characters, remove the first letter and append it at the end.
# now append three random characters at the starting and ending.
# else:
# simply reverse the String

# decoding:
# if the word contain less than 3 characters, reverse it 
# else:
#     remove 3 random characters from the start and end. now remove the last letter and append it to the beginning

# your program should ask whether you want to code or decode

"""solution"""
# st = input("Enter message: ")
# words= st.split(" ")
# coding = input("1 for coding and 0 for decoding")
# coding = True if (coding == "1") else False
# if (coding):
#     nwords = []
#     for word in words:
#         if (len(word)>= 3):
#             r1 = "uid"
#             r2 = "hbi"
#             stnew = r1 + word[1:] + word[0] + r2
#             nwords.append(stnew)
#         else:
#             nwords.append(word[::-1])
#     print(" ".join(nwords))

# else:
#     nwords = []
#     for word in words:
#         if (len(word)>= 3):
#             stnew = word[3:-3]
#             stnew = stnew[-1] + stnew[:-1]
#             nwords.append(stnew)
#         else:
#             nwords.append(word[::-1])
#     print(" ".join(nwords))


"""Class, obj and constructors(__init__)initialization"""
# class stu:
#     def __init__(self, nam, mth_mrks, sci_mrks) -> None:
#         self.name = nam
#         self.math_mrks = int(mth_mrks)
#         self.science_mrks = int(sci_mrks)
#         print(f'Student name: {self.name}, He get {self.math_mrks} in maths and get {self.science_mrks} in science.')
#         if (self.math_mrks and self.science_mrks >= 33):
#             print(f"{self.name} passed the exams.")
#         else:
#             print(f"{self.name} failed the exams.")

# stu1 = stu("Ramesh", 40, 90)
# stu2 = stu("Nita", 10, 20)


"""Rock, Paper, Scissors game"""
# import random

# def rslt(player, comp):
#     if comp == player:
#         return 0
    
#     if (comp == 0 and player == 2):
#         return -1
    
#     if (comp == 1 and player == 0):
#         return -1
    
#     if (comp == 2 and player == 1):
#         return -1
    
#     return 1

# run = True
# while run:
#     player = int(input("0 for Rock, 1 for Paper and 2 for Scissors:\n"))
#     comp = random.randint(0, 2)
#     score = rslt(player, comp)
#     print("You: ", player)
#     print("computer: ", comp)

#     if (score == 0):
#         print("it's a Draw")
#     elif (score == -1):
#         print("You Lose!")
#     else:
#         print("You Won!")
#         run = False

"""Clear the Clutter"""
import os
