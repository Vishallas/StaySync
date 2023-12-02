from typing import List
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

class Base(DeclarativeBase):
    pass

# class Outing(Base):
#     __tablename__ = "outing"
#     oid: Mapped[int] = mapped_column(primary_key=True)
#     sid: Mapped[int] = = mapped_column(ForeignKey("student.sid"))
#     exit: Mapped[]
#     fullname: Mapped[Optional[str]]
#     addresses: Mapped[List["Address"]] = relationship(
#         back_populates="user", cascade="all, delete-orphan"
#     )
#     def __repr__(self) -> str:
#         return f"User(id={self.id!r}, name={self.name!r}, fullname={self.fullname!r})"

class Student(Base):
    __tablename__ = "student"
    sid: Mapped[str] = mapped_column(primary_key=True)
    sname: Mapped[str]
    passw:Mapped[str]
    dept: Mapped[str] 
    year: Mapped[int]
    room: Mapped[int]
    def __repr__(self) -> str:
        return f"Student(sid={self.sid!r}, sname={self.sname!r},passw={self.passw!r} dept={self.dept!r}, year={self.year!r}, room={self.room!r})"