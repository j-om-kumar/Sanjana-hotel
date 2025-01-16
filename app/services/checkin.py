from app.models.checkin import CreateCheckIn,DateCheckIn
from app.db.database import db
from datetime import datetime

async def create_checkin(payload: CreateCheckIn):
    
    
    now = datetime.now().strftime("%Y-%m-%d")
    
    customerName = payload.customerName
    assetName = payload.assetName
    assetValue = payload.assetValue
    
    
    checkin = await db.checkin.create(
        data={
            'date': now,
            'customerName': customerName,
            'assetName': assetName,
            'assetValue' :assetValue
        }
    )

    return {"details":
        {
            'date': checkin.date,
            'customerName': checkin.customerName,
            'assetName': checkin.assetName,
            'assetValue' :checkin.assetValue
        }
        }
    

async def get_checkin():
    checkin = await db.checkin.find_many()
    
    details = [{'date': asset.date, 'name': asset.customerName,'assetValue':asset.assetValue} for asset in checkin]
    
    return {"details":details}

async def get_date_checkin(payload :DateCheckIn):
    date = payload.date
    
    checkin = await db.checkin.find_many(where={"date":date})
    
    details = [{'date': asset.date, 'name': asset.customerName,'assetValue':asset.assetValue} for asset in checkin]
    
    return {"details":details}


async def add_checkin(payload: CreateCheckIn):
    name = payload.name
    value = payload.value
    
    asset = await db.asset.find_first(where={'name':name})
    
    previous_value = asset.value

    updated_value = int(value + (previous_value))
    
    print(updated_value)
    asset = await db.asset.update(where={"id":asset.id},data={"value":updated_value})
    
    return {"details":
        {'name':asset.name,
         'value':asset.value
                       }
        }
    
    
    
