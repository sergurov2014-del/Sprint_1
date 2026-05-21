types = {
    1: "Блокирующий",
    2: "Критический",
    3: "Значительный",
    4: "Незначительный",
    5: "Тривиальный",
}
tickets = {
    1: ["API_45", "API_76", "E2E_4"],
    2: ["UI_19", "API_65", "API_76", "E2E_45"],
    3: ["E2E_45", "API_45", "E2E_2"],
    4: ["E2E_9", "API_76"],
    5: ["E2E_2", "API_61"],
}


def remove_copy(
    some_dict,
):  # удаляем дубли: добавляем элементы в множество all_items, создаём новый список из того, чего нет в all_items
    all_items = set()
    result = {}
    for key, value in some_dict.items():
        result[key] = []
        for v in value:
            if v not in all_items:
                all_items.add(v)
                result[key].append(v)

    return result  # вернёт {1: ['API_45', 'API_76', 'E2E_4'], 2: ['UI_19', 'API_65', 'E2E_45'], 3: ['E2E_2'], 4: ['E2E_9'], 5: ['API_61']} едем дальше


def ticket_to_type(type, ticket):
    tickets_by_type = {}
    for key, value in type.items():
        tickets_by_type[value] = remove_copy(ticket)[key]
    return tickets_by_type  # по условию задачи "Вызывать функцию необязательно." , но проверкой служил вызов print(ticket_to_type(types, tickets))
