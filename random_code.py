'''
mystr = 'banana'
for x in mystr:
    print(x) #prints each char of string separately
'''
'''
mystr = 'banana'
for x in mystr:
    pass
print(x) #returns a idk how did that happen sm explain to me T~T
'''
'''
n = int(input('Enter a number: '))
for i in range(1,n+1):
    print(i)
'''

'''
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
# print(myorder) #this just prints the myorder as it is mentioned
print(myorder.format(quantity, itemno, price)) #this edits the {} and puts in the mentioned values
'''
'''
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}." #the index values make sure the order we mention in the print code excecutes it exactly in that index
print(myorder.format(quantity, itemno, price))
'''
'''
a = 'yo wassup \rfu' #the carriage func \r just basically dominates over the first how many ever chars in the begginning of the string and yeets it out and starts ruling over the whole string all hair \r!!
print(a)
'''

# expandtabs(tabsize) sets tab size to specified number of whitespaces
# default = 8 spaces
'''
a = 'H\te\tl\tl\to'
# print(a)
print(a.expandtabs(4))
'''

# isdecimal() reutrns True if all chars are decimals (0-9) used on unicode objs
# syntax - <string>.isdecimal()
'''
txt = "\u0033" #unicode for 3
x = txt.isdecimal()
print(x)
'''

# isidentifier() returns True is string is a valid identifier, else False
# string considered a valid identifier if it only contains alphanumeric letter (a-z) and (0-9) or undesocre
# a valid identifier can't start w number or contains any spaces
# syntax - <string>.isidentifier()
'''
a = "MyFolder"
b = "Demo002"
c = "2bring"
d = "my demo"

print(a.isidentifier())
print(b.isidentifier())
print(c.isidentifier())
print(d.isidentifier())
'''

# maketrans() returns mapping table that can be used with translate() to replace specific chars
# syntax - <string>.maketrans(x,y,z)
# x is required. if only one parameter is specified, this has to be a dict describing how to perform replace. if 2 or more specified, this parameter has to be str specifying the chars you want to replace
# y - optional.string w same length as parameter x. each char in the first parameter will be replaced w correspoding char in this str
# z - optional. string describing chars to remove from origianl str
# ASDFGHJKL I DIDN'T UNDERSTAND THIS T~T
# okay so i got it cleared from photosynthesizing leaf clearedup (i just gotta solve ome examples then i'd understand this)
'''
txt = "Hello Sam!"
mytable = txt.maketrans("S", "P")
print(txt.translate(mytable))
'''
'''
txt = "Hi Sam!"
x = "mSa"
y = "eJo"
mytable = txt.maketrans(x, y)
print(txt.translate(mytable))
'''
'''
txt = "Good night Sam!"
x = "mSa"
y = "eJo"
z = "odnght"
print(txt.maketrans(x, y, z))
'''

# partition() - searches for a specified string, & splits the str into tuple having 3 elements, before the str, the str and after the str respectively
# this searched for first occurence of specified str only
# syntax - <String>.partition(value)
'''
txt = "I could eat bananas all day"
x = txt.partition("bananas") #3 tuples as output
print(x)
'''
'''
txt = "I could eat bananas all day"
x = txt.partition("apples")
print(x) #also 3 tuples as output but the whole str is one tuple, the other 2 are empty tuples
'''

# translate() - returns str where some specified chars are replaced w char described in a dict or in mapping table
# use maketrans() to create mapping table
# if char not specified in dict or table, char will not be replaced
# if using dict, MUST USE ascii codes
# syntax - <string>.translate(table)
'''
txt = "Good night Sam!"
mydict = {109: 101, 83: 74, 97: 111, 111: None, 100: None, 110: None, 103: None, 104: None, 116: None}
print(txt.translate(mydict))
'''

# zfill() - adds zeroes at beginning of str until it reaches specified length
# if value of len parameter is less than length of string, no filling is done
# syntaax = <string>.zfill(len)
'''
a = "hello"
b = "welcome to the jungle"
c = "10.000"

print(a.zfill(10)) #filling done
print(b.zfill(10)) #filling not done
print(c.zfill(10)) #filling done
'''

