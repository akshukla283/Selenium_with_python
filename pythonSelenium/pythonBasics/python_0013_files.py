# we can open file using 'with' it will
# automatically close once operation completed

# there is method, read (r), write(w), append(a) methods...

# let's do some exercise, read all content and reverse it and write back to file
with open("test.txt", 'r') as reader:
    content = reader.readlines()
    # now reversing the content
    reversed(content)
    # open the file again with 'w' mode
    with open("test.txt", 'w') as writer:
        for line in reversed(content):
            writer.write(line)
