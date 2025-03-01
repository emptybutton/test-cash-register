# test-cash-register
Тестовое задание для компании Гроссбит.

## Развертывание для разработки
```bash
git clone https://github.com/emptybutton/test-cash-register.git
docker compose -f test-cash-register/deployments/dev/docker-compose.yaml up
```

В контейнере используется своё виртуальное окружение, сохранённое отдельным volume-ом, поэтому можно не пересобирать образ при изменении зависимостей.

Для ide можно сделать отдельное виртуальное окружение в папке проекта:
```bash
uv sync --extra dev --directory test-cash-register
```

> [!NOTE]
> При изменении зависимостей в одном окружении необходимо синхронизировать другое с первым:
> ```bash
> uv sync --extra dev
> ```

Дополнительно настроен мониторинг, поэтому можно просматривать логи через [Grafana](http://localhost:3000).

## Структура кода
![*code-diagram*](https://github.com/emptybutton/test-cash-register/blob/main/assets/code.drawio.png?raw=true)

- `view` — определяет управляющий способ ввода-вывода
- `operation` — алгоритмическое ядро системы
- `detail` — определяет управляемый способ ввода-вывода.
