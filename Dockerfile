FROM python:3.6

RUN mkdir /src
WORKDIR /src
COPY ./requirements.txt .
RUN pip install -r requirements.txt

RUN mkdir ./services
RUN mkdir ./decimex
COPY ./decimex ./decimex
COPY ./services ./services
COPY ./consts.py .
COPY ./main.py .

CMD [ "python","./main.py" ]