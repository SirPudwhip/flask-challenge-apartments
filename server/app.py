from flask import Flask, make_response, request
from flask_migrate import Migrate
from flask_restful import Api, Resource
import ipdb

from models import db, Apartment, Tenant, Lease

app = Flask( __name__ )
app.config[ 'SQLALCHEMY_DATABASE_URI' ] = 'sqlite:///apartments.db'
app.config[ 'SQLALCHEMY_TRACK_MODIFICATIONS' ] = False

migrate = Migrate( app, db )
db.init_app( app )
api = Api(app)


class Apartments(Resource):
    def get(self):
        apartments = [a.to_dict(only=('id', 'number')) for a in Apartment.query.all()]
        return make_response(
            apartments,
            200
        )
    
    def post(self):
        data = request.get_json()
        new_record = Apartment(
            number=data['number']
        )

        db.session.add(new_record)
        db.session.commit()

        response_dict = new_record.to_dict()

        response = make_response(
            response_dict,
            201,
        )

        return response

api.add_resource(Apartments, '/apartments')

if __name__ == '__main__':
    app.run( port = 3000, debug = True )

