from flask import ( Blueprint, render_template, url_for, redirect )
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


@bp.route('/facts/new')
def new_fact():
    return redirect(url_for('new_fact'))

# # Define a route to render a page with a link to the form
# Define a route to render a page with a link to the form
# @bp.route('/facts/new', methods=['GET', 'POST'])
# def link_to_form():
#     # Generate URL to the new_fact route
#     form_url = url_for('pet.new_fact')
#     return f'<a href="{form_url}">New fact</a>'
