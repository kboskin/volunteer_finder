import uuid
from datetime import datetime
from uuid import UUID

from app.profile.user import DbUser
from app.profile.user.tables import UserTable
from enigine import DB, session


class UserService:
    @classmethod
    async def get_user_by_phone(cls, phone):
        result = session.query(DbUser).filter_by(phone_number=phone).first()
        return result

    @classmethod
    async def update_user_profile(cls, phone: str, user: dict):
        query = UserTable.update(). \
            where(UserTable.c.phone_number == phone). \
            values(**user, updated_time=datetime.utcnow()).returning(UserTable)
        user = await DB.fetch_one(query)
        return user

    @classmethod
    async def create_user_profile(cls, phone: str):
        query = UserTable.insert().values(
            {"user_id": uuid.uuid4(), "phone_number": phone, "is_active": True, "created_time": datetime.utcnow(),
             "updated_time": datetime.utcnow()})

        await DB.execute(query)
        return await cls.get_user_by_phone(phone)
