print('being a good person')
print('')
print("Clarusway will change my life")
# print('We should have enough time for our family")
example1 = 'sometimes what you say is less important than how you say it'
print(type(example1))
a = 36.5
b = '30'
c = '3.5'
d = ' F is enough for room temperature.'

print(str(a+int(b)+float(c))+d)
number = 2020
text = "children deserve respect as much as adults in"
print(text, number)
print("yesterday I ate", 2, "apples")
print('i', end=' ')
print('will say', end=' ')
print("'i missed you'", end=' ')
print('to my mother') 
x = 5
print ('value of x       : ', x)

x += 2
print ("2 more of x      : ", x, "\n") # using string expression '\n', 
                                       # we produce extra line. 
                                       # So that we had empty line.
y = 10
print ('value of y       : ', y)

y -= 2
print ("2 minus y        : ", y, "\n")

z = 6
print ('value of z       : ', z)

z *= 2
print ("2 times z        : ", z, "\n")
print('we', '\bare', '\bunited') # remember, normally print() function
# separates expressions by spaces
print('it\'s funny to learn Python') 
logic = True and False or not False or False
print(logic)
city = 'Phoenix'

print(city[1:])  # starts from index 1 to the end
print(city[:6])  # starts from zero to 5th index
print(city[::2])  # starts from zero to end by 2 step
print(city[1::2])  # starts from index 1 to the end by 2 step
print(city[-3:])  # starts from index -3 to the end
print(city[::-1])  # negative step starts from the end to zero
fruit = 'Orange'
vegetable = 'Tomato'
print("using + :", fruit + vegetable)
print("using * :", 3 * fruit)

fruit = 'orange'
fruit += ' apple'
fruit += ' banana'
fruit += ' apricot'

print(fruit)
phrase = 'I have %d %s and %.2f brothers' % (4, "children", 5)  
print (phrase)
sentence = "apologizing is a virtue"

print("%.11s" % sentence)  # we get first 11 characters of the string
fruit = 'Orange'
vegetable = 'Tomato'
amount = 4
print('The amount of {} we bought is {} pounds'.format(fruit, amount))
print('{state} is the most {adjective} state of the {country}'.format(state='California', country='USA', adjective='crowded'))
print("{6} {0} {5} {3} {4} {1} {2}".format('have', 6, 'months', 'a job', 'in', 'found', 'I will'))
print("{9} {7} {1} {10} {3} {2} {5} {8} {6} {0} {4}".format('in', 'know', 'bring', 'to', 'students.', 'out', 'best', 'teachers', 'the', 'Good', 'how'))

fruit = 'Orange'
vegetable = 'Tomato'
amount = 6
output = f"The amount of {fruit} and {vegetable} we bought are totally {amount} pounds"

print(output)
result = f"{4 * 5}"

print(result)

my_name = 'JOSEPH'
output = f"My name is {my_name.capitalize()}"

print(output)
name = "Joseph"
job = "teachers"
domain = "Data Science"
message = (
     f"Hi {name}. "
     f"You are one of the {job} "
     f"in the {domain} section."
)
print(message)
name = "Joseph"
job = "teachers"
domain = "Data Science"
message = f"Hi {name}. " \
     f"You are one of the {job} " \
     f"in the {domain} section."

print(message)

text = 'www.clarusway.com'
print(text.endswith('.com'))
print(text.startswith('http:'))
email = "clarusway@clarusway.com is my e-mail address"
print(email.startswith("@", 9))
print(email.endswith("-", 10, 32))

phrase = "myemailaddress@clarusway.com"

print(len(phrase))
print(phrase.startswith("@", 14))
print(phrase.endswith(".", 15, 24))
sentence = "I live and work in Virginia"

print(sentence.upper())  

print(sentence.lower())

print(sentence.swapcase())

print(sentence)  # note that, source text is unchanged

space_string = "     listen first      "
print(space_string.strip())  # removes all spaces from both sides

source_string = "interoperability"
print(source_string.strip("yi"))  
# removes trailing "y" or "i" or "yi" or "iy" from both sides

print('www', 'clarusway', "com", sep='.', end=' ')
print('will', end=' ')
print('open', end=' ')
print('your', end=' ')
print('path', end='.')

x = 12
y = x + 21
x = 2
print(y//x)
number = '32'
print(1988 + int(number))
print("{4} {9} {1} {7} {5} {0} {6} {8} {3} {2}".format('while', 'dream', 'work.', 'and', 'Some', 'success', 'others', 'of', 'wake up', 'people'))

print(not None or 1)

print('{3} {2} {4} {1} {0}'.format('job.', 'a', 'will', 'I', 'find'))

section_3_5 = "python data types and useful operations"
print(str.title(section_3_5))



# print(float("140" * int(input("Enter a number:" ))))

print(int("5" + "1"))
print(str("5" + "1"))
print("5" + "1")

var1 = "sleep"
var2 = "eat"
var3 = "better"
var4 = "life"
text = f"The less you {var1} and {var2}, the {var3} your {var4} will be."

city = "SARAJEVO"
text = f"I live in {city.title()}."
print(text)

print({0} and False or [])
print("a"+"bc")
print(3*1**3)

print(0xA + 0xB + 0xC)

print("abcd"[2:])
str1 = "hello"
str2 = ","
str3 = "world"
print(str1[-1:])
str1 = "world"

print(r"\nhello")

print("new" "line")

print("new" "line" "end", 3)
str1 = "clarsuway"
print(str1[::-1])

example = "snow world"
print("%s" % example[4:7])

print("DA", sep="-",end = ' ')
print("CA", end = '')
print("BA", sep="-", end = ' ')
print("AA", end = '')

# example = "snow world"
# example[3] = 's'
# print(example)
print(max("joseph"))

example="helloworld"
print(example[::-1].startswith("eh"))

print("hello\example\test.txt")
print("hello\"example\"test.txt")

print("hello\\example\\test.txt")

s = "\t\tWorld\n"
print(s.strip())

# print("hello" +"1+2+"3")
print(int("5" + "1"))
print(str("5" + "1"))
print("5" + "1")
text = "Clarusway, Clarusway, Clarusway,\n\tClarusway, Clarusway, Clarusway,\n\t\tClarusway, Clarusway, Clarusway"

print(text)

print({0} and False or [])

word = 'clarusway'
n = 3
front = word[0:3]
back = word[4:]
print(front + back)

text = "{0}! I am a {1} programmer and I {2} Clarusway".format("Hello", "new", "love")
print(text)