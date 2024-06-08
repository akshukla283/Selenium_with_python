
ItemsInCart = 0
# 2 items will be added to cart

# try, catch

# will use some file name which is not exist to catch error
try:
    with open("test_new.txt") as file:
        content = file.read()
        print(content)

except Exception as e:
    print(e)

finally:
    print("It's from \"finally\" block")
    print("this method always execute whether any failure or not")