from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api, Resource
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates
from sqlalchemy.ext.associationproxy import association_proxy

db = SQLAlchemy()


class Apartment(db.Model, SerializerMixin): 
    __tablename__ = 'apartments'

    serialize_rules = ('-leases.apartment',)

    id = db.Column(db.Integer, PrimaryKey = True)
    number = db.Column(db.Integer)
    
    leases = db.relationship("Lease", backref="apartment")

class Tenant(db.Model, SerializerMixin):
    __tablename__ = 'tenants'

    serialize_rules = ('-leases.tenant',)

    id = db.Column(db.Integer, PrimaryKey = True)
    name = db.Column(db.String, nullable = False)
    age = db.Column(db.Integer)

    leases = db.relationship("Lease", backref='tenant')


    @validates('age')
    def validate_age(self, key, age):
        if age < 18:
            raise ValueError("You are not old enough")
        return age

    @validates('name')
    def validate_name(self, key, name): 
        if not name:
            raise ValueError("Name is required")
        elif name == "":
            raise ValueError("Name is required")
        return name

    def __repr__(self):
        return f'name = {self.name} and age = {self.age}'


class Lease(db.Model, SerializerMixin):
    __tablename__ = "leases"

    serialize_rules = ('-tenant.leases', '-apartment.leases',)

    id = db.Column(db.Integer, PrimaryKey = True)

    rent = db.Column(db.Integer)
    tenant_id = db.Column(db.Integer, ForeignKey= 'tenants.id')
    apartment_id = db.Column(db.Integer, ForeignKey = 'apartments.id')



