const btnSwitch = document.querySelector('#switch');

if(btnSwitch){


    btnSwitch.addEventListener('click', () => {
        document.body.classList.toggle('dark');
        btnSwitch.classList.toggle('active');

        //guardar el modo en localstorage
        if(document.body.classList.contains('dark')){
            localStorage.setItem('dark-mode', 'true');
        } else {
            localStorage.setItem('dark-mode', 'false');
        }
    });

    //obtener el modo actual
    if(localStorage.getItem('dark-mode') == 'true'){
        document.body.classList.add('dark');
        btnSwitch.classList.add('active');

    } else{
        document.body.classList.remove('dark');
        btnSwitch.classList.remove('active');

    }


}
