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

class Updatesubcategory(BaseModel):
    id:int
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

class Updatebrand(BaseModel):
    id:int
    name:str

class Deletebrand(BaseModel):
    id:int

class Addproduct(BaseModel):
    category_id:int
    subcategory_id:int
    brand_id:int
    name:str
    manifacture:str
    product_code:int
    model_no:str
    description:str
    length:int
    height:int
    width:int
    mrp:int
    base_price:int
    gst:int

class Deleteproduct(BaseModel):
    id:int

class Updateproduct(BaseModel):
    id:int
    category_id:int
    subcategory_id:int
    brand_id:int
    name:str
    manifacture:str
    product_code:int
    model_no:str
    description:str
    length:int
    height:int
    width:int
    mrp:int
    base_price:int
    gst:int


class Getproduct(BaseModel):
    id:int