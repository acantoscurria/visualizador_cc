var map = null
var cluster_layer = null
var preloader = null
var tileLayerBase = null
var dt_localizaciones_by_search = null
var loc_selected = null
var marker_found = null
var markersAll = []
var filter_mode = false
var cueanexo = null

let options_sector = []
let options_ambito = []
let options_departamento = []

function loadFilter() {


    let filters = {
        sector: [
            'Estatal',
            'Privado',
            'Gestión social/cooperativa',
        ],
        ambito: [
            'Urbano',
            'Rural Disperso',
            'Rural Aglomerado',
        ],
        departamento: [
            'LIBERTAD',
            'SARGENTO CABRAL',
            '2 DE ABRIL',
            '1§ DE MAYO',
            'MAIPU',
            'GENERAL GUEMES',
            'SAN FERNANDO',
            'GENERAL BELGRANO',
            'QUITILIPI',
            'GENERAL DONOVAN',
            'MAYOR LUIS J FONTANA',
            '9 DE JULIO',
            '12 DE OCTUBRE',
            'INDEPENDENCIA',
            'TAPENAGA',
            '25 DE MAYO',
            'SAN LORENZO',
            'BERMEJO',
            'CHACABUCO',
            'O HIGGINS',
            'ALMIRANTE BROWN',
            'COMANDANTE FERNANDEZ',
            'PRESIDENCIA DE LA PLAZA',
            'FRAY JUSTO SANTA MARIA DE ORO',
            'LIBERTADOR GENERAL SAN MARTIN',
        ]

    }

    let filterModalEl = document.getElementById('modalFilter')

    let filerModal = new bootstrap.Modal(filterModalEl, {
        keyboard: false
    })

    filterModalEl.addEventListener('hidden.bs.modal', function (event) {
        console.log('hidden.bs.modal');
    })

    filterModalEl.addEventListener('shown.bs.modal', function (event) {
        console.log('shown.bs.modal');
    })

    let loadFormFilter = function () {

        let i = 0
        $('#modalFilter .container-sector').empty()
        filters.sector.forEach(option => {
            i++
            let html = $('#template-checkbox-filter').clone().html();
            html = html.replace('d-none', '');
            html = html.split('%col%').join('col-12');
            html = html.split('%type%').join('sector');
            html = html.split('%value%').join(option);
            html = html.split('%i%').join(i);
            $('#modalFilter .container-sector').append(html)
        })

        $('#modalFilter .container-ambito').empty()
        filters.ambito.forEach(option => {
            i++
            let html = $('#template-checkbox-filter').clone().html();
            html = html.replace('d-none', '');
            html = html.split('%col%').join('col-12');
            html = html.split('%type%').join('ambito');
            html = html.split('%value%').join(option);
            html = html.split('%i%').join(i);
            $('#modalFilter .container-ambito').append(html)
        })

        $('#modalFilter .container-departamento').empty()
        filters.departamento.forEach(option => {
            i++
            let html = $('#template-checkbox-filter').clone().html();
            html = html.replace('d-none', '');
            html = html.split('%col%').join('col-4');
            html = html.split('%type%').join('departamento');
            html = html.split('%value%').join(option);
            html = html.split('%i%').join(i);
            $('#modalFilter .container-departamento').append(html)
        })

    }

    let updateFilterCounter = function (value) {
        $('.badge-filter').html(value)
    }

    loadFormFilter()

    L.easyButton('<i class="fa-solid fa-filter"></i>', function () {
        filerModal.show()
    }).addTo(map);

    $('#modalFilter .btn-apply').click(function () {

        filerModal.hide()

        preloader = new jBox('Notice', {
            content: 'Filtrando <i class="fa-solid fa-circle-notch fa-spin"></i>',
            color: 'blue',
            position: {
                x: 'center',
            },
            closeButton: false,
            closeOnClick: false,
            animation: 'flip',
            autoClose: false
        });

        options_sector = []
        options_ambito = []
        options_departamento = []

        let checkboxes = document.querySelectorAll('input[name=option_sector]:checked')
        for (var i = 0; i < checkboxes.length; i++) {
            options_sector.push(checkboxes[i].value)
        }
        checkboxes = document.querySelectorAll('input[name=option_ambito]:checked')
        for (var i = 0; i < checkboxes.length; i++) {
            options_ambito.push(checkboxes[i].value)
        }
        checkboxes = document.querySelectorAll('input[name=option_departamento]:checked')
        for (var i = 0; i < checkboxes.length; i++) {
            options_departamento.push(checkboxes[i].value)
        }

        console.log('options_sector', options_sector);
        console.log('options_ambito', options_ambito);
        console.log('options_departamento', options_departamento);

        let data = new FormData();
        data.append("filter", JSON.stringify({
            sector: options_sector,
            ambito: options_ambito,
            departamento: options_departamento
        }));

        updateFilterCounter(options_sector.length + options_ambito.length + options_departamento.length)

        let headers = new Headers();
        headers.append('X-CSRFToken', csrftoken);

        fetch("/mapa/filter/", {
            headers: headers,
            method: "POST",
            body: data,
        })
            .then((response) => {

                console.log('/mapa/filter/ response', response);

                response.json().then(function (points_filtered) {

                    console.log('/mapa/filter/ points_filtered', points_filtered);

                    let markersFiltered = {}
                    points_filtered.forEach((cueanexo) => {
                        markersFiltered[cueanexo] = markersAll[cueanexo]
                    })

                    filter_mode = true

                    updateLayerMarkers(markersFiltered).then(() => {
                        preloader.close()
                    })
                })

            })
            .catch((error) => {
                console.error('mapa/filter catch', error);
                reject(e)
            })


    })

    $('#modalFilter .btn-clear-filter').click(function () {

        filerModal.hide()

        console.log('btn-clear-filter click');

        options_sector = []
        options_ambito = []
        options_departamento = []

        loadFormFilter()

        filter_mode = false
        updateFilterCounter(0)

        updateLayerMarkers(markersAll).then(() => {

        })
    })

}

