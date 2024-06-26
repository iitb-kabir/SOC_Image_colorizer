# print("hello world \n 7")      ------> and you can also hello world\n7 ----->No space  requried
''' triple code use for multiline comment out'''
# print("hey", 6,7, sep="@") --->  sep used for print hey@6@7----> give seperation between the data type like here @
#print("hey",6,     7,end=" 099\n") #---> print hey 6 7 099-----> end is used for when the program end then ended with 009

# print("kabir")

'''
a = complex(8, 2)    -----> representation of complex number 8+2i
b = True      -----> bool
c = "kabir"
d = None
print(a)
print(b)
a1 = 9    ----> integer
print(a + a1)
print("The type of a is ", type(a))   ---> type(a) represent here data type of "a"
print("The type of b is ", type(b))
print("The type of c is ", type(c))        '''


# list1 = [8, 2.3, [-4, 5], ["apple", "banana"]]   ----> store a list
# print(list1)

# tuple1 = (("parrot", "sparrow"), ("Lion", "Tiger"))
# print(tuple1)

# dict1 = {"name":"kabir", "age":19, "canVote":True}   ---> link one item to another
# print(dict1)     



                                                     # TYPECASTING 
# a="9"
# b="8"
# print(a+b)  # -----> we store all a,b in string so when we use + then it print 98


# print(int(a)+int(b))   -----> here python convert string into integer then it print 



                                                        # TAKING AN INPUT
# a= input("Enter your first Number :")
# b= input("Enter your second Number :")
'''  ------>in python  by default input is a string so we need to type cast it '''
# print(int(a)+int(b))


         # Double line string print -----> use '''  xyz  ''' or """  xyz  """

# k= ''' Hey,
#          How are you ?
#           I am fine '''
# print(k) 

             # INDEX
# x = "Hey, myself kabir I am good ,How are you ?"
# print(x)

# print(x[0])     ----->  print the character of x at place 1
# print(x[1])     ----->  print the character of x at place 1
# print(x[2])     ----->  print the character of x at place 1


                  
                          #LOOP
# x="Rohit"
# for character in x :              # ------> print all the character of x from 1 to end
#     print(character)                    


                    # string slicing    name[0:n]-----> print 0 index to n-1 index

#x= "mango"
# print(x[0:5])
#print(len(x))   ----> give 5 
#print(x[-1:-3])------->   print (x[len(x)-1:len(x)-3])------>print(x[4:2])------>python intreprate this print(x[2:4])
# print(x[-4:-2])      ------> when we used -ve then python use "len " means "Number of character present" 

#A=" !!!NAsiruddin kabir  !!!!!"
# B = "hello woRld"
                 #string are immutable
#print(A.upper())   # -----> change all the  character of A into upper case
# print(A.lower())     -----> change all the  character of A into lower case
# print(A.rstrip("!"))   ----> it remove the end part !!! and print  !!!NAsiruddin kabir
# print(A.replace("NAsiruddin","Nasir"))  ----> it used to replace a term
# print(A.split(" ")) ----> it split where it find gap like it print ['', '!!!NAsiruddin', 'kabir', '', '!!!!!']
# print(B.capitalize)  ------> it convert B into "Hello world"
# print(A.count("a"))    ----> count the number of scific character in a string 
# print(A.endwith("!"))  -----> give output true or false so here it is true
# print(A.find("kabir"))   ----->it help to find a word in the given string
# print(A.isalnum())   ------>  The isalnum() method returns True only if the entire string only consists of A-Z, a-z, 0-9. If any other characters or punctuations are present, then it returns False.
# print(A.isalpha())    -----> The isprintable() method returns True if all the values within the given string are printable, if not, then return False.
# print(A.istitle())     ----> The istitile() returns True only if the first letter of each word of the string is capitalized, else it returns False.
# print(A.isupper)      -----> The isupper() method returns True if all the characters in the string are upper case, else it returns False.
# print(A.startwith("kabir")) ---->The startwith() method checks if the string starts with a given value. If yes then return True, else return False.
# print(A.swapcase())------>  The swapcase() method changes the character casing of the string. Upper case are converted to lower case and lower case to upper case.
# print(A.title)   ----->  The title() method capitalizes each letter of the word within the string.


      
              # if ,elif, esle
              
