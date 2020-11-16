FROM tiangolo/uwsgi-nginx-flask:latest
RUN /usr/local/bin/python -m pip install --upgrade pip
COPY ./dashboard /app/
COPY ./requirements.txt .
RUN pip3 install -r requirements.txt
ENV LISTEN_PORT 5000
ENV UWSGI_INI /app/uwsgi.ini
EXPOSE 5000
WORKDIR /app
