from app.models import BaseModel
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from bcrypt import hashpw, gensalt, checkpw


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

    role = relationship('RoleModel', uselist=False)

    def hash_password(self):
        password_encode = self.password.encode('utf-8')
        password_hash = hashpw(password_encode, gensalt(rounds=10))
        self.password = password_hash.decode('utf-8')

    def check_password(self, password):
        return checkpw(
            password.encode('utf-8'),
            self.password.encode('utf-8')
        )