function loadSearch() {

    dt_localizaciones_by_search = $("#tabla-localizaciones")
        .DataTable({
            "ajax": {
                "url": "/mapa/search/",
                "type": "POST",
                "headers": { 'X-CSRFToken': csrftoken },
            },
            "columns": [
                {
                    "class": "left row-control",
                    "data": "cueanexo",
                    "name": "id",
                    "title": "#",
                    "render": function (data, type, row) {
                        return data ? data : ''
                    }
                },
                {
                    "class": "left row-control",
                    "data": "nom_est",
                    "name": "nom_est",
                    "title": "Nombre establecimiento",
                    "render": function (data, type, row) {
                        return data ? data : ''
                    }
                },
            ],
            "processing": true,
            "serverSide": true,
            "autoWidth": true,
            "scrollY": true,
            "scrollY": '600px',
            "scrollX": true,
            "scrollCollapse": true,
            "paging": true,
            "info": true,
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
            "lengthMenu": [[10, 100, -1], [10, 100, "Todas"]],
            "dom":
                "<'row justify-content-between'<'col-auto'l><'col-auto'f>>" +
                "<'row'<'col-xl-12'tr>>" +
                "<'row'<'col-xl-5'i><'col-xl-7'pb>>",
        })

    let searchModalEl = document.getElementById('modalSearch')

    let searchModal = new bootstrap.Modal(searchModalEl, {
        keyboard: false
    })

    searchModalEl.addEventListener('hidden.bs.modal', function (event) {
        console.log('hidden.bs.modal');
    })

    searchModalEl.addEventListener('shown.bs.modal', function (event) {
        console.log('shown.bs.modal');
        dt_localizaciones_by_search.draw()
        marker_found = null
    })

    map.on('moveend', function () {
        console.log('moveend !!');
        if (marker_found) {
            marker_found.bounce(5)
        }
    })

    $('#tabla-localizaciones tbody').on('click', '.row-control', function (e) {

        if (!$($(this).closest('tr')).find('.dataTables_empty').length) {

            loc_selected = dt_localizaciones_by_search.row($(this).closest('tr')).data()

            searchModal.hide()

            dt_localizaciones_by_search.search("").draw()

            console.log('loc_selected', loc_selected);

            cluster_layer.eachLayer((l) => {

                console.log('eachLayer', l);

                if (marker_found) { return }

                if (l instanceof L.Marker && loc_selected.cueanexo == l.cueanexo) {

                    marker_found = l
                    map.flyTo(marker_found.getLatLng(), 18)

                    console.log('marker_found', marker_found);
                }

            })

            if (!marker_found) {
                Swal.fire({
                    icon: 'info',
                    title: 'Establecimiento no encontrado.',
                    text: 'Verifique los filtros aplicados'
                })
            }
        }
    })

    L.easyButton('<i class="fa-solid fa-magnifying-glass"></i>', function () {
        searchModal.show()
    }).addTo(map);
}

function loadMap() {

    tileLayerBase = L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token=pk.eyJ1IjoiYm90aHJvcHMiLCJhIjoiY2tuZzN6M2R1MDAwdTJvczBuMGswdWV0cSJ9.eYUIhcQzUXfUQdkvYsjX0g', {
        attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
        maxZoom: 18,
        id: 'mapbox/streets-v11',
        tileSize: 512,
        zoomOffset: -1,
        accessToken: 'your.mapbox.access.token'
    })

    map = L.map('map', {
        center: [-27.445701, -58.952356],
        zoom: 7,
        zoomControl: true,
        maxZoom: 17,
        minZoom: 1,
        layers: [tileLayerBase]
    });

    console.log('loadMap tileLayer', map);
}

