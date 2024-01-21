from flask import Flask, jsonify
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)

@app.route('/api/xbox-store-data', methods=['GET'])
def xbox_store_data():
    # URL Xbox Store Турция
    url = 'https://www.microsoft.com/tr-tr/store/top-paid/games/xbox'
    
    # Запрос HTML
    response = requests.get(url)
    content = response.text

    # Используем BeautifulSoup для парсинга HTML
    soup = BeautifulSoup(content, 'html.parser')

    # Извлекаем данные с использованием CSS-селекторов
    games = soup.select('.m-channel-placement-item')

    # Список для хранения данных
    data = []

    for game in games:
        title = game.select_one('h3 a').text.strip()
        price = game.select_one('.c-price').text.strip()
        data.append({"title": title, "price": price})

    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)