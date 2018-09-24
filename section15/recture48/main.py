class Person:
    
    def __init__(self, name):
        self.name  = name   # name.setterのnameメソッド呼び出し _nameに格納される

    @property
    def name(self):
        """self.nameやperson.nameとアクセスすると、このメソッドが呼び出される """
        return self._name

    @name.setter
    def name(self, value):
        """ self.name= やperson.name= で呼び出される。 _nameに格納する"""
        if not value:
            value = '名無しの権兵衛'
        self._name = value

person = Person('')
print(person.name)
