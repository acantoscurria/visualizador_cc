var eb = function (c) {
    let s = "";
    for (let i = 0; i < c; i++) {
      s += "&nbsp";
    }
    return s;
};
  
var columns = {
    none: {
      none: [{}],
    },
    ra2021: {
        id: 'ID',
        cueanexo: 'CUEanexo',
        tipo_ed: 'Tipo de educacion',
        nivel: 'Nivel',
        escuela: 'Escuela',
        total: 'Total',
        tot_var: 'Total varones',
        nro_est: 'Nro establecimiento',
        /* fecha_creac_establec: 'Fecha creacion establecimiento', */
        region: 'Region',
        sector: 'Sector',
        ambito: 'Ambito',
        ref_loc: 'Referencia localizacion',
        calle: 'Calle',
        numero: 'Numero',
        localidad: 'Localidad',
        departamento: 'Departamento',
        cod_postal: 'CP',
        categoria: 'Categoria',
        estado_est: 'Estado establecimiento',
        estado_loc: 'Estado localizacion',
        telefono_cod_area: 'Cod de area',
        telefono_nro: 'Nro telefono',
        email_loc: 'Email localizacion'
      },
      ra2020: {
        id: 'ID',
        cueanexo: 'CUEanexo',
        tipo_ed: 'Tipo de educacion',
        nivel: 'Nivel',
        escuela: 'Escuela',
        total: 'Total',
        tot_var: 'Total varones',
        nro_est: 'Nro establecimiento',
        /* fecha_creac_establec: 'Fecha creacion establecimiento', */
        region: 'Region',
        sector: 'Sector',
        ambito: 'Ambito',
        ref_loc: 'Referencia localizacion',
        calle: 'Calle',
        numero: 'Numero',
        localidad: 'Localidad',
        departamento: 'Departamento',
        cod_postal: 'CP',
        categoria: 'Categoria',
        estado_est: 'Estado establecimiento',
        estado_loc: 'Estado localizacion',
        telefono_cod_area: 'Cod de area',
        telefono_nro: 'Nro telefono',
        email_loc: 'Email localizacion'
      }
    };


  function getColumns(ra) {
    let cols = [];
  
    let lista_de_valores = columns[ra];
  
    for (let clave in lista_de_valores) {
      console.log(clave, lista_de_valores[clave]);
      cols.push({
        class: "justify-content-center row-control text-center align-middle ",
        data: clave,
        name: clave,
        title: lista_de_valores[clave],
        render: function (data, type, row) {
          return data ? data : "";
        },
      });
    }
  
    console.log("cols", cols);
  
    return cols;
  }

  $(document).ready(function () {
    
      const csrftoken = document.querySelector("[name=csrfmiddlewaretoken]").value;
    
      var dt_matricula_aborigen = null;
    
      var reloadInstanceDatatable = function () {
        if (
          
          $("#relevamiento_input").val() == "none"
        ) {
          $(".alert-msg-none-selection").show();
        } else {
          $(".alert-msg-none-selection").hide();
    
          if (dt_matricula_aborigen) {
            dt_matricula_aborigen.clear();
            dt_matricula_aborigen.destroy();
    
            $("#tabla-matricula tbody").empty();
            $("#tabla-matricula thead").empty();
          }
    
       
            dt_matricula_aborigen = $("#tabla-matricula")
              .on("processing.dt", function (e, settings, processing) {
                if (processing) {
                }
              })
              .DataTable({
                ajax: {
                  url: "/reports/ra_matricula_aborigen_list/",
                  type: "POST",
                  headers: { "X-CSRFToken": csrftoken },
                  dataFilter: function (data) {
                    if (data) {
                      try {
                        let json = $.parseJSON(data);
                        if (json.error_msg) {
                          alert(json.error_msg);
                        }
                        return data;
                      } catch (e) {
                        console.error("error al obtener los datos de la tabla", e);
                      }
                    }
                  },
                  data: function (d) {
                    return $.extend({}, d, {
                      
                      ra_selected: $("#relevamiento_input").val(),
                    });
                  },
                },
                columns: getColumns(
                  $("#relevamiento_input").val(),
                  
                ),
                processing: true,
                serverSide: true,
                autoWidth: true,
                orderCellsTop: false,
                //"order": [[ 1, 'asc' ]],
                //"rowId": 'id',
                scrollY: true,
                scrollY: "600px",
                scrollX: true,
                scrollCollapse: true,
                paging: true,
                ordering: false,
                createdRow: function (row, data, index) {},
                infoCallback: function (settings, start, end, max, total, pre) {
                  return pre;
                },
                initComplete: function (settings, json) {
                  console.log("DataTables has finished its initialisation.");
                },
                language: {
                  decimal: "",
                  emptyTable: "Sin resultados.",
                  info: "_START_ al _END_ de _TOTAL_",
                  infoEmpty: "0 al 0 de 0",
                  infoFiltered: "",
                  infoPostFix: "",
                  thousands: ",",
                  lengthMenu: "Mostrar _MENU_ filas",
                  loadingRecords: $("#preloader").html(),
                  processing: $("#preloader").html(),
                  search: "Buscar:",
                  zeroRecords: "Sin resultados",
                  paginate: {
                    first: "Primero",
                    last: "Último",
                    next: "Siguiente",
                    previous: "Anterior",
                  },
                  aria: {
                    sortAscending: ": Activar para ordenar la columna ascendente",
                    sortDescending: ": Activar para ordenar la columna descendente",
                  },
                },
                pagingType: "numbers",
                lengthMenu: [
                  [10, 100, 500, 1000, -1],
                  [10, 100, 500, 1000, "Todas"],
                ],
                dom: "Bfrtip",
                buttons: ["csv", "excel"],
              });
        }
      };
    
      
    
      $("#relevamiento_input").change(function () {
        reloadInstanceDatatable();
      });
    
      reloadInstanceDatatable();
    });
    