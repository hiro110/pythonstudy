#numbers = [1,5,6,11,3,5,7,3]
#squares = [num**2 for num in numbers]
#print(squares)

words = ['django', 'python', 'tkinter']
#upper_words = [word.upper() for word in words]
# 左のfor文から評価 (for word in words) -> (for char in word)
one_word = [char for word in words for char in word]
print(one_word)

even_numbers = [x for x in range(1, 11) if x %2 == 0]
print(even_numbers)

#table = [[x * y for x in range(1, 10)] for y in range(1, 10)]
table = [[0 for x in range(5)] for y in range(5)]
print(table)

sets = {x:'デフォルト値' for x in range(10)}
print(sets)

score = {'math':80, 'eng':20}
new_score = {value:key for key, value in score.items()}
print(new_score)