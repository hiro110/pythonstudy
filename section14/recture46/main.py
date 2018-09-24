class A:
    def __init__(self):
        self.number = 10    #インスタンス変数

class B:
    number = 10             #クラス変数

#a = A()
#print(a.number)

#b = B()
#print(b.number)

print(B.number)
#print(A.number)