# Test
# API:
Для получения пользователем токена: GET запрос http://127.0.0.1:8000/api/users/ без параметров
Для получения списка активных вопросов: GET запрос http://127.0.0.1:8000/api/polls/ без параметров
Для ответа на опросы: GET запрос http://127.0.0.1:8000/api/users/ {"Answers": {"token": "токен пользователя", "question_id": "idОпроса_idОтвета"}}
Для добавления опроса: POST запрос http://127.0.0.1:8000/api/polls/ {"Active": {"title": "Название опроса", "date_published": "Дата публикации", "is_active": "Активен ли опрос (true/false)", "date_end": "Дата окончания в формате 2021-04-03T11:30:29.918772Z", "question_id": "Id опроса"}
