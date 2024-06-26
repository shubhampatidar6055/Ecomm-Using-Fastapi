from pydantic import BaseModel


class Categorydata(BaseModel):
    name : str
    description : str

class Getcategory(BaseModel):
    id:int

class Upadtecategory(BaseModel):
    id:int
    name:str
    description:str

class Deletecategory(BaseModel):
    id:int

class Subcategorydata(BaseModel):
    name:str
    description:str
    category:int
