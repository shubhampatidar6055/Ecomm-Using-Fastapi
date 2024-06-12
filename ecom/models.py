from tortoise.models import Model
from tortoise import fields

class Category(Model):
    name = fields.CharField(2500)
    category_img = fields.F