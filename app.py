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

    @app.route('/api/obtener-tasa-bcv')
    def getTasaBCV():
        url = "https://www.bcv.org.ve"
        response = requests.get(url, verify=False)

        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            data_elements = soup.find_all('div', class_='recuadrotsmc')
            date_elements = soup.find('div', class_='dinpro').find('span').text.strip()  

            tasa_data = []
            for element in data_elements:
                divisa = element.find('span').text.strip() 
                image = element.find('img').get('src')
                price = element.find('strong').text.strip()  
                tasa_data.append({'name': divisa, 'price': price, 'image': url+image, 'date': date_elements})
            return jsonify(tasa_data)
        else:
            error = {'error': 'Ocurrio un error interno'}
            return jsonify(error)
    
    return app

if __name__ == '__main__':
  app = crear_app()
  app.run()