# a=int(input("Enter your age : "))
# if(a>18):
#   print("You can drive")                   --------> There must be space in second line after  colon(:)    same as {in cpp} otherwise python treat it as out of braket
#   print("Yes")
# else:
#   print("You cannot drive")
#   print("No")

                   # MATCH CASE
'''
x = int(input("Enter the value of x: "))
# x is the variable to match
match x:
    # if x is 0
    case 0:
        print("x is zero")
    # case with if-condition
    case 4:
        print("case is 4")

    case _ if x!=90:
        print(x, "is not 90")
    case _ if x!=80:
        print(x, "is not 80")
    case _:
        print(x) '''
        
       # Q. Say goodmonring ,goodafternoon    
'''import time
Ttime=time.strftime('%H')
j=int(Ttime)
print(j)
if(16>=j>=12):
    print("Good AfterNoon")
elif(20>=j>=16):
    print("Good Evening")
elif(24>=j>=21):
    print("Good Night")
else:
    print("Good morning")    '''

        #LOOP
##    List

       # FOR LOOP
''' colors=['Red','Blue','Green','Yellow']
for color in colors:
    print(color)
    for j in color:
        print(j)           '''
        
'''for k in range(1,10):    #------>Print from 1 to 10 in range function the number start form (1,  ) and end (   ,10)
    print(k)   '''
 
              #WHILE LOOP
'''i=0
while(i<34):
    print(i)
    i=i+1          '''
        # Break statement
'''
for i in range(13):
    if(i==10):
        print("continue")
        continue
    print(i)
                       '''
            #    FUNCTION
'''def calmean(a,b):
    mean=(a+b)/2
    print(mean)
a=int(input("Frist Number:" ))
b=int(input("second  Number:" ))
calmean(a,b)        '''



'''def findmean(*num):       ## if we use *num then we can take as many as possible number for finding sum *num auto detect the number of input
    sum=0
    for i in num:
        sum=sum+i
    print(sum)
findmean(1,2,4,7)       '''

          #LIST 
'''marks=[2,3,67,"kabir","nasir",45,'rohit','Shuvo']
print(marks)
print(marks[2])
if 'kabir' in marks:  # -------> This syntax is use for finding some in a list or any other things
    print("yes")
else:
    print("No")
jumpindex=marks[1:4:2]   #------->[1:4:2]     HERE 2 is a jump index mean for printing the number the index is jump by 2
print(jumpindex) '''

             ## Making a list by condition 
'''lst={i*i for i in range(5)}
print(lst)   '''       


'''
l = [11, 45, 1, 2, 4, 6, 45,1, 1]
print(l)
# l.append(7)  --------> used 7 in the last of list l
#l.sort()  --------->    used for shorting in asending order of list 

# l.reverse()------->reversing the list in order
#print(l.index(45))#--------> print the index of that num where the 45 is present in frist place mean 1 here
#print(l.count(1))-------> count the number of one present in the list
# m = l.copy()------------> make a copy of list l
# m[0] = 0    ------------>update the index 0 
# l.insert(1, 899)
#m = [900, 1000, 1100]
# k = l + m
# print(k)
# l.extend(m)-----------> update the list l mean add 'm' on l      '''  


           # Tuple : Same like List but we cannot change tupel
           
'''       
tup = (1, 2, 76, 342, 32, "green", True)
# tup[0] = 90
print(type(tup), tup)
print(len(tup))
print(tup[0])
print(tup[-1])
print(tup[2])
# print(tup[34])

if  3421 in tup:
  print("Yes 342 is present in this tuple")
tup2 = tup[1:4]
print(tup2)      '''
    
          # NOTE: for changing tuple we have to first convert into list then change list into tuple again

                                # Project(KBC)
