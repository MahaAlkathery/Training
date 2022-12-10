from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note, Order 
from . import db
import json

views = Blueprint('views', __name__)


@views.route('/home', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        onum = request.form.get('order')

        order = Order.query.filter_by(onum=onum).first()
        if order:
             return render_template("home.html",onum= order.onum, status=order.status, user= current_user) 
        else:
            flash('Order does not exists.', category='error')

    return render_template("home.html", user=current_user)

@views.route('/homeA', methods=['GET', 'POST'])
@login_required
def homeA():
    if request.method == 'POST':
        onum = request.form.get('order')
        status = request.form.get('status')

        user = Order.query.filter_by(onum=onum).first()
        if user:
            flash('Order already exists.', category='error')

        else:
            new_order = Order(onum=onum, status=status)
            db.session.add(new_order)
            db.session.commit()
            flash('Order added!', category='success')

    return render_template("homeA.html", user=current_user)

@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})