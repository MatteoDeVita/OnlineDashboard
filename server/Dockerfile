FROM python
COPY ./app.py ./requirement.txt /home/
WORKDIR /home
RUN pip3 install -r requirement.txt
EXPOSE 5000
CMD python app.py
