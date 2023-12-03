from app.model.models import Student
from app import db
from app.hashing import password
from flask import jsonify

def check_sign_up(sid):
    q = Student.query.filter_by(id=sid).first()
    print(q)
    return q is None

def check_login(sid,passw):
    hpassw = password.form_password(passw)
    q = Student.query.filter_by(id=sid,passw=hpassw).first()
    print(q)
    return q is not None

def create_student(id, name, passw, dept, roomno, year):
    new_obj = Student(
            id=id,
            name=name,
            passw=password.form_password(passw),
            dept=dept,
            room=roomno,
            year=year
    )
    db.session.add(new_obj)
    db.session.commit()

def getUsers():
    q = Student.query.all()
    users = []
    for i in q:
        users.append(i.ret_dict())
    return jsonify(users)