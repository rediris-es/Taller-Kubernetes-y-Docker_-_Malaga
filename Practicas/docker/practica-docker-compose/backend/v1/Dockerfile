FROM python:3.9
WORKDIR /app
COPY . .
RUN pip install flask mysql-connector-python
ENV FLASK_APP=app.py
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
