FROM python:alpine3.7
COPY . /todo
WORKDIR /todo
RUN pip install -r requirements.txt 
EXPOSE 5001 
ENTRYPOINT [ "python" ] 
CMD [ "run.py" ] 