from pydantic import BaseModel


class CreateCheckIn(BaseModel):
    customerName: str
    assetName: str
    assetValue :int
    
class DateCheckIn(BaseModel):
    date :str
