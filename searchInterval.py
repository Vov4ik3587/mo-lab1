import imp
from function import func


def search(xi, x0) -> tuple[float, float, dict]:
    """Поиск интервала, содержащего минимум функции

    Поиск отрезка на прямой заключатся в
    том, что возрастающие по величине шаги осуществляются до тех пор,
    пока не будет пройдена точка минимума функции, т. е. убывание
    функции сменится на возрастание.

    Args:
        xi (float): Заданная точность  
        x0 (float): Начальная точка 
    Returns:
        tuple[float, float, dict]: Возвращает левую, правую границы и данные для таблицы
    """
    data_table_search = {
        "iter": [],
        "x": [],
        "f": [],
    }

    x = [x0, 0., 0.]
    h = 0.
    iter = 0

    if func(x[0]) > func(x[0] + xi):
        x[1] = x[0] + xi
        h = xi
    else:
        x[1] = x[0] - xi
        h = -xi
    h *= 2
    x[2] = x[1] + h
    while func(x[1]) > func(x[2]):
        iter += 1
        x[0] = x[1]
        x[1] = x[2]
        h *= 2
        x[2] = x[1] + h

        data_table_search["iter"].append(iter)
        data_table_search["x"].append(x[1])
        data_table_search["f"].append(func(x[1]))

    if x[0] > x[2]:
        x[0], x[2] = x[2], x[0]

    return x[0], x[2], data_table_search
