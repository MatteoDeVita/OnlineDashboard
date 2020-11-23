FROM python
COPY ./app.py /home
WORKDIR /home
#RUN apt-get -y install python3-venv
#RUN python3 -m venv env
#RUN source env/bin/activate
RUN pip3 install Flask==1.0.2 Flask-Cors==3.0.7
EXPOSE 5000
ENTRYPOINT python app.py
