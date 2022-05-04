var map = null
var layer_localizaciones = null
var cluster_layer_localizaciones = null

function loadMap(){

    console.log('loadMap');

    map = L.map('map', {
        center: [-27.445701, -58.952356],
        zoom: 7,
        zoomControl: true,
        maxZoom: 17,
        minZoom: 1,        
    }); 

    console.log('loadMap map', map);

    L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token=pk.eyJ1IjoiYm90aHJvcHMiLCJhIjoiY2tuZzN6M2R1MDAwdTJvczBuMGswdWV0cSJ9.eYUIhcQzUXfUQdkvYsjX0g', {
        attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
        maxZoom: 18,
        id: 'mapbox/streets-v11',
        tileSize: 512,
        zoomOffset: -1,
        accessToken: 'your.mapbox.access.token'
    }).addTo(map);

    console.log('loadMap tileLayer', map);
}

function showPopupPointDetail(feature, layer) {

    console.log('showPopupPointDetail feature', feature, layer );

    if (feature.properties) {

        fetch("/mapa/point_data/?cueanexo="+feature.id)
        .then((response) => {

            console.log('mapa/point_data/?cueanexo response', response)

            //layer.bindPopup('detalle de localizacion');
        })   
        .catch((error) => {

            console.error('mapa/point_data/?cueanexo catch', error);
        })

        
    }

}

function loadPoints(){

    console.log('loadPoints');

    var preloader = new jBox('Notice', {
        content: 'Obteniendo puntos <i class="fa-solid fa-circle-notch fa-spin"></i>',
        color: 'blue',
        position: {
            x: 'center',
        },
        closeButton: false,
        closeOnClick: false,
        animation: 'flip',
        autoClose: false
      });
 

    fetch("/mapa/points/")
    .then((response) => {

        console.log('mapa/points response data', response)

        response.json().then(function(points) {

            console.log('mapa/points response points', points)

            layer_localizaciones = L.geoJSON(points, {
                attribution: '',
                interactive: true,
                onEachFeature: showPopupPointDetail,
                layerName: 'Localizaciones'
            })

            console.log('mapa/points load geoJSON complete!')
        
            preloader.close()

            //cluster de marcadores
            cluster_layer_localizaciones = L.markerClusterGroup();
            cluster_layer_localizaciones.addLayer(layer_localizaciones);
            map.addLayer(cluster_layer_localizaciones)

        });

    })   
    .catch((error) => {
        console.error('mapa/points catch', error);
    })



}
    

$(document).ready(function(){

    console.log('document ready');

    loadMap()

    loadPoints()
   

})







