from yubaba import And, Nand, Nor, Or, Xnor, Xor


def return_true() -> bool:
    return True


def return_false() -> bool:
    return False


C1 = [True]
C2 = [False]
C3 = [True, True, True]
C4 = [True, True, False]
C5 = [True, False, False]
C6 = [False, False, False]


def test_and() -> None:
    # 1 bit
    assert And(C1) is True
    assert And(C2) is False
    # 3 bits
    assert And(C3) is True
    assert And(C4) is False
    assert And(C5) is False
    assert And(C6) is False


def test_or() -> None:
    # 1 bit
    assert Or(C1) is True
    assert Or(C2) is False
    # 3 bits
    assert Or(C3) is True
    assert Or(C4) is True
    assert Or(C5) is True
    assert Or(C6) is False


def test_xor() -> None:
    # 1 bit
    assert Xor(C1) is True
    assert Xor(C2) is False
    # 3 bits
    assert Xor(C3) is True
    assert Xor(C4) is False
    assert Xor(C5) is True
    assert Xor(C6) is False


def test_nand() -> None:
    # 1 bit
    assert Nand(C1) is False
    assert Nand(C2) is True
    # 3 bits
    assert Nand(C3) is False
    assert Nand(C4) is True
    assert Nand(C5) is True
    assert Nand(C6) is True


def test_nor() -> None:
    # 1 bit
    assert Nor(C1) is False
    assert Nor(C2) is True
    # 3 bits
    assert Nor(C3) is False
    assert Nor(C4) is False
    assert Nor(C5) is False
    assert Nor(C6) is True


def test_xnor() -> None:
    # 1 bit
    assert Xnor(C1) is False
    assert Xnor(C2) is True
    # 3 bits
    assert Xnor(C3) is False
    assert Xnor(C4) is True
    assert Xnor(C5) is False
    assert Xnor(C6) is True
