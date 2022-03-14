import math
from function import func


def golden(input_raw, xi) -> tuple[float, float, dict]:
    """Метод золотого сечения

    Точки x1, x2 находятся симметрично относительно середины от-
    резка [a0, b0] и делят его в пропорции золотого сечения, когда длина
    всего отрезка относится к длине большей его части так же, как длина
    большей части относится к длине меньшей части:

    Args:
        input_raw (class): объект класса, содержащий данную функцию и отрезок
        xi (float): Заданная точность вычисления 

    Returns:
        tuple[float, float, dict]: Возвращает xmin, fmin и данные для таблиц
    """
    data_table_gold = {
        "iter": [],
        "x1": [],
        "x2": [],
        "f(x1)": [],
        "f(x2)": [],
        "a": [],
        "b": [],
        "b - a": [],
        "ratio": [],
    }

    left = input_raw.left
    right = input_raw.right
    iter = 0
    gold = (float)(5**0.5 + 1) / 2

    x1 = left + (2 - gold) * (right - left)
    x2 = left + (gold - 1) * (right - left)

    f_1, f_2 = func(x1), func(x2)

    while (math.fabs(right - left) > xi):
        iter += 1

        length_i = abs(right - left)

        if (f_1 > f_2):
            left = x1
            x1 = x2
            f_1 = f_2
            x2 = left + (gold - 1) * (right - left)
            f_2 = func(x2)
        else:
            right = x2
            x2 = x1
            f_2 = f_1
            x1 = left + (2 - gold) * (right - left)
            f_1 = func(x1)

        length = abs(right - left)
        ratio = length / length_i

        f_1, f_2 = func(x1), func(x2)

        data_table_gold["iter"].append(iter)
        data_table_gold["x1"].append(x1)
        data_table_gold["x2"].append(x2)
        data_table_gold["f(x1)"].append(f_1)
        data_table_gold["f(x2)"].append(f_2)
        data_table_gold["a"].append(left)
        data_table_gold["b"].append(right)
        data_table_gold["b - a"].append(length)
        data_table_gold["ratio"].append(ratio)

    xmin = (left + right) / 2
    fmin = func(xmin)

    return xmin, fmin, data_table_gold
