from flask import Flask, make_response
from flask_migrate import Migrate
from flask_restful import Api, Resource

from models import db, Apartment, Tenant, Lease

app = Flask( __name__ )
app.config[ 'SQLALCHEMY_DATABASE_URI' ] = 'sqlite:///apartments.db'
app.config[ 'SQLALCHEMY_TRACK_MODIFICATIONS' ] = False

migrate = Migrate( app, db )
db.init_app( app )
api = Api(app)

class Apartments(Resource):
    def get(self):
        apartments = [a.to_dict() for a in Apartments.query.all()]
        return make_response(
            apartments,
            200
        )
    
    def post(self):
        new_apartment = Apartment(
            number = request.form["number"]
        )
api.add_resource(Apartments, '/apartments')

if __name__ == '__main__':
    app.run( port = 3000, debug = True )