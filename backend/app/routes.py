from flask import Blueprint, request, jsonify, flash, render_template
from .models import User, db

bp = Blueprint('routes', __name__)

@bp.route('/api/users/signup', methods=['POST'])
def signup():
    data = request.get_json()
    if request.method == 'POST':
        email = data.get('email')
        first_name = data.get('firstName')
        password1 = data.get('password1')
        password2 = data.get('password2')
        
    user = User.query.filter_by(email=email).first()
    if user:
        return jsonify({'error': 'Email already exists.'}), 400
    elif len(email) < 4:
        return jsonify({'error': 'Email must be greater than 3 characters.'}), 400
    elif len(first_name) < 2:
        return jsonify({'error': 'First name must be greater than 1 character.'}), 400
    elif password1 != password2:
        return jsonify({'error': 'Passwords don\'t match.'}), 400
    elif len(password1) < 7:
        return jsonify({'error': 'Password must be at least 7 characters.'}), 400
    else:
        new_user = User(email=email, first_name=first_name)
        new_user.set_password(password1)
        db.session.add(new_user)
        db.session.commit()
    
    return jsonify({'message': 'User created successfully'}), 201

@bp.route('/api/users/login', methods=['POST'])
def login():
    data = request.get_json()
    emil = data.get('email')
    password = data.get('password')
    
    user = User.query.filter_by(emil=emil).first()
    
    if user and user.check_password(password):
        return jsonify({'message': 'User logged in successfully'}), 200.
    else:
        return jsonify({'error': 'Invalid credentials'}), 401
    
