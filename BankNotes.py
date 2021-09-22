#we require four parameters / we have to post them in our fontend 
#pydantic = enforces type hints at runtime and provides user friendly errors when the data is unvalid

from pydantic import BaseModel
class BankNote(BaseModel):
    variance = float
    skewness = float
    curtosis = float
    entropy = float
