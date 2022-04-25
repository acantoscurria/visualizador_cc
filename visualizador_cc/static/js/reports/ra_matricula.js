$(document).ready(function(){

    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;

    let dt_matric_comun_inicial = $("#tabla-matric_comun_inicial").DataTable({
        "ajax": {

            "url": " /reports/matric_comun_inicial_list/",
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
                    "ra_selected": $("#relevamiento_input").val(),
                    "matricula_selected": $("#matricula_input").val(),

                })
            },

        },
        "columns": [
            {
                "class": "left row-control",
                "data": "id",
                "name": "id",
                "title": "ID",
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
                "title": "ID Fila",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            
            {
                "class": "left row-control",
                "data": "escuela",
                "name": "escuela",
                "title": "Escuela",
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
        ],
        "processing":true,
        "serverSide": true,
        "autoWidth": true,
        "orderCellsTop": false,
        "rowId": 'id',
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
        "lengthMenu": [[100, 500, 1000, -1], [100, 500, 1000, "Todas"]],
        "dom":
            "<'row justify-content-between'<'col-auto'l><'col-auto'f><'col-auto mt-1'>>" +
            "<'row'<'col-xl-12'tr>>" +
            "<'row'<'col-xl-5'i><'col-xl-7'pb>>",
    })


    $("#relevamiento_input").change(function(){
        dt_matric_comun_inicial.draw()
    })




})