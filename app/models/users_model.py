from app.models import BaseModel
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey


class UserModel(BaseModel):
    __tablename__ = 'users'

    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(120))
    last_name = Column(String(150))
    username = Column(String(80), unique=True)
    password = Column(String(255))
    email = Column(String(160), unique=True)
    rol_id = Column(Integer, ForeignKey('roles.id'))
    status = Column(Boolean, default=True)
