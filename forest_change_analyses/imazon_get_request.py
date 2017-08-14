import json
import requests

def count_imazon_alerts(geostore, period):
	'''Count Imazon Alerts for an area (defined by geostore) and time period of interest.
    Note that Imazon is only available for Brazil
	:param geostore: a unique hash assigned to a geographic area by the geostore microservice
	:param period: time period recorded in format YYYY-MM-DD,YYYY-MM-DD
	:return: a count of Glad Alerts for the area and time period, as well as download links'''

	#production api url
	api_path = 'http://production-api.globalforestwatch.org/imazon-alerts'

	get_request = (api_path + '?period=' + period + '&geostore=' + geostore + '&aggregate_values='
     + str(agg_values))

	r = requests.get(get_request)

	data = r.json()

	data_pretty = json.dumps(data, indent=2)

	print data_pretty


if __name__ == "__main__":

	count_imazon_alerts('3b58aa24c01ab2961a729650818cf0c7', '2015-01-01,2017-07-30')

	#view geostore on a map
	#https://production-api.globalforestwatch.org/geostore/3b58aa24c01ab2961a729650818cf0c7/view
