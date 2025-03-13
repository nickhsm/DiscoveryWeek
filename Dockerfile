FROM python:3.11
RUN apt update && apt upgrade && apt install libusb-1.0-0 && apt autoremove
COPY . /app
WORKDIR /app
RUN pip install --no-cache-dir -r requirements.txt
CMD ["streamlit", "run", "frontend.py"]
