v1 = 0
v2 = 1
print(v1)
print(v2)

counter = 2
def recursive(v1, v2):
    global counter
    if counter <= 18:
        new_value = v1 + v2
        print(new_value)
        counter += 1
        recursive(v2, new_value)

recursive(v1, v2)
