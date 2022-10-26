FROM python:alpine
WORKDIR /app
COPY query.py /app
RUN cd /app && pip install flask requests prometheus_client
EXPOSE 8000 80
CMD [ "python","/app/query.py" ]
