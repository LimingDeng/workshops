# python types
3/4
3.0/4.0

print("Hello " + "Ista")

# assignment
x = 3
y = 4
z = x + y
print(z)

## factorial
f8 = 8*7*6*5*4*3*2

## divisible by exercise (note that these would be treated as integers in python 2)

x = 123456789
y = [3607, 3803, 4013]

x / y[0]
x / y[1]
x / y[2]


x % y[0] == 0
x % y[1] == 0
x % y[2] == 0

## floats vs integers
## works
x ** 1000
## too big
(1.0 * x)**1000

## type conversion

xs = str(x)
xi = int(x)
xf = float(x)
type(xs)
type(xi)
type(xf)

## methods
xs.find("3")
xs.count("3")

## logic

1 < 5 < 4
(1 < 5) | (5 < 4)

## branching
if (x < 5):
    print(x) # can i put comments here?
else: # can i put comments here?
    print("x not less than 5") # can i put comments here?

# another way to use if:
z = "hello" if (x > 5) else "Good bye"
print(z)


## lists
x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
s = [] # empty list
s.append(1)
# lists can hold many things:
s.append("a")
s.append(s)
s.append([1, 2, 3])

"a" in s
1 in s
[1,2,3] in s
s.remove(s)

## delete by position
del s[2]

## append multiple elements
s.extend(["a", "b", "c"])

## insert
s.insert(0, s)

## indexing
s[4:7]
# if the first index is zero you can use the shortcut:
s[:4] # first four elements
s[-3:] # last three elements

len(xs)
len(s)

## dictionaries
s = {} # empty dictionary
s['bob'] = 1
s['alice'] = 1
s["ken"] = 2

s = {'bob': 1, 'alice': 2, 'ken': 3}
## index dictionaries
s['bob']


## tuples (unchangeable)
t = (1, 2)


## sets
myset = set([1, 2, 3])
myset == {1, 2, 3}


## functions
def f(x):
    return(x * x)

f(4)

## functions
def f(x, y):
    return(x * y)

f(3, 4)

def h(x):
    return(x*x)

def f(x,y,z):
    return(z(x) + z(y))

f(1, 2, h)

# default arguments
f(1, 2)

def f(x,y,z=h):
    return(z(x) + z(y))

f(1, 2)

def f(x=xi,y=xi,z=h):
    return(z(x) + z(y))


f(z = h, x = 1, y = 2) 

## package (*module*) management
import numpy ## import all numpy functions with numpy namespace
import math as m ## import math with m namespace
from math import * ## import all functions from math

## user writen files can be imported in the same way. The default namespace is the name of the file.


## for loops

names = ["alice", "robert", "jillian", "sue", "margret", "bobby"]

for name in names:
    print(name)

for i in range(0, len(names)):
    print(i)
## note that python2 has both range and xrange, python2 just has range, which mostly works like python2 xrange


[print(n) for n in names]

import urllib
import urllib.request

g = urllib.request.urlopen("http://google.com")

