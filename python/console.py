  import math

def trn():
    print("""
  Triangulation
 """)
    x1 = int(input("x1: "))
    z1 = int(input("z1: "))
    l1 = float(input("ang1: "))
    print("")
    x2 = int(input("x2: "))
    z2 = int(input("z2: "))
    l2 = float(input("ang2: "))
    print("")

    k1 = math.tan(math.radians(-l1))
    k2 = math.tan(math.radians(-l2))

    z = (x1-x2-k1*z1+k2*z2)/(k2 - k1)
    x = k1*(z - z1) + x1
    print("")
    print("x: ", round(x),"  z: ", round(z))
    print("distance: ", round(math.dist([x2,z2],[x,z])))
    a = input()

    if a == ".trn3":
        trn3(1,x,z)
    else:
        print("looser")

def dist():
    print("""
  Distance
 """)
    x1 = int(input("x1: "))
    z1 = int(input("z1: "))
    print('')
    x2 = int(input("x2: "))
    z2 = int(input("z2: "))
    print('')
    print("distance: ", round(math.dist([x2,z2],[x1,z1])))  

def nethconv():
    print("""
  Nether coord. converter
 """)
    x1 = int(input("x: "))
    z1 = int(input("z: "))
    print("""
 Nether coordinates:
 """)
    print("x: ", round(x1/8), " z: ", round(z1/8))
    
def trn3(mode = 0, x = 0, z = 0):
    
    def rotation(x2,z2):
        z1 = z2*math.cos(math.radians(120))-x2*math.sin(math.radians(120))
        x1 = x2*math.cos(math.radians(120))+z2*math.sin(math.radians(120))
        return(x1,z1)
        
        if mode == 0:  
            x = float(input("x: "))
            z = float(input("z: "))
            cord = rotation(x,z)
            print("x: ", round(cord[0]),"y: ",round(cord[1]))
            cord1 = rotation(cord[0],cord[1])
            print("x: ", round(cord1[0]),"y: ",round(cord1[1]))
        else:
            cord = rotation(x,z)
            print("x: ", round(cord[0]),"y: ",round(cord[1]))
            cord1 = rotation(cord[0],cord[1])
            print("x: ", round(cord1[0]),"y: ",round(cord1[1]))
    
    
command = ''
helpinf = """
Comands:
   /trn - triangulation
   /dist - distance btw 2 points
   /nethconv - Convert cordinates Gw and Neth
   /trn3"""

while(command != '.exit'):
    command = input(">>")
    command = command.split()
    if command[0] == '.trn':
        trn()
    elif command[0] == '.dist':
        dist()
    elif command[0] == '.nethconv':
        nethconv()
    elif command[0] == '.exit':
        break
    elif command[0] == '.help':
        print(helpinf)
    elif command[0] == '.trn3':
        trn3()
    else:
        print("unknown command")
    
