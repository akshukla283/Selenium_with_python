# 'for' loop
val = [1, 3, 5, 10]

for i in val:
    print(i)


# lop through val list and add all
list1 = [10, 20, 30, 50]
result = 0
for val in list1:
    result = result + val

print(f"Result : {result}")

# 'while' loop
# while loop continue till it get stopping condition
# so be careful when use 'while' loop

it = 4
while 4 <= it <= 10:
    print(it)
    it += 1

###############
print("======"*3)
# Important node
val = 10
while val > 1:
    if val == 9:  # at this step loop will stuck if don't provide any increment or decrement
        # because 'continue' statement will make skip all below step, so we have to provide one more condition here
        val = val -1
        continue
    if val == 3:
        break
    print(val)
    val = val - 1
