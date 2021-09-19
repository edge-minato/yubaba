from _pytest.capture import CaptureFixture

from tests.conftest import return_bool, return_false, return_true
from yubaba import F, If, Nif, print_if


def test_F() -> None:
    # without args
    f = F(return_true)
    assert f() is True
    # with args
    f = F(return_bool, True)
    assert f() is True
    f = F(return_bool, False)
    assert f() is False


def test_if() -> None:
    assert If(True, F(return_true)) is True
    assert If(True, F(return_false)) is False
    assert If(True, F(return_bool, True)) is True
    assert If(True, F(return_bool, False)) is False
    assert If(False, F(return_true)) is None
    assert If(True, lambda: return_bool(True)) is True


def test_nif() -> None:
    assert Nif(False, F(return_true)) is True
    assert Nif(False, F(return_false)) is False
    assert Nif(True, F(return_true)) is None


def test_print_if(capfd: CaptureFixture) -> None:
    # true
    print_if(True, "true")
    out, err = capfd.readouterr()
    assert out == "true\n"
    assert err == ""
    # false
    print_if(False, "false")
    out, err = capfd.readouterr()
    assert out == ""
    assert err == ""


def a() -> bool:
    if True:
        return True
