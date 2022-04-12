$(document).ready(function(){

    $("#tabla-ra_localizaciones").DataTable({
        "serverSide": true,
        "processing": true,
        "ajax": function(data, callback, settings) {
            $.get('/reports/ra_localizaciones_list/', {
                limite: data.length,
                inicio: data.start,
            }, function(res){
                console.log(res);
                callback({
                    recordsTotal: res.length,
                    recordsFiltered: res.length,
                    data: res
                })
            })
        },
        "Columnas": [
            {"data": "id_localizacion"},
            {"data": "nombre"},
            {"data": "cueanexo"},
            {"data": "c_estado"},
            {"data": "conflicto"},
            {"data": "codigo_jurisdiccional"},
            {"data": "sector"},
            {"data": "responsable"},
            {"data": "localidad"},
            {"data": "ambito"},
            {"data": "departamento"},
            {"data": "telefono"},
            {"data": "carga_baja"}
        ]
    })

})
