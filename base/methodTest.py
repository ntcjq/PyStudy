import math

la = [1,2,3,4,5]

def test():
    la.append(9)
    for idx,x in enumerate(la):
        if(len(la) -1 == idx):
            print(x)
        else:
            print(x, end=" ")