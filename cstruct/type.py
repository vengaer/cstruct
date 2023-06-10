import ctypes
import enum

from typing import Dict


class Type(enum.Enum):
    _Bool = ctypes.c_bool
    char = ctypes.c_char
    wchar_t = ctypes.c_wchar
    unsigned_char = ctypes.c_ubyte
    short = ctypes.c_short
    unsighed_short = ctypes.c_ushort
    int = ctypes.c_int
    unsigned = ctypes.c_uint
    long = ctypes.c_long
    unsigned_long = ctypes.c_ulong
    long_long = ctypes.c_longlong
    unsigned_long_long = ctypes.c_ulonglong
    size_t = ctypes.c_size_t
    ssize_t = ctypes.c_ssize_t
    float = ctypes.c_float
    double = ctypes.c_double
    c_string = ctypes.c_char_p

    @property
    def format(self) -> str:
        formats = {
            ctypes.c_bool: "?",
            ctypes.c_char: "c",
            ctypes.c_wchar: "I",
            ctypes.c_ubyte: "B",
            ctypes.c_short: "h",
            ctypes.c_ushort: "H",
            ctypes.c_int: "i",
            ctypes.c_uint: "I",
            ctypes.c_long: "l",
            ctypes.c_ulong: "L",
            ctypes.c_longlong: "q",
            ctypes.c_ulonglong: "Q",
            ctypes.c_size_t: "N",
            ctypes.c_ssize_t: "n",
            ctypes.c_float: "f",
            ctypes.c_double: "d",
            ctypes.c_char_p: "s",
        }
        return formats[self.value]  # type: ignore[index]
