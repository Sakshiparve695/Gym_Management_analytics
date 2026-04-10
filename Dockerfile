FROM python:3.10

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["uvicorn", "Gym_Management_System:app", "--host", "0.0.0.0", "--port", "8000"]