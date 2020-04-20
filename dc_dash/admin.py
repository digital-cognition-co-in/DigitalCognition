from django.contrib import admin

from .models import *

#pyFinTrader
#Sessions Django internal Model 
# NOT OK --- Shows ADMIN hash etc in plain text ==
#https://stackoverflow.com/questions/48466293/admin-class-not-defined-in-django
#https://stackoverflow.com/questions/4976015/django-how-to-see-session-data-in-the-admin-interface/23276672#23276672

from django.contrib.sessions.models import Session
class SessionAdmin(admin.ModelAdmin):
    def _session_data(self, obj):
        return obj.get_decoded()
    list_display = ['session_key', '_session_data', 'expire_date']
admin.site.register(Session, SessionAdmin)
#pvBonds--#pyFinTrader
admin.site.register(pvbonds_csv_document)

# EDA_Temp_Data_Sets
admin.site.register(temp_tableName_forMerge)
admin.site.register(temp_dataSetName_for_EDALanding)
admin.site.register(temp_colIndex_for_Eda)
admin.site.register(temp_dataSetName_dfFromEDA)
#
admin.site.register(eda_inputs_search_and_replace)


#eda_inputs_MatchSimilarText
admin.site.register(eda_inputs_MatchSimilarText)

admin.site.register(SqlQueryStr)
admin.site.register(news_startup_1)
admin.site.register(model_SearchTracxn)
admin.site.register(model_ScrapeTracxn)
admin.site.register(model_init_lnkd)
admin.site.register(model_scrape_lnkd)
admin.site.register(csv_document)




#

