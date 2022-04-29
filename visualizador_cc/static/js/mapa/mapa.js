
// const InternatCall = function(path, method = 'GET') {

//     return new Promise(function(resolve, reject) {

//         var req = new XMLHttpRequest();   
        
//         req.open(method, path);        

//         req.onload = function() {

//             if (req.status == 200) {

//                 try {
                    
//                     resolve(JSON.parse(req.response));
//                 }
//                 catch(error) {
                    
//                     reject();
//                 }

//             } else {

//                 if (req.status == 403) {
//                     console.error("La sesión ha expirado");
//                 } else {
//                     console.error('Error InternatCall', req);
//                 }               
//                 reject();
//             }
//         };

//         req.send();
//     })
// }




$(document).ready(function(){


     //capa base
    //  var capa_base = L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token=pk.eyJ1IjoiYm90aHJvcHMiLCJhIjoiY2tuZzN6M2R1MDAwdTJvczBuMGswdWV0cSJ9.eYUIhcQzUXfUQdkvYsjX0g', {
    //     attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
    //     maxZoom: 18,
    //     id: 'mapbox/streets-v11',
    //     tileSize: 512,
    //     zoomOffset: -1,
    //     accessToken: 'your.mapbox.access.token'
    // });

    //   // mapa
    //   var mymap = L.map('mimapa', {
    //     center: [-26.3102254, -61.0360629],
    //     zoom: 7,
    //     zoomControl: true,
    //     maxZoom: 17,
    //     minZoom: 1,
    //     layers: [capa_base]
    // });

    // InternatCall('/mapa/mapa_points/').then(response => {

    //     console.log(response);

    //     // let establecimientos = []
    //     // var capa_unica = L.geoJSON(establecimientos, {
    //     //     attribution: '',
    //     //     interactive: true,
    //     //     // onEachFeature: etiquetasFeatures,
    //     //     layerName: 'capa_unica'
    //     // });

    // }).catch((e) => {

    //     console.error('App/getDatas/', e)

    // })


   

})







