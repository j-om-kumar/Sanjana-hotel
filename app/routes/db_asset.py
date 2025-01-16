from fastapi import APIRouter, HTTPException,Depends,Request
from app.models.db_asset import CreateAsset
from app.services.db_asset import create_asset,get_asset,add_asset,get_date_asset

router = APIRouter()


@router.get("/assets")
async def get_asset_route():
    return await get_asset()

@router.get("/date/assets/{date}")
async def get_date_asset_route(date):
    return await get_date_asset(date)

@router.post("/create-asset")
async def create_asset_route(payload: CreateAsset):
    return await create_asset(payload)


@router.post("/add-asset")
async def add_asset_route(payload: CreateAsset):
    return await add_asset(payload)
