a=40
b=36
c=30
d=a-b
e=b-c
if d<e:
    print("the second time")
elif d == e:
    print(' two training has the same influence.')
elif d>e:
    print("the first time")

# Results: e is greater, and the second training regime is better. 


X = True
Y = False

W = X or Y


print("W:", W)


# X | Y | W 
# -------------------
# T | F | T 
# F | T | T  
# F | F | F  
# T | T | T  
