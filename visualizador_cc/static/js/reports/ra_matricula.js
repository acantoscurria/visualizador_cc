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
    matricula_especial_inicial: {
      cueanexo: "CUEanexo",
      escuela: "Escuela",
      sala: "Sala",
      turno: "Turno",
      tipo_secc: "Tipo de Seccion",
      total: "Total",
      total_var: "Total varones",
      nom_secc: "Nombre de sección",
      cinco_anios: "5 años",
      seis_anios: "6 años",
      siete_anios: "7 años",
      cero_a_dos_anios: "8 años",
      tres_anios: "3 años",
      cuatro_anios: "4 años",
      ocho_o_mas_anios: "8+ años",
      nom_est: "Nombre establecimiento",
      nro_est: "Número establecimiento",
      anio_creac_establec: "Año de creacion est.",
      fecha_creac_establec: "Fecha de creacion est",
      region: "Region",
      udt: "UDT",
      cui: "CUI",
      cua: "CUA",
      cuof: "CUOF",
      sector: "Sector",
      ambito: "Ambito",
      ref_loc: "Ref Loc",
      calle: "Calle",
      numero: "Numero",
      localidad: "Localidad",
      departamento: "Departamento",
      cod_postal: "CP",
      categoria: "Categoria",
      estado_est: "Estado establecimento",
      estado_loc: "Estado localizacion",
      telefono_cod_area: "Cod de área",
      telefono_nro: "Nro telefono",
      per_funcionamiento: "Per funcionamiento",
      email_loc: "Email localizacion",
    },
    matricula_comun_inicial:matricula_comun_inicial_columns,
    matricula_comun_primaria:matricula_comun_primaria_columns,
    matricula_comun_secundaria:matricula_comun_secundaria_columns,
    matricula_comun_snu:matricula_comun_snu_columns,
    matricula_adultos_primaria:matricula_adultos_primaria_columns,
    matricula_adultos_secundaria:matricula_adultos_secundaria_columns,
    matricula_especial_primaria:matricula_especial_primaria_columns,
  },
  ra2020: {
    none: [{}],
    matricula_especial_inicial: {
      cueanexo: "CUEanexo",
      escuela: "Escuela",
      sala: "Sala",
      turno: "Turno",
      tipo_secc: "Tipo de Seccion",
      total: "Total",
      total_var: "Total varones",
      nom_secc: "Nombre de sección",
      cinco_anios: "5 años",
      seis_anios: "6 años",
      siete_anios: "7 años",
      cero_a_dos_anios: "8 años",
      tres_anios: "3 años",
      cuatro_anios: "4 años",
      ocho_o_mas_anios: "8+ años",
      nom_est: "Nombre establecimiento",
      nro_est: "Número establecimiento",
      anio_creac_establec: "Año de creacion est.",
      fecha_creac_establec: "Fecha de creacion est",
      region: "Region",
      udt: "UDT",
      cui: "CUI",
      cua: "CUA",
      cuof: "CUOF",
      sector: "Sector",
      ambito: "Ambito",
      ref_loc: "Ref Loc",
      calle: "Calle",
      numero: "Numero",
      localidad: "Localidad",
      departamento: "Departamento",
      cod_postal: "CP",
      categoria: "Categoria",
      estado_est: "Estado establecimento",
      estado_loc: "Estado localizacion",
      telefono_cod_area: "Cod de área",
      telefono_nro: "Nro telefono",
      per_funcionamiento: "Per funcionamiento",
      email_loc: "Email localizacion",
    },
    matricula_comun_inicial:matricula_comun_inicial_columns,
    matricula_comun_primaria:matricula_comun_primaria_columns,
    matricula_comun_secundaria:matricula_comun_secundaria_columns,
    matricula_comun_snu:matricula_comun_snu_columns,
    matricula_adultos_primaria:matricula_adultos_primaria_columns,
    matricula_adultos_secundaria:matricula_adultos_secundaria_columns,
    matricula_especial_primaria:matricula_especial_primaria_columns,
  },
};

function getColumns(ra, matricula) {
  let cols = [];

  let lista_de_valores = columns[ra][matricula];

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
      $("#matricula_input").val() == "none" ||
      $("#relevamiento_input").val() == "none"
    ) {
      $(".alert-msg-none-selection").show();
    } else {
      $(".alert-msg-none-selection").hide();

      if (dt_matricula) {
        dt_matricula.clear();
        dt_matricula.destroy();

        $("#tabla-matricula tbody").empty();
        $("#tabla-matricula thead").empty();
      }

    //   console.log(
    //     "columns",
    //     columns[$("#relevamiento_input").val()][$("#matricula_input").val()]
    //   );

        dt_matricula = $("#tabla-matricula")
          .on("processing.dt", function (e, settings, processing) {
            if (processing) {
            }
          })
          .DataTable({
            ajax: {
              url: "/reports/ra_matricula_list/",
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
                  matricula_selected: $("#matricula_input").val(),
                  ra_selected: $("#relevamiento_input").val(),
                });
              },
            },
            columns: getColumns(
              $("#relevamiento_input").val(),
              $("#matricula_input").val()
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

  $("#matricula_input").change(function () {
    reloadInstanceDatatable();
  });

  $("#relevamiento_input").change(function () {
    reloadInstanceDatatable();
  });

  reloadInstanceDatatable();
});
