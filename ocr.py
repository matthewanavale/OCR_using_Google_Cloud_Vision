import base64
import json
import os

from google.cloud import vision

def detect_text(path):
    client = vision.ImageAnnotatorClient()

    with open(path, 'rb') as image_file:
        content = image_file.read()
    image=vision.Image(content=content)
    response = client.text_detection(image=image)
    texts = response.text_annotations
    ocr_text = []
    for text in texts:
        ocr_text.append(text.description)
    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(response.error.message))
    return texts[0].description

def main():
    image = "Assets/receipt3.jpg"

    text = detect_text(image)
    #print(image_path)
    print(text)

if __name__ == "__main__":
    main()