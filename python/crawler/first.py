import urllib.request

def download_web_image(url):
    urllib.request.urlretrieve(url, "messi.jpg")

download_web_image('https://media-public.fcbarcelona.com/20157/0/document_thumbnail/20197/11/31/187/45817611/1.0-10/45817611.jpg?t=1493315026000')