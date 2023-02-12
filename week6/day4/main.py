#exercise 1
my_fav_numbers = {8,18,32,48,49}
print(my_fav_numbers)
my_fav_numbers.add(46)
my_fav_numbers.add(465)
print(my_fav_numbers)
my_fav_numbers.pop()
print(my_fav_numbers)
friend_fav_numbers ={50,222,33,44}
print(friend_fav_numbers)
our_fav_numbers= my_fav_numbers.union(friend_fav_numbers)
print(our_fav_numbers)

#exercise 2
#tuples are immutable so you cannot add items to it.
# (the way you can do it is to convert the tuple to a list and then add)

#exercise 3


sample_dict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"

}
keys_to_remove = ["name", "salary"]

for key in keys_to_remove:
    if key in sample_dict:
        del sample_dict[key]
print(sample_dict)