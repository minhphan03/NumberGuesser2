FROM python:3

RUN mkdir GAME_REPO
RUN cd GAME_REPO

WORKDIR /GAME_REPO

COPY . .

CMD ["python3", "-u", "src/main.py"]

 
