# 1. Start with a lightweight Linux OS that already has Python installed
FROM python:3.11-slim

# 2. Set the folder inside the container where we will do our work
WORKDIR /app

# 3. Copy our dependency list into the container
COPY requirements.txt .

# 4. Tell the container to install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy all our actual backend code (main.py) into the container
COPY . .

# 6. Document that this container needs port 8000 open
EXPOSE 8000

# 7. The exact terminal command to run when the container wakes up
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]