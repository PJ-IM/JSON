from Tools.scripts.patchcheck import status
from pydantic import BaseModel, validator, \
    ValidationError, PositiveInt, conint, constr, EmailStr
from typing import List, Optional
import json


#class

class OrderStatus(BaseModel):
    code: str
    orderCode: str
    orderPortalCode: str
    salesChannelCode: Optional = str
    status: int
    addresses: str
