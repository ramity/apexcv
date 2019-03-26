FROM python:latest

RUN apt-get update

RUN pip install Pillow
RUN pip install opencv-python-headless
RUN pip install opencv-contrib-python-headless
RUN pip install pytesseract

RUN apt-get install -y tesseract-ocr
RUN apt-get install -y tesseract-ocr-eng

WORKDIR /var/src

ENTRYPOINT tail -f /dev/null
