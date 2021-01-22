from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
  name = 'Hello World!'
  return name

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