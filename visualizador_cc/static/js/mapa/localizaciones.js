var dt_localizaciones = null

$(document).ready(function(){

    let radio = $('#radio').val()
    let centro = $('#centro').val()
    let filter_dpto = $('#dpto').val()
    let filter_ambito = $('#ambito').val()
    let filter_sector = $('#sector').val()

    console.log('****radio', radio)
    console.log('****centro', centro)  
    console.log('****dpto', filter_dpto)
    console.log('****ambito', filter_ambito)
    console.log('****sector', filter_sector)

    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;  

    dt_localizaciones = $("#tabla-localizaciones")
    .on( 'processing.dt', function ( e, settings, processing ) {
        if (processing) {
        } 
    })
    .DataTable({
        "ajax": {
            "url": " /mapa/localizaciones_by_circle_list/",
            "type": "POST",
            "headers": {'X-CSRFToken': csrftoken },
            "dataFilter": function( data ) {
                return data 
            },
            "data": function ( d ) {
                return $.extend( {}, d, {
                    radio,
                    centro,
                    filter_dpto,
                    filter_ambito,
                    filter_sector,
                })
            },

        },
        "columns": [
          
            {
                "class": "row-control",
                "data": "cueanexo",
                "name": "cueanexo",
                "title": "cueanexo",
            },
            {
                "class": "row-control",
                "data": "nom_est",
                "name": "nom_est",
                "title": "nom_est",
            },
            {
                "class": "row-control",
                "data": "sector",
                "name": "sector",
                "title": "sector",
            },
            {
                "class": "row-control",
                "data": "ambito",
                "name": "ambito",
                "title": "ambito",
            },
            {
                "class": "row-control",
                "data": "region_loc",
                "name": "region_loc",
                "title": "region_loc",
            },
            {
                "class": "row-control",
                "data": "localidad",
                "name": "localidad",
                "title": "localidad",
            },
            {
                "class": "row-control",
                "data": "departamento",
                "name": "departamento",
                "title": "departamento",
            },
        ],     
        "processing":true,
        "serverSide": false,
        "autoWidth": true,
        "orderCellsTop": false,
        "scrollY": true,
        "scrollY": '600px',
        "scrollX": true,
        "scrollCollapse": true,
        "paging": true,
        "ordering": true,              
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
        "<'row justify-content-between'<'col-auto'l><'col-auto'B><'col-auto'f>>" +
        "<'row'<'col-xl-12 filterApplied'>>" +
        "<'row'<'col-xl-12'tr>>" +
        "<'row'<'col-xl-5'i><'col-xl-7'pb>>",
        "buttons": [
                 'csv', 'excel',
                 {
                    extend: 'print',
                    text: 'Imprimir',               
                 }
            ]
    }) 

})
