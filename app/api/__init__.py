from flask import Blueprint
api=Blueprint("api",__name__)
from . import network, livetranslate,Pictranslate,Cuoti 