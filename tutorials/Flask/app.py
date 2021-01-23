from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/home/<string:user_name>/<int:age>')
def home(user_name, age):
  # login_user = user_name
  login_user = {
    'name' : user_name,
    'age'  : age,
  }
  return render_template('home.html', login_user = login_user)

@app.route('/userlist')
def user_list():
  user_list = [
    'Taro', 'Jiro', 'Saburo', 'Shiro'
  ]
  return render_template('userlist.html', users = user_list)

@app.route('/good')
def good():
  name = 'Good!'
  return name

# 型指定と変数の間にはスペースはいらない
@app.route('/post/<int:post_id>')
def show_post(post_id):
  print(type(post_id))
  return 'post = {}'.format(post_id)

if __name__ == "__main__":
  # デバッグモードの追加はここ
  app.run(debug=True)