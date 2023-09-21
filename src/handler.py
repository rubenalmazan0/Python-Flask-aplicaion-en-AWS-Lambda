from flask import Flask, render_template
from dotenv import load_dotenv
import os

from config.mongodb import mongo
#carpeta + archivo + modulo
from routes.vacc import vaccine 

load_dotenv()

handler = Flask(__name__)

handler.config['MONGO_URI'] = os.getenv('MONGO_URI')
mongo.init_app(handler)

@handler.route('/')
def index():
    return render_template('index.html')

handler.register_blueprint(vaccine, url_prefix='/vaccine')

if __name__ == '__main__':
    handler.run(debug=True)



