FROM python:3.11-slim
WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE=1 \
PYTHONUNBUFFERED=1
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
ENV FLASK_APP=app.py
# simple helper so docker-compose command works
RUN printf '#!/usr/bin/env python3\nfrom src.db import db_up\nif __name__=="__main__": db_up()\n' > /usr/local/bin/flask-db-up && \
chmod +x /usr/local/bin/flask-db-up
CMD ["flask", "run", "--host=0.0.0.0", "--port=8000"]
