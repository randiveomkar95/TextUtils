'''
(c) learning 2020

Purpose : Learning one to many relation
Ideas : https://dev.to/coderasha/how-to-export-import-data-django-package-series-3-39mk
'''
import csv
from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse

from ..models import Status, Detail

def export_csv(request):
	'''
	Dump model data in a csv file
	'''
	now = datetime.now()
	date = str(now.year)+'-'+str(now.month)+'-'+str(now.day)
	response = HttpResponse(content_type='text/csv')
	response['Content-Disposition'] = 'attachment;filename="Report_{}.csv"'.format(str(date))
	writer = csv.writer(response)
	writer.writerow(['ID', 'Name', 'Type', 'Pencentage','started_time','status'])

	status_fields = [field.name for field in Status._meta.concrete_fields]
	detail_fields = ['detail__{}'.format(field.name) for field in Detail._meta.concrete_fields]
	all_fields = ['id', 'detail__name', 'detail__type', 'detail__percentage','started_time', 'status']
	training_report_list = list(Status.objects.values_list(*all_fields))

	for report in training_report_list:
		writer.writerow(report)
	return response
