FROM ubuntu


RUN apt update
RUN apt install python3-pip -y
RUN pip3 install Flask
RUN pip3 install python-dotenv
RUN pip3 install click


WORKDIR /app

COPY app.py .
COPY environment.txt .

CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]