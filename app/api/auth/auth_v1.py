from flask import request
from app.model import query
from app.api.auth import auth_bp

@auth_bp.route("/signup", methods = ["POST"])
def insert_user():
    if(query.check_sign_up(request.json['id'])):
        query.create_student(id=request.json['id'],
                              name=request.json['sname'],
                              passw=request.json['passw'],
                              dept=request.json['dept'],
                              roomno = request.json['room'],
                              year = request.json['year'])
        return {'Status':'Success'}
    else:
        return {'Status':'Fail',
                'reason':'user exist'}

@auth_bp.route('/login',methods=['POST'])
def login():
    if query.check_login(request.json['id'],request.json['passw']):
        return {'Status':'Success'}
    else:
        return {'Status':'Fail',
                'reason':'wrong id-password'}
    
