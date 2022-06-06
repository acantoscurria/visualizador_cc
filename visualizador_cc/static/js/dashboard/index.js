
function dynamicColors() {
    var r = Math.floor(Math.random() * 255);
    var g = Math.floor(Math.random() * 255);
    var b = Math.floor(Math.random() * 255);
    return "rgb(" + r + "," + g + "," + b + ")";
};

function getColorsList(n){
    
    let array = []

    for (let index = 0; index < n; index++) {        
        array.push(dynamicColors())        
    }

    return array

}

const colorList = getColorsList(18)

//chart_bar_oferta_educativa

const div_chart_bar_oferta_educativa = document.getElementById('chart_bar_oferta_educativa').getContext('2d');

const myChart_chart_bar_oferta_educativa = new Chart(div_chart_bar_oferta_educativa, {
    type: 'bar',
    data: {
        labels: [
            'R.E.1', 
            'SUB. R.E. 1',
            'R.E. 2', 
            'SUB. R.E. 2', 
            'R.E. 3', 
            'SUB. R.E. 3', 
            'R.E. 4-A', 
            'R.E. 4-B', 
            'R.E. 5', 
            'SUB. R.E. 5', 
            'R.E. 6', 
            'R.E. 7', 
            'R.E. 8-A', 
            'R.E. 8-B', 
            'R.E. 9', 
            'R.E. 10-A', 
            'R.E. 10-B', 
            'R.E. 10-C',           
        ],
        datasets: [{
            label: 'Ofertas',
            data: [
                141, 
                46, 
                380, 
                135, 
                146, 
                55, 
                257, 
                278, 
                172, 
                129, 
                136, 
                170, 
                289, 
                145, 
                423, 
                357, 
                356, 
                341   
            ],
            backgroundColor: colorList,
            borderColor: colorList,
            borderWidth: 1
        }]
    },
    options: {
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
});


//chart_bar_matricula

const div_chart_bar_matricula = document.getElementById('chart_bar_matricula').getContext('2d');

const myChart_chart_bar_matricula = new Chart(div_chart_bar_matricula, {
    type: 'bar',
    data: {
        labels: [
            'R.E.1', 
            'SUB. R.E. 1',
            'R.E. 2', 
            'SUB. R.E. 2', 
            'R.E. 3', 
            'SUB. R.E. 3', 
            'R.E. 4-A', 
            'R.E. 4-B', 
            'R.E. 5', 
            'SUB. R.E. 5', 
            'R.E. 6', 
            'R.E. 7', 
            'R.E. 8-A', 
            'R.E. 8-B', 
            'R.E. 9', 
            'R.E. 10-A', 
            'R.E. 10-B', 
            'R.E. 10-C',           
        ],
        datasets: [{
            label: 'Mátriculas',
            data: [
                7198, 
                1804, 
                26933, 
                9221, 
                14553, 
                4455, 
                37545, 
                31492, 
                17945, 
                9668, 
                10471, 
                15090, 
                32181, 
                10231, 
                42750, 
                68848, 
                65573, 
                46547, 
                 
            ],
            backgroundColor: colorList,
            borderColor: colorList,
            borderWidth: 1
        }]
    },
    options: {
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
});


