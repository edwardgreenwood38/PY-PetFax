from flask import ( Blueprint, render_template )
import json

pets = json.load(open('pets.json'))
print(pets)

bp = Blueprint('pet', __name__, url_prefix="/pets")


# routes
@bp.route('/')
def index(): 
    return render_template('index.html', pets=pets)


@bp.route('/<pet_id>')
def show(pet_id): 
    pet = [pet for pet in pets if pet['pet_id'] == int(pet_id)][0]
    return render_template('show.html', pet=pet)
