import json
from datetime import datetime
from functools import wraps

FILE_JSON_PATH = "input_file.json"
FILE_JSON_LIST_PATH = "input_file_list.json"
FILE_NOT_JSON_PATH = "not_json.json"
FILE_INCORRECT_JSON_PATH = "json_with_errors.json"

def handle_obj_or_list(func):
    @wraps(func)
    def wrapper(cls):
        instance = cls._get_instance()
        if isinstance(instance, list):
            for obj in instance:
                func(cls, obj)
        else:
            func(cls, instance)
    return wrapper


def modify_obj(func):
    @wraps(func)
    def wrapper(cls):
        instance = func(cls)

        if isinstance(instance, list):
            for obj in instance:
                if hasattr(obj, 'id'):
                    del obj.id
                if hasattr(obj, 'birth_date'):
                    obj.birth_date = datetime.strptime(obj.birth_date, "%m/%d/%Y").strftime("%Y-%m-%d")
        else:
            if hasattr(instance, 'id'):
                del instance.id
            if hasattr(instance, 'birth_date'):
                instance.birth_date = datetime.strptime(instance.birth_date, "%m/%d/%Y").strftime("%Y-%m-%d")
        return instance
    return wrapper

class JSONProcessor:
    _instance = None
    _json_object = None

    def __init__(self, **kwargs):
        self.__dict__.update(**kwargs)

    def __new__(cls, *args, **kwargs):
        json_to_parse = args[0]
        if isinstance(json_to_parse, list):
            cls._instance = cls.__create_list_of_objects(json_to_parse)
        elif isinstance(json_to_parse, dict):
            cls._instance = cls.__create_object(json_to_parse)
        return cls._instance

    def __repr__(self):
        return str(self.__dict__)

    @classmethod
    def _get_instance(cls):
        return cls._instance

    @classmethod
    @modify_obj
    def get_instance(cls):
        return cls._instance

    @classmethod
    def __create_object(cls, _object):
        instance = super().__new__(cls)
        instance.__init__(**_object)
        return instance

    @classmethod
    def __create_list_of_objects(cls, _objects):
        objects_to_create = [cls.__create_object(obj) for obj in _objects]
        return objects_to_create

    @classmethod
    def load_json_file(cls, filepath):
        try:
            with open(filepath, 'r') as file:
                cls._json_object = json.load(file)
        except FileNotFoundError as e:
            print(f"ERROR while searching the file: '{e.strerror}' | File Name: {e.filename}")
            #raise(Exception(f"ERROR while searching the file: '{e.strerror}' | File Name: {e.filename}"))
        except json.JSONDecodeError as e:
            print(f"ERROR while decoding the file: '{e.msg}'| Error at line: {e.lineno} | Unable to decode following "
                  f"content:\n'{e.doc}'")
            #raise(Exception(f"ERROR while decoding the file: '{e.msg}'| Error at line: {e.lineno} | Unable to decode
            # following content:'{e.doc}'"))
        except Exception as e:
            print("Unexpected Error has occurred")
            #raise(Exception("Unexpected Error has occurred"))

    @classmethod
    def write_json_file(cls, filename):
        try:
            file = open(filename, "w")
            if isinstance(cls._get_instance(), list):
                file.write(json.dumps([obj.__dict__ for obj in cls._get_instance()], indent=4))
            else:
                file.write(json.dumps(cls._instance.__dict__, indent=4))
        except FileNotFoundError as e:
            print(f"ERROR while searching the file: '{e.strerror}' | File Name: {e.filename}")
            # raise(Exception(f"ERROR while searching the file: '{e.strerror}' | File Name: {e.filename}"))

    @classmethod
    def convert_to_object(cls):
        return cls.__new__(cls, cls._json_object)

    @classmethod
    @handle_obj_or_list
    def remove_id_property(cls, inct=None):
        obj = inct or cls._get_instance()
        if hasattr(obj, 'id'):
            del obj.id

    @classmethod
    @handle_obj_or_list
    def change_date_format(cls, inct=None):
        obj = inct or cls._get_instance()
        obj.birth_date = datetime.strptime(obj.birth_date, "%m/%d/%Y").strftime("%Y-%m-%d")




JSONProcessor.load_json_file(FILE_JSON_LIST_PATH)
JSONProcessor.convert_to_object()
print(JSONProcessor.get_instance())

# JSONProcessor.load_json_file(FILE_NOT_JSON_PATH)
# JSONProcessor.load_json_file(FILE_INCORRECT_JSON_PATH)
#
# JSONProcessor.load_json_file(FILE_JSON_LIST_PATH)
# JSONProcessor.convert_to_object()
# #JSONProcessor.write_json_file("output_json_file_list.json")
# print(JSONProcessor.get_instance())
# JSONProcessor.change_date_format()
# print(JSONProcessor.get_instance())
# #JSONProcessor.write_json_file("output_json_file_list_date.json")
# JSONProcessor.remove_id_property()
# print(JSONProcessor.get_instance())
# #JSONProcessor.write_json_file("output_json_file_list_no_ID.json")
# JSONProcessor.load_json_file(FILE_JSON_PATH)
# python_object = JSONProcessor.convert_to_object()
# print(JSONProcessor.get_instance())
# #JSONProcessor.write_json_file("output_json_file.json")
# JSONProcessor.remove_id_property()
# print(JSONProcessor.get_instance())
# JSONProcessor.change_date_format()
# print(JSONProcessor.get_instance())
#
# #JSONProcessor.write_json_file("output_json_file_no_ID.json")
#
# kek = JSONProcessor.get_instance()
