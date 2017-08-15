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
    {"type":"Polygon","coordinates":[[[-5.273512601852417,42.81137220349083],[-5.273512601852417,42.811803118457306]
    ,[-5.272732079029083,42.811803118457306],[-5.272732079029083,42.81137220349083],[-5.273512601852417,42.81137220349083]]]}}]})

    create_geostore(geojson)
