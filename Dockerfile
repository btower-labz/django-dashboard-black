FROM python:3.6

ENV FLASK_APP run.py

# TODO: .env should be mounted
RUN pwd
COPY manage.py gunicorn-cfg.py requirements.txt ./
COPY app app
COPY authentication authentication
COPY core core

RUN pip install -r requirements.txt

RUN python manage.py collectstatic
#RUN python manage.py makemigrations
#RUN python manage.py migrate

EXPOSE 5005
CMD ["gunicorn", "--config", "gunicorn-cfg.py", "core.wsgi"]
