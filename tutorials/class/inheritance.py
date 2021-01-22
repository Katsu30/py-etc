class Car(object):
  def __init__(self, model = None):
    self.model = model

  def run(self):
    print('run')

class ToyotaCar(Car):
  # メソッドの上書きも可能
  def run(self):
    print('fast')

class TeslaCar(Car):
  # 継承クラスでもコンストラクタを作成可能
  def __init__(self, model = 'Model S', enable_auto_run = False):
    # super()で継承元クラスのコンストラクタを利用できる
    super().__init__(model)
    self.enable_auto_run = enable_auto_run

  # 継承クラスの中でも新しいメソッドを記述可能
  def auto_run(self):
    print('self run')

car = ToyotaCar('Lexus')
print(car.model)
car.run()

tesla_car = TeslaCar('Model S')
print(tesla_car.model)
tesla_car.run()
tesla_car.auto_run()