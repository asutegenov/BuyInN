# Automated Testing #

## Сценарий проверки тестов для Linux и macOS ##

>__В тесте участвуют только файлы, в начале имени которых есть `test_`__
>__Проверьте установлен ли у вас `Python 3`. Введите в терминале `python3 --version`__
>__Если у вас не установлен `Python 3`, в таком случае перейдите по этой ссылке [Download Python 3.8.9](https://www.python.org/downloads/release/python-389/)__

### Инструкция ###

1. Скачать [ChromeDriver](https://chromedriver.chromium.org)
2. Переместить `chromedriver` в директорию `/usr/local/bin` и дать разрешения на запуск
   * Отройте Терминал
   * Перейдите в директорию, куда скачался `chromedriver`
   * Переместите `sudo mv chromedriver /usr/local/bin` webdriver
   * Дайте разрешения на запуск `sudo chmod +x /usr/local/bin/chromedriver`

3. Настроить окружение через Терминал:
   * Откройте Терминал
   * Создайте директорию `BuyInN` и перейдите в нее
   * Создайте окружение `env_buy` -- `python3 -m venv env_buy`
   * Активируйте окружение `source env_buy/bin/activate`
   * Клонируйте этот репозиторий и перейдите к тему в Терминале
   * Находясь в корневой директории репозитория введите в терминале `pip install -r requirements.txt`

    >__Окружение создано и готово к работе!__

4. Запустить тест
   * В Терминале, перейдите в корневую директорию склонированного репозитория
   * Введите в Терминал `python -m pytest -sv test_business_process.py`
