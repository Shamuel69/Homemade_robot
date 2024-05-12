import os
import ctypes
#C:\Users\tobba\programming folder\python\FixingAverage\CarlBot2-Github\Libs\Tinkering.c

clibrary = ctypes.CDLL(r"C:\Users\tobba\programming folder\python\FixingAverage\CarlBot2-Github\Libs/cTinkering.so")



def JSON_grab():
    clibrary.display()


if __name__ == "__main__":
    JSON_grab