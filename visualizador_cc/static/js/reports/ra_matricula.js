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
    'ra2021': {
        none: [{}],
        matricula_comun_inicial: [
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
}

$(document).ready(function(){

    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;

    var dt_matricula = null

    var reloadInstanceDatatable = function(){

        if($("#matricula_input").val() == "none" || $("#relevamiento_input").val() == "none"){

            $(".alert-msg-none-selection").show()
        }
        else{

            $(".alert-msg-none-selection").hide()

            if(dt_matricula){

                dt_matricula.clear();
                dt_matricula.destroy();

                $("#tabla-matricula tbody").empty();
                $("#tabla-matricula thead").empty();
            }    

            console.log("columns", columns[$("#relevamiento_input").val()][$("#matricula_input").val()])     

            dt_matricula = $("#tabla-matricula")
            .on( 'processing.dt', function ( e, settings, processing ) {
                if (processing) {
                } 
            })
            .DataTable({
                "ajax": {
                    "url": "/reports/ra_matricula_list/",
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
                            "ra_selected": $("#relevamiento_input").val(),
                        })
                    },
    
                },
                "columns": columns[$("#relevamiento_input").val()][$("#matricula_input").val()],     
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
                    loadingRecords: $('#preloader').html(),
                    processing: $('#preloader').html(),
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

    $("#relevamiento_input").change(function(){

        reloadInstanceDatatable()
    })

    reloadInstanceDatatable()

})