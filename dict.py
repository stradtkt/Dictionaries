fruit = {
  "orange": "a sweet orange, citrus fruit",
  "apple": "good for making cider",
  "lemon": "a sour lemon",
  "grape": "a small sweet fruit grown in bunches"
  }

fruit['pear'] = "an odd shaped apple"
fruit['lime'] = "great with tequila"

veg = {
  "cabbage": "every childs favorite",
  "sprouts": "mmm, lovely",
  "spinach": "can I have some more fruit please"
}
fruit.update(veg)
print(veg)
veg.update(fruit)
print(veg)

# fruit.clear() this clears the items in the dictionary

# while True:
#   dict_key = input("Please enter a fruit: ")
#   if dict_key == 'quit':
#     break
#   if dict_key in fruit:
#     description = fruit.get(dict_key)
#     print(description)
#   else:
#     print("We don't have a ", dict_key)
    

# for snack in fruit:
#   print(fruit[snack])

# for i in range(10):
#   for snack in fruit:
#     print (snack + " is " + fruit[snack])
#   print('-'* 40)

# ordered_keys = list(fruit.keys())
# ordered_keys.sort()
# ordered_keys = sorted(list(fruit.keys()))
# for f in ordered_keys:
#   print(f + " - " + fruit[f])

# for f in sorted(fruit.keys()):
#   print(f + " - " + fruit[f])

# for val in fruit.values():
#   print(val)

# print(fruit.items())
# f_tuple = tuple(fruit.items())
# print(f_tuple)

# for snack in f_tuple:
#   item, description = snack
#   print(item + " is " + description)

# print(dict(f_tuple))