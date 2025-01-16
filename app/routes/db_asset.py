from fastapi import APIRouter, HTTPException,Depends,Request
from app.models.db_asset import CreateAsset
from app.services.db_asset import create_asset,get_asset,add_asset,get_date_asset

router = APIRouter()


@router.get("/assets") # To get all the assets from DB
async def get_asset_route():
    return await get_asset()

@router.get("/date/assets/{date}") # to get assets on a particular data in space of date u must enter the date example '2024-01-15'
async def get_date_asset_route(date):
    return await get_date_asset(date)

@router.post("/create-asset") # to create a new asset
async def create_asset_route(payload: CreateAsset):
    return await create_asset(payload)


@router.post("/add-asset") # to add or remove values for pre-existing assets
async def add_asset_route(payload: CreateAsset):
    return await add_asset(payload)
