# mapping
from sqlalchemy.orm import mapper
import app.profile.user.tables

from app.profile.user.models import DbUser
from app.profile.user.tables import UserTable

mapper(DbUser, UserTable)
