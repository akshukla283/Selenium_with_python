file = open("test.txt")
# to read all content of the file
# print(file.read())
# read n number of character by passing parameter
# print(file.read(5))
# we can read file line by line
# print(file.readline())
# print(file.readline())

# use logic to print each line by using 'readline' method

# line = file.readline()
# while line != "":
#     print(line)
#     # stopping condition
#     line = file.readline()

# 'readlines' method
# it store all line in list

for line in file.readlines():
    print(line)

file.close()