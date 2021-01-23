from typing import NoReturn
from flask import Flask, render_template
app = Flask(__name__)

class UserInfo:
  def __init__(self, name, age, id, path):
    self.name = name
    self.age  = age
    self.id   = id
    self.path = path

members = [
  UserInfo('太郎', 21, 1, 'image/taro.jpg'),
  UserInfo('二郎', 20, 2, 'image/jiro.jpg'),
  UserInfo('良子', 22, 3, 'image/ryoko.jpg'),
  UserInfo('花子', 21, 4, 'image/hanako.jpg'),
]

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/member')
def member():
  return render_template('member.html', members = members)

@app.route('/detail/<int:user_id>')
def detail(user_id):
  user_data = None
  for user in members:
    if user.id == user_id:
      user_data = user
  return render_template('detail.html', user_data = user_data)

@app.route('/conditions')
def conditions():
  return render_template('conditions.html')

@app.errorhandler(404)
def page_not_found(error):
  return render_template('not_found.html')

if __name__ == "__main__":
  # デバッグモードの追加はここ
  app.run(debug=True)