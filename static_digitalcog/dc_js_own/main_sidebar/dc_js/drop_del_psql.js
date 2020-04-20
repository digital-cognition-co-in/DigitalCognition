document.addEventListener('DOMContentLoaded', function() { 
        //alert("===/Static_in_PRO/=====")
        var csrftoken_from_drop_del_psql = jQuery("[name=csrfmiddlewaretoken]").val();

        $("#drop_del_PSQL_Tables").hover(function () {
            var fontawesomeicon = document.getElementsByClassName("font_awesome_icon_for_hover")[0];
            fontawesomeicon.setAttribute("style", "color:  rgb(230, 180, 19); "); 
        });

        $("#drop_del_PSQL_Tables").hover(function () {
            var var_modal_drop_del_psql_tables = document.getElementById('modal_drop_del_psql_tables');
            var_modal_drop_del_psql_tables.style.display = "block"; 
        });


}) // Closes the MAIN --- Outer == document.addEventListener('DOMContentLoaded', function() { 

