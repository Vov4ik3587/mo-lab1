from dihotomy import dih
from goldenRatio import golden
from searchInterval import search
from function import func
import json

from searchInterval import search


class Source:
    def __init__(self, func, a, b):
        self.func = func  # Заданная по варианту функция
        self.left = a     # левая граница исследуемого отрезка
        self.right = b    # Правая граница отрезка


def main():
    a = -2  # Левая граница
    b = 20  # Правая граница

    xi = 1e-7  # Задаваемая точнсть

    data_table_dih = {}
    data_table_golden_ratio = {}
    data_table_search = {}

    # Создаем объект класса, который передадим в методы
    task1 = Source(func, a, b)

    result_dih, func_result_dih, data_table_dih = dih(
        task1, xi)

    result_gold, func_result_gold, data_table_golden_ratio = golden(
        task1, xi)

    result_search_a, result_search_b, data_table_search = search(xi, 0.)

    print(
        f"Dihotomy: Xmin = {result_dih}, Fmin = {func_result_dih}, Accuracy = {xi}")

    print(
        f"Golden Ratio: Xmin = {result_gold}, Fmin = {func_result_gold}, Accuracy = {xi}")

    print(
        f"Search Interval: Xmin from [{result_search_a};{result_search_b}] Accuracy = {xi}")

    with open("./dih.json", "w", encoding="utf_8") as file1:
        json.dump(data_table_dih, file1)

    with open("./golden.json", "w", encoding="utf_8") as file2:
        json.dump(data_table_golden_ratio, file2)

    with open("./search.json", "w", encoding="utf_8") as file3:
        json.dump(data_table_search, file3)


if __name__ == "__main__":
    main()
