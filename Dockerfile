FROM python:3.9
RUN ls
EXPOSE 5000
RUN ls
COPY ./ /app

CMD ["uvicorn", ".main:app", "--host", "0.0.0.0", "--port", "5000"]