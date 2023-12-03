from app.api.manage_user import user_manag_bp
from flask import request
from app.model import query

@user_manag_bp.route('/users',methods=['GET'])
def users():
    if request.method == 'GET':
        return query.getUsers()
    