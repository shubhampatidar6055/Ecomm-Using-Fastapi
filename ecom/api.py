from fastapi import APIRouter, File, UploadFile,Depends
from .models import*
from .pydantic_models import Categorydata,Getcategory,Upadtecategory,Deletecategory,Subcategorydata,Getsubcategory,Deletesubcategory
import os
from datetime import datetime, timedelta


app = APIRouter()

@app.post("/")
async def create_user(data:Categorydata= Depends(),image:UploadFile= File(...)):
    if await Category.exists(name=data.name):
        return {"status":False, "message":"Category Already Exists"}
    
    else:
        FILEPATH = "static/images/category/"

        if not os.path.isdir(FILEPATH):
            os.mkdir(FILEPATH)

        filename = image.filename
        extension = filename.split(".")[1]
        imagename = filename.split(".")[0]

        if extension not in ["png","jpg","jpeg"]:
            return {"status":"error", "detial":"File extension not allowed"}
        
        dt = datetime.now()
        dt_timestamp = round(datetime.timestamp(dt))    

        modified_image_name = imagename+"_"+str(dt_timestamp)+"_"+extension 
        genrated_name =  FILEPATH+modified_image_name
        file_contant = await image.read()

        with open(genrated_name, "wb")as file:
            file.write(file_contant)
            file.close()

        category_obj = await Category.create(image=genrated_name,
                                             name=data.name,
                                             description=data.description)
        return {'category_obj':category_obj}
    
@app.post("/get_category/")
async def read_category(data:Getcategory):
    obj = await Category.get(id=data.id)
    return obj

@app.put("/update_category/")
async def update_category(data:Upadtecategory= Depends(), image:UploadFile = File(...)):

    getid = await Category.get(id=data.id)

    FILEPATH = "static/images/category"

    if not os.path.isdir(FILEPATH):
        os.mkdir(FILEPATH)

    filename = image.filename
    extension = filename.split(".")[1]
    imagename = filename.split(".")[0]

    if extension not in ["png","jpeg","jpg"]:
        return {"status":"error", "detail":"File extention not allowed"}
    
    dt = datetime.now()
    dt_timestamp = round(datetime.timestamp(dt))

    modified_image_name = imagename+"_"+str(dt_timestamp)+"_"+extension
    generated_name = FILEPATH+modified_image_name
    file_content =await image.read()

    with open(generated_name, "wb")as file:
        file.write(file_content)
        file.close()

        await Category.filter(id=data.id).update(name=data.name,description=data.description,
                                                 image=generated_name)
        return {"Catyegory update sucessfully"}
    
@app.delete("/delete_category/")
async def delete_category(data:Deletecategory):
    await Category.get(id=data.id).delete()
    return{'message':'Category delete sucessfully'}

@app.post("/create_subcategory/")
async def create_subcategory(data:Subcategorydata=Depends(), image:UploadFile = File(...)):
    if await Category.exists(id=data.category_id):
        category_obj = await Category.get(id = data.category_id)

        if await Subcategory.exists(name=data.name):
            return {"status":False, "message":"Name already exists"}
        else:
            FILEPATH="static/images/subcategory"

            if not os.path.isdir(FILEPATH):
                os.mkdir(FILEPATH)

            filename = image.filename
            extension = filename.split(".")[1]
            imagename = filename.split(".")[0]

            if extension not in["jpg","png","jpeg"]:
                return {"status":"error", "detail":"File extention is not allowed"}
        
            dt=datetime.now()
            dt_timestamp = round(datetime.timestamp(dt))

            modified_image_name = imagename+"_"+str(dt_timestamp)+"_"+extension
            generated_name = FILEPATH+modified_image_name
            file_content = await image.read()

            with open(generated_name,"wb")as file:
                file.write(file_content)
                file.close()

            subcategory_obj = await Subcategory.create(subcategory_image=generated_name,
                                                       name=data.name, category=category_obj,
                                                       description=data.description)
            return {"subcategory_obj":subcategory_obj}
        
@app.post("/get_subcategory/")
async def read_subcategory(data:Getsubcategory):
    object = await Subcategory.get(id=data.id)
    return object

@app.post("/delete_subcategory/")
async def delete_subcategory(data:Deletesubcategory):
    await Subcategory.get(id=data.id).delete()
    return{"message":"Subcategory deleted sucessfully"}
