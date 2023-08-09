from flask import Flask
from recommendation.logger import logging

app = Flask(__name__)


@app.route('/', methods=['GET','POST'])

def index():
    logging.info('We are start the project based on Book Recommendation System')
    return 'Hello...  Hi , My Project name is Book Recommendation System'

if __name__=='__main__':
    app.run(debug=True)