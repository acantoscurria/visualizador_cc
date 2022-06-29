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
      none: [{}],
      trayectoria_comun_primaria:{
        cueanexo: "CUEanexo",
        escuela: "Escuela",
        fila: "Fila",
        nivel: "Nivel",
        total_matric: "Total Matricula",
        var_matric: "Varones Matricula",
        total_entrados: "Total entrados",
        var_entrados: "Varones entrados",
        total_salido_con_pase: "Total salidos con pase",
        var_salido_con_pase: "Varones salidos con pase",
        total_salido_sin_pase: "Total salidos sin pase",
        var_salido_sin_pase: "Varones salidos sin trayectoria",
        total_ultimo_dia_clase: "Total ultimo dia clase",
        var_ultimo_dia_clase: "Varones ultimo dia clase",
        total_promovidos: "Total promovidos",
        var_promovidos: "Varones promovidos",
        total_promovidos_examen: "Total promovidos examen",
        var_promovidos_examen: "Varones promovidos examen",
        total_no_promovidos: "Total no promovidos",
        var_no_promovidos: "Varones no promovidos",
        total_prom_dyf: "Total promo dic y feb",
        var_prom_dyf: "Varones promo dic y feb",
        total_porm_otros: "Total promo otros",
        var_porm_otros: "Varones promo otros",
        total_egresados: "Total egresados",
        var_egresados: "Varones egresados",
        nom_est: "Nombre establecimiento",
        nro_est: "Numero establecimiento",
        /* fecha_creac_establec : "Fecha creacion establecimiento", */
        region: "Region",
        sector: "Sector",
        ambito: "Ambito",
        ref_loc: "Referencia localizacion",
        calle: "Calle",
        numero: "Numero",
        localidad: "Localidad",
        departamento: "Departamento",
        cod_postal: "CP",
        categoria: "Categoria",
        estado_est: "Estado establecimiento",
        estado_loc: "Estado localizacion",
        telefono_cod_area: "Cod de area",
        telefono_nro: "Nro de telefono",
        email_loc: "Email localizacion"
      },
      
    }
  }

function getColumns(ra, nivel) {
    let cols = [];
  
    let lista_de_valores = columns[ra][nivel];
  
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
  //   getColumns("ra2021", "matric_especial_inicial");
    const csrftoken = document.querySelector("[name=csrfmiddlewaretoken]").value;
  
    var dt_matricula = null;
  
    var reloadInstanceDatatable = function () {
      if (
        $("#nivel_input").val() == "none" ||
        $("#relevamiento_input").val() == "none"
      ) {
        $(".alert-msg-none-selection").show();
      } else {
        $(".alert-msg-none-selection").hide();
  
        if (dt_matricula) {
          dt_matricula.clear();
          dt_matricula.destroy();
  
          $("#tabla-trayectoria tbody").empty();
          $("#tabla-trayectoria thead").empty();
        }
  
      //   console.log(
      //     "columns",
      //     columns[$("#relevamiento_input").val()][$("#matricula_input").val()]
      //   );
  
          dt_matricula = $("#tabla-trayectoria")
            .on("processing.dt", function (e, settings, processing) {
              if (processing) {
              }
            })
            .DataTable({
              ajax: {
                url: "/reports/ra_trayectoria_list/",
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
                    nivel_selected: $("#nivel_input").val(),
                    ra_selected: $("#relevamiento_input").val(),
                  });
                },
              },
              columns: getColumns(
                $("#relevamiento_input").val(),
                $("#nivel_input").val()
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
  
    $("#nivel_input").change(function () {
      reloadInstanceDatatable();
    });
  
    $("#relevamiento_input").change(function () {
      reloadInstanceDatatable();
    });
  
    reloadInstanceDatatable();
  });
