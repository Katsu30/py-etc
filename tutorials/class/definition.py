# Python2の名残りで(object)という表記が使用される
class Person(object):
  # コンストラクタ
  def __init__(self, name = 'Dean'):
    self.name = name
    print('first {}'.format(self.name))

  def say_something(self):
    print('Hello {}'.format(self.name))

  # デストラクタ
  def __del__(self):
    print('Good bye...')

person = Person()
person.say_something()