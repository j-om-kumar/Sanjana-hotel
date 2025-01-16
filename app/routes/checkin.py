from fastapi import APIRouter, HTTPException,Depends,Request
from app.models.checkin import CreateCheckIn,DateCheckIn
from app.services.checkin import create_checkin,get_checkin,get_date_checkin

router = APIRouter()


@router.get("/check-in") # To get all the checkin's
async def get_checkin_route():
    return await get_checkin()

@router.post("/create-checkin") # To create a new check-in check CreateCheckIn for inputs
async def create_checkin_route(payload: CreateCheckIn):
    return await create_checkin(payload)

@router.post("/date/check-in") # to create a Check-in on a particular date check DateCheckIn for inputs
async def get_date_checkin_route(payload:DateCheckIn):
    return await get_date_checkin(payload)

# @router.post("/add-checkin")
# async def add_asset_route(payload: CreateCheckIn):
#     return await add_asset(payload)
