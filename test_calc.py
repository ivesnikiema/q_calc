import pytest
from calc import solve


@pytest.mark.parametrize('expr, result', [
    ("123", '123'),

    ("(add 1 1)", '2'),
    ("(add 1 (add 1 1))", '3'),
    ("(add (add 1 2) 3)", '6'),
    ("(add (add 1 2) (add 1 2))", '6'),
    ("(add (add 1 (add 1 2)) (add (add 1 2) 2))", '9'),
    ("(add (add 1 (add (add 1 2) 2)) (add 1 2))", '9'),

    ("(multiply 1 1)", '1'),
    ("(multiply 1 (multiply 1 1))", '1'),
    ("(multiply (multiply 1 2) 3)", '6'),
    ("(multiply 3 (multiply (multiply 3 3) 3))", '81'),
    ("(multiply (multiply 1 2) (multiply 1 2))", '4'),
    ("(multiply (multiply 1 (multiply 1 2)) (multiply (multiply 1 2) 2))", '8'),
    ("(multiply (multiply 1 (multiply (multiply 1 2) 2)) (multiply 1 2))", '8'),

    ("(multiply 1 (add 1 1))", '2'),
    ("(multiply (add 1 2) 3)", '9'),
    ("(multiply (add 1 2) (add 1 2))", '9'),
    ("(add (multiply 1 (add 1 2)) (multiply (add 1 2) 2))", '9'),
    ("(multiply (add 1 (add (multiply 1 2) 2)) (add 1 2))", '15'),
])
def test_calc(expr: str, result: str):
    assert solve(expr) == result


@pytest.mark.parametrize('expr', ["(divide 2 1)",
                                 "(random 2 1)",
                                 "(substract 2 1)"])
def test_exception_not_found(expr: str):
    with pytest.raises(AssertionError):
        solve(expr)
