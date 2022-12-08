warning = 'You must quit smoking!'

print(len(list(warning)))

fruits = ['apple', 'banana', 'watermelon', 'orange', 'mango', 'avocado']

fruit_list = []
fruit_list.insert(0, fruits)
print(fruit_list[0][2][7])

even_numbers = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

print(even_numbers[4:9])
print(len([[12, 34, 56]]))
# print(len([[12, 34, 56]][0]))
# mix_value = (10, False, 'fruit', 1.618)
# mix_value.append(['vegetable', 2+3j])

# print(len(mix_value))


list_1 = list(range(1,11))
list_1.sort(reverse=True)
print(list_1)

grocer = ["banana", ["orange", ["apple", "eggplant", "melon", "spinach", "cheese", "leek" ], "water"], "mandarin"]

print(grocer[1][1][1::2])

text = "My two favorite flowers are tulip and rose, two favorite colors are blue and green."

flowers = [["jasmine", ["lavender", "rose"], "tulip"]]
colors = ["red", ("blue", ["yellow", "green"]), "pink"]
text = "My two favorite flowers are {} and {}, two favorite colors are {} and {}.".format(flowers[0][2], flowers[0][1][1], colors[1][0], colors[1][1][1])
print(text)

escapes = ["\n\t", ("\t", "\t\t"), ["\n", "\n\t\t"]]
sentence = "I am 40 years old. {}I have two children. {}Data Science is my IT domain.".format(escapes[0],escapes[2][1])
print(sentence)

student_ages = {"Harry": 29,
                "Clark": 32,
                "Peter": 22,
                "Bruce": 36
                }

print(student_ages["Clark"])

print(len(set('listen to the voice of enlisted')))

numbers = {}

numbers['x'] = 12
numbers['y'] = 4
numbers.update({'z': 3})

print(numbers['x'] + numbers['y'] + numbers['z']**2)

numbers_10 = [10, 30, 40, 50, 60, 70, 80, 90, 100]
numbers_10.insert(1,20)
print(numbers_10)

fruits_vegetables = ["fruit", "vegetable", ["apple", "banana", ["mango", "avocado"]], ["spinach", "broccoli"]]


list1 = [123]
print(type(list1))

family_members = ['Meghan', 'Tom', 'Nicole', 'Tim']
family_members = tuple(family_members)
print(family_members)

flowers = ['Rose', 'Orchid', 'Tulip']
count1 = len(flowers)
count2 = 0

while count1>0 :
    print(flowers[count2])
    count1 -= 1
    count2 += 1

for i in {'n1' : 'one', 'n2' : 'two'} : print(i)

iterable = [1, 2, 3, 4]
for i in iterable:
    print(i**2)

    a = 3
while a**2 < 299:
    print('I will stop smoking')
    a += 3



# math_mark = int(input('Please enter the mark: '))
# if math_mark >= 85:
#     print('A (Excellent)')
# elif 70 <= math_mark <= 84:
#     print('B (Good)')
# elif 60 <= math_mark <= 69:
#     print('C (Medium)')
# elif 45 <= math_mark <= 59:
#     print('D (Not Bad)')
# else:
#     print('F (Failed)')

a=998
if a >= 999 :
    print(a ** 0)  

else :
    print(a * 2)

print()
a = 49
while a <= 62:
    print(a)
    a += 5
print()
# a = 49
# while a > 10:
#     print(a)
#     a += 5

# number = int(input('Please enter a number: '))
# count = 0
# while count < number:
#     print(count**2)
#     count+=1

sample_list = [{"section":5, "topic":2}, 'clarusway', [1, 4], 2020, 3.14, 1+618j, False, (10, 20)]

for i in sample_list:
    print('The type of {} is {}'.format(i, type(i)))

n=int(input('Enter a number to check if it is a prime number : '))
count=0
for i in range(1, n+1):
    if n%i==0 : count += 1
    else : count += 0
if count < 3: print('{} is a prime number '.format(n))
else : print('{} is not a prime number'.format(n))

prime=[]  # created an empty list to collect prime numbers in it

for num in range(2, 101):
    status = True
    for i in range(2, num):
        if num % i == 0: # check if the only factors are 1 and itself
            status = False
    if status:
        prime.append(num)  # collect prime numbers in the list

print(prime)