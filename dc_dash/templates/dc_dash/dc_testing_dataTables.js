<table id="example" class="display" cellspacing="0" width="100%">
</table>

<script>
        var myUrl = "{% url 'django_url_withJSON' %}" 
        var dataSet;
        var my_columns = []; 

        $(document).ready(function(){
            $.ajax({
                    url: myUrl,
                    type: 'GET',     
                    dataType: 'json', 
                    success: function(dict_json_from_py) {
                      console.log("-----dict_json_from_py--Data displays fine in Console--")
                      console.log(dict_json_from_py)
                      var dataSet = dict_json_from_py.data_json.columns;
                      //console.log(dataSet)
                      $.each(dataSet, function( key, value ) {
                                                var my_item = {};
                                                my_item.data = key; 
                                                my_item.title = value;
                                                console.log(my_item.data)
                                                console.log(my_item.title)
                                                my_columns.push(my_item); 
                                                console.log(my_columns)
                                                return my_columns
                                        });

                        assignToEventsColumns(my_columns,dict_json_from_py);
                    }, // Close - success:
                })    // Close - "ajax":

            function assignToEventsColumns(my_columns,dict_json_from_py) {

                    var table = $('#example').DataTable({
                        "bAutoWidth" : false, //bAutoWidth -- b == BOOLEAN
                        "serverSide": false, // 
                        "aaData": dict_json_from_py.data_json.data, 
                        "columns" : my_columns,
                      })
                  }
              }); 

    </script>









