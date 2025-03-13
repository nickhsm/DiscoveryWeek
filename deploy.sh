#!/bin/bash
sudo docker build -t dw:latest .
sudo docker run -d -p 80:8501 dw:latest
