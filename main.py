from flask import Flask, request, jsonify
from flask_cors import CORS
from db import create_table_news
import news_models
from flask_httpauth import HTTPBasicAuth
from flask_bcrypt import Bcrypt


app = Flask(__name__)
CORS(app)
auth = HTTPBasicAuth()
bcrypt = Bcrypt(app)


@app.route('/news', methods=['GET'])
def get_news():
    result = news_models.get_news()
    
    data = {
            
            'status': 200,
            'data': result
        
        }
    
    resp = jsonify(data)
    resp.status_code = 200
    
    return resp


@app.route('/news/<id>', methods=['GET'])
def get_news_by_id(id):
    try:
        result = news_models.get_news_by_id(id)
        data = {
                
                'status': 200,
                'data': result
            
            }
        
        resp = jsonify(data)
        resp.status_code = 200
        
        return resp
    except:
        data = {
                
                'status': 404,
                'message': "Data Not Found"
            
            }
        
        resp = jsonify(data)
        resp.status_code = 404
        
        return resp
      
    
@app.route('/news', methods=['POST'])
def insert_news():
    
    news_details = request.json
    title = news_details['title']
    content = news_details['content']
    datetime = news_details['datetime']
    result = news_models.insert_news(title, content, datetime)
    
    data = {
        
            'status': 201,
            'message': 'Success!'
        
        }
    
    resp = jsonify(data)
    resp.status_code = 201
    
    return resp


@app.route('/news/<id>', methods=['PUT'])
def update_news(id):
    
    news_details = request.json
    id = news_details['id']
    title = news_details['title']
    content = news_details['content']
    datetime = news_details['datetime']
    result = news_models.update_news(id, title, content, datetime)
    
    data = {
        
            'status': 200,
            'message': 'Success!'
        
        }
    
    resp = jsonify(data)
    resp.status_code = 200
    
    return resp


@app.route('/news/<id>', methods=['DELETE'])
def delete_news(id):
    result = news_models.delete_news(id)
    
    data = {
            
            'status': 200,
            'message': "Success!"
        
        }
    
    resp = jsonify(data)
    resp.status_code = 200
    
    return resp


@app.errorhandler(404)
def not_found(error=None):
    message = {
        
            'status': 404,
            'message': 'Not Found: ' + request.url
        }
    
    resp = jsonify(message)
    resp.status_code = 404
    
    return resp


if __name__ == "__main__":
    #create_table_students()
    #print(get_data())
    app.run(debug=True)