function markerOnClick(e) {
    preloader = new jBox('Notice', {
        content: 'Obteniendo datos del punto <i class="fa-solid fa-circle-notch fa-spin"></i>',
        color: 'blue',
        position: {
            x: 'center',
        },
        closeButton: false,
        closeOnClick: false,
        animation: 'flip',
        autoClose: false
    });

    fetch("/mapa/point_data/?cueanexo=" + e.target.cueanexo)
        .then((response) => {

            response.json().then(function (data) {

                if (data && data.length > 0) {

                    let point_data = data[0]

                    preloader.close()

                    let html = $('#template-point_data').clone().html();
                    html = html.replace('d-none', '');
                    html = html.split('%nom_est%').join(point_data.nom_est);
                    html = html.split('%cueanexo%').join(point_data.cueanexo);
                    html = html.split('%sector%').join(point_data.sector);
                    html = html.split('%ambito%').join(point_data.ambito);
                    html = html.split('%region_loc%').join(point_data.region_loc);
                    html = html.split('%localidad%').join(point_data.localidad);
                    html = html.split('%departamento%').join(point_data.departamento);
                    html = html.split('%estado_loc%').join(point_data.estado_loc);

                    L.popup({ offset: L.point(0, -20) })
                        .setLatLng(e.latlng)
                        .setContent(html)
                        .openOn(map);

                } else {

                    console.error('mapa/point_data/?cueanexo data SIN DATOS');
                }
            })

        })
        .catch((error) => {

            console.error('mapa/point_data/?cueanexo catch', error);
        })

}

function loadPoints() {

    return new Promise(function (resolve, reject) {

        fetch("/mapa/points/")
            .then((response) => {

                console.log('/mapa/points/ response', response);

                response.json().then(function (points) {

                    points.features.forEach(point => {
                        let marker = L.marker(point.geometry.coordinates.reverse()).on('click', markerOnClick)
                        marker.cueanexo = point.id
                        markersAll[marker.cueanexo] = marker
                    })

                    resolve()
                })

            })
            .catch((error) => {
                console.error('mapa/points catch', error);
                reject(e)
            })
    })
}

function updateLayerMarkers(markers) {

    return new Promise(function (resolve, reject) {

        if (cluster_layer) {
            map.removeLayer(cluster_layer);
        }

        cluster_layer = L.markerClusterGroup();

        let i = 0
        for (const cueanexo in markers) {

            if (markers[cueanexo]) {
                cluster_layer.addLayer(markers[cueanexo])
                i++
            }

        }

        map.addLayer(cluster_layer);

        $('.badge-amount-localizacion').html(i)

        resolve(true)

    })
}


function leafletDraw() {


    var drawnItems = new L.FeatureGroup();
    map.addLayer(drawnItems);
    var drawControl = new L.Control.Draw({
        edit: {
            featureGroup: drawnItems
        }
    });
    map.addControl(drawControl);

    map.addEventListener("draw:created", function (e) {
        console.log(e.layerType)
        drawnItems.clearLayers();

        e.layer.addTo(drawnItems);

        if (e.layerType === "circle") {

            let geojson = e.layer.toGeoJSON();
            geojson.properties['radio'] = e.layer.getRadius();

            const params = new URLSearchParams({
                radio: geojson.properties.radio,
                coordenadas: geojson.geometry.coordinates,
                sector: options_sector,
                ambito: options_ambito,
                dpto: options_departamento,
            })

            let url = '/mapa/localizaciones_by_draw?' + params.toString();
            window.open(url, '_blank').focus();

        }

        if (e.layerType === "polygon") {
            polygon = e.layer.toGeoJSON().geometry.coordinates;
            console.log(polygon)

            let geojson = e.layer.toGeoJSON().geometry;

            const params = new URLSearchParams({
                polygon: JSON.stringify(geojson),
                sector: options_sector,
                ambito: options_ambito,
                dpto: options_departamento,
            })

            let url = '/mapa/localizaciones_by_draw?' + params;
            window.open(url, '_blank').focus();

        }

    })

}

const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;

$(document).ready(function () {

    console.log('document ready');

    loadMap()

    preloader = new jBox('Notice', {
        content: 'Obteniendo puntos <i class="fa-solid fa-circle-notch fa-spin"></i>',
        color: 'blue',
        position: {
            x: 'center',
        },
        closeButton: false,
        closeOnClick: false,
        animation: 'flip',
        autoClose: false
    })

    loadPoints().then(() => {

        updateLayerMarkers(markersAll).then(() => {

            preloader.close()

            loadSearch()

            loadFilter()

            leafletDraw()

        })

    })

})
