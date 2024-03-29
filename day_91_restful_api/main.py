from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import random

'''
Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)
app.config['SECRET_KEY'] = 'some_secret_key'
##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy()
db.init_app(app)


##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        # Method 1. 
        # dictionary = {}
        # # Loop through each column in the data record
        # for column in self.__table__.columns:
        #     #Create a new dictionary entry;
        #     # where the key is the name of the column
        #     # and the value is the value of the column
        #     dictionary[column.name] = getattr(self, column.name)
        # return dictionary
        
        #Method 2. Altenatively use Dictionary Comprehension to do the same thing.
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}

with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")
    
@app.route("/random")
def get_random_cafe():
    result = db.session.execute(db.select(Cafe).order_by(Cafe.id.desc()))
    all_cafes = result.scalars().all()

    # Generate a random index to select a random cafe
    # total_cafes = len(all_cafes)
    # random_id = random.randint(0, total_cafes - 1)
    # random_cafe = all_cafes[random_id]
    
    # or use random.choice() because it is much simpler!
    random_cafe = random.choice(all_cafes)

    # Print random cafe information
    print(random_cafe.id)
    print(random_cafe.name)

    # return jsonify(
    #     id=random_cafe.id, 
    #     name=random_cafe.name, 
    #     map_url=random_cafe.map_url,
    #     location=random_cafe.location,
    #     seats=random_cafe.seats,
    #     has_toilet=random_cafe.has_toilet,
    #     has_wifi=random_cafe.has_wifi,
    #     has_sockets=random_cafe.has_sockets,
    #     can_take_calls=random_cafe.can_take_calls,
    #     coffee_price=random_cafe.coffee_price)

    # return jsonify(cafe={
    #     # Omit the id from the response
    #     # "id": random_cafe.id,
    #     "name": random_cafe.name,
    #     "map_url": random_cafe.map_url,
    #     "img_url": random_cafe.img_url,
    #     "location": random_cafe.location,
    #     # "seats": random_cafe.seats,
    #     # "has_toilet": random_cafe.has_toilet,
    #     # "has_wifi": random_cafe.has_wifi,
    #     # "has_sockets": random_cafe.has_sockets,
    #     # "can_take_calls": random_cafe.can_take_calls,
    #     # "coffee_price": random_cafe.coffee_price,
        
    #     #Put some properties in a sub-category (optional)
    #     "amenities": {
    #       "seats": random_cafe.seats,
    #       "has_toilet": random_cafe.has_toilet,
    #       "has_wifi": random_cafe.has_wifi,
    #       "has_sockets": random_cafe.has_sockets,
    #       "can_take_calls": random_cafe.can_take_calls,
    #       "coffee_price": random_cafe.coffee_price,
    #     }
    #     })

    return jsonify(cafe=random_cafe.to_dict())

@app.route("/all")
def get_all_cafes():
    result = db.session.execute(db.select(Cafe).order_by(Cafe.id.desc()))
    all_cafes = result.scalars().all()
    ## Convert each cafe to a dictionary and create a list of dictionaries:
    cafes_list = [cafe.to_dict() for cafe in all_cafes]
    return jsonify(cafe=cafes_list)

@app.route("/search")
def get_cafe_at_location():
    query_location = request.args.get("loc")
    result = db.session.execute(db.select(Cafe).where(Cafe.location == query_location))
    # Note, this may get more than one cafe per location
    all_cafes = result.scalars().all()
    if all_cafes:
        return jsonify(cafes=[cafe.to_dict() for cafe in all_cafes])
    else:
        return jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location."}), 404

@app.route("/add", methods=["POST"])
def add_new_cafe():
    new_cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("location"),
        has_sockets=bool(request.form.get("has_sockets")),
        has_toilet=bool(request.form.get("has_toilet")),
        has_wifi=bool(request.form.get("has_wifi")),
        can_take_calls=bool(request.form.get("can_take_calls")),
        seats=request.form.get("seats"),
        coffee_price=request.form.get("coffee_price"),
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe."}), 200

## HTTP GET - Read Record

## HTTP POST - Create Record

## HTTP PUT/PATCH - Update Record
# Updating the price of a cafe based on a particular id:
@app.route("/update-price/<int:cafe_id>", methods=["PATCH"])
def update_price(cafe_id):
    new_price = request.args.get("new_price")
    all_cafes = db.session.execute(db.select(Cafe)).scalars()
    all_cafe_ids = [cafe.id for cafe in all_cafes]
    if cafe_id in all_cafe_ids:
        # cafe_to_update = db.get_or_404(Cafe, cafe_id)
        cafe_to_update = db.session.execute(db.select(Cafe).where(Cafe.id == cafe_id)).scalar()
        cafe_to_update.coffee_price = new_price
        db.session.commit()
        ## Just add the code after the jsonify method. 200 = Ok
        return jsonify(response={"success": "Successfully updated the price"}), 200
    else:
        #404 = Resource not found
        return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database"}), 404

## HTTP DELETE - Delete Record
# Deletes a cafe with a particular id.
@app.route("/report-closed/<int:cafe_id>", methods=["DELETE"])
def delete_cafe(cafe_id):
    api_key = request.args.get("api-key")
    all_cafes = db.session.execute(db.select(Cafe)).scalars()
    all_cafe_ids = [cafe.id for cafe in all_cafes]
    if api_key == "TopSecretAPIKey":
        if cafe_id in all_cafe_ids:
            # cafe_to_delete = db.get_or_404(Cafe, cafe_id)
            cafe_to_delete = db.session.execute(db.select(Cafe).where(Cafe.id == cafe_id)).scalar()
            db.session.delete(cafe_to_delete)
            db.session.commit()
            ## Just add the code after the jsonify method. 200 = Ok
            return jsonify(response={"success": "Successfully removed the cafe from the database."}), 200
        else:
            #404 = Resource not found
            return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database"}), 404
    else:
        #403 = Forbidden
        return jsonify(error={"Forbidden": "Sorry, that's not allowed. Make sure you have the correct api key."}), 403

if __name__ == '__main__':
    app.run(debug=True)
