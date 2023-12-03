from app import db

class Student(db.Model):
    __tablename__ = "student"
    id = db.Column(db.String,primary_key = True)
    name = db.Column(db.String,nullable=False)
    passw = db.Column(db.String,nullable=False)
    dept = db.Column(db.String,nullable=False)
    room = db.Column(db.String,nullable=False)
    year = db.Column(db.String,nullable=False)

    def __init__(self,id,name,passw,dept,room,year):
        self.id = id
        self.name = name
        self.passw = passw
        self.dept = dept
        self.room = room
        self.year = year

    def __repr__(self) -> str:
        return f"Student(sid={self.id!r}, sname={self.name!r}, dept={self.dept!r}, year={self.year!r}, room={self.room!r})"
    
    def ret_dict(self):
        return { 'id':self.id,
                'name':self.name,
                'dept':self.dept,
                'room':self.room,
                'year':self.year
            }
