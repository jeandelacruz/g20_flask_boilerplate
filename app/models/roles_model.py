from app import db
from sqlalchemy import Column, Integer, String, Boolean


class RoleModel(db.Model):  # role_model
    __tablename__ = 'roles'

    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(30))
    status = Column(Boolean, default=True)
