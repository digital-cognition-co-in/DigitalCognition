# -*- coding: utf-8 -*-

from django import forms
from django.forms.widgets import RadioSelect
from django.forms.widgets import *
from .models import *

	
class form_csvUp_pvBonds_csvToPsql(forms.ModelForm):
	"""
	JIRA_ROHIT_PendingTask --- get rid of this Form - upload files directly into mySQL pSql bypass Django 
	"""
	class Meta:
		print("------FORMS.py HIT --pvbonds_csv_document-------------------")
		model = pvbonds_csv_document
		fields = ('pvBonds_csv_file','pvBonds_csv_file_name','pvBonds_dataset_name', ) #
   

class eda_form(forms.ModelForm):
	class Meta:
		model = eda_inputs_search_and_replace
		#fields = ('dataset_name','form_input_new_column','django_form_input_operation_type','column_name','str_search','str_replace',)
		fields = ('form_input_new_column','django_form_input_operation_type','str_search','str_replace',)

class eda_MatchSimilarText_form(forms.ModelForm):
	class Meta:
		model = eda_inputs_MatchSimilarText
		fields = ('fuzziness','str_to_compare_with',)

class eda_ceil_floor_form(forms.ModelForm):
	class Meta:
		model = temp_ceil_floor_params
		fields = ('single_col','col_index','ceil_mode',)

class sql_query_form(forms.ModelForm):
	class Meta:
		model = SqlQueryStr
		fields = ('table_name','limit_records','new_table_name','sql_query_input',)





"""
Both FORMS Below -- Loading Data Into SAME Model . 
"""

class form_csv_up_csv_to_psql(forms.ModelForm):
	class Meta:
		model = csv_document
		fields = ('csv_file_name','csv_file','dataset_name', ) #
		# csv_file_name = forms.CharField(max_length=1000 , required=False)
		# csv_file = forms.FileField()

class form_csv_up(forms.ModelForm):
	class Meta:
		model = csv_document
		fields = ('csv_file_name','csv_file','dataset_name', ) #
		# csv_file_name = forms.CharField(max_length=1000 , required=False)
		# csv_file = forms.FileField()

