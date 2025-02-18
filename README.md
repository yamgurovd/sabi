# СБИС

## Краткое описание

1. Создать и активировать виртуальное окружение

```angular2html
python3 -m venv .venv
source .venv/bin/activate
```

2. Установить библиотеки из requirements.txt

```shell
pip install -r requirements.txt
```

## 2 Команды для запуска тестов на локальном компьютере

### Запуск тестов с генерацией отчета

```shell
python -m pytest -s -v --html=report.html -n auto reports/
```

###  Запуск всех тестов

```shell
pytest
```

### Запуск конкретного теста

```shell
pytest tests/test_saby_to_tensor_navigation.py::test_saby_to_tensor_navigation
```

### Запуск с генерацией HTML-отчета

```shell
pytest --html=report.html
```

### Запуск с маркерами

```shell
pytest -m smoke
```

### Параллельный запуск (требуется pytest-xdist)

```shell
pytest -n auto
```

## 3 Установка и настройка docker в локальном компьютере для линукса - https://docs.docker.com/engine/install/ubuntu/

1. Set up Docker's apt repository.

```shell
# Add Docker's official GPG key:
sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

# Add the repository to Apt sources:
echo \
"deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
$(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
```

2. Install the Docker packages.

```shell
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

3. Verify that the Docker Engine installation is successful by running the hello-world image.

```shell
sudo docker run hello-world
```

4. Для запуска docker без sudo необходимо сделать:

```shell
sudo usermod -aG docker $USER
```

5. /home/d/.docker - В директории на локальном компьютере удалить папку
6. Выполнить reboot

## 3.1 Запуск проекта в Docker

1. Перейти в директорию проекта на локальном компьютере через терминал пример:
   <img alt="Пример" height="100" src="![img.png](img.png)" title="Пример" width="100"/>
2. Собрать образ контейнера

```shell
docker build -t ui .
```

3. Проверить добавление образа

```shell
docker images
```

5. Команды, чтобы удалить контейнер и образ

```angular2html
docker rm
<id_container>
    docker rmi
    <id_images>
```
