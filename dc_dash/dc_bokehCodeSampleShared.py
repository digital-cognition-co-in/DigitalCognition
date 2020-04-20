def dc_bokeh_BoxPlot_view(request):
        """
        This method defined in - dc_dash/utily.py
        ##bokeh_tukey_summary_boxplot 
        """
        #
        bokeh_class_obj = bokeh_class() #
        js_bokeh,div_bokeh,cdn_js,cdn_css = bokeh_class_obj.bokeh_tukey_summary_boxplot_large()#
        #
        context = {"graphname": "tukey_boxPlot",
                "div_bokeh": div_bokeh,
                "js_bokeh": js_bokeh,
                "cdn_js": cdn_js,
                "cdn_css": cdn_css,
                    }
        return render(request,'dc_dash/includes/Charts_and_Plots/dc_bokeh_tukey_boxplot_apr19.html',context) #
        # This PAGE = dc_bokeh_tukey_boxplot_apr19 ...as iFRAME in the eda_SideBar MODAL . 
    

def bokeh_tukey_summary_boxplot_large(self):
    """
    #This method defined in = dc_bokeh_plots.py 
    """

        from bokeh.plotting import figure, show, output_file
        from bokeh.plotting import figure
        from bokeh.models import Range1d
        from bokeh.embed import components
        from bokeh.layouts import row

        df_for_bokeh = pd.read_pickle("./df_holoviewPlots.pkl")
        
        #FOO_MAIN_GUESS the CATEGORICAL COLUMN  - Count Unique values in Each Column -- See which Column is categorical / Ordinal / Continous variable etc ...
        col_names_fromPSQL =  list(df_for_bokeh)
        ls_SeriesName = []
        ls_SeriesUnqCnts = [] 
        for k in range(len(col_names_fromPSQL)):
            series_name = str(col_names_fromPSQL[k])
            ls_SeriesName.append(series_name)
            unq_values_list = df_for_bokeh[series_name].unique()
            ls_SeriesUnqCnts.append(len(unq_values_list))
        df_calcUnq = pd.DataFrame({'ls_SeriesName':ls_SeriesName,'ls_SeriesUnqCnts':ls_SeriesUnqCnts})
        min_valIndex = df_calcUnq['ls_SeriesUnqCnts'].idxmin()
        col_with_CategoricalValues = df_calcUnq.iloc[min_valIndex]['ls_SeriesName']
        unq_values_list_final = df_for_bokeh[col_with_CategoricalValues].unique()

        groups = df_for_bokeh.groupby(str(col_with_CategoricalValues))
        q1 = groups.quantile(q=0.25) # print("-------------q1-----------------",q1) #
        ## Check if better way than QUANTILE to get QUANTILES  ## Should get QUANTILES same as SUMMARY Stats -UpperQ ,LowerQ== RStats  ?? 
        q2 = groups.quantile(q=0.5)
        q3 = groups.quantile(q=0.75) #print("-------------q3-----------------",q3)
        iqr = q3 - q1
        upper = q3 + 1.5*iqr #print("------------GROUPS ---- UPPER -------------",upper)
        lower = q1 - 1.5*iqr #print("------------GROUPS ---- LOWER -------------",lower)
        
        col_names_fromPSQL = list(df_for_bokeh) #
        ls_SeriesName = []
        ls_SeriesUnqCnts = [] 
        for k in range(len(col_names_fromPSQL)):
            series_name = str(col_names_fromPSQL[k])
            ls_SeriesName.append(series_name)
            unq_values_list = df_for_bokeh[series_name].unique() #print("---unq_values_list----",unq_values_list)
            ls_SeriesUnqCnts.append(len(unq_values_list))
        df_calcUnq = pd.DataFrame({'ls_SeriesName':ls_SeriesName,'ls_SeriesUnqCnts':ls_SeriesUnqCnts}) #print(df_calcUnq)
        min_valIndex = df_calcUnq['ls_SeriesUnqCnts'].idxmin()  ## this -- min_valIndex --- is INDEX of SERIES with LEAST NUMBER of UNIQUE VALUES 
        col_with_CategoricalValues = df_calcUnq.iloc[min_valIndex]['ls_SeriesName']         #print(col_with_CategoricalValues)

        unq_values_list_final = df_for_bokeh[col_with_CategoricalValues].unique()
        #print("-------unq_values_list_final-------------",unq_values_list_final)
        # GET other 2 Column Names / Column Labels // Series Names --- which are NOT Categorical Variables
        list_of_other_Cols = []
        for k in range(len(col_names_fromPSQL)):
            if str(col_names_fromPSQL[k]) == col_with_CategoricalValues:
                pass
            else:
                list_of_other_Cols.append(str(col_names_fromPSQL[k]))
        
        # Get the UNIQUE Categories from SEGMENTS 
        ## col_with_CategoricalValues
        unq_segments_list = df_for_bokeh[col_with_CategoricalValues].unique() #

        # find the outliers for each category
        def outliers(group):
            #print("----------within_Function == OUTLIERS_group----------",group) 
            #print("---TYPE---within_Function == OUTLIERS_group----------",type(group))
            ## The CAT_A --- Grouped DF 

            # Get the UNIQUE Categories from SEGMENTS 
            ## col_with_CategoricalValues
            unq_segments_list = df_for_bokeh[col_with_CategoricalValues].unique() #
            values_col = list_of_other_Cols[0] #
            
            for k in range(len(unq_segments_list)): ## Getting only 2 categories --- may need a RANGE == LENgth + 1 etc .etc ..
                cat = unq_segments_list[k] #
            #     print("-----for LOOP ----group.name ==----cat________=========Within Func Outliers -------",cat)
            #     print("--------group.height > upper.loc[cat]['height']----------",group.height > upper.loc[cat][values_col])
            #     print("--------group.height < upper.loc[cat]['height']----------",group.height < upper.loc[cat][values_col])
            # #return group[(group.height > upper.loc[cat]['height']) | (group.height < lower.loc[cat]['height'])]['height']
            return group[(group[values_col] > upper.loc[cat][values_col])][values_col]
            # nuts = " "
            # return nuts
        out = groups.apply(outliers).dropna()
        #print("-------bokeh_large-----TYPE--out----------",type(out)) #OK# <class 'pandas.core.frame.DataFrame'>
        #print("-------bokeh_large-------out-----OUTLIERS from ALL Categories DataFrame---------",out) ## Can be EMPTY -- Empty DataFrame

        # prepare outlier data for plotting, we need coordinates for every outlier.
        if not out.empty:
            outx = []
            outy = []
            for keys in out.index:
                outx.append(keys[0])
                #print("-----bokeh_large----outx-----------",outx) 
                outy.append(out.loc[keys[0]].loc[keys[1]])
                #print("-----bokeh_large----outy-----------",outy) #
                # --------outx----------- ['CAT_C', 'CAT_C', 'CAT_C']
                # --------outy----------- [277.0, 355.0, 255.0]

        TOOLTIPS = """
            <div style="background-color:orange;">
                <div>
                    <span style="font-size: 15px; color: #966;">@cats</span>
                </div>
                
                <div>
                    <span style="font-size: 10px; color: black;">($y{int})</span>
                </div>
            </div>
        """                        

        # Get UNIQUE Categories --- CAT_A , CAT_B , CAT_C , from SEGMENTS 
        # The --- unq_segments_list --- defined above. 
        cats = unq_segments_list
        ## The --- list_of_other_Cols --- defined above. 
        values_col = list_of_other_Cols[0] #

        #p = figure(tools="", background_fill_color="#efefef", x_range=cats,plot_width=195, plot_height=550,tooltips=TOOLTIPS)
        ### As per Answer to Own SO Question ---- TOOLTIP not to be added at the FIGURE Level. 
        p = figure(tools="", background_fill_color="#efefef", x_range=cats,plot_width=625, plot_height=400)
        ## This -- plot_width=600, plot_height=550 --- INCLUDES the TOOLBAR on RIGHT .
        # This --  plot_height= 475 ---- If it goes above --- 475 cant see the X Scale. 
        from bokeh.models import HoverTool , WheelZoomTool , LassoSelectTool ,BoxZoomTool, ResetTool , PanTool
        b1 = p.vbar(cats, 0.7, q2[values_col], q3[values_col], fill_color="#E08E79", line_color="black")
        #print("-----------B1 ===========",b1)
        b2 = p.vbar(cats, 0.7, q1[values_col], q2[values_col], fill_color="#3B8686", line_color="black")
        #print("-----------B2 ===========",b2)
        #b3 = p.rect(cats, lower.height, 0.4, 0.15,angle=-0.7,fill_color="blue", line_color="pink") ## OK Experi with ANGLE  
        b3 = p.rect(cats, lower[values_col], 0.2, 0.01,fill_color="blue", line_color="red") ## 
        b4 = p.rect(cats, upper[values_col], 0.2, 0.01, fill_color="blue", line_color="red") ## OK Own SO 

        hover = HoverTool(tooltips = TOOLTIPS, renderers = [b1, b2, b3,b4])
        p.add_tools(hover,WheelZoomTool(),LassoSelectTool(),BoxZoomTool(), ResetTool(),PanTool())

        # if no outliers, shrink lengths of stems to be no longer than the minimums or maximums
        qmin = groups.quantile(q=0.00)
        qmax = groups.quantile(q=1.00)
        #upper.score = [min([x,y]) for (x,y) in zip(list(qmax.loc[:,'score']),upper.score)]
        
        # stems
        #[values_col]
        p.segment(cats, upper[values_col], cats, q3[values_col], line_color="black") #
        # # Ok Last Working Code --- 1400h_6MAY

        #p.segment(cats, lower.score, cats, q1.score, line_color="black")
        p.segment(cats, lower[values_col], cats, q1[values_col], line_color="black")
        # outliers
        if not out.empty:
            p.circle(outx, outy, size=6, color="#F38630", fill_alpha=0.6)
            #print("----CIRCLE --------",p.circle(outx, outy, size=6, color="#F38630", fill_alpha=0.6))
            ## Above == GlyphRenderer(id='

        p.xgrid.grid_line_color = "pink"
        p.ygrid.grid_line_color = "white"
        p.grid.grid_line_width = 2
        p.xaxis.major_label_text_font_size="12pt"

        #p.toolbar.logo = None
        #p.toolbar_location = None
        js_boxplot, div_boxplot = components(p)
        cdn_js_boxplot=CDN.js_files[0] # NOT REQD ?? 
        cdn_css_boxplot=CDN.css_files[0] # NOT REQD ?? 
        
        return js_boxplot,div_boxplot ,cdn_js_boxplot,cdn_css_boxplot
