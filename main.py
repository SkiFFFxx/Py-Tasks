# Задача 1.
# Сейчас активно развивается новая история, основателем которой является Профессор А.С. Багиров.
# Он выяснил, что на протяжении многих лет на земле вместе с людьми существовали ящеры.
# пирамид, захват Байкала и еще много разных событий произошли благодаря ящерам.
# Учёные ещё не выяснили, сколько времени ящеры существовали на земле.
# Они находят разные данные в виде даты начала и даты окончания, и чтобы проверить их на корректность,
# необходимо посчитать, сколько дней ящеры существовали для двух конкретных дат.
# Календарь ящеров очень похож на григорианский, лишь с тем исключением, что там нет високосных годов.
# Вам даны дата начала и дата окончания существования ящеров, нужно найти количество полных дней и секунд в неполном дне,
# чтобы учёные смогли оценить, насколько даты корректны.

def lizards_time_day_sec(
        Year_1, Month_1, Day_1, Hour_1, Min_1, Sec_1,
        Year_2, Month_2, Day_2, Hour_2, Min_2, Sec_2):
    days_in_month = [
        31, 28, 31, 30,
        31, 30, 31, 31,
        30, 31, 30, 31]

    start_total_days = sum(days_in_month[:Month_1 - 1]) + Day_1
    end_total_days = sum(days_in_month[:Month_2 - 1]) + Day_2

    diff_years = Year_2 - Year_1
    all_days_between_years = diff_years * 365

    total_days = all_days_between_years + end_total_days - start_total_days

    start_seconds = Hour_1 * 3600 + Min_1 * 60 + Sec_1
    end_seconds = Hour_2 * 3600 + Min_2 * 60 + Sec_2
    diff_seconds = end_seconds - start_seconds
    if diff_seconds < 0:
        total_days -= 1
        diff_seconds += 24 * 3600

    return total_days, diff_seconds


Year_1, Month_1, Day_1, Hour_1, Min_1, Sec_1 = 980, 2, 12, 10, 30, 1
Year_2, Month_2, Day_2, Hour_2, Min_2, Sec_2 = 980, 3, 1, 10, 31, 37
print("Task 1")
print(lizards_time_day_sec(Year_1, Month_1, Day_1, Hour_1, Min_1, Sec_1,
                           Year_2, Month_2, Day_2, Hour_2, Min_2, Sec_2))

Year_1, Month_1, Day_1, Hour_1, Min_1, Sec_1 = 1001, 5, 20, 14, 15, 16
Year_2, Month_2, Day_2, Hour_2, Min_2, Sec_2 = 9009, 9, 11, 12, 21, 11
print("Task 1")
print(lizards_time_day_sec(Year_1, Month_1, Day_1, Hour_1, Min_1, Sec_1,
                           Year_2, Month_2, Day_2, Hour_2, Min_2, Sec_2))


# Задача 2.
# Два друга A и B постоянно играют в коллекционную карточную игру (ККИ), поэтому у каждого игрока скопилась довольно большая коллекция карт.
# Каждая карта в данной игре задаётся целым числом (одинаковые карты — одинаковыми числами, разные карты — разными).
# Таким образом коллекцию можно представить как неупорядоченный набор целых чисел (с возможными повторениями).
# После каждого изменения коллекций друзья вычисляют показатель разнообразия следующим образом:
# •	A и B выкладывают на стол все карты из своей коллекции в два раздельных ряда;
# •	Далее друзья итеративно делают следующее:
# 1.	Если среди лежащих на столе карт игрока A есть такая же карта, как и среди лежащих карт игрока B — каждый игрок убирает данную карту со стола;
# 2.	Если таковых совпадений нет — процесс заканчивается.
# •	Разнообразием коллекций друзья называют суммарное количество оставшихся карт на столе.
# Обратите внимание: друзья убирают карты только со стола, карты не удаляются из коллекций при вычислении разнообразия.
# Даны начальные состояния коллекций игроков, а также Q изменений их коллекций. После каждого изменения необходимо вычислить разнообразие коллекций друзей.

def diversity_after_changes(initial_a, initial_b, updates):
    unique_a = set(initial_a)
    unique_b = set(initial_b)
    results = []

    for update in updates:
        action, who, card = update

        if who == 'A':
            if action == 1:
                unique_a.add(card)
            elif card in unique_a:
                unique_a.remove(card)
        elif who == 'B':
            if action == 1:
                unique_b.add(card)
            elif card in unique_b:
                unique_b.remove(card)

        remaining_a = unique_a - unique_b
        remaining_b = unique_b - unique_a
        total_unique = len(remaining_a) + len(remaining_b)
        results.append(total_unique)

    return results

# Пример работы функции
cards_a = [1, 2]
cards_b = [1, 2, 3, 4, 5]
modifications = [
    (1, 'A', 3),
    (1, 'A', 4),

]
print("Task 2")
print(diversity_after_changes(cards_a, cards_b, modifications))



