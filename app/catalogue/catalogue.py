from app.catalogue.tables import Categories
from enigine import session


class CatalogueService:
    @classmethod
    async def get_catalogue(cls):
        return session.query(Categories).all()
