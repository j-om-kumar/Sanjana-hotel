from fastapi import APIRouter, HTTPException,Depends,Request
from app.models.checkin import CreateCheckIn,DateCheckIn
from app.services.checkin import create_checkin,get_checkin,get_date_checkin

router = APIRouter()


@router.get("/check-in")
async def get_checkin_route():
    return await get_checkin()

@router.post("/create-checkin")
async def create_checkin_route(payload: CreateCheckIn):
    return await create_checkin(payload)

@router.post("/date/check-in")
async def get_date_checkin_route(payload:DateCheckIn):
    return await get_date_checkin(payload)

# @router.post("/add-checkin")
# async def add_asset_route(payload: CreateCheckIn):
#     return await add_asset(payload)
