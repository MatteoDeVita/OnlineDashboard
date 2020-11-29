FROM python
COPY ./app.py ./requirement.txt ./client_secret.json /home/
WORKDIR /home
RUN pip3 install -r requirement.txt
EXPOSE 5000
CMD python app.py