# WHY WOULD THIS CODE BELOW PRINT TRUE!?
# update - photosynth. leaf cleared this for me again so basically anything that has a value will have a bool True
# strings, which have a value, print True
# print(bool('abc'))
# print(bool('')) #this code here printed false cuz the string has no value apparently

# import math
# a = int(input('Enter coeff of x^2: '))
# b = int(input('Enter coeff of x: '))
# c = int(input('Enter the constant: '))
# root1 = (-b + math.sqrt(b**2 - 4 * a * c))/2*a
# root2 = (-b - math.sqrt(b**2 - 4 * a * c))/2*a
# print('roots of quad equation are: ', root1, root2)

# for i in range(1,5):
#     for j in range(1,10):
#         if j < i:
#             print(1, end = ' ')
#     print(0)

# for i in range(1,5):
#     for j in range(1,10):
#         if j < i:
#             print(i, end = ' ')
#     print(i)

# for i in range(1,5):
#     for j in range(1,10):
#         if j < i:
#             print(j, end = ' ')
#     print(i)

# for i in range(1,5):
#     for j in range(1,10):
#         if j < i:
#             print(0, end = ' ')
#     print(1)

# l1 = ['A','B','C','D', 'E', 'F', 'G', 'H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
# for i in range(0,5):
#     for j in range(0,5):
#         if j <= i:
#             print(l1[i], end = ' ')
#     print(' ')

# l1 = ['A','B','C','D', 'E', 'F', 'G', 'H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
# val = 65
# inc = 1
# for i in range(0,5):
#     for j in range(0,inc):
#         ch = chr(val)
#         print(ch, end = ' ')
#         val += 1
#     inc += 2
#     print(' ')


# def basic_calc(x,y):
#     return x + y
# print(basic_calc(3,4))


# def giraffe_lang_translate(x):
#     vowels_list = ['a','e','i','o','u']
#     translated_word = ''
#     for i in x:
#         if i in vowels_list:
#             translated_word =  translated_word + 'g'
#         else:
#             translated_word = translated_word + i
#     return translated_word

# a = input('Enter a word: ')
# print('The word', a , 'in Giraffe Language is', giraffe_lang_translate(a))

# class Student:
#     def __init__(self, name, srn, branch):
#         self.name = name; self.srn = srn; self.branch = branch

# s = Student
# student1 = s('Myla Kinnera Sri', 'PES1202201581','EEE')
# print(student1.name, student1.srn, student1.branch)

# def fizz_buzz(q):
#     if q % 3 == 0:
#         print('fizz')
#     elif q % 5 == 0:
#         print('buzz')
#     elif q % 3 == 0 and q % 5 == 0:
#         print('fizzbuzz')
#     else:
#         return q

    
# print(fizz_buzz(15))
# print(fizz_buzz(7))
# print(fizz_buzz(9))

# def runningSum(n): #Line 1 
#     while n < 5: #Line 2 
#         n = n + 1 #Line 3# 
# n = 1 #Line 4
# runningSum(n) #Line 5
# print(n) #Line 6


#from tkinter import *
#root = Tk()
#def myCLick():
#    label1 = Label(root, text = 'look, i clicked a button!')
#    label1.pack()
#button1 = Button(root, text = 'Click me', command = myCLick, fg = '#FF5733')
#button1.pack()
#root.mainloop()

#from tkinter import *
#root = Tk()
#e = Entry(root, width = 70)
#e.pack()
#e.insert(0, 'Enter your name: ')
#def myCLick():
#    label1 = Label(root, text = e.get())
#    label1.pack()
#button1 = Button(root, text = 'Click me', command = myCLick, fg = '#FF5733')
#button1.pack()
#root.mainloop()

# str1 = 'fjs'
# try:
#     str3 = int(str1)
# except:
#     str3 = 1
# print(str3)

#import re
#pattern = re.compile("^[a-z A-Z 0-9 \s]+$")
#print(pattern.search('HELLOWORLD'))
#print(pattern.search('HelloWorld1'))
#print(pattern.match('HELLOWORLD'))
#print(pattern.search('     '))
#print(pattern.match('7654238948'))
#print(pattern.search('HELLO 465r 535 WORLD'))

#import re
#pattern1 = re.compile('^[a-z]{3}[0-9]{3,5}[^a-z A-Z 0-9]{1}[A-Z]{0,2}$')
#print(pattern1.search('eih4524#R'))
#print(pattern1.search('eih4524#@R'))