'''
Question= ['Who is known as the "Father of the Indian Constitution"?','Which planet is known as the Red Planet?','What is the capital city of Japan?','Who wrote the epic poem "The Odyssey"?','Which element has the chemical symbol "o"?']
option1=["A. Mahatma Gandhi","A. Earth","A. Beijing","A. Homer","A. Gold"]
option2=["B. Jawaharlal Nehru","B. Venus","B. Tokyo","B. Shakespeare","B. Oxygen"]
option3=["C. B. R. Ambedkar","C. Mars","C. Seoul","C. Virgil","C. Osmium"]
option4=["D. Sardar Vallabhbhai Patel","D. Jupiter","D. Bangkok","D. Dante","D. Oganesson"]
i=0
score=0
while(i<5):
    a=int(input())
    if (a==1):
     print(Question[0],"\n",option1[0],"\n",option2[0],"\n",option3[0],"\n",option4[0],"\n")
    elif (a==2):
      print(Question[1],"\n",option1[1],"\n",option2[1],"\n",option3[1],"\n",option4[1],"\n")
    elif (a==3):
     print(Question[2],"\n",option1[2],"\n",option2[2],"\n",option3[2],"\n",option4[2],"\n")
    elif (a==4):
     print(Question[3],"\n",option1[3],"\n",option2[3],"\n",option3[3],"\n",option4[3],"\n")
    elif (a==5):
     print(Question[4],"\n",option1[4],"\n",option2[4],"\n",option3[4],"\n",option4[4],"\n")
    print("choose a option: ")
    b=input()
    if(a==1 and b=="C"):
            score=score+4
    elif(a==1 and b!="C"):
            score=score-1
    if(a==2 and b=="C"):
         
     score=score+4
    elif(a==2 and b!="C"):
        score=score-1
    if(a==3 and b=="B"):
            score=score+4
    elif(a==3 and b!="B"):
            score=score-1
    if(a==4 and b=="A"):
    
            score=score+4
    elif(a==4 and b!="A"):
            score=score-1
    if(a==5 and b=="B"):

     score=score+4
    elif(a==5 and b!="B"):
         score=score-1

    i=i+1
print(score)        '''

                          # f-string
'''                         
letter = "Hey my name is {1} and I am from {0}"
country = "India"
name = "Harry"

print(letter.format(country, name))     ---------> #used for display above line in sequence 'name' then 'country'
print(f"Hey my name is {name} and I am from {country}")    #----------> Here we use f string so the line automatically pickup by finding key word
print(f"We use f-strings like this: Hey my name is {{name}} and I am from {{country}}")
price = 49.01877
txt = f"For only {price:.2f} dollars!"#------->price:.2f used for rounding off up to 2 decimal places
print(txt)
# print(txt.format())
print(type(f"{2 * 30}"))        
                           '''
                  
                                #DOC STRING

# def square(n):
#   '''Takes in a number n, returns the square of n'''
#   print(n**2)
# square(5)
# print(square.__doc__)#-------> for ascess that doc string we have write function name.__doc__   and STRING MUST BE JUST BELOW OF THE FUNCTION         
                                 # RECURSION
'''                                
def fact(n):
  if (n == 0 or n == 1):
    return 1
  else:
    return n * fact(n - 1)
print(fact(6))      '''

                          
                                         #SET

s = {"Carla", 19, False, 5.9, 19}
print(s)       # when we print set then it print in random way but if there are two item have same value the it automatically remove one of its like here 19
'''info = {"Carla", 19, False, 5.9}
for item in info:         
   print(item)    '''    # for access of each and every item of set we use for loop 
                        #  for indivdual access frint we have to convert set int list


                         #union and update
'''                        
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}   ''' 

