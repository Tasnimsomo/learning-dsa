#initialize the 2 first fibonacci numbers
v1 = 0
v2 = 1

#print the first 2 fibonacci numbers
print(v1)
print(v2)

#calculate and print the next 18 fibonacci numbers
for _ in range(18):
    new_value = v1 + v2
    print(new_value)
    #update variable that holds 2 fibonacci numbers
    v1 = v2
    v2 = new_value