#import re
#p1 = re.compile('^.{10}$')
#print(p1.search('yigrfk5742'))
#print(p1.search('yigrfk5f742'))

#import re
#p2 = re.compile('^[a-z A-Z 0-9 \. \-_]+@{1}[a-z A-Z 0 9]+\.{1}[a-z A-Z]{2,3}$')
#print(p2.search('mail@whatevexample.com'))

#import re
#y = re.findall('(\S+@\S+)', 'rhguig ERGSG sivf@gre fg')
#print(y)



#from tkinter import *
#from tkinter.ttk import Entry

#root = Tk()
#root.title('Simple calc')
#root.geometry('200x350')

#entry_wid = Entry(root, width = 30).grid(row = 0, column = 0, columnspan=3)
#def display_num(num):
#    #entry_wid = Entry(root, width = 30).grid(row = 0, column = 0)
#    if num in [0,1,2,3,4,5,6,7,8,9]:
#        get_entered = entry_wid.get(str(num))
#    return num
#entry_wid = Entry(root, width = 30).grid(row = 0, column = 0, columnspan=3)

##def show_name(num):
##   # Create a Label widget
##   label = Label(root, text= '' + str(entry_wid.get(str(num))), font=('Calibri 25')).pack(pady=20)
##   entry_wid.delete(0, END)

#b0 = Button(root, text = '0', padx = 20, pady = 20, command = lambda: display_num(0)).grid(row = 1, column = 0)
#b1 = Button(root, text = '1', padx = 20, pady = 20, command = lambda: display_num(1)).grid(row = 1, column = 1)
#b2 = Button(root, text = '2', padx = 20, pady = 20, command = lambda: display_num(2)).grid(row = 1, column = 2)
#b3 = Button(root, text = '3', padx = 20, pady = 20, command = lambda: display_num(3)).grid(row = 2, column = 0)
#b4 = Button(root, text = '4', padx = 20, pady = 20, command = lambda: display_num(4)).grid(row = 2, column = 1)
#b5 = Button(root, text = '5', padx = 20, pady = 20, command = lambda: display_num(5)).grid(row = 2, column = 2)
#b6 = Button(root, text = '6', padx = 20, pady = 20, command = lambda: display_num(6)).grid(row = 3, column = 0)
#b7 = Button(root, text = '7', padx = 20, pady = 20, command = lambda: display_num(7)).grid(row = 3, column = 1)
#b8 = Button(root, text = '8', padx = 20, pady = 20, command = lambda: display_num(8)).grid(row = 3, column = 2)
#b9 = Button(root, text = '9', padx = 20, pady = 20, command = lambda: display_num(9)).grid(row = 4, column = 0)
#b_equal = Button(root, text = '=', padx = 20, pady = 20).grid(row = 4, column = 1)
#b_plus = Button(root, text = '+', padx = 19, pady = 20).grid(row = 4, column = 2)
#b_minus = Button(root, text = '-', padx = 20, pady = 20).grid(row = 5, column = 0)
#b_multiply = Button(root, text = '*', padx= 21, pady = 20).grid(row = 5, column = 1)
#b_divide = Button(root, text = '/', padx = 21, pady = 20).grid(row = 5, column = 2)

#root.mainloop()




#from tkinter import *
#from tkinter.ttk import *

#def close_window():
#    global entry
#    entry = E.get()
#    root.destroy()

#root = Tk()
#E = Entry(root)
#E.pack(anchor = CENTER)
#B = Button(root, text = "OK", command = close_window)
#B.pack(anchor = S)
#root.mainloop()

#from tkinter import *

#win = Tk()

## Set the size of the tkinter window
#win.geometry("700x350")

#def show_name():
#   # Create a Label widget
#   label = Label(win, text="Hello " + str(entry.get()) + "👋", font=('Calibri 25')).pack(pady=20)
#   entry.delete(0, END)

## Create a Label
#Label(win, text="Enter Your Name").pack()

## Create an Entry widget
#entry = Entry(win, width=25)
#entry.pack(pady=20)

#Button(win, text="Submit", command=show_name).pack()

#win.mainloop()


# from tkinter import *
# from PIL import ImageTk, Image

