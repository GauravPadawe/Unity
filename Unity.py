a = [1, 2, 4, 6, 8]
b = [5, 9, 10, 4, 2, 8]

def unity(a, b):                  # Passing the above list
    for i in b:                   # for "i" as individual value in b
        if i not in a:            # if "i" is not present in a
            a.append(i)           # Modify a
            
print (unity(a, b))
print (a)

# CODED BY - GAURAV PADAWE
