
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

const ctx = document.getElementById('chart_bar_oferta_educativa').getContext('2d');

const colorList = getColorsList(18)

var data = {
    "R.E.1": 141,  
    "SUB. R.E. 1": 46, 
    "R.E. 2": 380,  
    "SUB. R.E. 2": 135,  
    "R.E. 3": 146,  
    "SUB. R.E. 3": 55,  
    "R.E. 4-A": 257,  
    "R.E. 4-B": 278,  
    "R.E. 5": 172,  
    "SUB. R.E. 5": 129,  
    "R.E. 6": 136,  
    "R.E. 7": 170,  
    "R.E. 8-A": 289,  
    "R.E. 8-B": 145,  
    "R.E. 9": 423,  
    "R.E. 10-A": 357,  
    "R.E. 10-B": 356,  
    "R.E. 10-C": 341   
}

const myChart = new Chart(ctx, {
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
            label: '# of Votes',
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