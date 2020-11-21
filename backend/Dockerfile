FROM python:3.7.2
WORKDIR /app
ADD . /app
RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple --upgrade pip 
RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt
CMD [ "uwsgi", "app.ini" ]