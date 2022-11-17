# Dictionary: Key-Value pairs, Unordered, Mutable
mydict = {"name": "Max", "age": 28, "city": "New York"}
print(mydict)

# various way to delete key-value pair
# del mydict["name"]
# mydict.pop("name")
# mydict.popitem()
# print(mydict)

# key must be hashable, therefore, numbers and tuples can be used as keys,
# but list, which is mutable, is unhashable and can't be used as keys
