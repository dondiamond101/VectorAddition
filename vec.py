
#2d Vector
class twDvector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

#3d Vector
class thDvector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

#2d vector defining
def twDvecDefine():
    x = input("X: ")
    y = input("Y: ")
    newVec = twDvector(x, y)
    return newVec
#2d Vecotr addition
def twDvecAdd(Vec1, Vec2):
    sumX = int(Vec1.x) + int(Vec2.x)
    sumY = int(Vec1.y) + int(Vec2.y)
    return sumX, sumY
#2d Vector subtraction
def twDvecSub(Vec1, Vec2):
    sumX = int(Vec1.x) - int(Vec2.x)
    sumY = int(Vec1.y) - int(Vec2.y)
    return sumX, sumY
#2d Vector multiplication
def twDvecMult(Vec1, Vec2):
    sumX = int(Vec1.x) * int(Vec2.x)
    sumY = int(Vec1.y) * int(Vec2.y)
    return sumX, sumY


#3d vector defining
def thDvecDefine():
    x = input("X: ")
    y = input("Y: ")
    z = input("Z: ")
    new3dVec = thDvector(x, y, z)
    return new3dVec
#3d Vecotr addition
def thDvecAdd(Vec1, Vec2):
    sumX = int(Vec1.x) + int(Vec2.x)
    sumY = int(Vec1.y) + int(Vec2.y)
    sumZ = int(Vec1.z) + int(Vec2.z)
    return sumX, sumY, sumZ
#3d Vector subtraction
def thDvecSub(Vec1, Vec2):
    sumX = int(Vec1.x) - int(Vec2.x)
    sumY = int(Vec1.y) - int(Vec2.y)
    sumZ = int(Vec1.z) - int(Vec2.z)
    return sumX, sumY, sumZ
#3d Vector multiplication
def thDvecMult(Vec1, Vec2):
    sumX = int(Vec1.x) * int(Vec2.x)
    sumY = int(Vec1.y) * int(Vec2.y)
    sumZ = int(Vec1.z) * int(Vec2.z)
    return sumX, sumY, sumZ


addSub = input("Do you want to add, sub, or mult: ")
thTW = input("3d or 2d vector: ")

if addSub == 'add':
    if thTW == '3d':
        vect1 = thDvecDefine()
        vect2 = thDvecDefine()
        sum = thDvecAdd(vect1, vect2)
        print(sum)
    elif thTW == '2d':
        vect1 = twDvecDefine()
        vect2 = twDvecDefine()
        sum = twDvecAdd(vect1, vect2)
        print(sum)
    else:
        print("Choose a valid option.")
elif addSub == 'sub':
    if thTW == '3d':
        vect1 = thDvecDefine()
        vect2 = thDvecDefine()
        sum = thDvecSub(vect1, vect2)
        print(sum)
    elif thTW == '2d':
        vect1 = twDvecDefine()
        vect2 = twDvecDefine()
        sum = twDvecSub(vect1, vect2)
        print(sum)
    else:
        print("Choose a valid option.")
elif addSub == 'mult':
    if thTW == '3d':
        vect1 = thDvecDefine()
        vect2 = thDvecDefine()
        sum = thDvecMult(vect1, vect2)
        print(sum)
    elif thTW == '2d':
        vect1 = twDvecDefine()
        vect2 = twDvecDefine()
        sum = twDvecMult(vect1, vect2)
        print(sum)
    else:
        print("Choose a valid option.")
