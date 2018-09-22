#def hello(text, name='匿名'):
#    print(name, text)
#
#hello(text='こんにちは')
#hello(text='こんにちは', name='hiroaki')


#def hello(*args, **kwargs):
#    print(args, kwargs)
#
#hello()
#hello('こんにちは', a=1)
#hello('こんばんは', 'hiroaki', 'ハロー', a=1, b=2, c=3)

def hello(text, *, name='hiroaki'):
    print(text, name)


hello('こんにちは')
hello('こんにちは', name='taro')