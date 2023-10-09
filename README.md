Flask приложение с OpenAI и Llama2 Serve Online
Это Flask-приложение использует OpenAI и Llama2 Serve Online для генерации последовательностей аминокислот на основе заданных свойств.

Требования
Docker
Docker Compose
Установка и запуск
Клонируйте репозиторий:

bash
Copy code
git clone [ссылка на ваш репозиторий]
cd [название директории вашего репозитория]
Установите переменные окружения:

Создайте файл .env в корневой директории проекта и добавьте в него ваш ключ OpenAI и информацию о Llama2 Serve Online:

makefile
Copy code
OPENAI_API_KEY=ваш_ключ_openai
LLAMA2_SERVE_URL=ссылка_на_llama2_serve_online
Запустите приложение с помощью Docker Compose:

bash
Copy code
docker-compose up --build
После этого ваше приложение будет доступно по адресу http://localhost:5000.

Использование
Откройте веб-браузере http://localhost:5000 и следуйте инструкциям на странице.
