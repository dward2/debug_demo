import pytest

def test_pick_a_direction_error():
    from errors import pick_a_direction
    with pytest.raises(ValueError):
        pick_a_direction("g")


def test_pick_a_direction_good():
    from errors import pick_a_direction
    answer = pick_a_direction("n")
    expected = "n"
    assert answer == expected

@pytest.mark.parametrize("a, b, errortype", [
    (1, -1, ValueError),
    (1, 2.3, TypeError),
])
def test_add_two_numbers(a, b, errortype):
    from errors import add_two_numbers
    with pytest.raises(errortype):
        add_two_numbers(a, b)
