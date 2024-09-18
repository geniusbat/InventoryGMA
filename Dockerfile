#--AUTOMATE-BUILD--
#Deploy image for InventoryGMA
FROM python:3.12.4

WORKDIR /InventoryGMA

ENV PYTHONUNBUFFERED=1
ENV IGMA_DEBUG=True
ENV IGMA_EXTERNAL_DB=False

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8145

CMD ["python", "InventoryGMA/manage.py", "runserver", "0.0.0.0:8145"]
#CMD ["gunicorn","--bind", ":8145", "InventoryGMA/InventoryGMA.wsgi:application"]