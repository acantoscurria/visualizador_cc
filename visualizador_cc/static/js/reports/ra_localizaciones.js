$(document).ready(function(){

    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;

    let dt_ra_localizaciones = $("#tabla-ra_localizaciones").DataTable({
        "ajax": {

            "url": " /reports/ra_localizaciones_list/",
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
                })
            },

        },
        "columns": [
            {
                "class": "left row-control",
                "data": "id_localizacion",
                "name": "id_localizacion",
                "title": "Id Localizacion",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "nombre",
                "name": "nombre",
                "title": "Nombre",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "c_estado",
                "name": "c_estado",
                "title": "Estado",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "conflicto",
                "name": "conflicto",
                "title": "Conflicto",
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
                "data": "codigo_jurisdiccional",
                "name": "codigo_jurisdiccional",
                "title": "Codigo jurisdiccional",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "sector",
                "name": "sector",
                "title": "Sector",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "responsable",
                "name": "responsable",
                "title": "Responsable",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "localidad",
                "name": "localidad",
                "title": "Localidad",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "ambito",
                "name": "ambito",
                "title": "Ambito",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "departamento",
                "name": "departamento",
                "title": "Departamento",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "telefono",
                "name": "telefono",
                "title": "Telefono",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "carga_baja",
                "name": "carga_baja",
                "title": "Carga baja",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
        ],
        "processing":true,
        "serverSide": true,
        "autoWidth": true,
        "orderCellsTop": false,
        "rowId": 'id_localizacion',
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
        dt_ra_localizaciones.draw()
    })




})
