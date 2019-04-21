FROM python:3.5.3
 
WORKDIR /app/
 
COPY requirements.txt /app/
RUN pip install -r ./requirements.txt
 
COPY app.py init.py /app/
COPY Insurance_charge_prediction.pkl /app/

EXPOSE 5000
 
ENTRYPOINT python ./app.py
 
