from types import MethodDescriptorType
from flask import Flask, render_template, request

app = Flask(__name__)

class UserInfo:
  # コンストラクタの最後尾にカンマはいらない
  def __init__(self, last_name, first_name, job, gender, message):
    self.last_name  = last_name
    self.first_name = first_name
    self.job        = job
    self.gender     = gender
    self.message    = message

@app.route('/signup')
def sign_up():
  return render_template("signup.html")

@app.route('/home', methods=['GET', 'POST'])
def home():
  # GETリクエストで値を取得するにはrequest.args.get('')の形
  # user_info = UserInfo(
  #   request.args.get('last_name'),
  #   request.args.get('first_name'),
  #   request.args.get('job'),
  #   request.args.get('gender'),
  #   request.args.get('message'),
  # )

  # POSTリクエストで値を取得するにはrequest.form.get('')の形
  user_info = UserInfo(
    request.form.get('last_name'),
    request.form.get('first_name'),
    request.form.get('job'),
    request.form.get('gender'),
    request.form.get('message'),
  )

  return render_template('home.html', user_info = user_info)

if __name__ == '__main__':
  app.run(debug=True)