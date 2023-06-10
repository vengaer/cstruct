import cstruct


def test_simple_unpacked_string_annotation():
    @cstruct.cstruct
    class Unpacked:
        a: "int"
        b: "unsigned char"
        c: "unsigned long long"

    u = Unpacked(a=0, b=1, c=2)

    assert u.a == 0
    assert u.b == 1
    assert u.c == 2


def test_simple_packed_string_annotation():
    @cstruct.cstruct_packed
    class Packed:
        a: "int"
        b: "unsigned char"
        c: "unsigned long long"

    p = Packed(a=0, b=1, c=2)

    assert p.a == 0
    assert p.b == 1
    assert p.c == 2


def test_simple_unpacked_type_annotation():
    @cstruct.cstruct
    class Unpacked:
        a: cstruct.Type.int
        b: cstruct.Type.unsigned_char
        c: cstruct.Type.unsigned_long_long

    u = Unpacked(a=0, b=1, c=2)

    assert u.a == 0
    assert u.b == 1
    assert u.c == 2


def test_simple_packed_type_annotation():
    @cstruct.cstruct_packed
    class Packed:
        a: cstruct.Type.int
        b: cstruct.Type.unsigned_char
        c: cstruct.Type.unsigned_long_long

    p = Packed(a=0, b=1, c=2)

    assert p.a == 0
    assert p.b == 1
    assert p.c == 2


def test_cstruct_string():
    @cstruct.cstruct
    class Unpacked:
        a: "c_string"

    u = Unpacked(a="Some string".encode())
    assert u.a.decode() == "Some string"
