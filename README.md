# test-cash-register
Тестовое задание для компании Гроссбит.

## Развертывание для разработки
```bash
git clone https://github.com/emptybutton/test-cash-register.git

docker plugin install grafana/loki-docker-driver:2.9.4 --alias loki --grant-all-permissions
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

Настроен мониторинг, поэтому можно [просматривать логи](http://localhost:3000) через Grafana.

## Структура кода
![*code-diagram*](https://github.com/emptybutton/test-cash-register/blob/main/assets/code.drawio.png?raw=true)

- `view` — определяет управляющий способ ввода-вывода
- `operation` — алгоритмическое ядро системы
- `detail` — определяет управляемый способ ввода-вывода.
