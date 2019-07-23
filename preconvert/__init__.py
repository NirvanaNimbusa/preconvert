"""A Library to enable preconversion of any Python type into one that is easily serializable"""
__version__ = "0.0.2"

from preconvert import convert, exceptions, output
from preconvert.convert import default_serializer
from preconvert.register import bson, converter, json, msgpack

__all__ = [
    "converter",
    "json",
    "bson",
    "msgpack",
    "exceptions",
    "convert",
    "output",
    "unserializable",
]
