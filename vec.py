
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
def twDvecDefine(x, y):
    newVec = twDvector(x, y)
    return newVec

#2d Vecotr addition
def twDvecAdd(Vec1, Vec2):
    sumX = int(Vec1.x) + int(Vec2.x)
    sumY = int(Vec1.y) + int(Vec2.y)
    newVec = twDvector(sumX, sumY)
    return newVec

#2d Vector subtraction
def twDvecSub(Vec1, Vec2):
    sumX = int(Vec1.x) - int(Vec2.x)
    sumY = int(Vec1.y) - int(Vec2.y)
    newVec = twDvector(sumX, sumY)
    return newVec
#2d Vector multiplication
def twDvecMult(Vec1, Vec2):
    sumX = int(Vec1.x) * int(Vec2.x)
    sumY = int(Vec1.y) * int(Vec2.y)
    newVec = twDvector(sumX, sumY)
    return newVec


#3d vector defining
def thDvecDefine(x, y, z):
    new3dVec = thDvector(x, y, z)
    return new3dVec


#3d Vecotr addition
def thDvecAdd(Vec1, Vec2):
    sumX = int(Vec1.x) + int(Vec2.x)
    sumY = int(Vec1.y) + int(Vec2.y)
    sumZ = int(Vec1.z) + int(Vec2.z)
    new3dVec = thDvector(sumX, sumY, sumZ)
    return new3dVec

#3d Vector subtraction
def thDvecSub(Vec1, Vec2):
    sumX = int(Vec1.x) - int(Vec2.x)
    sumY = int(Vec1.y) - int(Vec2.y)
    sumZ = int(Vec1.z) - int(Vec2.z)
    new3dVec = thDvector(sumX, sumY, sumZ)
    return new3dVec


#3d Vector multiplication
def thDvecMult(Vec1, Vec2):
    sumX = int(Vec1.x) * int(Vec2.x)
    sumY = int(Vec1.y) * int(Vec2.y)
    sumZ = int(Vec1.z) * int(Vec2.z)
    new3dVec = thDvector(sumX, sumY, sumZ)
    return new3dVec
