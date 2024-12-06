# name = input("What is your name? ")
# age = input("What is your age? ")
# print("Person's name is " + name + " and age is " + age)

# wt_pounds = int(input("What is your weight (in pounds): "))
# wt_kg = wt_pounds * .4563
# print("Weight in kg: ", wt_kg)

# cost = 1000000
# credit = int(input("Enter credit: "))
# yourmom = 0
# if credit >= cost:
#     yourmom = .1 * cost
# else:
#     yourmom = .2 * cost
# print(yourmom)

# relay = False
# command = ""
# while command.lower() != "quit":
#     command = input("> ")
#     if command.lower() == "start":
#         if relay == False:
#             print("Car has started!")
#             relay = True
#         else:
#             print("Car has already started")
#     elif command.lower() == "stop":
#         if relay == True:
#             print("car has stopped")
#             relay = False
#         else:
#             print("Car has already stopped")
#     elif command.lower() == "help":
#         print("""
#               start - to start car
#               stop - to stop car
#               quit - to exit
#               """)
#     elif command.lower() == "quit":
#         break
#     else:
#         print("*in google assistant's voice* sorry, i didn't catch that")
    
# prices = [10, 20, 30]
# sum = 0
# for i in prices:
#     sum += i
# print(sum)

# pattern = [1,1,1,4]
# for i in pattern:
#     output = ""
#     for j in range(i):
#         output += "x "
#     print(output)

# list = [3,6,2,8,4,9,4]
# max_num = list[0]
# for i in range(len(list)):
#     if max_num >= list[i]:
#         continue
#     elif max_num < list[i]:
#         max_num = list[i]
# print(max_num)
# max_num = max(list)
# print(max_num)

# list = [4,6,3,8,9,6,4,8,9,3,5,7,4,3,7]
# l2 = []
# count = 0
# for i in list:
#     if i not in l2:
#         l2.append(i)
#     else:
#         continue
# print(l2)

# num = {
#     "1": "one",
#     "2": "two",
#     "3": "three",
#     "4": "four",
#     "5": "five",
#     "6": "six",
#     "7": "seven",
#     "8": "eight",
#     "9": "nine",
#     "10": "ten"}
# s = input("Enter your phone number: ")
# for i in s:
#     print(num.get(i), end = " ")

# str = input("> ")
# message = str.split(" ")
# def theemoji(s):
#     emojis = {
#         ":)": "😊",
#         ":')": "🥲",
#         "T~T": "😭"
#     }
#     output = ""
#     for i in s:
#         output += emojis.get(i,i)
#     print(output)

# theemoji(message)

# class Person:
#     def __init__(self, name):
#         self.name = name

#     def talk(self):
#         print(f"Person name = {self.name}")


# person1 = Person("p1")
# person1.talk()

# import random
# dice_1 = random.randint(1,6)
# dice_2 = random.randint(1,6)
# print(f"{dice_1},{dice_2}")

# import random
# class Dice:
#     def roll(self):
#         dice_1 = random.randint(1,6)
#         dice_2 = random.randint(1,6)
#         return dice_1, dice_2
    
# dice = Dice()
# print(dice.roll())

# from pathlib import Path
# path = Path()
# print(path.glob('*.*'))

