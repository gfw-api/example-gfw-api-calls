import requests
import json

def count_tcloss(geostore, period, thresh, agg_values=None):
	'''Summarize UMD Tree cover loss, gain and tree cover extent areas for a region
    (defined by a geostore id) and time period of interest
	:param geostore: a unique hash assigned to a geographic area by the geostore microservice
	:param period: time period recorded in format YYYY-MM-DD,YYYY-MM-DD
	:param aggregate_values: organize alert counts by year
	:return: a count of Tree cover loss, gain and tree cover extent extent for the area and time periods'''

	#production api url
	api_path = 'http://production-api.globalforestwatch.org/umd-loss-gain'

	get_request = (api_path + '?period=' + period + '&geostore=' + geostore + '&aggregate_values='
    + str(agg_values) + '&thresh=' + str(thresh))

	r = requests.get(get_request)

	data = r.json()

	data_pretty = json.dumps(data, indent=2)

	print data_pretty


if __name__ == "__main__":

	count_tcloss('b6b73060bed0be0ec7cd75248e12843c', '2001-01-01,2015-12-30', thresh=30)

	#view geostore on a map
	#https://production-api.globalforestwatch.org/geostore/b6b73060bed0be0ec7cd75248e12843c/view
