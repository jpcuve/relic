from flask import Flask
from sqlalchemy import MetaData, Column, Table, Integer, String, UniqueConstraint, ForeignKey, Text, select, Identity

from relic import sql_alchemy


class Database:
    def __init__(self):
        self.engine = None
        self.metadata = MetaData()
        self.users = Table(
            'users', self.metadata,
            Column('id', Integer, nullable=False, primary_key=True),
            Column('username', String(255), nullable=False),
            Column('api_key', String(64), nullable=False),
            UniqueConstraint('api_key')
        )

    def init_app(self, app: Flask):
        with app.app_context():
            self.engine = sql_alchemy.get_engine('sparrow')

    def create_all(self):
        self.metadata.create_all(self.engine)


db = Database()