#print(cities.union(cities2)) #-------------> used for union of two set 
#cities.update(cities2) # -------------->it update cities by combined with cities2
#print(cities)  
#print(cities.intersection(cities2))--------->it print intersection of cities and cities2
#print(cities.symmetric_difference(cities2))------------>print (A U B - A n B)
#print(cities.difference(cities2)) -------------->print(A- A n B)
#print(cities.isdisjoint(cities2))   ---------> return True if the set the sets are disjoint
#print(cities.issuperset(cities2))------------> return True if cities2 is the subset of cities
#cities.add("Helsinki")     ------------->used for adding "Helsinki" on cities
#print(cities)                   
#cities.remove("Tokyo")  --------->used for removing Tokyo from cities
#print(cities)
#print( cities.pop())  #------------>here one item get picked up randomly 
#cities.clear()  -------------> clear the entire set 
#print(cities)
'''info = {"Carla", 19, False, 5.9}
if "Carla" in info:
    print("Carla is present.")
else:
    print("Carla is absent.") '''      #-------> checking one perticluar item is present or not

# info = {'name':'Karan', 'age':19, 'eligible':True}
# print(info) 
# print(info.keys())  #------------>print all the keys of info
# print(info.values())   #------------>print all the values of info
# print(info['name'])    #-------->find the key and print the corresponding to value   # if nothing is found then give a error 
# print(info.get('eligible')) #---------> same like above but don't throw error if Keyword is not found

# for key in info.keys():
#   print(f"The value corresponding to the key {key} is {info[key]}")
'''
ep1 = {122: 45, 123: 89, 567: 69, 670: 69}
ep2 = {222: 67, 566: 90}  '''

# ep1.update(ep2)---------->update the ep1 by combining with ep2
# ep1.clear() ----------> crear the ep1 and give a empty dic
# print(ep1.pop(122))#-----------> poping the value corresponding to 122 
#print(ep1.popitem())#---------------> poping the last item of the ep1
# del ep1[122]      -------------> delete the value and key of corresponding to 122 key
# print(ep1) 

                            #For Loop with else
'''for i in range(3):
    print(i)
else:
    print("Program run smoothly")'''
    
'''
for i in range(8):
    print(i)
    if(i==5):
        break
else:                      #    Here and in above case else is with for so , in 2 case it not run 
    ("Program Not run smoothly")                '''

                       # Exception Handling  : Used for to overcome from the problem the there are any error and in above for that below lines are also not run  
'''                      
try:                               # first try statement run if there are any error the it shifted to except    
    num=int(input("Enter a Integer :"))
    print(f"It is {num}")
except:
    print("It is not an integer ") '''
    
    
                 # Finally vs print 
'''                 
def func1():
  try:
    l = [1, 5, 6, 7]
    i = int(input("Enter the index: "))
    print(l[i])
    return 1
  except:
    print("Some error occurred")
    return 0

  finally:
    print("I am always executed")
  # print("I am always executed")


x = func1()
print(x)'''
             #Explaination: LIke in the above case if we use only print then the "I am always executed " will not print becoz above function only return value so, finally have main work in function



                         # CUSTOM ERROR
'''
salary = int(input("Enter salary amount: "))
if not 2000 < salary < 5000:
    raise ValueError("Not a valid salary") '''     # Here the comilper throw a valueError if the salary not b/w (2000,5000) may be it is an integer 

# we can also customised my error type by using CLASS 
 
      
                    #SHORT HAND IF ELSE
'''
a = int(input("enter Number a:"))
b = int(input("enter Number b:"))
print("A") if a > b else print("B") if a==b else print("c")''' #------> This one line is the replace of:
                                                            # if(a>b):
                                                            #     print("A")
                                                            # elif(a==b):
                                                            #     print("B")
                                                            # else:
                                                            #     print("c")


                                #Enumerate    syntax: enumerate(iterable, start=0)
                            #used for printing or  index using of list,tupel ect.
'''marks=[1,34,567,789,98,786,65]
for index, mark in enumerate(marks, start=1):
 print(index ,end="  ")
 print(mark ) 
 if(index==3):
     print(end=" ")
 if(index == 3):
    print("Third Index ")'''
    
                    ## Virtual Environment
                    ## whole things we have do in a folder
# Create a virtual environment
#syntax:     python -m venv myenv

# Activate the virtual environment (Linux/macOS)
#syntax:    source myenv/bin/activate

# Activate the virtual environment (Windows)
#syntax :   myenv\Scripts\activate.bat

