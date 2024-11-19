import streamlit as st
import random

# Список вопросов и ответов
questions = [
    {
        "question": "1. Под методом экономического анализа понимается:",
        "options": ["а) совокупность приемов и способов изучения экономической действительности;", 
                    "б) системное, комплексное изучение, измерение и обобщение влияния факторов на результаты деятельности предприятия;", 
                    "в) все вышеперечисленное."],
        "answer": "б"
    },
    {
        "question": "2. Особенность метода экономического анализа заключается в:",
        "options": ["а) разработке и использовании системы показателей;", 
                    "б) раскрытии и изучении причин (факторов);", 
                    "в) измерении взаимосвязи и взаимозависимости между показателями;", 
                    "г) все вышеперечисленное."],
        "answer": "г"
    },
    {
        "question": "3. Методика экономического анализа представляет собой:",
        "options": ["а) совокупность конкретных приемов, способов и средств;", 
                    "б) план проведения анализа хозяйственной деятельности экономического субъекта;", 
                    "в) процесс обработки, передачи и хранения экономической информации на предприятии;", 
                    "г) все вышеперечисленное."],
        "answer": "а"
    },
    {
        "question": "4. Методика экономического анализа должна содержать:",
        "options": ["а) цели и задачи анализа;", 
                    "б) систему показателей;", 
                    "в) рекомендации по последовательности и периодичности;", 
                    "г) описание способов исследования;", 
                    "д) все вышеперечисленное."],
        "answer": "д"
    },
    {
        "question": "5. Относительные величины представляют собой:",
        "options": ["а) обобщение соответствующей совокупности типичных показателей;", 
                    "б) соотношение величины изучаемого явления с величиной другого явления;", 
                    "в) количественные размеры явления в единицах меры;", 
                    "г) абсолютные величины."],
        "answer": "б"
    },
    {
        "question": "6. Обобщение соответствующей совокупности типичных показателей показывает:",
        "options": ["а) относительные величины;", 
                    "б) абсолютные величины;", 
                    "в) средние величины;", 
                    "г) все вышеперечисленное."],
        "answer": "в"
    },
    {
        "question": "7. Группировка, которая используется при выделении групп населения по роду деятельности:",
        "options": ["а) структурная;", 
                    "б) типологическая;", 
                    "в) аналитическая."],
        "answer": "б"
    },
    {
        "question": "8. Аналитическая группировка используется при:",
        "options": ["а) изучении состава предприятий;", 
                    "б) определении наличия, направления и формы связи;", 
                    "в) выделении групп населения;", 
                    "г) все вышеперечисленное."],
        "answer": "б"
    },
    {
        "question": "9. Анализ рядов динамики используется для:",
        "options": ["а) выявления основной тенденции;", 
                    "б) выделения сезонных колебаний;", 
                    "в) выявления связи между явлениями;", 
                    "г) все вышеперечисленное."],
        "answer": "г"
    },
    {
        "question": "10. Прием сравнения используется для:",
        "options": ["а) проверки качества информации;", 
                    "б) выделения сезонных колебаний;", 
                    "в) определения общих черт и различий;", 
                    "г) все вышеперечисленное."],
        "answer": "в"
    },
    {
        "question": "11. Балансовый прием используется для:",
        "options": ["а) проверки качества информации;", 
                    "б) детализации факторов;", 
                    "в) определения количественного влияния;", 
                    "г) все вышеперечисленное."],
        "answer": "г"
    },
    {
        "question": "12. Случаи, при которых используется сравнительная оценка:",
        "options": ["а) необходимо сопоставить работу нескольких объектов;", 
                    "б) необходимо сопоставить работу на основе единой системы;", 
                    "в) для сопоставления результатов во времени;", 
                    "г) все вышеперечисленное."],
        "answer": "д"
    },
    {
        "question": "13. Основным этапом сравнительной оценки является:",
        "options": ["а) анализ рядов динамики;", 
                    "б) расчет интегрального показателя;", 
                    "в) расчет и оценка баланса отклонений;", 
                    "г) все вышеперечисленное."],
        "answer": "б"
    },
    {
        "question": "14. При проведении сравнительной оценки используют:",
        "options": ["а) метод скользящей средней;", 
                    "б) метод аналитического выравнивания;", 
                    "в) метод суммы мест;", 
                    "г) все вышеперечисленное."],
        "answer": "е"
    },
    {
        "question": "15. Модель в экономическом анализе должна:",
        "options": ["а) отражать существенные свойства объекта;", 
                    "б) быть адекватной действительности;", 
                    "в) все вышеперечисленное."],
        "answer": "в"
    },
    {
        "question": "16. Детерминированная модель имеет место, когда:",
        "options": ["а) связь факторов с результативным показателем носит функциональный характер;", 
                    "б) связь факторов является неполной;", 
                    "в) все вышеперечисленное."],
        "answer": "а"
    },
    {
        "question": "17. Факторный анализ – это:",
        "options": ["а) определение формы зависимости;", 
                    "б) методика комплексного изучения;", 
                    "в) использование приемов абсолютных и относительных разниц;", 
                    "г) все вышеперечисленное."],
        "answer": "б"
    },
    {
        "question": "18. Основными задачами факторного анализа являются:",
        "options": ["а) отбор факторов;", 
                    "б) определение формы зависимости;", 
                    "в) моделирование взаимосвязей;", 
                    "г) расчет влияния факторов;", 
                    "д) все вышеперечисленное."],
        "answer": "е"
    },
    {
        "question": "19. При обратном факторном анализе происходит:",
        "options": ["а) исследование дедуктивным способом;", 
                    "б) исследование причинно-следственных связей;", 
                    "в) все вышеперечисленное."],
        "answer": "б"
    },
    {
        "question": "20. По времени применения факторный анализ подразделяется на:",
        "options": ["а) одноступенчатый и многоступенчатый;", 
                    "б) оперативный, перспективный и ретроспективный;", 
                    "в) прямой и обратный;", 
                    "г) детерминированный и стохастический."],
        "answer": "б"
    },
    {
        "question": "21. Последовательность расстановки факторов в модели не имеет значения при применении:",
        "options": ["а) приема цепных подстановок;", 
                    "б) приема относительных разниц;", 
                    "в) приема абсолютных разниц;", 
                    "г) интегрального метода."],
        "answer": "б,г"
    },
    {
        "question": "22. Прием абсолютных разниц применяется:",
        "options": ["а) в моделях аддитивного типа;", 
                    "б) в моделях мультипликативного типа;", 
                    "в) в смешанных моделях;", 
                    "г) все вышеперечисленное."],
        "answer": "д"
    },
    {
        "question": "23. Основной характер зависимости, обуславливающий выбор метода относительных разниц:",
        "options": ["а) результативный признак изменяется пропорционально;", 
                    "б) результативный признак изменяется в большей степени;", 
                    "в) результативный признак изменяется в меньшей степени."],
        "answer": "а"
    },
    {
        "question": "24. Особенность интегрального метода состоит в том, что:",
        "options": ["а) дает более точные результаты;", 
                    "б) расположение факторов в модели не имеет значения;", 
                    "в) все вышеперечисленное."],
        "answer": "в"
    },
    {
        "question": "25. Экономико-математические методы в экономическом анализе по разделам математики подразделяются на:",
        "options": ["а) эвристические;", 
                    "б) приближенные;", 
                    "в) методы исследования операций;", 
                    "г) методы математического программирования;", 
                    "д) эконометрические;", 
                    "е) все вышеперечисленное за исключением «а»;", 
                    "ж) все вышеперечисленное за исключением «а» и «б»."],
        "answer": "а,в,г,д"
    },
    {
        "question": "26. Признак, по которому экономико-математические методы в экономическом анализе подразделяются на балансовые, факторные, оптимизационные и имитационные:",
        "options": ["а) тип аналитических задач;", 
                    "б) точность результатов;", 
                    "в) раздел математики."],
        "answer": "а"
    },
    {
        "question": "27. Для анализа связи между показателями организационно-технического уровня организации и такими показателями производства, как производительность труда, фондоотдача, рентабельность, используют:",
        "options": ["а) эконометрические методы;", 
                    "б) методы элементарной математики;", 
                    "в) методы математической статистики;", 
                    "г) методы исследования операций."],
        "answer": "в"
    },
    {
        "question": "28. Методы исследования операций используются для:",
        "options": ["а) анализа экономических явлений;", 
                    "б) разработки методов целенаправленных действий;", 
                    "в) решения экономических задач на основе интуиции;", 
                    "г) изучения стохастической связи между явлениями."],
        "answer": "б"
    },
    {
        "question": "29. Методы математического программирования используются для:",
        "options": ["а) решения задач оптимизации хозяйственной деятельности;", 
                    "б) решения экономических задач на основе интуиции;", 
                    "в) изучения стохастической связи между явлениями;", 
                    "г) разработки методов целенаправленных действий."],
        "answer": "а"
    },
    {
        "question": "30. При построении отраслевых, межотраслевых балансов, а также балансов отдельного предприятия используют:",
        "options": ["а) методы элементарной математики;", 
                    "б) корреляционно-регрессионный анализ;", 
                    "в) эконометрические методы;", 
                    "г) дисперсионный анализ."],
        "answer": "в"
    },
]

