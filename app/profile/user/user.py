from app.profile.user.tables import UserTable
from main import DB


class LoginException(Exception):
    pass


class UserService:
    @classmethod
    async def get_user_by_phone(cls, phone):
        select_query = UserTable.select().where(UserTable.c.phone == phone)
        return await DB.fetch_one(select_query)
