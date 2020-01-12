for letter in 'Python':
	print 'Current Letter :', letter

fruits = ['banana', 'apple', 'mango']
for fruit in fruits:
	print 'Current fruit :', fruit

count = 0
while (count < 9):
	print 'The count is:', count
	count = count + 1

def sum(a, b):
	return (a+b)

print sum(2,3)

def plus(c, d = 10):
	return (c+d)

print plus(15)

#Khai bao chuoi tren nhieu dong

paragraph = """This is line 1
This is line 2
This is line 3"""

str1 = 'Hello'
str2 = 'World'

str = str1 + ' ' +str2
print str[0:4]
print str[:4]
print str[-3:]
print str[6:-3]

print len(str)

newstr = str.replace('Hello', 'Hi')
print newstr

print str.find("World")

print "Good bye!"