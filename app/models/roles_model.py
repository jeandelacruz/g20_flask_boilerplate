from app.models import BaseModel
from sqlalchemy import Column, Integer, String, Boolean


class RoleModel(BaseModel):  # role_model
    __tablename__ = 'roles'

    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(30))
    status = Column(Boolean, default=True)
