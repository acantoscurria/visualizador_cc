$(document).ready(function(){

    $("#tabla-localizaciones").Datatable({
        "serverSide": true,
        "processing": true,
        "ajax": function(data, callback, settings) {
            $.get('/reports/localizaciones/', {
            }, function(res){
                console.log(res);
                callback({
                    recordsTotal: "",
                    recordsFiltered: "",
                    data:""
                })
            })
        }
    })

})
