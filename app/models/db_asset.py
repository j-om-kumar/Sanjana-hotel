from pydantic import BaseModel


class CreateAsset(BaseModel):
    name: str
    value :int
    
