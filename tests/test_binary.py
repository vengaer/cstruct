import struct

import cstruct


def test_simple_unpacked_raw_string_annotation():
    @cstruct.cstruct
    class Unpacked:
        a: "int"
        b: "unsigned char"
        c: "unsigned long long"

    packed = struct.pack("@iBQ", 0, 1, 2)

    u = Unpacked(raw=packed)

    assert u.a == 0
    assert u.b == 1
    assert u.c == 2


def test_simple_packed_raw_string_annotation():
    @cstruct.cstruct_packed
    class Packed:
        v: "int"
        x: "unsigned char"
        y: "unsigned char"

    raw = struct.pack("@iBB", 0, 1, 2)

    p = Packed(raw=raw)

    assert p.v == 0
    assert p.x == 1
    assert p.y == 2
