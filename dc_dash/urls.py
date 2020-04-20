from django.conf.urls import url
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

from . import views
#from . import bokeh_views

#from . import pred_views
from . import utily
from . import utility_eda_only
#from .pyFinTrader import utily_bonds
from . import utily_bonds

from dc_dash.views import *
#from dc_dash.bokeh_views import *
#from dc_dash.pred_views import *
from dc_dash.utily import *

from django.conf.urls import *


from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

from . import views
#from . import utily
#from dc_dash.views import *
#from dc_dash.utily import *
from django.conf.urls import *
from django.contrib.auth.decorators import login_required, permission_required


urlpatterns = [

    #for_eda_dataset_name_listView
    # FOO-SEP19___THE DC LANDING PAGE -- without LINKEDIN / TRACXN.
    # This has the link to URL === EDA>>Go! 
    #http://localhost:8000/dc/datasets_listView

    ##JIRA_ROHIT_PendingTask
    ## APR_20 == http://127.0.0.1:8000/dc/data_ListView/
    
    url(r'^datasets_listView',  
    for_eda_dataset_name_listView.as_view(), 
    #login_required(for_eda_dataset_name_listView.as_view()), ##Ends - login_required
    ## Instead use a --- LoginRequiredMixin,
    name='for_eda_dataset_name_listView'), # 
    #


    #call_eda_dataset_json_dtable
    #url(r'^eda_dataset_json_dtable/',utily.utily_class.eda_dataset_json_dtable, name='call_eda_dataset_json_dtable'), # 
    
    #url(r'^eda_action/(?P<dataset_name>[a-zA-Z0-9-]+)/$', views.eda_landing_view, name='call_eda_landing_view'), # 
    ### Above URL basic pattern is OK for == http://localhost:8000/dashboard/eda_index/Name1/
    url(r'^eda_action/(?P<unq_id_nameField>.*)/$', views.eda_landing_view, name='call_eda_landing_view'), # 
    ## template == dc_dash/eda_landing_index.html
    ### here ABOVE == call_eda_landing_view , is the REVERSE URL Given in MODELS.py 
    ### Above URL -- Now is a REGEX Catch_All == http://localhost:8000/dashboard/eda_index/csv_UnqFldName1 ## OK Now 


    #-- pvBonds -- URL-1 == pvBonds_csvToPsql 
    url(r'^pvBonds_csvToPsql/',utily_bonds.utily_bondsClass.pvBonds_csvToPsql, name='call_pvBonds_csvToPsql'),
    
    #-- pvBonds -- URL-2
    #### Need to be Redirected here from the CSV upload Form Submit button === dc_dash/pyFindTrader_templates/pvBondsLanding_index.html
    ### OR ---- /dc_dash/pyFindTrader_templates/pvBonds_initLanding_index_bonds_go.html
    url(r'^pvbonds_initLandingListView/',utily_bonds.utily_bondsClass.pvbonds_initLandingListView, name='call_pvbonds_initLandingListView'), # earlier == call_pvbonds_landing_view

    #-- pvBonds -- URL-3
    ### JIRA_ROHIT_PendingTask this below is 2nd_PAGE for pvBonds dataFrame uploaded from CSV to PSQL --- it has the pvBonds_unq_id_nameField in its URL 
    #def get_absolute_url(self):
    # return reverse("call_pvbonds_landing_view",kwargs ={"pvBonds_unq_id_nameField" : self.pvBonds_unq_id_nameField})   ### JIRA_ROHIT_PendingTask Main TBD  
    url(r'^pvbonds_action/(?P<pvBonds_unq_id_nameField>.*)/$',utily_bonds.utily_bondsClass.pvBonds_listView, name='call_pvbonds_landing_view'), # 

    #-- pvBonds -- URL-4
    #class for_pvBonds_dataset_name_listView(ListView):
    url(r'^for_pvBonds_dataset_name_listView/',utily_bonds.for_pvBonds_dataset_name_listView.as_view(), name='for_pvBonds_dataset_name_listView'), # earlier == call_pvbonds_landing_view

    #
    #pvBonds_landing_init_dataTable
    url(r'^pvBonds_landing_init_dataTable/',utily_bonds.utily_bondsClass.pvBonds_landing_init_dataTable, name='call_pvBonds_landing_init_dataTable'), # 

    #view_pvBondsLanding_index
    url(r'^view_pvBondsLanding_index/',utily_bonds.utily_bondsClass.view_pvBondsLanding_index, name='call_view_pvBondsLanding_index'), # 
    ##colClick_indx_fromJs    
    url(r'^colClick_indx_fromJs/',utily_bonds.colClick_indx_fromJs, name='colClick_indx_fromJs'), # 



    #iFrame_pvBonds_view
    url(r'^iFrame_pvBonds_view/',utily_bonds.utily_bondsClass.iFrame_pvBonds_view, name='call_iFrame_pvBonds_view'),
    #view_pvBonds_csvUploadiFrame
    url(r'^view_pvBonds_csvUploadiFrame/',utily_bonds.utily_bondsClass.view_pvBonds_csvUploadiFrame, name='call_view_pvBonds_csvUploadiFrame'),
    #call_pvBonds_renderPage
    url(r'^pvBonds_renderPage/',utily_bonds.utily_bondsClass.view_pvBonds_renderPage, name='call_pvBonds_renderPage'),
    #js_toPy_params_pvBonds
    url(r'^js_toPy_params_pvBonds/',utily_bonds.js_toPy_params_pvBonds, name='js_toPy_params_pvBonds'),
    #py_toJS_DF_pvBonds
    url(r'^py_toJS_DF_pvBonds/',utily_bonds.py_toJS_DF_pvBonds, name='py_toJS_DF_pvBonds'),

    


    # #FOO##TEST == /templates/dc_dash/includes/modalSimpleTest.html
    # url(r'^modalSimpleTest/',utily.utily_class.modalSimpleTest, name='modalSimpleTest'),

    #eda_ExtractEmailParts
    #url(r'^eda_ExtractEmailParts/',utility_eda_only.utility_eda_only_class.eda_ExtractEmailParts, name='call_eda_ExtractEmailParts'), # 
    #extractEmailPart_outPut
    url(r'^extractEmailPart_outPut/',utily.utily_class.extractEmailPart_outPut, name='call_extractEmailPart_outPut'),
    #renderPage_extractEmailPart
    url(r'^renderPage_extractEmailPart/',utily.utily_class.renderPage_extractEmailPart, name='call_renderPage_extractEmailPart'),
    #

    #eda_MatchSimilarText_renderPage
    url(r'^eda_ColActions_MatchSimilarText_outPut/',utily.utily_class.eda_MatchSimilarText_renderPage, name='call_eda_MatchSimilarText_renderPage'),
    

    #iFrame_EdaColActions_view
    url(r'^iFrame_EdaColActions_view/',utily.utily_class.iFrame_EdaColActions_view, name='call_EdaColActions_view'),

    #modal_psql_CentOS
    url(r'^modal_psql_CentOS/',utily.utily_class.modal_psql_CentOS, name='call_modal_psql_CentOS'), 
   
    ### JIRA_ROHIT_PendingTask_test === tableAu_reportsDimensions
    url(r'^tableAu_reportsDimensions/',utily.utily_class.tableAu_reportsDimensions, name='call_tableAu_reportsDimensions'), 

    ### JIRA_ROHIT_PendingTask--Test -- nonModal_TableAuReports
    url(r'^nonModal_TableAuReports/',utily.utily_class.nonModal_TableAuReports, name='call_nonModal_TableAuReports'), 
    
    # 

    #drop_table_psql_view
    url(r'^sql_action/(?P<unq_id_nameField>.*)/$', views.drop_table_psql_view, name='call_drop_table_psql_view'), # 
    ### here ABOVE == call_eda_landing_view , is the REVERSE URL Given in MODELS.py 

    #eda_initList_display
    url(r'^eda_initList_display/',utily.utily_class.eda_initList_display, name='call_eda_initList_display'), # 

    #eda_landing_init_dataTable
    url(r'^eda_landing_init_dataTable/',utily.utily_class.eda_landing_init_dataTable, name='call_eda_landing_init_dataTable'), # 
    

    # modal_data_summary_stats
    url(r'^modal_data_summary_stats/',utily.utily_class.modal_data_summary_stats, name='call_modal_data_summary_stats'), # 

    #summaryStats_getColVal
    url(r'^summaryStats_getColVal/',utily.utily_class.summaryStats_getColVal, name='summaryStats_getColVal'), # 

    #tableName_from_js1  
    #url(r'^tableName_from_js1/',utily.utily_class.tableName_from_js1, name='tableName_from_js1'), # 
    
    #psql_tableNames_from_py   
    url(r'^psql_tableNames_from_py/',utily.utily_class.psql_tableNames_from_py, name='psql_tableNames_from_py'), # 

    #cell_getJSVal1 
    #url(r'^cell_getJSVal1/',utily.utily_class.psql_tableNames_from_js_for_merge, name='cell_getJSVal1'), # 
    url(r'^cell_getJSVal1/',utily.utily_class.psql_tableNames_js_to_py, name='cell_getJSVal1'), # 
    #
    #CodeMirror
    #view_pyTo_codeMirror
    url(r'^url_pyTo_codeMirror/',utily.utily_class.view_pyTo_codeMirror, name='call_pyTo_codeMirror'), # 
    ##CodeMirror    
    url(r'^url_codeMirror_toPy/',utily.utily_class.view_codeMirror_toPy, name='url_codeMirror_toPy'), # 
    #
    #autocomplete   
    url(r'^autocomplete/',utily.utily_class.autocomplete, name='autocomplete'), # 
    #reports_codeMirror
    url(r'^reports_codeMirror/',utily.utily_class.reports_codeMirror, name='call_reports_codeMirror'), # 



    #render_merged_table_htmlPage ---JIRA_ROHIT_PendingTask-- This called by the REDIRECT from JavaScript == window.location = forMergeRedirectURL;
    url(r'^call_merged_table_view/',utily.utily_class.render_merged_table_htmlPage, name='call_merged_table_view'), # 
    
    url(r'^holoviews_bar_small/',utily.utily_class.holoviews_bar_small_view, name='call_holoviews_bar_small'), # 
    url(r'^dc_holoviews_violinPlot_small/',utily.utily_class.dc_holoviews_violinPlot_small, name='call_dc_holoviews_violinPlot_small'), # 
    url(r'^modal_psqlDB_Conn_Status/',utily.utily_class.modal_psqlDB_Conn_Status, name='call_modal_psqlDB_Conn_Status'), # 
    #
    url(r'^bokeh_boxplot/',utily.utily_class.dc_bokeh_BoxPlot_view, name='call_bokeh_boxplot'), # 
    #
    #url(r'^holoviews_plot1/',utily.utily_class.dc_holoviews_plotview, name='call_holoviews_plot1'), 
    # 
    #test_CodeMirror
    url(r'^test_CodeMirror/',utility_eda_only.utility_eda_only_class.test_CodeMirror, name='call_test_CodeMirror'), # 

    #send_dfToJSON_forBokeh
    url(r'^send_dfToJSON_forBokeh/',utily.utily_class.send_dfToJSON_forBokeh, name='call_send_dfToJSON_forBokeh'), # 
    
  
    #dc_holoviews_violinPlot_large
    url(r'^dc_holoviews_violinPlot_large/',utily.utily_class.dc_holoviews_violinPlot_large, name='call_dc_holoviews_violinPlot_large'), # 


    #url(r'^bokeh_boxplot_small/',utily.utily_class.dc_bokeh_BoxPlot_viewSmall, name='call_bokeh_boxplot_small'), # 
    #bokeh_boxplot_clicks_from_js
    #
    url(r'^bokeh_boxplot_clicks_from_js/',utily.utily_class.bokeh_boxplot_clicks_from_js, name='bokeh_boxplot_clicks_from_js'), # 
    #

    #dc_bokeh_scatterPlot_view
    url(r'^dc_bokeh_scatterPlot_view/',utily.utily_class.dc_bokeh_scatterPlot_view, name='call_dc_bokeh_scatterPlot_view'), # 

    #showCategoricalCols_view
    url(r'^showCategoricalCols_view/',utility_eda_only.utility_eda_only_class.showCategoricalCols_view, name='showCategoricalCols_view'), # 
    #


    #MIGHT NOT BE REQUIRED --- CHECK 
    #cell_getJSVal2 == FOO
    #url(r'^cell_getJSVal2/',utily.utily_class.psql_tableNames_from_js_for_merge1, name='cell_getJSVal2'), # 
    #
    #


    #drop_delete_click_from_js
    url(r'^drop_delete_click_from_js/',utily.utily_class.drop_delete_click_from_js, name='drop_delete_click_from_js'), # 

    #cell_get_js_val_drop_psql
    url(r'^cell_get_js_val_drop_psql/',utily.utily_class.psql_tableNames_from_js_for_drop, name='cell_get_js_val_drop_psql'), # 

    #col_get_js_val_bokeh
    url(r'^col_get_js_val_bokeh/',utility_eda_only.utility_eda_only_class.get_userInput_BokehBoxPlot, name='col_get_js_val_bokeh'), # 



    #psql_click_from_js
    url(r'^psql_click_from_js/',utily.utily_class.psql_click_from_js, name='psql_click_from_js'), # 

    #eda_get_value_from_js    
    url(r'^eda_get_value_from_js/',utily.utily_class.eda_get_value_from_js, name='eda_get_value_from_js'), # 

    #eda_createDuplicate_Col    
    url(r'^eda_createDuplicate_Col/',utily.utily_class.eda_createDuplicate_Col, name='call_eda_createDuplicate_Col'), # 
    












    
    ### call_eda_SearchAndReplace_formSave
    url(r'^eda_actionSearchAndReplace_/',utily.utily_class.eda_SearchAndReplace_formSave, name='call_eda_SearchAndReplace_formSave'), # 
    
    #call_eda_df_to_dataTable --- Changed to == eda_SearchAndReplace_outPut
    url(r'^eda_actionSearchAndReplace/',utily.utily_class.eda_SearchAndReplace_outPut, name='eda_SearchAndReplace_outPut'), # 
    ### Testing_21MAY19 == RAW_JSON --- Seen at the above URL == eda_actionSearchAndReplace





















    #eda_actionMatchSimilarText_
    url(r'^eda_actionMatchSimilarText_/',utily.utily_class.eda_MatchSimilarText_formSave, name='call_eda_MatchSimilarText_formSave'), # 
    #eda_MatchSimilarText_outPut
    url(r'^eda_actionMatchSimilarText/',utily.utily_class.eda_MatchSimilarText_outPut, name='eda_MatchSimilarText_outPut'), # 
    #

    url(r'^json_dataTable/',utily.utily_class.SqlDb_to_json, name='call_json_for_dt'), # 
    #json_to_dataTable
    url(r'^json_to_dataTable/',utily.utily_class.json_to_dataTable, name='call_json_to_dataTable'), # 
    #csv_to_psql
    url(r'^csv_to_psql/',utily.utily_class.csv_to_psql, name='call_csv_to_psql'), # 
    url(r'^json_to_dtable_csv_to_psql/',utily.utily_class.json_to_dtable_csv_to_psql, name='call_json_to_dtable_csv_to_psql'), # 
    #
    url(r'^test_loader/', views.test_loader, name='call_test_loader'), # 
    #
    # df_afterMerge_toAjax === gets the DF >> JSON to DataTable for MERGE 
    url(r'^json_df_afterMerge_toAjax/',utily.utily_class.df_afterMerge_toAjax, name='json_df_afterMerge_toAjax'), 
    # 

    # This URL hits VIEWs.py FUNC created same as == for_eda_dataset_name_listView ---
    # The View Func RENAMED as ==  call_eda_dataset_name_listView - to fit INTO -- eda_Sidebar.html
    # JIRA_ROHIT_PendingTask --- this was PROBBALY done --- as when we reach eda_sidebar.html - we may again want to call == for_eda_dataset_name_listView
    # JIRA_ROHIT_PendingTask --- Check this and document carefully 
    url(r'^call_datasets_listView',  call_eda_dataset_name_listView.as_view(), name='call_eda_dataset_name_listView'), # 
    #


    
    # This below was LANDING PAGE == LINKEDIN and TRACXN.
    #data_ListView === ALL OK === Checked for DataTables.js -- Alternate ROW ORANGE / PINK ERROR in MODALS 
    #http://localhost:8000/dc/data_ListView
    #for_eda_dataset_name_listView.as_view()
    url(r'^data_ListView/', for_eda_dataset_name_listView.as_view() , name='data_ListView'), #.as_view() -as its a -CLASS BASED VIEW -ListView 
    #url(r'^data_ListView/', data_ListView.as_view() , name='data_ListView'), #.as_view() -as its a -CLASS BASED VIEW -ListView 
    #


    #data_ListView_index
    # Not being used -- was used for TRACXN ??
    url(r'^$',  data_ListView_index.as_view(), name='data_ListView_index'),  #
    # 
    url(r'^data_ListView1/', data_ListView_scrapTracxn_view.as_view() , name='data_ListView_scrapTracxn_view'), #.as_view() -as its a -CLASS BASED VIEW -ListView 
    #initSearchTracxn_view ## data_ListView_initSearch
    #initSearchTerms_ListView
    #url(r'^initSearchTerms/', initSearchTerms_ListView.as_view() , name='initSearchTerms_ListView'), #.as_view() -as its a -CLASS BASED VIEW -ListView 
    url(r'^form_view/', views.form_view , name='call_form_view'),
    #eda_dc_jan19
    url(r'^ea_dc_api/', views.eda_dc_jan19 , name='call_eda_dc_jan19'),

    url(r'^initSearchTerms/', views.initSearchTerms_ListView , name='initSearchTerms_ListView'),
    #url(r'^init_PortalSearchTerms/', views.initSearch_LinkedIn_view , name='initSearch_LinkedIn_view'),
    #init_scrap_linkedin
    url(r'^tgt_PortalSearchTerms/', utily.utily_class.scrapLnkd_view, name='call_scrapLnkd_view'),
    #
    # url(r'^initSearch/', utily.utily_class.initSearchTracxn_view , name='initSearch_view'),
    #scrapTracxn_view
    url(r'^initScrape/', utily.utily_class.scrapTracxn_view , name='initScrape_view'),
    #deduplicate_data_view
    url(r'^url_deduplicate_data_view/', views.deduplicate_data_view , name='call_deduplicate_data_view'), 
    #TREE-d3Js - view_d3jsTree
    url(r'^url_view_d3jsTree/', views.view_d3jsTree , name='call_view_d3jsTree'), 
    # API JSON Urls for D3Charts
    #url(r'^api/count_a', views.count_a, name='count_a'),
    #url(r'^api/json_for_d3js', views.json_for_d3js, name='json_for_d3js'),
    # Upload CSV Page --1 FEB19 --- Testing 
    #upload_csv_page
    url(r'^upload_csv_page/$', views.upload_csv_page, name='upload_csv_page'),      ## 
    #
    





    #JIRA_ROHIT_PendingTask--Above Class Based Views- VIEWNAME.as_view()  --- defined in the Views.py 

    #url(r'^data_from_model/$', utily.utily_class.all_DataListView, name='data_from_model'), # data_from_model
    #url(r'^data_from_model/$', utily.utily_class.records_from_modFields, name='records_from_modFields'), # data_from_model
    
    #url(r'^$', views.index, name='index'), # Index.html includes - base1.html and NOT base.html as it has NAVBAR in it 
    #url(r'^crawl_clear/$', views.hot_crawl_view, name='crawl_clear'), # Uncomment to get Hotels data into DB by CRAWL
    
    ##### Digital Cognition --------------------
    ### Bokeh --- https://github.com/bokeh/bokeh/tree/0.12.2
    #vbar_chart_bokeh
    #url(r'^bokeh_vbar/$', bokeh_views.vbar_chart_bokeh, name='vbar_chart_bokeh'), ## vbar_chart_bokeh
    
    #url(r'^bokeh_vbar/$', bokeh_views.charts_bokeh, name='charts_bokeh'), ## vbar_chart_bokeh
    #
    #url(r'^bokeh_multi_axis/$', bokeh_views.bokeh_multi_axis, name='bokeh_multi_axis'), ## 
    #
    #url(r'^bokeh_pivot_table/$', bokeh_views.bokeh_pivot_table, name='bokeh_pivot_table'), ## 
    #
    
    #JIRA_ROHIT_PendingTask CHECK --- url(r'^pred_1/$', pred_views.pred_anal, name='pred_anal'), ## 
    #
    #Bokeh_1 --- ### Not Ok -- 22 Jan 18 --- probably needs New Bokeh 
    #url(r'^bokeh_1/$', views.bokeh_1, name='bokeh_1'), ## Bokeh_1    
    #time_series --- ### Not Ok -- 22 Jan 18 --- probably needs New Bokeh 
    #url(r'^time_series/$', views.time_series, name='time_series'), ## time_series
    #boxplot_view --- ### Not Ok -- 22 Jan 18 --- probably needs New Bokeh    
    #url(r'^boxplot/$', views.boxplot_view, name='boxplot_view'), ## boxplot_view
    #scatter_plot
    #url(r'^scatter_plot/$', views.scatter_plot, name='scatter_plot'), ## scatter_plot
    #bokeh_area_chart
    #url(r'^bokeh_area_chart/$', views.bokeh_area_chart, name='bokeh_area_chart'), ## bokeh_area_chart
    #
    
    ### HTML Table Display 
    #
    
    # Rename Field - testing 
    
    url(r'^pred_df_1/$', views.pred_df_1, name='pred_df_1'),     ## pred_df_1 - Testing
    # url(r'^index_1/$', views.index_1, name='index_1'),       ## Step-1- Landing page with Links 
    
    
    
    
    
    
    
    ##### Old Dummy URL's 
    #
    #
    #url(r'^uploads/home/$', views.home, name='home'), 
    #url(r'^uploads/simple/$', views.simple_upload, name='simple_upload'),  
    #url(r'^uploads/form/$', views.model_form_upload, name='model_form_upload'), 
    #url(r'^index_1/$', views.list_csv, name='list_csv'),      ## Step-1- Landing page with Links 
    #url(r'^selected/$', views.selected, name='selected'),     ## Step-1- Shows All File Objects from the MODEL Document
    #url(r'^calc_1/$', views.computation, name='computation'), ## Step-1- Computation
    #url(r'^visualisation/$', views.visualisation, name='visualisation'), ## Step-1- Computation
    #url(r'^graph/$', views.graph, name='graph'), ## Step-1- graph
    #url(r'^learning/$', views.learning, name='learning'), ## Step-1- Computation
    

    
    url(r'^chart_1/$', utily.utily_class.chart_1, name='chart_1'),   ## Step-3- Chart_1 
    url(r'^summary_stats_index/$', utily.utily_class.summary_stats_index, name='summary_stats_index'),#Sumry_stats_index
    url(r'^data_del_index/$', utily.utily_class.data_del_index, name='data_del_index'),  ## data_del_index
    url(r'^data_del_1/$', views.data_del_1, name='data_del_1'),      
    url(r'^data_del_2/$', views.data_del_2, name='data_del_2'),      
    url(r'^data_del_3/$', views.data_del_3, name='data_del_3'),      
    url(r'^data_del_4/$', views.data_del_4, name='data_del_4'),      
    
    
    
    
    #summary_stats_1 --- In these --- utily.utily_class. ---- we have BYPASSED the views.py file ...

    url(r'^summary_stats_1/$', utily.utily_class.summary_stats_1, name='summary_stats_1'), ## summary_stats_1 --- Model ==1
    url(r'^summary_stats_2/$', utily.utily_class.summary_stats_2, name='summary_stats_2'), ## summary_stats_2 --- Model ==2
    url(r'^summary_stats_3/$', utily.utily_class.summary_stats_3, name='summary_stats_3'), ## summary_stats_3 --- Model ==3
    url(r'^summary_stats_4/$', utily.utily_class.summary_stats_4, name='summary_stats_4'), ## summary_stats_3 --- Model ==4
    url(r'^summary_stats_5/$', utily.utily_class.summary_stats_5, name='summary_stats_5'), ## summary_stats_3 --- Model ==5
    
    
    
    
    
    #url(r'^data_create_model4/$', views.data_create_model4, name='data_create_model4'), #Step-5-Create Table- again 
    
    #url(r'^calc_a/$', views.calc_a, name='calc_a'), ## Ok Uncomment
    #url(r'^calc_b/$', views.calc_b, name='calc_b'), ## TBD
    #url(r'^calc_c/$', views.calc_c, name='calc_c'), ## Ok Uncomment
    #url(r'^calc_c/$', views.calc_d, name='calc_d'),  ## TBD
    #url(r'^dash/$', views.dash_1, name='dash_1'),
    

    #url(r'^login/', views.dcdash_login, name='call_dvcad_loginIndex'), ## no DOLLAR after / 
    #url(r'^index/', views.dcdash_landing, name='call_dvcad_landing'), ## JIRA_ROHIT_PendingTask FAILS == decorators=['django.contrib.auth.decorators.login_required'] 
    

    ## Test == get_siteID
    #url(r'^get_siteID/$', views.get_siteID, name='call_get_siteID'), 
    #url(r'^eda_dataset_json_dtable/',utily.utily_class.eda_dataset_json_dtable, name='call_eda_dataset_json_dtable'), # 
    
    #url(r'^eda_action/(?P<dataset_name>[a-zA-Z0-9-]+)/$', views.eda_landing_view, name='call_eda_landing_view'), # 
    ### Above URL basic pattern is OK for == http://localhost:8000/dashboard/eda_index/Name1/
    #url(r'^eda_action/(?P<unq_id_nameField>.*)/$', views.eda_landing_view, name='call_eda_landing_view'), # 
    ## template == dc_dash/eda_landing_index.html
    #url(r'^snapdeal/', SNAP_P_LVIEW.as_view() , name='snapdeal'), #JIRA_ROHIT_PendingTask-- Class Based Views- VIEWNAME.as_view() 
    #url(r'^snap_prod/$', Prod_DetailView.as_view() , name='snap_prod'), #JIRA_ROHIT_PendingTask-- Class Based Views- VIEWNAME.as_view() 

]
