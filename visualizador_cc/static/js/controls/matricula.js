

var columns = {
    none: [{}],   
    matricula_comun_inicial: COLUMNAS_CONTROL_MATRICULA_COMUN_INICIAL,
    matricula_comun_primaria: COLUMNAS_CONTROL_MATRICULA_COMUN_PRIMARIA,
    matricula_comun_secundaria: COLUMNAS_CONTROL_MATRICULA_COMUN_SECUNDARIA   
}
 

//inputs

var optionsMatriculas = {
    none: {
        text: 'Seleccione mátricula', 
        control_types: {
            none: 'Seleccione control'                    
        }
    },
    matricula_comun_inicial: {
        text: 'Mátricula comun inicial', 
        control_types: {
            none: 'Seleccione control',
            precocidad: 'Precocidad',
            sobreedad: 'Sobreedad'
        }
    },
    matricula_comun_primaria: {
        text: 'Mátricula comun primaria', 
        control_types: {
            none: 'Seleccione control',
            precocidad: 'Precocidad',
            sobreedad: 'Sobreedad'           
        }
    },
    matricula_comun_secundaria: {
        text: 'Mátricula comun secundaria', 
        control_types: {
            none: 'Seleccione control',
            precocidad: 'Precocidad',
           
        }
    }     
}


function setOpcionsControlTypeByMatricula() {

    let mat_selected = $('.matricula_input').val()  

    $('.control_type_input').empty()    

    let control_types = optionsMatriculas[mat_selected].control_types  

    for(const value in control_types) {

        $('.control_type_input').append($('<option>', {
            text: control_types[value],
            value
        }))
    }        
}



function setOpcionsMatricula() {

    $('.matricula_input').empty()     

    for(const value in optionsMatriculas) {

        $('.matricula_input').append($('<option>', {
            text: optionsMatriculas[value].text,
            value
        }))
    } 

    $('.matricula_input').val('none')   
    $('.matricula_input').change()  
    
}




$(document).ready(function(){

    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value; 
    
    var dt_matricula = null

    var reloadInstanceDatatable = function(){

        console.log('reloadInstanceDatatable dt_matricula', dt_matricula);
        console.log('metricula', $("#matricula_input").val());
        console.log('control', $("#control_type_input").val());

        if(dt_matricula){

            console.log('1');

            dt_matricula.clear();

            console.log('2');

            dt_matricula.destroy();

            console.log('3');

            $("#tabla-matricula tbody").empty();

            console.log('4');

            $("#tabla-matricula thead").empty();

            console.log('5');

            dt_matricula = null
        } 

        if($("#matricula_input").val() == "none" || $("#control_type_input").val() == "none"){

            $(".alert-msg-none-selection").show()

            console.log('lert-msg-none-selection show');
        }
        else{

            $(".alert-msg-none-selection").hide()

            console.log('lert-msg-none-selection hide'); 

            console.log('create DataTable columns', columns[$("#matricula_input").val()] );

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
                        return data 
                    },
                    "data": function ( d ) {
                        return $.extend( {}, d, {
                            "matricula_selected": $("#matricula_input").val(),
                            "control_type_selected": $("#control_type_input").val(),
                        })
                    },
    
                },
                "columns": columns[$("#matricula_input").val()],     
                "processing":true,
                "serverSide": false,
                "autoWidth": true,
                "orderCellsTop": false,
                //"order": [[ 1, 'asc' ]],
                //"rowId": 'id',
                "scrollY": true,
                "scrollY": '600px',
                "scrollX": true,
                "scrollCollapse": true,
                "paging": true,
                "ordering": true,
                "createdRow": function( row, data, index ) {
                    // if(data.error){
                    //     $(row).addClass('bg-danger text-light')
                    // }
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

        setOpcionsControlTypeByMatricula()

        reloadInstanceDatatable()       
    })

    $("#control_type_input").change(function(){

        reloadInstanceDatatable()
    })

    setOpcionsMatricula()


})
