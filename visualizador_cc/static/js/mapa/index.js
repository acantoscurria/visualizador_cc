var map = null

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

function loadPoints(){

    console.log('loadPoints');

    var preloader = jBox('Notice', {
        content: 'Cargando puntos...',
        color: 'blue',
        animation: 'flip',
        showCountdown: true,
        autoClose: 10000,
        position: {
            x: 'center',
        },
        theme: 'TooltipDark',
        closeButton: false,
        closeOnClick: false,
    })

    fetch("/mapa/points/")
    .then((response) => {

        console.log('mapa/points response data', response)

        response.json().then(function(json) {

            console.log('mapa/points response json', json)

            L.geoJSON(json).addTo(map);

            console.log('mapa/points load geoJSON complete!')
        
            preloader.destroy()
            
           

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







