# Data Types - immutable (passed by value)
# int, float, string, bool
a = 'ahmed'

# Everything is an object
print(dir (1))

# Data Structure
# passed by reference

a = []
b = a
c = b
c.append(1)
print(a)

# Dictionary
# Mutable unordered collection of key-value pairs
# Allows int, float, string, bool as keys
print({})
print(dict())

# List
# Mutable ordered collection
print([])
print(list())

# Tuple
# Immutable ordered list
print(())
print(tuple())


# Set
# Mutable unordered collection
print(set())

# Functions

def function_name():
  global a
  a = "something else"
  for myInt in range(0, 5):
    print(myInt)

function_name()

# Updating globals

global1 = "a"
global2 = "a"

def update_global():
  global global1
  global1 = 'b'
  global2 = 'b'

update_global()
print(global1)
print(global2)

# Classes

class person:
  def __init__(self, name):
    self.name = name
  def greet(self, greeting):
    print(greeting + ' ' + self.name)

me = person("ben")
me.greet("hello")

# IO

f = open("./wh-speech.txt")
print(f)
f.close()

# Fib example

def fib(n):
  if n < 2:
    return 1
  else:
    return fib(n - 1) + fib (n - 2)

for do_fib in range(1, 8):
  print(fib(do_fib))

# Ngram example

def ngram(s, n):
  ns = s.split()
  for word in range(len(ns) - n + 1):
    print(ns[word:word+n])

ngram('youview is really great', 2)

# Example using default parameters, dictionary access

def fib_cached (n, d={}):
  if n not in d.keys():
    if n < 2:
      d[n] = 1
    else:
      d[n] = fib_cached (n - 1) + fib_cached (n - 2)
  return d[n]

for do_fib in range(1, 8):
  print(fib_cached(do_fib))

# Default parameter value is being shared between function calls

def add(n, myList = []):
  myList.append(n)
  print(myList)

for do_add in range(1, 8):
  add(do_add)
