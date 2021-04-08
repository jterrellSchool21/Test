# Test
# Запуск:
Для запуска: sh run.sh
# API:
Для получения пользователем токена: GET запрос http://127.0.0.1:8000/api/get_token
Для получения списка активных опросов: GET запрос http://127.0.0.1:8000/api/polls
Для получения списка активных вопросов: GET запрос http://127.0.0.1:8000/api/questions
Для ответа на опросы: POST запрос http://127.0.0.1:8000/api/vote/ HEADER: {"Token": "токен пользователя"} BODY: {"question_id": "idВопроса", "answers": "Ответ на вопрос"}
Для добавления опроса: POST запрос http://127.0.0.1:8000/api/questions/<int:question_id>/ {"name": "Название опроса", "date_start": "Дата начала опроса", "date_end": "Дата окончания опроса"}