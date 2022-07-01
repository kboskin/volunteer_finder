import uuid
from datetime import datetime

from app.profile.user.tables import User
from enigine import session


class UserService:
    @classmethod
    async def get_user_by_phone(cls, phone):
        result = session.query(User)\
            .filter_by(phone_number=phone)\
            .first()
        return result

    @classmethod
    async def update_user_profile(cls, phone: str, user: dict):
        session.query(User) \
            .filter(User.phone_number == phone) \
            .update({**user, 'updated_time': datetime.utcnow()}) \
            .commit()

        return await cls.get_user_by_phone(phone)

    @classmethod
    async def create_user_profile(cls, phone: str):
        session.add(
            User(
                **{"user_id": uuid.uuid4(),
                   "phone_number": phone,
                   "is_active": True,
                   "created_time": datetime.utcnow(),
                   "updated_time": datetime.utcnow()
                   }
            )
        )
        session.commit()
        return await cls.get_user_by_phone(phone)
