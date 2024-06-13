import os
from peewee import *

real_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'database.db')
peewee_db = SqliteDatabase(real_path)
print("DB Path: " + real_path)
print("DB: " + str(peewee_db))


class BaseModel(Model):
    class Meta:
        database = peewee_db


class Author(BaseModel):
    author_name = CharField()
    style = CharField()

    class Meta:
        database = peewee_db


class Article(BaseModel):
    title = CharField()
    content = CharField()
    author = ForeignKeyField(Author, backref='name')

    class Meta:
        database = peewee_db


