from flask import Flask, render_template, request, redirect, url_for
import requests

app = Flask(__name__)

NEWS_API_KEY = 'pub_28783cf27bd01a39a34d31850d08ad638e93d'
NEWS_API_URL = 'https://newsdata.io/api/1/news'

def get_news(query):
    params = {
        'apikey': NEWS_API_KEY,
        'q': query,
        'language': 'en'
    }
    response = requests.get(NEWS_API_URL, params=params)
    return response.json()

@app.route('/', methods=['GET', 'POST'])
def home():
    query = 'technology'  # default query
    if request.method == 'POST':
        query = request.form.get('query', 'technology')
    
    news_data = get_news(query)
    articles = news_data.get('results', [])
    for article in articles:
        article['address'] = id(article)
    
    return render_template("index.html",articles=articles, query=query)
if __name__ == '__main__':
    app.run(debug=True,port=5000) # if project id not work then you change port number and run again same port which you mention in port=?


