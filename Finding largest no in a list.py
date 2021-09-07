number = [5, 1010, 33, 44, 55, 66, 88, 99, 1010, 90, 88, 5555 ]
max = number[0]
for x in number:
    if x > max: # x<max (lowest num)
        max = x
print(max)
