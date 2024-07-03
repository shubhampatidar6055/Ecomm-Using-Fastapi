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
    category_id:int
    name:str
    description:str

class Getsubcategory(BaseModel):
    id:int

class Deletesubcategory(BaseModel):
    id:int

class Brand(BaseModel):
    name:str

class Getbrand(BaseModel):
    id:int

class Deletebrand(BaseModel):
    id:int