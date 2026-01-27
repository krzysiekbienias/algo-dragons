import pytest
from matrix import clean_up_after_your_dog


@pytest.mark.parametrize(
    "garden,bags,cap,expected",
    [
        ([['_','_','_','_'], ['_','_','_','@'], ['_','_','@', '_']], 2, 2, "Clean"),
        ([['_','_','_','_'], ['_','_','_','@'], ['_','_','@', '_']], 1, 1, "Cr@p"),
        ([['_','_'], ['_','@'], ['D','_']], 2, 2, "Dog!!"),
        ([['_','_','_','_'], ['_','_','_','_'], ['_','_','_', '_']], 2, 2, "Clean"),
        ([['@','@'], ['@','@'], ['@','@']], 3, 2, "Clean"),
    ],
)
def test_basic_cases(garden, bags, cap, expected):
    # x[:] w Codewars robi "płytką kopię" listy wierszy; tu zachowujemy to samo:
    assert clean_up_after_your_dog(garden[:], bags, cap) == expected
