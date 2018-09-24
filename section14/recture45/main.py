# 親クラス
class Charcter:
    def __init__(self, name):
        self.name = name

    def show_profile(self):
        profile = '名前:{0} 種族:Charcter'.format(self.name)
        print(profile)

# 子クラス
class Monster(Charcter):
    def __init__(self, name):
        super().__init__(name)
        #self.name = name
        self.hp = 20

    def show_profile(self):
        profile = '名前:{0} 種族:Monster HP:{1}'.format(self.name, self.hp)
        print(profile)


#char_a = Charcter('キャラA')
#print(char_a.name)
monster_a = Monster('モンスターA')
#print(monster_a.name)
monster_a.show_profile()