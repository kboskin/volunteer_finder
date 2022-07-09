from fastapi import Request

from fastapi import APIRouter, Depends

from app.catalogue.catalogue import CatalogueService
from app.generic.base import BaseSuccessResponse, object_as_dict
from app.profile.user.tables import User

catalogueRouter = APIRouter()


@catalogueRouter.get("/")
async def get_catalogue():
    categories = await CatalogueService.get_catalogue()

    return BaseSuccessResponse({"categories": [object_as_dict(item) for item in categories]})
