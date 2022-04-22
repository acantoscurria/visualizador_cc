
    /*
    columns = {
        nombre_matricula_1: {
            tipo_control_1: {
                {
                    "class": "left row-control",
                    "data": "id",
                    "name": "id",
                    "title": "#",
                    "render": function ( data, type, row ) {
                        return data ? data : ''
                    }
                },
                {
                    "class": "left row-control",
                    "data": "cueanexo",
                    "name": "cueanexo",
                    "title": "Cueanexo",
                    "render": function ( data, type, row ) {
                        return data ? data : ''
                    }
                },
            }
        }
    }
    */

var eb = function(c){
    let s = ""
    for (let i = 0; i < c; i++) {
        s+="&nbsp"             
    }
    return s
}

var columns = {
    none: {
        none: [{}]
    },
    matricula_comun_inicial: {
        none: [{}],
        precocidad: [
            {
                "class": "left row-control",
                "data": "id",
                "name": "id",
                "title": "#",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "tipo_ed",
                "name": "tipo_ed",
                "title": "Tipo ed.",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "nivel",
                "name": "nivel",
                "title": "Nivel",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "cueanexo",
                "name": "cueanexo",
                "title": "Cueanexo",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "id_fila",
                "name": "id_fila",
                "title": "Id fila",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "escuela",
                "name": "escuela",
                "title": eb(25)+"Escuela"+eb(25),
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "sala",
                "name": "sala",
                "title": "Sala",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "turno",
                "name": "turno",
                "title": "Turno",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "nom_secc",
                "name": "nom_secc",
                "title": "Nom secc",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "tipo_secc",
                "name": "tipo_secc",
                "title": "Tipo secc",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "total",
                "name": "total",
                "title": "Total",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "total_var",
                "name": "total_var",
                "title": "Total var",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "menos_1_año",
                "name": "menos_1_año",
                "title": "Menos 1 año",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "un_año",
                "name": "un_año",
                "title": "Un año",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "dos_años",
                "name": "dos_años",
                "title": "Dos años",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "tres_años",
                "name": "tres_años",
                "title": "Tres años",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "cuatro_años",
                "name": "cuatro_años",
                "title": "Cuatro años",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "cinco_años",
                "name": "cinco_años",
                "title": "Cinco años",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "seis_años",
                "name": "seis_años",
                "title": "Seis años",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "total_disc",
                "name": "total_disc",
                "title": "Total disc",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
        ]
    },
    matricula_comun_inicial: {
        none: [{}],
        precocidad: [
            {
                "class": "left row-control",
                "data": "id",
                "name": "id",
                "title": "#",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "tipo_ed",
                "name": "tipo_ed",
                "title": "Tipo ed.",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "nivel",
                "name": "nivel",
                "title": "Nivel",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "cueanexo",
                "name": "cueanexo",
                "title": "Cueanexo",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "id_fila",
                "name": "id_fila",
                "title": "Id fila",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "escuela",
                "name": "escuela",
                "title": eb(25)+"Escuela"+eb(25),
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },           
            {
                "class": "left row-control",
                "data": "turno",
                "name": "turno",
                "title": "Turno",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "total",
                "name": "total",
                "title": "Total",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "total_var",
                "name": "total_var",
                "title": "Total var",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "nivel_or",
                "name": "nivel_or",
                "title": "Nivel or",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "edad_12",
                "name": "edad_12",
                "title": "Edad 12",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "edad_13",
                "name": "edad_13",
                "title": "Edad 13",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "edad_14",
                "name": "edad_14",
                "title": "Edad 14",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "edad_15",
                "name": "edad_15",
                "title": "Edad 15",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "edad_16",
                "name": "edad_16",
                "title": "Edad 16",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "edad_17",
                "name": "edad_17",
                "title": "Edad 17",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "total_rep",
                "name": "total_rep",
                "title": "Total rep",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "var_rep",
                "name": "var_rep",
                "title": "var rep",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "nro_orden_pe",
                "name": "nro_orden_pe",
                "title": "nro orden pe",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "año_est",
                "name": "año_est",
                "title": "año est",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "nom_div",
                "name": "nom_div",
                "title": "nom div",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "tipo_div",
                "name": "tipo_div",
                "title": "tipo div",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "orientacion",
                "name": "orientacion",
                "title": "orientacion",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "edad_11_y_menos",
                "name": "edad_11_y_menos",
                "title": "edad 11 y menos",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "edad_18",
                "name": "edad_18",
                "title": "edad 18",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "edad_19",
                "name": "edad_19",
                "title": "edad 19",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "edad_25_y_mas",
                "name": "edad_25_y_mas",
                "title": "edad 25 y mas",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "edad_20_24",
                "name": "edad_20_24",
                "title": "edad 20 24",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "denom_pe",
                "name": "denom_pe",
                "title": "denom pe",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "total_disc",
                "name": "total_disc",
                "title": "total disc",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "var_disc",
                "name": "var_disc",
                "title": "var disc",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            
        ]
    },

}

$(document).ready(function(){

    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value; 

    var dt_matricula = null

    var reloadInstanceDatatable = function(){

        if($("#matricula_input").val() == "none" || $("#control_type_input").val() == "none"){

            $(".alert-msg-none-selection").show()
        }
        else{

            $(".alert-msg-none-selection").hide()

            if(dt_matricula){
                dt_matricula.destroy();
            }    
            
            dt_matricula = $("#tabla-matricula")
            .on( 'processing.dt', function ( e, settings, processing ) {
                if (processing) {
                } 
            })
            .DataTable({
                "ajax": {
                    "url": " /controls/matricula_list/",
                    "type": "POST",
                    "headers": {'X-CSRFToken': csrftoken },
                    "dataFilter": function( data ) {
                        if (data) {
                            try {
                                let json = $.parseJSON( data )
                                if(json.error_msg){
                                    alert(json.error_msg)
                                }  
                                return data                
    
                            } catch(e) {
                                console.error('error al obtener los datos de la tabla', e);
                            }
                        }
                    },
                    "data": function ( d ) {
                        return $.extend( {}, d, {
                            "matricula_selected": $("#matricula_input").val(),
                            "control_type_selected": $("#control_type_input").val(),
                        })
                    },
    
                },
                "columns": columns[$("#matricula_input").val()][$("#control_type_input").val()],     
                "processing":true,
                "serverSide": true,
                "autoWidth": true,
                "orderCellsTop": false,
                //"order": [[ 1, 'asc' ]],
                //"rowId": 'id',
                "scrollY": true,
                "scrollY": '600px',
                "scrollX": true,
                "scrollCollapse": true,
                "paging": true,
                "ordering": false,
                "createdRow": function( row, data, index ) {
    
                },
                "infoCallback": function( settings, start, end, max, total, pre ) {
    
                    return pre
                },
                "initComplete": function(settings, json) {
    
                    console.log( 'DataTables has finished its initialisation.' );          
            
                },
                "language": {
                    decimal: "",
                    emptyTable: "Sin resultados.",
                    info: "_START_ al _END_ de _TOTAL_",
                    infoEmpty: "0 al 0 de 0",
                    infoFiltered: "",
                    infoPostFix: "",
                    thousands: ",",
                    lengthMenu: "Mostrar _MENU_ filas",
                    loadingRecords: "Cargando...",
                    processing: "Cargando ...",
                    search: "Buscar:",
                    zeroRecords: "Sin resultados",
                    paginate: {
                        first: "Primero",
                        last: "Último",
                        next: "Siguiente",
                        previous: "Anterior"
                    },
                    aria: {
                        sortAscending: ": Activar para ordenar la columna ascendente",
                        sortDescending: ": Activar para ordenar la columna descendente"
                    }
                },
                "pagingType": "numbers",
                "lengthMenu": [[10, 100, 500, 1000, -1], [10, 100, 500, 1000, "Todas"]],
                "dom":
                    "<'row justify-content-between'<'col-auto'l><'col-auto'f><'col-auto mt-1'>>" +
                    "<'row'<'col-xl-12'tr>>" +
                    "<'row'<'col-xl-5'i><'col-xl-7'pb>>",
            }) 

        }


       
        
    }

    $("#matricula_input").change(function(){

        reloadInstanceDatatable()
    })

    $("#control_type_input").change(function(){

        reloadInstanceDatatable()
    })

    reloadInstanceDatatable()






})
