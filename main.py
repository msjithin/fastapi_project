# main.py
from fastapi import FastAPI

app = FastAPI()

from routes_users import *
from routes_items import *
from routes_auth import *
