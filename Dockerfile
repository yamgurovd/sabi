FROM ubuntu:22.04


ENV TZ=Europe/Moscow
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone


RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    wget \
    unzip \
    curl \
    chromium-browser \
    chromium-chromedriver \
    && rm -rf /var/lib/apt/lists/*


WORKDIR /tests


COPY requirements.txt .


RUN pip3 install --no-cache-dir -r requirements.txt


COPY . .


CMD ["python3", "-m", "pytest", "-v", "-s", "--html=reports/report.html"]