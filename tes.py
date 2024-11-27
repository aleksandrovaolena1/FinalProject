import requests

# Простой тест для проверки импорта
response = requests.get("https://www.google.com")
print(response.status_code)
