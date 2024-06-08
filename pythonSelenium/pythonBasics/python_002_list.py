# we can add same data type variable
a = "Hello"
b = "World"
print(a + " " + b)

# List in python can store different data type
values = [1, 1.34, "Hello", 4, 5]
# we can get values from list using index
print(values[2])
# print last value
print(values[-1])
# want sub list
print(values[1:3])
# we can insert word

values.insert(3, "Ankit")
print(values)
# add value at end of the list
values.append("Latest")
print(values)
# update the value
values[-1] = "Shukla"
print(values)
# clear the list
values.clear()
print(values)
# completely delete
del values
# print(values)