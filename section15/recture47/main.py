class A:
    def __init__(self):
        self.__value = 1 #プライベート変数

class B:
    def __init__(self, name):
        super().__init__()
        self.name = name

class C(B):
    def __init__(self, name):
        super().__init__(name)
        self.value=10