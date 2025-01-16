from app.models.db_asset import CreateAsset
from app.db.database import db
from datetime import datetime,timedelta

async def create_asset(payload: CreateAsset):
    
    name = payload.name
    value = payload.value
    
    asset = await db.asset.create(
        data={
            'name': name,
            'value':value
        }
    )


    return {"details":
        {'name':asset.name,
         'value':asset.value
                       }
        }
    

async def get_asset():
    assets = await db.asset.find_many()
    
    details = [{'name': asset.name, 'value': asset.value} for asset in assets]
    
    return {"details":details}


async def add_asset(payload: CreateAsset):
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
    
  
async def get_date_asset(date: str):
    # Step 1: Fetch all check-in records filtered by the date
    query_date = datetime.strptime(date, "%Y-%m-%d")
    checkins = await db.checkin.find_many(where={"date": {
            "gte": (query_date - timedelta(days=2)).strftime("%Y-%m-%d"),
            "lte": query_date.strftime("%Y-%m-%d")
        }})
    print(checkins)
    # Step 2: Extract unique asset names from the check-in records
    checkin_asset_values = {checkin.assetName: checkin.assetValue for checkin in checkins}

    # Step 3: Fetch all assets from the Asset table
    assets = await db.asset.find_many()
    
    # Step 4: Update the asset values if they exist in the check-in records
    modified_assets = []
    for asset in assets:
        # If the asset name is found in check-in records, modify its value
        if asset.name in checkin_asset_values:
            subtracted_value = asset.value - checkin_asset_values[asset.name]
            modified_assets.append({"name": asset.name, "value": subtracted_value})
        else:
            # If not found in check-in records, keep the original value
            modified_assets.append({"name": asset.name, "value": asset.value})

    # Step 5: Return the modified Asset table
    return {"date": date, "modifiedAssets": modified_assets}


    
    
