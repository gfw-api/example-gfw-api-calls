import requests
import json

def create_geostore(geojson):

    api_path = "https://production-api.globalforestwatch.org/geostore"

    payload = {"geojson": geojson}

    r = requests.post(api_path, json=payload)

    geostore_id = r.json()["data"]["id"]

    print geostore_id

if __name__ == "__main__":

    geojson = ({"type":"FeatureCollection","features":[{"type":"Feature","properties":{},"geometry":
    {"type":"Polygon","coordinates":[[[-70.0104,-13.0211],[-70.0054,-13.0123],[-69.9946,-13.0169],
    [-69.987,-13.0158],[-69.9827,-13.0114],[-69.9759,-13.0139],[-69.9778,-13.0203],[-69.969,-13.0171],
    [-69.9642,-13.0241],[-69.9625,-13.0283],[-69.9548,-13.0357],[-69.951,-13.0345],[-69.9496,-13.029],
    [-69.9398,-13.0276],[-69.9381,-13.0337],[-69.9256,-13.0372],[-69.913,-13.0338],[-69.9125,-13.0464],
    [-69.9362,-13.0572],[-69.9867,-13.0467],[-70.0104,-13.0211]]]}}]})

    create_geostore(geojson)
