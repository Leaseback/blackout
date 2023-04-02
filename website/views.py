from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Contract
from . import db
import json
from sqlalchemy import text

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    # if request.method == 'POST':
    #     note = request.form.get('contract')#Gets the note from the HTML
    #
    #     if len(note) < 1:
    #         flash('Note is too short!', category='error')
    #     else:
    #         new_note = Note(data=note, user_id=current_user.id)  #providing the schema for the note
    #         db.session.add(new_note) #adding the note to the database
    #         db.session.commit()
    #         flash('Note added!', category='success')

    return render_template("home.html", user=current_user)

@views.route('/users', methods=['GET'])
@login_required
def users():
    users = db.session.execute(text("SELECT * FROM user"))
    return render_template("users.html",user=current_user, users=users)

@views.route('/contracts/<int:contract_id>')
@login_required
def contract_page(contract_id):
    # code to fetch the contract data for the given contract_id
    contract_data = Contract.query.filter_by(id=contract_id).first()
    return render_template('contract.html', user=current_user, contract=contract_data)

# @views.route('/delete-note', methods=['POST'])
# def delete_note():
#     note = json.loads(request.data) # this function expects a JSON from the INDEX.js file
#     noteId = note['noteId']
#     note = Note.query.get(noteId)
#     if note:
#         if note.user_id == current_user.id:
#             db.session.delete(note)
#             db.session.commit()
#
#     return jsonify({})
