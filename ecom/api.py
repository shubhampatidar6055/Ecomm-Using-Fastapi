from fastapi import APIRouter, File, UploadFile,Depends
from .models import*
from .pydantic_models import Categorydata,Getcategory,Upadtecategory,Deletecategory,Subcategorydata,Updatesubcategory,Getsubcategory,Deletesubcategory,Brand,Getbrand,Updatebrand,Deletebrand,Addproduct,Deleteproduct,Updateproduct,Getproduct
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

            subcategory_obj = await Subcategory.create(image=generated_name,
                                                       name=data.name, Category=category_obj,
                                                       description=data.description)
            return {"subcategory_obj":subcategory_obj}
        
@app.put("/update_subcategory/")
async def update_subcategory(data:Updatesubcategory=Depends(), image:UploadFile = File(...)):
    
    getsubcategory_id = await Subcategory.get(id=data.id)
    category_obj = await Category.get(id = data.category_id)

    FILEPATH ="static/images/subcategory"

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

    update_subcategory_obj = await Subcategory.filter(id=data.id).update(name=data.name, description=
                                                          data.description, image=generated_name)
    return {'message':'Subcategory update sucessfully'}

@app.post("/get_subcategory/")
async def read_subcategory(data:Getsubcategory):
    object = await Subcategory.get(id=data.id)
    return object

@app.delete("/delete_subcategory/")
async def delete_subcategory(data:Deletesubcategory):
    await Subcategory.get(id=data.id).delete()
    return{"message":"Subcategory deleted sucessfully"}

@app.post("/create_brand/")
async def create_brand(data:Brand):
    if await Addbrand.exists(brand_name=data.name):
        return {"status":False, "message":"Brand Name Already Exists"}
    else:
        brand_obj = await Addbrand.create(brand_name=data.name)

        return brand_obj
    
@app.post("/get_brand/")
async def get_brand(data:Getbrand):
    get_brand_obj = await Addbrand.get(id=data.id)
    return get_brand_obj

@app.put("/update_brand/")
async def update_brand(data:Updatebrand):
    brandid = await Addbrand.get(id=data.id)
    
    await Addbrand.filter(id=data.id).update(brand_name=data.name)

    return {"message":"Brand update sucessfully"}

@app.delete("/delete_brand/")
async def delete_brand(data:Deletebrand):
    await Addbrand.get(id=data.id).delete()
    return {"message":"Brand Deleted sucessfully"}

@app.post("/add_product/")
async def add_product(data:Addproduct=Depends(), product_image:UploadFile=File(...)):
    if await Category.exists(id=data.category_id):
        category_obj = await Category.get(id = data.category_id)
        
    if await Subcategory.exists(id=data.subcategory_id):
        subcategory_obj = await Subcategory.get(id=data.subcategory_id)

    if await Addbrand.exists(id=data.brand_id):
        brand_obj = await Addbrand.get(id=data.brand_id)

        if await Product.exists(name=data.name):
            return {'status':False, 'message':'Product already Exists'}
                
        else:
                    FILEPATH = "static/images/product/"

                    if not os.path.isdir(FILEPATH):
                        os.mkdir(FILEPATH)

                    filename = product_image.filename
                    extension = filename.split(".")[1]
                    imagename = filename.split(".")[0]

                    if extension not in ["png","jpg","jpeg"]:
                        return {"status":"error", "detial":"File extension not allowed"}
                    
                    dt = datetime.now()
                    dt_timestamp = round(datetime.timestamp(dt))

                    modified_image_name = imagename+"_"+str(dt_timestamp)+"_"+extension
                    genrated_name =  FILEPATH+modified_image_name
                    file_contant = await product_image.read()

                    with open(genrated_name, "wb")as file:
                        file.write(file_contant)
                        file.close()

                    product_obj = await Product.create(name=data.name, manifacture=data.manifacture,
                                                       product_image=genrated_name,
                                                       product_code=data.product_code,
                                                       model_no=data.model_no, description=data.description,
                                                       length=data.length, height=data.height, weight=data.width,
                                                       mrp=data.mrp, base_price=data.base_price, gst=data.gst,
                                                       category_key = category_obj, subcategory_key=subcategory_obj,
                                                       brand=brand_obj)
                    return {'status':True, 'message':'added','product_obj':product_obj}
        
@app.delete("/delete_product/")
async def delete_product(data:Deleteproduct):
    await Product.get(id=data.id).delete()
    return {'message':'Product Deleted Sucessfully'}

@app.put("/update_product/")
async def update_product(data:Updateproduct= Depends(), image:UploadFile = File(...)):

    getproduct_id = await Product.get(id=data.id)

    if await Category.exists(id=data.category_id):
        category_obj = await Category.get(id=data.category_id)

    if await Subcategory.exists(id=data.subcategory_id):
        subcategory_obj = await Subcategory.get(id=data.subcategory_id)

    if await Addbrand.exists(id=data.brand_id):
        brand_obj = await Addbrand.get(id=data.brand_id)

    FILEPATH = "static/images/category"

    if not os.path.isdir(FILEPATH):
        os.mkdir(FILEPATH)

    filename = image.filename
    extension = filename.split(".")[1]
    imagename = filename.split(".")[0]

    if extension not in ["png", "jpg", "jpeg"]:
        return {"status": "error", "detail":"File extention not allowed"}
    
    dt = datetime.now()
    dt_timestamp = round(datetime.timestamp(dt))

    modified_image_name = imagename+"_"+str(dt_timestamp)+"_"+extension
    generated_name = FILEPATH+modified_image_name
    file_content = await image.read()

    with open(generated_name ,"wb")as file:
        file.write(file_content)
        file.close()

    await Product.filter(id=data.id).update(name=data.name, manifacture=data.manifacture,
                                            product_image=generated_name,
                                            product_code=data.product_code,
                                            model_no=data.model_no, description=data.description,
                                            length=data.length, height=data.height, weight=data.width,
                                            mrp=data.mrp, base_price=data.base_price, gst=data.gst,
                                            category_key = category_obj, subcategory_key=subcategory_obj,
                                            brand=brand_obj)
    return {"Product update sucessfully"}

@app.post("/get_product/")
async def get_product(data:Getproduct):
    get_product_obj = await Product.get(id=data.id)
    return {"get_product_obj":get_product_obj}