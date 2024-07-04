from tortoise.models import Model
from tortoise import Tortoise, fields

class Category(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(200)
    description = fields.TextField()
    image = fields.TextField()
    is_active = fields.BooleanField(default= True)
    create_at = fields.DatetimeField(auto_now_add= True)
    update = fields.DatetimeField(auto_now=True)

class Subcategory(Model):
    id = fields.IntField(pk = True)
    name = fields.CharField(250)
    description = fields.TextField()
    image = fields.TextField()
    Category = fields.ForeignKeyField("models.Category", related_name='Subcategory',
                                       on_delete='CASCADE')
    is_active = fields.BooleanField(default=True)
    create_at = fields.DatetimeField(auto_now_add=True)
    update = fields.DatetimeField(auto_now=True)

class Addbrand(Model):
    id = fields.IntField(pk = True)
    brand_name = fields.CharField(250)
    is_active = fields.BooleanField(default=True)
    create_at = fields.DatetimeField(auto_now_add=True)
    updated = fields.DatetimeField(auto_now=True)

class Product(Model):
    id = fields.IntField(pk = True)
    name = fields.CharField(250)
    manifacture = fields.CharField(250)
    product_image = fields.TextField()
    product_code = fields.IntField()
    model_no = fields.IntField()
    description = fields.TextField()
    length = fields.IntField()
    height = fields.IntField()
    weight = fields.IntField()
    mrp = fields.IntField()
    base_price = fields.IntField()
    gst = fields.IntField()
    category_key = fields.ForeignKeyField("models.Category", related_name='Subcategory_key',
                                       on_delete='CASCADE')
    subcategory_key = fields.ForeignKeyField("models.Subcategory", related_name='Product',
                                       on_delete='CASCADE')
    brand = fields.ForeignKeyField("models.Addbrand", related_name='Product',
                                       on_delete='CASCADE')
    is_active = fields.BooleanField(default=True)
    updated = fields.DatetimeField(auto_now=True)
    created = fields.DatetimeField(auto_now_add=True)


Tortoise.init_models(['ecom.models'], 'models')

