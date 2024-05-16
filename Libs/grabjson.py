import os
import ctypes
import json
#C:\Users\tobba\programming folder\python\FixingAverage\CarlBot2-Github\Libs\Tinkering.c

clibrary = ctypes.CDLL(r"C:\Users\tobba\programming folder\python\FixingAverage\CarlBot2-Github\Libs\Tinkering.dll")
# gcc -shared -o Tinkering.dll Tinkering.c

def json_checker(Json_PATH:str):
    with open(Json_PATH, "r") as f:
        user = json.load(f)
    return user

def JSON_grab():
    str2 = ctypes.create_string_buffer(100)
    str2.value =b"when he was just a supple young lad,"
    
    print(str2)


    clibrary.display(b"penis", 18, str2.value)


if __name__ == "__main__":
    print(json_checker("Datasets/posneg.json"))
    integer = ctypes.c_int(18)
    print((clibrary.json_loader()))