from flask import Blueprint, request, jsonify
from flask_jwt_extended import (
    create_access_token, jwt_required, get_jwt_identity
)
from models.database import get_db_connection
from config import Config   
from utils.hash_password import CheckPassword, HashPassword

auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    hashed = HashPassword(password)
    
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        cursor.execute('INSERT INTO users123 (username, password) VALUES (%s, %s)', (username, hashed))
        conn.commit()
        
        return jsonify({'message': 'data inserted successfully'}), 200
    except:
        return jsonify({'message': 'data insertion failed'}), 500
    finally:
        cursor.close()
        conn.close()
        
@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try: 
        cursor.execute('SELECT id, username, password FROM users123 WHERE username = %s', (username,))
        user = cursor.fetchone()
        
        if user and CheckPassword(user['password'], password):
            access_token = create_access_token(identity=str(user['id']))
            return jsonify({'access_token': access_token, 'message': 'login successful'}), 200
    except:
        return jsonify({'message': 'login failed'})
    finally:
        cursor.close()
        conn.close()
        
        
@auth_bp.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    curr_user = get_jwt_identity()
    return jsonify({'message': curr_user}), 200