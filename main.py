from flask import Flask
import random
app = Flask(__name__)

facts_list= ["Teknolojik bağımlılıktan mustarip olan çoğu kişi, kendilerini şebeke kapsama alanı dışında bulduklarında veya cihazlarını kullanamadıkları zaman yoğun stres yaşarlar."," 2018 yılında yapılan bir araştırmaya göre 18-34 yaş arası kişilerin %50'den fazlası kendilerini akıllı telefonlarına bağımlı olarak görüyor.","Teknolojik bağımlılık çalışması, modern bilimsel araştırmanın en ilgili alanlarından biridir.", "bunu görme şansın %0,00001!"]

aa = ["bir roblox gift kodu! :AD64 AWW7 U448 Q983", "Diğer zaman iyi şanslar dilerim"]
@app.route("/")
def home():
    return f'<h1>MERHABA! Bu sayfada, teknolojik bağımlılıklar hakkında birkaç ilginç gerçeği öğrenebilirsiniz!<a href="/random_fact">Rastgele bir gerçeği görüntüle!</a>'

@app.route("/random_fact")
def hello_world():
    return f'<p>{random.choice(facts_list)}</p>'

@app.route("/secret")
def hello_world2():
    return f'<p>{random.choice(aa)}</p>'


app.run(debug=True)