# root = Tk()
# img1 = ImageTk.PhotoImage(Image.open("tinywow_Snapchat-1987187958_13102420.png"))
# label1 = Label(root, image = img1).pack()
# def quit_window():
#    root.quit()

# quitbutton = Button(root, text = 'Exit Program', command = quit_window).pack()

# root.mainloop()


#import socket as s
#s = s.socket()
#print('Socket created')
#s.bind(('localhost', 9999))
#s.listen(3)
#print('waiting for connections')
#while True:
#    c, addr = s.accept()
#    name = c.recv((1024)).decode()
#    print('Connected with', addr, name)
#    c.send(bytes('bleh bleh', 'utf-8'))

#class A:
#    def __init__(self, l1):
#        self.l1 = l1
#    def __iter__(self):
#        self.i = 0
#        return self
#    def __next__(self):
#        self.i += 1
#        if self.i <= len(self.l1):
#            return self.l1[self.i - 1]
#        else:
#            raise StopIteration

#a = ['a','b','c','d','e']
#c = A(a)
#for k in c:
#    print(k)

# a = input('enter whatever: ')
# print(format("what you entered was {a}"))
# someone tell me syntax of format no T~T

#def create_new_dict(og_dict):
#    new_dict = {}
#    for key, value in og_dict.items():
#        if value in new_dict:
#            new_dict[value].append(key)
#        else:
#            new_dict[value] = [key]
#    return new_dict

#d1 = {'a': 1, 'b': 2, 'c': 2, 'd': 3}
#print(create_new_dict(d1))

#def sum(a,b):
#    return a + b
#l1 = [3,5,3,8]
#l2 = [4,8,2,6]
#res = list(map(sum, l1, l2))
#print(res)
#res1 = list(map(lambda x,y: sum(x,y), l1, l2))
#print(res1)
# map already iterates through. don't need lambda in this example

#import datetime
#print(datetime.__doc__)

#import math

#def calc(f):
#    def inner(*args):
#        f(*args)
#        print('whatev')
#    return inner

#@calc
#def factorial(n):
#    k = math.factorial(n)
#    print(k)
#    return k

#def fact(n):
#    h = math.factorial(n)
#    print(h)
#    return h

#factorial(4)
#fact(4)

#d = {'a':1,'b':2,'c':3,'d':4,'e':5,'x':24,'y':25}
#print(d.pop('x'))
#print (d.popitem())
##print (d.popitem())
##print (d.popitem())
##print (d.popitem())
## popitem always returns last key-value pair in the dict
#d.setdefault('a')

#s1 = {3,5,6,2,7,8,5,8}
#s2 = {'d','f','a','r','u','x'}
###s1.remove(9) #key error raised
##s1.discard(9) # doesn't raise an error
#print(s1)
#s1.pop()
#print(s1)
#s1.pop()
#print(s1) #pop removes first element/ smallest or min element
#s2.pop()
#print(s2)
#s2.pop()
#print(s2)

#a = 'your mommy'
#print(a[2+1]) # index of a string can be accessed when the index is expressed an an arithmetic operation
#print(a[2*1])
#print(a.count('y'))
#print(a.count('c')) # when value is not in string, doesn't raise error, just returns 0

#a = None #variable w no value cuz in future gonna assign sm value to it
#l1 = [3,5,3]
#a = l1
#print(a)

#inc = 1
#val = 65
#for i in range(0,5):
#    for j in range(0,inc):
#        ch = chr(val)
#        print(ch, end = ' ')
#        val += 1
#    inc += 2
#    print()

#def returnSqaures(l):
#    res = list(map(lambda x: x**2, l))
#    res.sort()
#    print(res)
#    return res

#l1 = [4,8,3,5,7,2,5,7,4]
#returnSqaures(l1)

#def returnEvens(l):
#    res = list(filter(lambda x: x%2 == 0, l))
#    print(l)
#    print(res)
#    return res

#l1 = [4,8,3,5,7,2,5,7,4]
#returnEvens(l1)

#def zeroCheck(x,y,z):
#    if x == 0 or y == 0 or z == 0:
#        print(True)
#        return True
#    else:
#        print(False)
#        return False

#zeroCheck(6,2,4)
#zeroCheck(2,0,7)

#a = [4,7,3,7,'c']
#for i in range(len(a)):
#    a[i] = str(a[i])
#print(a)
