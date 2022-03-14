import math
from function import func


def dih(input_raw, xi) -> tuple[float, float, dict]:
    """Метод дихотомии - деление отрезка пополам

    Args:
        input_raw (class): объект класса, содержащий данную функцию и отрезок
        xi (float): Заданная точность вычисления 

    Returns:
        tuple[float, float, dict]: Возвращает xmin, fmin и данные для таблиц
    """
    data_table_dih = {
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
    delta = xi / 2

    while (math.fabs(right - left) > xi):

        iter += 1

        x1 = (left + right - delta) / 2
        x2 = (left + right + delta) / 2

        length_i = abs(right - left)

        if (input_raw.func(x1) < input_raw.func(x2)):
            right = x2
        else:
            left = x1

        length = abs(right - left)
        ratio = length / length_i
        f_1, f_2 = func(x1), func(x2)

        data_table_dih["iter"].append(iter)
        data_table_dih["x1"].append("{:.}".format(x1))
        data_table_dih["x2"].append("{:.}".format(x2))
        data_table_dih["f(x1)"].append("{:.}".format(f_1))
        data_table_dih["f(x2)"].append("{:.}".format(f_2))
        data_table_dih["a"].append("{:.}".format(left))
        data_table_dih["b"].append("{:.}".format(right))
        data_table_dih["b - a"].append("{:.}".format(length))
        data_table_dih["ratio"].append("{:.}".format(ratio))

    xmin = (left + right) / 2
    fmin = func(xmin)

    return xmin, fmin, data_table_dih
