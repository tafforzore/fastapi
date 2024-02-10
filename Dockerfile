FROM python:3.9
RUN cd app/
RUN pip install -r requirements.txt
RUN cd ../
EXPOSE 5000
COPY ./app /app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "5000"]