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