# -*- coding: utf-8 -*-

from django import forms
from django.forms.widgets import RadioSelect
from django.forms.widgets import *
from .models import *


#pyFinTrader
"""
JIRA_ROHIT_PendingTask --- get rid of this Form - upload files directly into mySQL pSql bypass Django 
"""
	
class form_csvUp_pvBonds_csvToPsql(forms.ModelForm):
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


class sql_query_form(forms.ModelForm):
	class Meta:
		model = SqlQueryStr
		fields = ('table_name','limit_records','new_table_name','sql_query_input',)
		#print("FORMS.py HIT -----------sql_query_form--------------")


class initSearchTracxn(forms.Form):
	initSearchStrTracxn = forms.CharField(max_length=1000)
	#name="initSearchStrTracxn" value = "{{initStrTracxn}}" type="text" placeholder="Initial Search.."  
	
class initSearch_Portal_form(forms.Form):
	#print("FORMS.py HIT -------------------------")
	Designation = forms.CharField(max_length=1000 , required=False)
	Organization_Name = forms.CharField(max_length=1000 , required=False)
	Geo_City = forms.CharField(max_length=1000 , required=False)
	Geo_Country = forms.CharField(max_length=1000 , required=False)
	college = forms.CharField(max_length=1000 , required=False)
	university = forms.CharField(max_length=1000 , required=False)


"""
Both FORMS Below -- Loading Data Into SAME Model . 
"""

class form_csv_up_csv_to_psql(forms.ModelForm):
	class Meta:
		model = csv_document
		#print("---------AAA--------FORMS.py HIT ---form_csv_up_csv_to_psql--------------------")
		fields = ('csv_file_name','csv_file','dataset_name', ) #
		# csv_file_name = forms.CharField(max_length=1000 , required=False)
		# csv_file = forms.FileField()

class form_csv_up(forms.ModelForm):
	class Meta:
		model = csv_document
		#print("---------AAA--------FORMS.py HIT ---form_csv_upload----------------------")
		fields = ('csv_file_name','csv_file','dataset_name', ) #
		# csv_file_name = forms.CharField(max_length=1000 , required=False)
		# csv_file = forms.FileField()



# class DocumentForm(forms.ModelForm):
# 	class Meta:
# 		#print("CSV FORM HIT in Forms .py --------------------------")
# 		model = csv_document
# 		fields = ('description', 'csvfile', ) #
    
class Form_1(forms.Form):
    user_input_1 = forms.CharField(max_length=1000)
    user_input_2 = forms.CharField(max_length=1000)
#    user_input_1s = forms.CharField(max_length=1000)
#    user_input_2s = forms.CharField(max_length=1000)
    
    # selected_choice = forms.CharField(max_length=100)

    # def __unicode__(self):
    #     return self.your_product
    
    
class Form_2(forms.Form):
    user_input_1s = forms.CharField(max_length=1000)
    user_input_2s = forms.CharField(max_length=1000)
    
    
# TBD ---- for CheckBox Form in Summary_Stats.html page 
#

Alt_Choices = [
    ('1','Yes'),
    ('2','No')
]

DISPLAY_CHOICES = (
    ("locationbox", "Display Location"),
    ("displaybox", "Display Direction")
)

class MyForm(forms.Form):
    display_type = forms.ChoiceField(required=True,widget=forms.RadioSelect, choices=DISPLAY_CHOICES,initial = '1')  
    
    

    
    
    
""" 
## Original InfoBot - PyAddicts Code 
#

class SelectForm(forms.Form):
	vertical_choices = (("1", "ONE"),("2", "TWO"),("3","Three"),("4","Four"),("5","Five") )
	selected_choice = forms.MultipleChoiceField(required=True, widget=forms.CheckboxSelectMultiple,)


# 	from django import forms

# class NameForm(forms.Form):
#     your_product = forms.CharField(max_length=1000)
#     # selected_choice = forms.CharField(max_length=100)

#     # def __unicode__(self):
#     #     return self.your_product
# class SelectForm(forms.Form):
# 	vertical_choices = (("1", "ONE"),("2", "TWO"),("3","Three"),("4","Four"),("5","Five") )
# 	selected_choice= forms.MultipleChoiceField(required=False, widget=forms.CheckboxSelectMultiple)


from django import forms

from django.forms.models import modelformset_factory


from .models import Variation, Category


CAT_CHOICES = (
	('electronics', 'Electronics'),
	('accessories', 'Accessories'),
)

class ProductFilterForm(forms.Form):
	q = forms.CharField(label='Search', required=False)
	category_id = forms.ModelMultipleChoiceField(
		label='Category',
		queryset=Category.objects.all(), 
		widget=forms.CheckboxSelectMultiple, 
		required=False)
	# category_title = forms.ChoiceField(
	# 	label='Category',
	# 	choices=CAT_CHOICES, 
	# 	widget=forms.CheckboxSelectMultiple, 
	# 	required=False)
	max_price = forms.DecimalField(decimal_places=2, max_digits=12, required=False)
	min_price = forms.DecimalField(decimal_places=2, max_digits=12, required=False)



class VariationInventoryForm(forms.ModelForm):
	class Meta:
		model = Variation
		fields = [
			"price",
			#"sale_price",
			#"inventory",
			"active",
		]


VariationInventoryFormSet = modelformset_factory(Variation, form=VariationInventoryForm, extra=0)
"""    