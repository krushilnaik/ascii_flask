from pathlib import Path
import sys

from util.custom_logging import critical

try:
    from peewee import CharField, Model, SqliteDatabase
except ImportError:
    critical("Failed to import peewee. Did you install it with pip?")
    sys.exit(1)

db = SqliteDatabase(Path(__file__).parent.parent / 'alphabet.db')


class Letter(Model):
    letter = CharField()
    representation = CharField()

    class Meta:
        database = db
