import json
import inspect
from bson import ObjectId
from time import time
from fastapi.encoders import jsonable_encoder



def timestamp_now():
    return int(time())


class JSONEncoder(json.JSONEncoder):
    """
    Make my own encoder because jsonable_encoder cannot serialize <class 'bson.objectid.ObjectId'>
    """
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return jsonable_encoder(o)
