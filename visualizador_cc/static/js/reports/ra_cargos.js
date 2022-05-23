var eb = function (c) {
    let s = "";
    for (let i = 0; i < c; i++) {
      s += "&nbsp";
    }
    return s;
  };

const columns_cargos = {
    cueanexo: 'CUEanexo',
    escuela: "Escuela",
    cargos: "Cargos",
    total: "Total",
    titular: "Titular",
    interinos: "Interinos",
    sin_cubrir: "Sin Cubrir",
    contratados: "Contratados",
    planes_programas: "Planes/Programas",
    itinerantes: "Itinierantes",
    pasantias: "Pasantias",
    nom_est: "Nombre institucion",
    nro_est: "Nro institucion",
    fecha_creac_establec: "Fecha de creacion est.",
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
    estado_est: "Estado Establecimiento",
    estado_loc: "Estado Localizacion",
    telefono_cod_area: "Cod de area",
    telefono_nro: "Num de telefono",
    email_loc: "Email localizacion"
}

var columns = {
    none: {
      none: [{}],
    },
    ra2021: {
        none: [{}],
        comun_inicial_maternal: columns_cargos,
        comun_inicial_jardin: columns_cargos,
        comun_primaria: columns_cargos,
        comun_secundaria: columns_cargos,
        comun_snu: columns_cargos,
        comun_artistica: columns_cargos,
        comun_servicios_complementarios: columns_cargos,
        adultos_primaria: columns_cargos,
        adultos_secundaria: columns_cargos,
        adultos_form_prof: columns_cargos,
        especial: columns_cargos,
    }
}

function getColumns(ra, nivel_oferta) {
    let cols = [];
  
    let lista_de_valores = columns[ra][nivel_oferta];
  
    for (let clave in lista_de_valores) {
      console.log(clave, lista_de_valores[clave]);
      cols.push({
        class: "justify-content-center row-control text-center",
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
  
    var dt_matricula = null;
  
    var reloadInstanceDatatable = function () {
      if (
        $("#nivel_oferta_input").val() == "none" ||
        $("#relevamiento_input").val() == "none"
      ) {
        $(".alert-msg-none-selection").show();
      } else {
        $(".alert-msg-none-selection").hide();
  
        if (dt_matricula) {
          dt_matricula.clear();
          dt_matricula.destroy();
  
          $("#tabla-nivel_oferta tbody").empty();
          $("#tabla-nivel_oferta thead").empty();
        }
  
      //   console.log(
      //     "columns",
      //     columns[$("#relevamiento_input").val()][$("#matricula_input").val()]
      //   );
  
          dt_matricula = $("#tabla-nivel_oferta")
            .on("processing.dt", function (e, settings, processing) {
              if (processing) {
              }
            })
            .DataTable({
              ajax: {
                url: "/reports/ra_cargos_list/",
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
                    nivel_oferta_selected: $("#nivel_oferta_input").val(),
                    ra_selected: $("#relevamiento_input").val(),
                  });
                },
              },
              columns: getColumns(
                $("#relevamiento_input").val(),
                $("#nivel_oferta_input").val()
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
              dom: "frtip",
              buttons: ["copy", "csv", "excel", "pdf", "print"],
            });
      }
    };
  
    $("#nivel_oferta_input").change(function () {
      reloadInstanceDatatable();
    });
  
    $("#relevamiento_input").change(function () {
      reloadInstanceDatatable();
    });
  
    reloadInstanceDatatable();
  });
  