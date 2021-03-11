#def greet():
#    return "Hello Andrew!"

# ======================


'''
Functions with parameters
'''
#def greet(name):
#  return f"Hello {name}, good morning!"
  
'''
Greets a person passed in as argument
name: a name of a person to greet
'''

#print(greet("Andrew"))
#print(greet("Stacey"))
#print(greet("Bailey"))

#help(greet)

# ======================

'''
Arbitrary parameters
'''
#def fruits(*names):

'''
  Accepts unknown number of fruit names and prints each of them
  *name: list of fruits
'''
  #names are tuples
 # for fruit in names:
  #  print(fruit)

#fruits('Orange', 'Apple','Pears', 'Banana')

'''
Keyword parameters
'''

#def greet(name, msg):

#  '''
#    This function greets a person with a given message
#    name: person to greet
#    msg: message to greet person with
#  '''

#   return f"Hello {name}, {msg}"

#print(greet('Andrew','good morning!'))
#print(greet(msg='Good afternoon', name='Stacey'))

'''
Arbitrary Keywords
'''

#def person(**student):
#    print(type(student))
#    print(student)
#  for key in student:
#    print(student[key])

#person(fname="Andrew", lname="George")
#person(fname='Stacey', lname='Nurse', subject='Call of Duty')

'''
Default parameter values
'''

#def greet(name='Bailey'):
#    return f"Hello, {name}"

#print(greet())
#print(greet("Stacey"))

'''
pass statement
'''

#def greet():
#    pass

'''
Recursion
'''

#def factorial_recursive(n):
 
 #   '''
 #   Multiply a given number by every number less than it #downt to 1 in a factorial way
 #   e.g if n is 5 then calculate 5*4*3*2*1 = 120
 #   n: is the highest starting number
 #   '''

#    if n == 1:
#        return True
#    else:
#        return n * factorial_recursive(n -1)

#print(factorial_recursive(50))








