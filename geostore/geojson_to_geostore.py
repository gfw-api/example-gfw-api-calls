import requests
import json

def create_geostore(geojson):

    api_path = "https://production-api.globalforestwatch.org/geostore"

    payload = {"geojson": geojson}

    r = requests.post(api_path, json=payload)

    geostore_id = r.json()["data"]["id"]

    print geostore_id

if __name__ == "__main__":

    geojson = ({"type":"FeatureCollection","features":[{"type":"Feature","properties":{},"geometry":{"type":"Polygon","coordinates":
    [[[-70.0711,-13.0029],[-70.0794,-13.0323],[-70.0372,-13.0434],[-69.9826,-13.0494],[-69.9105,-13.0571],
    [-69.8936,-13.0397],[-69.9005,-13.022],[-69.9441,-13.0123],[-69.9654,-13.0046],[-70.0018,-13.0029],
    [-70.0299,-13.0046],[-70.0598,-13.0012],[-70.0711,-13.0029]]]}}]})

    create_geostore(geojson)