# Deactivate the virtual environment
#syntax : deactivate

# Output the list of installed packages and their versions to a file
#syntax : pip freeze > requirements.txt

# Install the packages listed in the requirements.txt file
#syntax : pip install -r requirements.txt

            #IMPORTING Different type of module
'''
import math #---------> Import math all function of math
result = math.sqrt(9)
print(result)  # Output: 3.0   '''

# import math  ----------> importing all the function of math module
# from math import sqrt, pi---------> only two function are import pi,sqrt
# from math import *       ----------> import full file of  math module 
# import math as m------------>here we can rename the math module by 'm'
# print(dir(math))-------------> here all the function which are present in the math module are printed 


       #if "__name__ == "__main__"
       
       
       #os Module
import os

# Open the file in read-only mode
f = os.open("c:/Users/nasir/OneDrive/Documents/myfile.txt", os.O_RDONLY)

# Read the contents of the file
contents = os.read(f, 1024)

# Close the file
os.close(f)


# Open the file in write-only mode
g = os.open("c:/Users/nasir/OneDrive/Documents/myfile.txt", os.O_WRONLY)

# Write to the file
os.write(g, b"Hello, world!")

# Close the file
os.close(g)


# Get a list of the files in the current directory
files = os.listdir(".")
print(files)  # Output: [print all the file present my my laptop]

# Create a new directory
os.mkdir("newdir")

x = 10  # global variable
def my_function():
  global x
  x = 5  # this will change the value of the global variable x
  y = 5  # local variable


my_function()
print(x)  # prints 5
# print(y) # this will cause an error because y is a local variable and is not accessible outside of the function


# f = open('myfile.txt', 'r')
# # print(f)
# text = f.read()
# print(text)
# f.close()

# WRITING A FILE

# f = open('myfile.txt', 'a')
# f.write('Hello, world!')
# f.close()

# with open('myfile.txt', 'a') as f:
#   f.write("Hey I am inside with")


                       #LEC 50


  
# f = open('myfile.txt', 'r')
# i = 0
# while True:
#   i = i + 1
#   line = f.readline()
#   if not line:
#     break
#   m1 = int(line.split(",")[0])
#   m2 = int(line.split(",")[1])
#   m3 = int(line.split(",")[2])
#   print(f"Marks of student {i} in Maths is: {m1*2}")
#   print(f"Marks of student {i} in English is: {m2*2}")
#   print(f"Marks of student {i} in SST is: {m3*2}")

#   print(line)

# f = open('myfile2.txt', 'w')
# lines = ['line 1\n', 'line 2\n', 'line 3\n']
# f.writelines(lines)
# f.close()

                       #LEC 51
'''with open('sample.txt', 'w') as f:
  f.write('Hello World3!')
  f.truncate(3)

with open('sample.txt', 'r') as f:
  print(f.read())  '''

# def double(x):
#   return x*2

def appl(fx, value):
  return 6 + fx(value)

double = lambda x: x * 2    # lambda use to used one line function
cube = lambda x: x * x * x
avg = lambda x, y, z: (x + y + z) / 3

print(double(5))
print(cube(5))
print(avg(3, 5, 10))
print(appl(lambda x: x * x , 2))

                            # map,filter  and reduce  function
# # MAP 
# # def cube(x):
# #   return x * x * x


# # print(cube(2))

# l = [1, 2, 4, 6, 4, 3]
# # newl = []
# # for item in l:
# #   newl.append(cube(item))

# newl = list(map(lambda x: x*x*x, l))
# print(newl)

# # FILTER
# def filter_function(a):
#   return a>2
  
# newnewl = list(filter(filter_function, l))
# print(newnewl)

from functools import reduce

# List of numbers
numbers = [1, 2, 3, 4, 5] 

# Calculate the sum of the numbers using the reduce function
def mysum(x, y):
  return x + y
  
sum = reduce(mysum, numbers)

# Print the sum
print(sum)
                    
               ##     diffference b/w is and ==

a = None
b = None

print(a is b) # exact location of object in memory
print(a is None) # exact location of object in memory
print(a == b) # value