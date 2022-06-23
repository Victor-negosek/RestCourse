import os 
from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager 

from resources.user import UserRegister, User, UserLogin
from resources.item import Item, ItemList
from resources.store import Store, StoreList


app= Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI', 'sqlite:///data.db')
app.config['SQLACHEMY_TRACK_MODIFICATION'] = False
app.secret_key = 'jose' #app.config['JWT_SECRET_KEY']
api = Api(app)

jwt = JWTManager(app) # not creating /auth

api.add_resource(Item, '/item/<string:name>') 
api.add_resource(ItemList, '/items') 
api.add_resource(Store, '/store/<string:name>') 
api.add_resource(StoreList, '/stores') 
api.add_resource(UserRegister, '/register')
api.add_resource(User, '/user/<int:user_id>')
api.add_resource(UserLogin, '/login')


if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)