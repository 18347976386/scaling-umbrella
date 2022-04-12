from flask import Flask,render_template
import sqlite3

app = Flask(__name__)


@app.route('/')
def index():  # put application's code here
    return render_template('index.html')

@app.route('/index')
def home():  # put application's code here
    return render_template('index.html')

@app.route('/movie')
def movie():  # put application's code here
    datalist = []
    con = sqlite3.connect('movieTop.db')
    cur = con.cursor()
    sql = "select * from movieTop"
    data = cur.execute(sql)
    for item in data:
        datalist.append(item)
    # con.close()
    # cur.close()
    return render_template('movie.html',datalist=datalist)

@app.route('/score')
def score():  # put application's code here
    scorelis = []           # 评分
    numberlis = []          # 每个评分对应的数目
    con = sqlite3.connect('movieTop.db')
    cur = con.cursor()
    sql = "select score,count(score) from movieTop group by score"
    data = cur.execute(sql)
    for item in data:
        scorelis.append(item[0])
        numberlis.append(item[1])
    # con.close()
    # cur.close()
    return render_template('score.html',scorelis=scorelis,numberlis=numberlis)

@app.route('/wordcloud')
def wordcloud():  # put application's code here
    return render_template('wordcloud.html')

@app.route('/team')
def team():  # put application's code here
    return render_template('team.html')

if __name__ == '__main__':
    app.run()
