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