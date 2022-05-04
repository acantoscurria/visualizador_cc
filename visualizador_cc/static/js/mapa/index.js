var map = null
var layer_localizaciones = null
var cluster_layer_localizaciones = null
var preloader = null


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


function markerOnClick(e)
{

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

    console.log('markerOnClick', e, e.latlng, e.target.cueanexo);

    fetch("/mapa/point_data/?cueanexo=" + e.target.cueanexo)
    .then((response) => {

        response.json().then(function(data) {

            console.log('mapa/point_data/?cueanexo data', data)

            if(data && data.length > 0){

                let point_data = data[0]

                preloader.close()

                let html = $('#template-point_data').clone().html();
                html = html.replace('d-none', '');
                html = html.split('%nom_est%').join( point_data.nom_est );
                html = html.split('%cueanexo%').join( point_data.cueanexo );   
                html = html.split('%sector%').join( point_data.sector );   
                html = html.split('%ambito%').join( point_data.ambito );   
                html = html.split('%region_loc%').join( point_data.region_loc );   
                html = html.split('%localidad%').join( point_data.localidad );   
                html = html.split('%departamento%').join( point_data.departamento );   
                html = html.split('%estado_loc%').join( point_data.estado_loc );   
          
                L.popup({offset: L.point(0, -17)})
                .setLatLng(e.latlng)               
                .setContent(html)
                .openOn(map);

            }else{

                console.error('mapa/point_data/?cueanexo data SIN DATOS');
            }            
        })        

    })   
    .catch((error) => {

        console.error('mapa/point_data/?cueanexo catch', error);
    })

}

function loadPoints(){

    console.log('loadPoints');

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
    });
 

    fetch("/mapa/points/")
    .then((response) => {

        // console.log('mapa/points response data', response)

        response.json().then(function(points) {

            // console.log('mapa/points response points',  points.features)

            cluster_layer_localizaciones = L.markerClusterGroup();

            points.features.forEach(point => {  
                let marker = L.marker(point.geometry.coordinates.reverse()).on('click', markerOnClick)
                marker.cueanexo = point.id
                cluster_layer_localizaciones.addLayer(marker);
            });

            map.addLayer(cluster_layer_localizaciones);   
        
            preloader.close()           

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







