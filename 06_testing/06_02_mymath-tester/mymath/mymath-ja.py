# 以下に示す`subtract_divide()`関数について、
# `test_mymath.py`にunittestテストスイートを記述します。
# 詳しい説明は`test_mymath.py`を参照してください。

class CustomZeroDivsionError(Exception):
    pass


def subtract_divide(dividend, x, y):
    try:
        z = x - y
        return dividend / z
    except ZeroDivisionError:
        raise CustomZeroDivsionError(f"This won't work because {x} - {y} = 0.")
