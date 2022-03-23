from operator import length_hint
from flask import Flask
from flask import request
from flask import render_template
from flask_pymongo import PyMongo
from datetime import datetime
from bson.objectid import ObjectId
from flask import abort
import time
from flask import redirect
from flask import url_for
import math
from flask import flash
from flask import session
from datetime import timedelta
import os
from flask_wtf.csrf import CSRFProtect
from flask import jsonify


app = Flask(__name__)
csrf = CSRFProtect(app)
app.config["MONGO_URI"] = "mongodb://mongo:27017/myweb"
app.config["SECRET_KEY"] = "abcd"
app.config["PERMANENT_SESSION_LIFETIME"] = timedelta(minutes=30)
mongo = PyMongo(app)


#이미지, 첨부파일 저장할 경로 지정
#directoryForImage = "C:\\Python\\images"
#directoryForUpload = "C:\\Python\\uploads"

#if not os.path.exists(directoryForImage):
#    os.makedirs(directoryForImage)
#BOARD_IMAGE_PATH = directoryForImage

#if not os.path.exists(directoryForUpload):
#    os.makedirs(directoryForUpload)
#BOARD_ATTACH_FILE_PATH = directoryForUpload

BOARD_IMAGE_PATH = "/files/images"
BOARD_ATTACH_FILE_PATH = "/files/uploads"

ALLOWED_EXTENSIONS=set(["txt", 'pdf', "png", "jpg", "jpeg", "gif"])
app.config["BOARD_IMAGE_PATH"] = BOARD_IMAGE_PATH
app.config["MAX_CONTENT_LENGTH"]= 15*1024*1024
app.config["BOARD_ATTACH_FILE_PATH"] = BOARD_ATTACH_FILE_PATH

if not os.path.exists(app.config["BOARD_IMAGE_PATH"]):
    os.mkdir(app.config["BOARD_IMAGE_PATH"])
    
if not os.path.exists(app.config["BOARD_ATTACH_FILE_PATH"]):
    os.mkdir(app.config["BOARD_ATTACH_FILE_PATH"])


from .common import login_required, allowed_file, rand_generator, check_filename, hash_password, check_password
from .filter import format_datetime
from . import board
from . import member

app.register_blueprint(board.blueprint)
app.register_blueprint(member.blueprint)

