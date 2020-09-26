# Captionify
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1iqwn5OKrrBD1vxx7EoGJRvEquBfxwQpX?usp=sharing)]

## Description
Uploading an image, and our application will generate a description for this image. The 

## Visuals
Below is the demo output of our model

![alt_text](https://github.com/jaykshirsagar05/captionify/blob/master/caption1.png)

## Installation
Basic requirements
* Python3
* Docker

## Deploy as a docker image and run
Steps to run in your local system:
```bash
git clone https://github.com/jaykshirsagar05/captionify.git
cd Captionify
Docker-compose build
Docker-compose up
```
visit to http://172.19.0.3:8501/ for streamlit app.

visit to for http://127.0.0.1:8000/docs server side(fastapi)

NOTE: You need to change the path of pre-trained model in ![caption.py](https://github.com/jaykshirsagar05/captionify/blob/master/fastapi/caption.py) file.

## Support

## Roadmap

## Contributing

## Authors and acknowledgement
![Jay Kshirsagar](https://github.com/jaykshirsagar05)

![Qiaochu Xiong](https://github.com/6390wer)

### References


## Project Status
