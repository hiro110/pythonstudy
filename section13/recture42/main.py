# ラムダ関数
#def my_sort(string):
#    return string[-1]

def price_sort(tpl):
    return tpl[1]

#my_list = ['python', 'django', 'tkinter', 'requests', 'kivy']
my_list = [('納豆', 78),('ヨーグルト', 90),('コーヒー',  120),('コーラ', 120),('鯖缶', 100)]
#my_list.sort(key=my_sort)
#my_list.sort(key=price_sort)
my_list.sort(key=lambda tpl:tpl[1])
print(my_list)

# lamda 引数:返す値
