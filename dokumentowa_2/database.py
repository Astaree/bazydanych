import os
from dotenv import load_dotenv
from mongoengine import Document, StringField, IntField, BinaryField, ListField, ReferenceField, DateTimeField, connect, \
    disconnect
from mongoengine.connection import get_db, register_connection


# Database structure:
# Delivery < ref - Order []
# Order    < embedded - Client (1 client)
#          < ref - Drink []
#          < ref - Meal []
# Meal     < embedded - ingredient []
#          < ref - picture []
# Drink    < ref - picture []
def disconnect_existing_connection():
    disconnect()


def check_and_create_collections():
    db = get_db(alias="default")

    # Check if collections exist
    if "client" not in db.list_collection_names():
        db.create_collection("client")

    if "drink" not in db.list_collection_names():
        db.create_collection("drink")

    if "meal" not in db.list_collection_names():
        db.create_collection("meal")

    if "order" not in db.list_collection_names():
        db.create_collection("order")

    if "delivery" not in db.list_collection_names():
        db.create_collection("delivery")


def connect_to_database():
    connect(name="restaurant", host=os.getenv("DATABASE_URL"), alias="default")


class Database:
    def __init__(self):
        load_dotenv()
        disconnect_existing_connection()
        connect_to_database()
        check_and_create_collections()


class Client(Document):  # Class needing CRUD
    name = StringField(required=True)
    address = StringField(required=True)
    phoneNumber = IntField(required=True)
    email = StringField(required=True)


class Ingredient(Document):  # Embedded class
    name = StringField(required=True)
    quantity = IntField(required=True)


class Picture(Document):  # Embedded class
    name = StringField(required=True)
    picture = BinaryField(required=True)


class Drink(Document):  # Class needing CRUD
    name = StringField(required=True)
    type = StringField(required=True)
    price = IntField(required=True)
    picture = ListField(ReferenceField(Picture))


class Meal(Document):  # Class needing CRUD
    name = StringField(required=True)
    description = StringField()
    averageTimeToCook = IntField(required=True)
    price = IntField(required=True)
    ingredients = ListField(
        ReferenceField(Ingredient, required=True),
        quantity=IntField()
    )
    picture = ListField(ReferenceField(Picture))


class Order(Document):  # Class needing CRUD
    client = ReferenceField(Client, required=True)
    drinks = ListField(
        ReferenceField(Drink, required=True),
        quantity=IntField()
    )
    meals = ListField(
        ReferenceField(Meal, required=True),
        quantity=IntField()
    )
    dateOfOrder = DateTimeField(required=True)
    dateOfDelivery = DateTimeField(required=True)
    status = StringField(required=True)


class Delivery(Document):  # Main class which references everything else, needs CRUD
    name = StringField(required=True)
    company = StringField(required=True)
    order = ListField(
        ReferenceField(Order, required=True)
    )