# Функция для запуска теста
def run_test():
    st.title("Экономический анализ - Тест")
    score = 0
    total_questions = len(questions)
    answered_questions = []

    # Перемешиваем вопросы один раз
    shuffled_questions = random.sample(questions, len(questions))

    # Словарь для хранения ответов
    user_answers = {}

    # Отображаем все вопросы
    for i, question in enumerate(shuffled_questions):
        st.write(question["question"])
        for option in question["options"]:
            st.write(option)

        # Ввод ответа с уникальным ключом
        user_answers[i] = st.text_input(f"Введите ваш ответ (а, б, в, г, д, е, ж) для вопроса {i + 1}:", max_chars=10, key=f"answer_{i}")

    # Кнопка для проверки ответов
    if st.button("Проверить ответы"):
        for i, question in enumerate(shuffled_questions):
            if user_answers[i].strip() in question["answer"].split(","):
                score += 1
                answered_questions.append((question["question"], "Правильно"))
            else:
                answered_questions.append((question["question"], "Неправильно"))

        # Результаты
        st.write(f"Ваш результат: {score} из {total_questions} баллов.")
        st.write("Список вопросов и ваши ответы:")
        for q, result in answered_questions:
            st.write(f"{q} - {result}")

# Запуск теста
if __name__ == "__main__":
    run_test()
