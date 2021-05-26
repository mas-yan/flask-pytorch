import requests


resp = requests.post("http://localhost:5000/predict",
                     files={'file': open('dog.png', 'rb')})
print(resp.text)
