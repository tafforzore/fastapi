FROM python:3.9
RUN ls
RUN pip install -r requirements.txt
EXPOSE 5000
RUN ls
COPY ./ /app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "5000"]