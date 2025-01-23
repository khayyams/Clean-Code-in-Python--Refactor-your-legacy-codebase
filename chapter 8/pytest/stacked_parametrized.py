import pytest

@pytest.mark.parametrize("x", (1, 2))
@pytest.mark.parametrize("y", ("a", "b"))
def test_my_test(x, y):
    print(f"Running test with x={x} and y={y}")