from flask import Flask, jsonify
from flask_cors import CORS
import requests
from bs4 import BeautifulSoup
from urllib3.exceptions import InsecureRequestWarning
from urllib3 import disable_warnings

disable_warnings(InsecureRequestWarning)

def crear_app():
    app = Flask(__name__)
    CORS(app, origins=['*'])

    #api para obtener la tasa del BCV
    @app.route('/api/obtener-tasa-bcv')
    def getTasaBCV():
        url = "https://www.bcv.org.ve"
        try:
            response = requests.get(
                url,
                headers={'User-Agent': 'Mozilla/5.0'},
                verify=False,
                timeout=15
            )
            response.raise_for_status()
        except requests.RequestException:
            return jsonify({
                'success': False,
                'error': 'No se pudo obtener la tasa del BCV',
                'message': 'La tasa del BCV no está disponible en este momento. Intenta nuevamente más tarde.'
            }), 502

        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            data_elements = soup.find_all('div', class_='recuadrotsmc')
            date_container = soup.find('div', class_='dinpro')
            date_elements = date_container.find('span').text.strip() if date_container and date_container.find('span') else ''

            tasa_data = []
            for element in data_elements:
                span = element.find('span')
                img = element.find('img')
                strong = element.find('strong')

                if not span or not img or not strong:
                    continue

                divisa = span.text.strip()
                image = img.get('src')
                price = strong.text.strip()
                tasa_data.append({'name': divisa, 'price': price, 'image': image})

            return jsonify({'date': date_elements, 'data': tasa_data})
        else:
            return jsonify({
                'success': False,
                'error': 'Ocurrió un error interno',
                'message': 'No se pudo cargar la tasa del BCV en este momento.'
            })
    
    return app

app = crear_app()

if __name__ == '__main__':
  app.run()












