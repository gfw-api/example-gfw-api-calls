import requests
import json

def count_glad_alerts(geostore, period, gladConfirmOnly=False, agg_values=False, agg_by=False):
	'''Count Glad Alerts for an area (defined by geostore) and time period of interest
	:param geostore: a unique hash assigned to a geographic area by the geostore microservice
	:param period: time period recorded in format YYYY-MM-DD,YYYY-MM-DD
	:param gladConfirmOnly: boolean to filter alerts by confirmed only
	:param aggregate_values: organize alert counts by time interval (defaults to julian day)
	:param aggregate_by: specify the time interval to organize alert counts by (day, week, month, quarter, year)
	:return: a count of Glad Alerts for the area and time period, as well as download links'''

	#production api url
	api_path = 'http://production-api.globalforestwatch.org/glad-alerts'

	get_request = (api_path + '?period=' + period + '&geostore=' + geostore + '&gladConfirmOnly='
	+ str(gladConfirmOnly) + '&aggregate_values=' + str(agg_values) + '&aggregate_by=' + str(agg_by))

	r = requests.get(get_request)

	data = r.json()

	data_pretty = json.dumps(data, indent=2)

	print data_pretty


if __name__ == "__main__":

	count_glad_alerts('b6b73060bed0be0ec7cd75248e12843c', '2015-01-01,2017-07-30')

	#view geostore on a map
	#https://production-api.globalforestwatch.org/geostore/b6b73060bed0be0ec7cd75248e12843c/view
