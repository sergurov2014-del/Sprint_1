class TestCase:

    def __init__(
        self, steps={}, result=None
    ):  # инициализируются поля: steps — шаги тест-кейса, в качестве параметра принимает пустой словарь; result — ожидаемый результат выполнения тест-кейса, принимает None в качестве параметра.
        self.steps = steps
        self.result = result

    def set_step(
        self, step_number, step_text
    ):  # добавляет в словарь steps шаг тест-кейса. Принимает два параметра: step_number и step_text. Ключ — это step_number(номер шага), а значение — step_text (текстовое описание шага).
        self.steps[step_number] = step_text

    def delete_step(
        self, step_number
    ):  # удаляет шаг из steps по ключу step_number, который передали в метод.
        self.steps.pop(step_number)

    def set_result(
        self, result
    ):  # устанавливает ожидаемый результат. Он помещает его в атрибут result по параметру result, который передали методу.
        self.result = result

    def get_test_case(
        self,
    ):  # печатает информацию о составе тест-кейса в формате {'Шаги': {<номер шага>: '<описание шага>'}, 'Ожидаемый результат': '<вывод ожидаемого результата>'}

        print(f"{{'Шаги': {self.steps}, 'Ожидаемый результат': '{self.result}'}}")


