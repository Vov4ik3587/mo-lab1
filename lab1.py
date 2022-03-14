from dihotomy import dih
from function import func
import json


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
    
    # Создаем объект класса, который передадим в методы
    task1 = Source(func, a, b)
    
    result_dih, func_result_dih, data_table_dih = dih(
        task1, xi)

    """ result_gold_ratio[j], func_result_gold_ratio[j], data_table_golden_ratio = goldenRatio(
            task1, xi(i)) """

    print(f"Dihotomy: Xmin = {result_dih}, Fmin = {func_result_dih}, Accuracy = {xi}")
    
    """ print(f"GoldenRatio: Xmin = {result_dih}, Fmin = {func_result_dih}, Accuracy = {xi}") """
    
    with open("./dih.json", "w", encoding="utf_8") as file:
        json.dump(data_table_dih, file)


if __name__ == "__main__":
    main()