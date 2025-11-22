'''import pyjokes

print("Printing jokes...")
joke = pyjokes.get_jokes()
print(joke)'''

'''
print("abhinikesh")
print("3+7")'''

'''
import pyttsx3

engine = pyttsx3.init()
engine.say("Ahinikesh asdfghjklqwertyuiopkumar yadav Hello, pyttsx3 is notworking abhinikesh kumar hey i am good !")
engine.runAndWait()
print("Done speaking.")'''

'''
import time
import threading
from playsound import playsound

def type_lyric(line, char_delay=0.065):
    """Print each character like a typing effect"""
    for char in line:
        print(char, end="", flush=True)
        time.sleep(char_delay)
    print()  # new line

def print_lyrics():
    lyrics = [
        "Dil jo tumhara hai,",
        "kaisa bechara hai,",
        "Maane na besharam, bilkul khatara hai,",
        "Tu kare dil beqaraar,",
        "kyun karoon main tujhse pyar"
    ]
    delays = [1.5, 1.5, 2.0, 1.8, 2.3]

    time.sleep(1.5)  # small intro pause
    for i, line in enumerate(lyrics):
        type_lyric(line)
        time.sleep(delays[i])  # pause between lines

def play_song():
    playsound("mysong.mp3")  # <-- your audio file name

# Run the music in a background thread so lyrics print simultaneously
music_thread = threading.Thread(target=play_song)
music_thread.start()

# Start typing the lyrics
print_lyrics()

# Wait for music to finish before exiting
music_thread.join()
'''



'''
import time
import sys

def type_lyric(line, char_delay=0.065):
    for char in line:
        print(char, end="", flush=True) 
        time.sleep(char_delay)
    print()
def print_lyrics():

    lyrics = [
        "Dil jo tumhara hai,",
        "kaisa bechara hai,",
        "Maane na besharam, bilkul khatara hai,",
        "Tu kare dil beqaraar,",
        "kyun karoon main tujhse pyar"


    ]

    delays = [1.0, 1.0, 0.8, 3.0, 30.0]
    time.sleep(1.5)

    for i, line in enumerate(lyrics):
        type_lyric(line)
        time.sleep(delays[i])

print_lyrics()
'''

'''
import os
directory_path = '/home/elite'

contents = os.listdir(directory_path)

for item in contents:
    print(item)
'''

#                            variable and datatype
'''
a = 4
b = 6
b = 89
u = 90
print(a+b+b+u-b-b)

a = 4-2
b = 6
b += 3
print(b+a)

d = 5<4
print(d)

d = 5==9
print(d)
'''
'''
a = 31
t = type(a)
print(t)

a = 3.2
t = type(a)
print(t)

a = "abhi"
t = type(a)
print(t)

a = False
t = type(a)
print(t)

a = None
t = type(a)
print(t)

a = "32.2"
b = float(a)
c = int(b)
t = type(c)
print(t)
'''
'''
a = int(input("enter number 1:"))
b = int(input("enter number 2:"))
print("number a is: ",a)
print("number b is: ",b)

print("sum",a+b)
'''
'''
a = 34
b = 5

print("remainder when a is divided by b is", a%b)
print("divisor when a is divided by b is ",a/b)

a = input("enter the value of a: ")
print(type(a))
'''
'''
a = int(input("enter number 1: "))
b = int(input("enter number 2: "))

print("a is greater than b is", a>b)
'''


'''
b = float(input("enter the value of 1:"))
g = float(input("enter the value of 2:"))

print("b is greater than g is", b<g)
'''


'''
a = int(input("enter number 1: "))
b = int(input("enter number 2: "))

print("the average of these two number is", (a+b)/2)
'''

'''
a = int(input("enter your number: "))

print("the square of the number is", a**2)
print("the cube of the number is", a**3)
'''


'''
name = "Harry"

nameshort = name[0:3] 
print(nameshort)
character1 = name[1]
print(character1)
'''


'''
name = "Harry"

print(name[0:3])

print(name[-4: -1])
print(name[1:4])

print(name[:4])
print(name[1:5])



b = "qwertyuiop"
print(b[1:9:3])

print (b[1:9])
'''

'''
s = "harry"

print(len(s))

print(s.endswith("rry"))

print(s.startswith("ha"))

print(s.capitalize())

index = (s.find("arr"))
print(index)

p = "abhinikesh is a good boy"

index = (p.replace("good","bad"))
print(index)
'''


'''
a = "harry is a good \n boy and bad boy \n also"

print(a)
'''


'''
name = input("enter your name: ")
print(f"good afternoon, {name}")
'''



#                            list,tuple,dictonary,tables etc
'''
friends = ["Apple", "orange", 5, 345.06, False, "Aakash", "Rohan"]

print(friends[5])
friends[2] = "grapes"

print(friends[2])

print(friends)
print(friends[1:4])

friends.append("abhinikesh")
print(friends)

f = [1,34,23,23,75,34]
f.sort()
print(f)


f.reverse()
print(f)

print(f.pop(2))
print(f)
'''

'''
a = (4,56,897,67)
print(type(a))
print(a)

no = a.count(56)
print(no)

o = a.index(67)
print(o)
'''


'''
fruits = []

f1 = input("enter fruit name: ")
fruits.append(f1)

f2= input("enter fruit name: ")
fruits.append(f2)

f3= input("enter fruit name: ")
fruits.append(f3)

f4= input("enter fruit name: ")
fruits.append(f4)

f5= input("enter fruit name: ")
fruits.append(f5)

f6= input("enter fruit name: ")
fruits.append(f6)

print(fruits)

fruits.sort()
print(fruits)
'''

'''
l = [34,89,67,356]

print(sum(l))
'''


#                          Dictionary



'''
marks = {
    "Harry": 100,
    "Shubham": 90, 
    "Rohan": 23,
}

print(marks, type(marks))
'''


'''
fruits = {
    "kela": "1kg",
    "banana": "2kg",
    "seib": "3kg",
    "potato": "4kg",
}

print(fruits, type(fruits))
print(fruits["potato"])

print(fruits.items())
print(fruits.keys())
print(fruits.values())

fruits.update({"kela": "10kg"})
print(fruits)


print(fruits.get("kela2"))
print(fruits["kela2"])
'''



#                      sets in python


'''
s = {1, 5, 32}

e = set(7)
'''



'''
s = {1,5,45,9,78,32, "abhi"}
print(s, type(s))
'''


'''
s1 = {1,56,89,4}
s2 = {7,8,98,56}

print(s1.union(s2))
print(s1.intersection(s2))
'''


'''
a = int(input("enter your age: "))

if(a>=18):
    print("you are above the age of consent")
    print("good for you")

elif(a<0):
    print("you are entering a invalid age ")

elif(a==0):
    print("you are entering 0 which is not a valid age")

else:
    print("you are below the age of consent")
'''

'''
post = input("enter the post: ")

if("harry".lower() in post.lower()):
    print("this post is talking about harry")

else:
    print("this post is not talking about harry")
'''



#                                 loops
'''
for i in range(1,6):
    print(i)
'''

'''
a = 12
b = 67
c = 89

average = (a + b + c)/3
print(average)
'''

''''''
def avg():
    a = int(input("enter your number: "))
    b = int(input("enter your number: "))
    c = int(input("enter your number: "))

    average = (a+b+c)/3
    print(average)

avg()
''''''