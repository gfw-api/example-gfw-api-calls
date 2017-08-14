import requests
import json

def count_prodes(geostore, period, agg_values=True):
	'''Count Prodes deforestatoin area for a region (defined by geostore) and time period of interest
	:param geostore: a unique hash assigned to a geographic area by the geostore microservice
	:param period: time period recorded in format YYYY-MM-DD,YYYY-MM-DD
	:return: an area estimate of prodes deforestation for the area and time periods'''

	#production api url
	api_path = 'http://production-api.globalforestwatch.org/prodes-loss'

	get_request = (api_path + '?period=' + period + '&geostore=' + geostore)

	r = requests.get(get_request)

	data = r.json()

	data_pretty = json.dumps(data, indent=2)

	print data_pretty


if __name__ == "__main__":

	count_prodes('3b58aa24c01ab2961a729650818cf0c7', '2001-01-01,2015-12-30')

	#view geostore on a map
	#https://production-api.globalforestwatch.org/geostore/3b58aa24c01ab2961a729650818cf0c7/view
