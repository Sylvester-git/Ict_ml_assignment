# 1 Write a pyhton programm that will accept a sequence of comma separarted words as input and prints the words in a comma separated sequence after sorting them alphabetically
'''
inputwords = str(input('Enter your words:'))
newwords = inputwords.split(',')
newwords.sort()
sortedwords = (', ').join(newwords)
print(sortedwords)
'''

# 2 write a program that computes the value of x+xx+xxx+xxxx with a given digit s the value of x. if the input is: 9. Then the output should be: 11106.

'''
x = int(input('Input your value:'))

n1 = int("%x" % x)
n2 = int("%x%x" % (x,x))
n3 = int("%x%x%x" % (x,x,x))
n4 = int("%x%x%x%x" % (x,x,x,x))

result = n1 + n2 + n3 + n4

if x > 9:
    print('Value should be less than 10')
else:
    print(result)
'''

# 3 use python to solve one of the more well known mathematical equations: the quadratic equation (ax² +bx + c= 0)


'''
import math

a = float(input('Enter the coefficients of a: '))
b = float( input('Enter the coefficients of b: '))
c = float(input('Enter the coefficients of c: '))

d = b**2-4*a*c # discriminant

if d < 0:
    print('This equation has no real solution')
elif d == 0:
      x = (-b+math.sqrt(b**2-4*a*c))/2*a
      print('This equation has one solutions: ', x)
else:
    x1 = (-b+math.sqrt(b**2-4*a*c))/2*a
    x2 = (-b-math.sqrt(b**2-4*a*c))/2*a
    print('This equation has two solutions: ',x1 ,' and' , x2)
'''