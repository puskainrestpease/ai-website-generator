# API Documentation

## Authentication 🔐

`POST /api/auth/register` - Регистрация пользователя  
`POST /api/auth/login` - Авторизация

## Projects 🛠️

`POST /api/projects` - Создать новый проект  
`GET /api/projects/{id}` - Получить проект  
`DELETE /api/projects/{id}` - Удалить проект

Пример запроса:
```json
{
  "prompt": "Создай лендинг для стартапа",
  "framework": "nextjs"
}