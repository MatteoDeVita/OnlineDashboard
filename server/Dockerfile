FROM python
COPY ./app.py ./requirement.txt /home/
WORKDIR /home
#RUN apt-get -y install python3-venv
#RUN python3 -m venv env
#RUN source env/bin/activate
RUN pip3 install -r requirement.txt
EXPOSE 5000
CMD python app.py
