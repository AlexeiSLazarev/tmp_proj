'''
Пример 1. Задача с leetcode о мердже двух строк.
'''

# базовая версия
class Solution(object):

    def merge_recursive(self,
                        word: str,
                        word1: str, w1_index: int,
                        word2: str, w2_index: int):

        word1_end = w1_index >= len(word1)
        word2_end = w2_index >= len(word2)

        if len(word1) == 0:
            word1_end = True
        if len(word2) == 0:
            word2_end = True

        if word1_end:
            if word2_end:
                return word
            else:
                remain: str = word2[w2_index:]
                return word + remain
        else:
            if word2_end:
                remain: str = word1[w1_index:]
                return word + remain

        word += word1[w1_index] + word2[w2_index]
        return self.merge_recursive(word, word1, w1_index+1, word2, w2_index+1)

    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        return self.merge_recursive('', word1, 0, word2, 0)

# Версия после рефакторинга
class Solution(object):

    def merge_recursive(self,
                        word: str,
                        word1: str, w1_index: int,
                        word2: str, w2_index: int):

        word1_end = (w1_index >= len(word1)) or len(word1)==0
        word2_end = w2_index >= len(word2) or len(word2)==0

        if word1_end and word2_end:
            return word
        if word1_end:
            remain: str = word2[w2_index:]
            return word + remain
        if word2_end:
            remain: str = word1[w1_index:]
            return word + remain

        word += word1[w1_index] + word2[w2_index]
        return self.merge_recursive(word, word1, w1_index+1, word2, w2_index+1)


    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        w1_index: int = 0
        w2_index: int = 0
        word = ''
        return self.merge_recursive(word, word1, 0, word2, 0)

'''
исходная ЦС - 6
конечная ЦС - 4
Примеы снижения - исключение else, исключение вложенных циклов 
'''

'''
Пример 2. Выбор алгоритма сортировки
'''
# базовая версия
def sort_data(data, reverse=False, key=None, algorithm="quick"):
    if algorithm == "quick":
        sorted_data = quick_sort(data, reverse, key)
    elif algorithm == "merge":
        sorted_data = merge_sort(data, reverse, key)
    elif algorithm == "bubble":
        sorted_data = bubble_sort(data, reverse, key)
    else:
        raise ValueError("Unknown sorting algorithm")

    if reverse:
        sorted_data = sorted_data[::-1]

    if key is not None:
        sorted_data = sorted(sorted_data, key=key)

    return sorted_data

def quick_sort(data, reverse, key):
    # Реализация алгоритма быстрой сортировки
    return sorted(data)

def merge_sort(data, reverse, key):
    # Реализация алгоритма сортировки слиянием
    return sorted(data)

def bubble_sort(data, reverse, key):
    # Реализация пузырьковой сортировки
    return sorted(data)


# Версия после рефакторинга
class SortAlgorithm:
    def sort(self, data, reverse=False, key=None):
        raise NotImplementedError()

class QuickSort(SortAlgorithm):
    def sort(self, data, reverse=False, key=None):
        return sorted(data, reverse=reverse, key=key)

class MergeSort(SortAlgorithm):
    def sort(self, data, reverse=False, key=None):
        return sorted(data, reverse=reverse, key=key)

class BubbleSort(SortAlgorithm):
    def sort(self, data, reverse=False, key=None):
        return sorted(data, reverse=reverse, key=key)

def get_sort_algorithm(algorithm):
    algorithms = {
        "quick": QuickSort(),
        "merge": MergeSort(),
        "bubble": BubbleSort()
    }
    return algorithms.get(algorithm, QuickSort())

def sort_data(data, reverse=False, key=None, algorithm="quick"):
    sorter = get_sort_algorithm(algorithm)
    return sorter.sort(data, reverse, key)

'''
исходная ЦС - 6
конечная ЦС - 2
Примеы снижения - Полиморфизм(классический), использование паттерна Фабрика.
'''

'''
Рефлексия.
Долго ждал этой темы - "Anti-if programming". Впервые касались на курсе clean code,
уже тогда впечатлил результат применения сравнительно простых приемов.
Ну а теперь конечно в полный рост.
Поторебуется время для внимательного, вдумчивого и всеобъемлющего изученяи этой темы.
Не хватает полноценного опыта в ООАП и паттернах проектирования. 
Во всех красках тема заиграет после полноценного изучения последних двух тем.
Так же необходимо писать больше алгоритмов с различными вариантами развития событий - давно мечтал 
написать RPG игру. Видимо время пришло. Думаю как раз там эта тема очень пригодится. 
'''

