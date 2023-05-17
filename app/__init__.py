"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-chi807m4dadc9vm2bbf0-a.oregon-postgres.render.com",
        database="todo_xtxj",
        user="root",
        password="XE605md0Vy8xgT2clgGE09H1ixNmDDnV")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
