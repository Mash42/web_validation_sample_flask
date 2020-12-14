from flask import Flask, render_template, request
import pymysql
import requests
import re
from flask import Markup
import MeCab
from wordcloud import WordCloud

app = Flask(__name__)

# ホーム
@app.route('/', methods=["GET", "POST"])
def index():
    return render_template("index.html", mail_address="")

# ワードクラウド作成
@app.route('/validation', methods=["GET", "POST"])
def validation():
    mail_address = ""
    if request.method == "POST":
        mail_address = request.form['mail_address']
        error_message = mail_address_validation(mail_address)
        
    return render_template("index.html"
                          ,error_message=error_message
                          ,mail_address=mail_address)



def mail_address_validation(mail_address):
    error_message = 'メールアドレスの形式になっていました！！'
    result = re.fullmatch(r'^[0-9a-zA-Z_\.]+@([0-9a-zA-Z])+\.([0-9a-zA-Z\.])+([0-9a-zA-Z])+$', mail_address)
    
    if result is None:
        error_message = 'メールアドレスの形式になっていません。'

    return error_message
# アプリ起動
if __name__ == '__main__':
    app.run(host="localhost", port=5000, debug=True)
