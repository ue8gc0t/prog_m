import math


def Main_Func(Xn,k):
    return(k*Xn-k*Xn*Xn)

def Firstfcount(Xn,k,i=0):
    while(i<10000):
        Xn = Main_Func(Xn,k)
        i = i+1
    return(Xn)

def Lasttcount(Xn,k,i=0):
    results = []
    Xn = Firstfcount(Xn,k)
    while(i<10):
        Xn = Main_Func(Xn,k)
        results.append(round(Xn,5))
        i = i + 1
    return(set(results))
    
def Main(Xn = 0.9, k = -2):
    while(k<=3):
        print("k = ",round(k, 1))
        Pk = (Lasttcount(Xn,k))
        print("len:",len(Pk))
        print(Pk)
        k = k+0.1
        input()
    while(k<=4):
        print("k = ",round(k, 2))
        Pk = (Lasttcount(Xn,k))
        print("len:",len(Pk))
        print(Pk)
        k = k+0.01
        input()
Main()




    
