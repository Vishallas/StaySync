from flask import Flask, request
import dotenv, os
from sqlalchemy import create_engine,select
from sqlalchemy.orm import Session
from model import Student
import hashlib

dotenv.load_dotenv()
app = Flask(__name__)

HASH_SALT =b"@/$"

engine = create_engine(f"{os.environ.get('DB')}://{os.environ.get('DB_USER')}:{os.environ.get('DB_PASS')}@{os.environ.get('DB_HOST')}:{os.environ.get('DB_PORT')}/{os.environ.get('DB_NAME')}")

@app.route("/signup", methods = ["POST"])
def insert_user():

    sid = request.json['sid']
    sname = request.json['sname']
    passw = hashlib.sha256(HASH_SALT+request.json['passw'].encode()+HASH_SALT).hexdigest()
    dept = request.json['dept']
    room = request.json['room']
    year = request.json['year']

    with Session(engine) as session:

        row_exists = session.query(Student).filter_by(sid=sid).first() is None

        if row_exists:
            new_student = Student(sid=sid,sname=sname,passw=passw,dept=dept,room=room,year=year)
            session.add(new_student)
            session.commit()
            return {"status":"success"}
        
    return {"status":"fail"}

if __name__ == "__main__":
    app.run(host='0.0.0.0')