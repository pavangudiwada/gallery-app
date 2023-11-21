# Build using docker build -t galleryapp .
# Run using docker run -p 8501:8501 galleryapp
FROM python:3.11-slim

WORKDIR /galleryapp

COPY pyproject.toml poetry.lock ./
RUN pip install poetry

#No virtual env's because its already container
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev

COPY . .

EXPOSE 8501 
EXPOSE 8888

CMD ["poetry", "run", "streamlit", "run", "app.py"]