#Задача 3
# Петя пришел на стажировку, и первая его задача была познакомиться с SQL.
# У Пети есть табличка, состоящая из N строк и M столбцов, значениями которой являются целые числа. Каждой колонке соответствует уникальное имя — строка из латинских символов.
# Пете задан запрос из Q ограничений вида:
# ColumnNamek qk valk.
# qk может принимать два значения:
# 1.	> — учитывать только те строки, где значения в ColumnNamek строго больше valk;
# 2.	< — учитывать только те строки, где значения в ColumnNamek строго меньше valk.
# Задача Пети заключается в том, чтоб посчитать сумму во всех строках, которые удовлетворяют всем ограничениям. Юный стажер уже написал скрипт и вычислил ответ. Но Петя волнуется, что где-то ошибся, поэтому просит вас перепроверить его вычисления.


N, M, Q = 2, 2, 3
cols = ['a', 'b']
rows = [
    [1, 1],
    [2, 2]
]
rules = [
    ('a', '<', 3),
    ('b', '>', 1),
    ('b', '<', 3)
]

idx_map = {col: idx for idx, col in enumerate(cols)}


def apply_filters(rows, rules, idx_map):
    result = rows
    for col, op, val in rules:
        if op == '>':
            result = [row for row in result if row[idx_map[col]] > val]
        else:
            result = [row for row in result if row[idx_map[col]] < val]
    return result


def calculate_total(rows, rules, idx_map):
    final_rows = apply_filters(rows, rules, idx_map)
    total = sum(sum(row) for row in final_rows)
    return total

print("Task 3")
result = calculate_total(rows, rules, idx_map)
print(f"Сумма значений в строках, удовлетворяющих заданным условиям: {result}")



# Задача 4.
# Межпланетная организация имеет иерархическую древовидную структуру:
# •	Корнем иерархии является генеральный директор;
# •	У каждого сотрудника 0 или более непосредственных подчиненных;
# •	Каждый сотрудник, кроме генерального директора, является непосредственным подчиненным ровно одному сотруднику.
# Каждый сотрудник, кроме генерального директора, говорит либо на языке A, либо на языке B. Директор говорит на двух языках для управления всей организацией.
# Структура всей организации хранится в текстовом документе. Каждый сотрудник представлен уникальным идентификатором - целым числом от 0 до N включительно, где 0 - идентификатор генерального директора.

#Не успел


# def calculate_language_barrier(n, languages, hierarchy):
#     employees = {i: [] for i in range(n + 1)}
#     language_of = {i: lang for i, lang in enumerate(languages, start=1)}
#     language_of[0] = 'AB'
#
#     for i in range(0, len(hierarchy), 2):
#         parent, child = hierarchy[i], hierarchy[i + 1]
#         if parent != child:
#             employees[parent].append(child)
#
#
#     def dfs(employee_id, language_path):
#         if employee_id in language_path:
#             return 0
#         new_path = language_path + [language_of[employee_id]]
#         barrier = 0
#         while new_path[-1-barrier] != new_path[0] and barrier < len(new_path) - 1:
#             barrier += 1
#         barriers[employee_id] = barrier
#         for subordinate in employees[employee_id]:
#             dfs(subordinate, new_path)
#
#     barriers = {}
#     dfs(0, ['AB'])
#
#     return [barriers[i] for i in range(1, n + 1)]
#
#
# n1 = 5
# languages1 = ['A', 'B', 'B', 'A', 'B']
# hierarchy1 = [0, 1, 1, 2, 3, 4, 4, 5, 5, 3, 2, 0]
# n2 = 4
# languages2 = ['A', 'B', 'A', 'A']
# hierarchy2 = [0, 1, 2, 3, 3, 4, 4, 2, 1, 0]
#
# barriers1 = calculate_language_barrier(n1, languages1, hierarchy1)
# barriers2 = calculate_language_barrier(n2, languages2, hierarchy2)




# Задача 5.
# Определим близость двух целочисленных массивов как длину их наибольшего совпадающего префикса (см. примечание).
# Примеры:
# •	Близость [1, 2, 1, 3] и [1, 2, 3, 2] равна 2 — префикс [1, 2] совпадает;
# •	Близость [1, 2, 3] и [3, 2, 1] равна 0.
# Дано n целочисленных массивов a1,a2,…,an.
# Необходимо вычислить сумму близостей массивов ai и aj для каждой пары 1≤i<j≤n.


def find_prefix_length(arr1, arr2):
    index = 0
    while index < len(arr1) and index < len(arr2) and arr1[index] == arr2[index]:
        index += 1
    return index

def sum_prefix_lengths(all_arrays):
    total_prefix_length = 0
    for i in range(len(all_arrays)):
        for j in range(i + 1, len(all_arrays)):
            total_prefix_length += find_prefix_length(all_arrays[i], all_arrays[j])
    return total_prefix_length

example_arrays_1 = [
    [1, 2],
    [1, 3],
    [1, 2, 3]
]

example_arrays_2 = [
    [5],
    [1, 2],
    [5, 1, 2]
]

result_1 = sum_prefix_lengths(example_arrays_1)
result_2 = sum_prefix_lengths(example_arrays_2)
print("Task 5")
print(f"Для первого примера общая сумма префиксов: {result_1}")
print(f"Для второго примера общая сумма префиксов: {result_2}")