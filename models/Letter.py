# import orm_sqlite as orm


# class Letter(orm.Model):
#     id = orm.IntegerField(primary_key=True)
#     letter = orm.StringField()
#     representation = orm.StringField()


# db = orm.Database('../alphabet.db')
# Letter.objects.backend = db


from pathlib import Path
from peewee import CharField, Model, SqliteDatabase

db = SqliteDatabase(Path(__file__).parent.parent / 'alphabet.db')


class Letter(Model):
    letter = CharField()
    representation = CharField()

    class Meta:
        database = db
