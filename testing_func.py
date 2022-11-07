from main import func


def test_method1():
    assert func(3) == 4


def test_method2():
    a = 5
    b = 10
    assert 2*a == b


def test_method3():
    txt = "hello"
    assert "h" in txt


def test_method4():
    assert func(4) == 5
