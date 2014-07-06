from collapsible_tree import converter
from types import FunctionType
import json

METHOD_NAME = 'converte'

BASE_1 = """Structure"""
RESULT_1 = """{"name": "Structure", "children": []}"""

BASE_2 = "NOME"
RESULT_2 = """{"name": "NOME", "children": []}"""

cases = []
cases.append((BASE_1, RESULT_1))
cases.append((BASE_2, RESULT_2))

def setup():
    print 'SETUP!'

def teardown():
    print 'TEAR DOWN!'

def test_has_method():

    assert METHOD_NAME in converter.__dict__ and type(converter.__dict__[METHOD_NAME]) is FunctionType


def comparar_jsons(json1, json2):

    return json.loads(json1) == json.loads(json2)

def test_comparar_jsons_ignore_whites():

    assert comparar_jsons("""{"name":"Structure", "children": []}""","""{"name":  "Structure",   "children": []}""")

def test_cases():

    for base, result in cases:
        yield assert_convert, base, result

def assert_convert(base, result):

    assert comparar_jsons(result, converter.converte(base))

