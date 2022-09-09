const matricula_comun_inicial_columns= {   
    cueanexo: 'CUEanexo',//0 
    escuela: 'Escuela', //1
    sala: 'Sala', //2
    turno: 'Turno', //3
    nom_secc: 'Nombre Seccion',//4
    tipo_secc: 'Tipo Seccion', //5
    total: 'Total',//6
    //total_var: 'Total varones',
    //total_disc: 'Total alumnos con discapacidad',
    //var_disc: 'Total Varones con discapacidad',    
    //nom_est: 'Nombre establecimiento',
    //nro_est: 'Nro Establecimiento',
    region: 'Region', //7
    //udt: 'UDT',
    //cui: 'CUI',
    //cua: 'CUA',
    //cuof: 'CUOF',
    sector: 'Sector', //8
    ambito: 'Ambito', //9
    //ref_loc: 'Referente local',
    calle: 'Calle',//10
    numero: 'Numero',//11
    localidad: 'Localidad',//12
    departamento: 'Departamento', //13
    cod_postal: 'CP',//14
    //categoria: 'Categoria',
    //estado_est: 'Estado establecimiento',
    //estado_loc: 'Estado localizacion',
        //telefono_cod_area: 'cod de area',
        //telefono_nro: 'nro telefono',
    //email_loc: 'Email de localizacion',
    target_filters: [7,8,9,12]
};

const matricula_comun_primaria_columns = {
    cueanexo: 'CUEanexo', //0
    escuela: 'Escuela',//1
    turno: 'Turno',//2    
    nombre_secc: 'Nombre sección',//3
    tipo_secc: 'Tipo sección',//4
    total: 'Total',//5
    //total_var: 'Total varones',
    nivel: 'Nivel',//6
    grado_anio: 'Grado año',//7
    //total_rep: 'Total repitentes',
    //var_rep: 'Varones repitentes',
    //tot_alum_promoasis: 'Total alumnos promo',
    //var_alum_promoasis: 'Varones promo',
    //tot_discapacidad: 'Total discapacidad',
    //var_discapacidad: 'Varones discapacidad',
    //nom_est: 'Nombre establecimiento',
    //nro_est: 'Nro establecimiento',
    /* fecha_creac_establec: 'Fecha creacion establecimiento', */
    region: 'Region',//8
    sector: 'Sector',//9
    ambito: 'Ambito',//10
    //ref_loc: 'Referencia de localizacion',
    calle: 'Calle',//11
    numero: 'Numero',//12
    localidad: 'Localidad',//13
    departamento: 'Departamento',//14
    cod_postal: 'CP',//15
    //categoria: 'Categoría',
    //estado_est: 'Estado establecimiento',
    //estado_loc: 'EStado localizacion',
    //telefono_cod_area: 'Cod de área',
    //telefono_nro: 'Nro telefono',
    //email_loc: 'Email localizacion',
    target_filters: [8,9,10,13]
}

const matricula_comun_secundaria_columns = {
    cueanexo: 'CUEanexo',
    nom_est: 'Nombre establecimiento',
    nro_est: 'Nro establecimiento',
    orientacion: 'Orientacion',
    anio_est: 'Año/Grado',
    nom_div: 'Nombre divicion',
    tipo_div: 'Tipo divicion',
    turno: 'Turno',
    
    total: 'Total',
    total_var: 'Total varones',
    nivel: 'Nivel',
    total_rep: 'Total repitentes',
    var_rep: 'Varones repitentes',
    
    
    denom_pe: 'Denominacion plan de estudio',
    total_disc: 'Total discapacidad',
    var_disc: 'Varones discapacidad',
    
    /* fecha_creac_establec: 'Fecha creacion establecimiento', */
    region: 'Region',
    sector: 'Sector',
    ambito: 'Ambito',
    ref_loc: 'Referencia localizacion',
    calle: 'Calle',
    numero: 'Numero',
    localidad: 'Localidad',
    departamento: 'Departamento',
    cod_postal: 'CP',
    categoria: 'Categoria',
    estado_est: 'Estado establecimiento',
    estado_loc: 'Estado localizacion',
    telefono_cod_area: 'Cod de área',
    telefono_nro: 'Nro telefono',
    email_loc: 'Email localizacion',
}

const matricula_comun_snu_columns = {
    cueanexo: 'CUEanexo',
    escuela: 'Escuela',
    n_plan_estudio: 'Nro plan de estudio',
    plan_est_titulo: 'Titulo de plan de estudio',
    tipo_carrera: 'Tipo de carrera',
    tipo_formacion: 'Tipo formacion',
    modalidad_dicatado: 'Modalidad dictado',
    carrera_termino: 'Carrera termino',
    total: 'Total',
    total_var: 'Total varones',
    total_ingresante: 'Total ingresantes',
    var_ingresante: 'Varones ingresantes',
    total_pasantia_practicas: 'Total pasantia practicas',
    var_pasantia_practicas: 'Varones pasantia practicas',
    total_residencia: 'Total residencia',
    var_residencia: 'Varones residencia',
    nom_est: 'Nombre establecimiento',
    nro_est: 'Nro establecimiento',
    /* fecha_creac_establec: 'Fecha creacion establecimiento', */
    region: 'Region',
    sector: 'Sector',
    ambito: 'Ambito',
    ref_loc: 'Referencia localizacion',
    calle: 'Calle',
    numero: 'Numero',
    localidad: 'Localidad',
    departamento: 'Departamento',
    cod_postal: 'CP',
    categoria: 'Categoria',
    estado_est: 'Estado establecimiento',
    estado_loc: 'Estado localizacion',
    telefono_cod_area: 'Cod de área',
    telefono_nro: 'Nro telefono',
    email_loc: 'Email localizacion',
}

const matricula_adultos_primaria_columns = {
    cueanexo: 'CUEanexo',
    nom_est: 'Nombre establecimiento',
    nro_est: 'Nro establecimiento',
    turno: 'Turno',
    tipo_secc: 'Tipo sección',
    nivel: 'Nivel',
    nom_secc: 'Nombre seccion',
    ciclo_etapa: 'Ciclo etapa',
    total: 'Total',
    total_var: 'Total varones',
    
    /* fecha_creac_establec: 'Fecha creacion establecimiento', */
    region: 'Region',
    sector: 'Sector',
    ambito: 'Ambito',
    ref_loc: 'Referencia localizacion',
    calle: 'Calle',
    numero: 'Numero',
    localidad: 'Localidad',
    departamento: 'Departamento',
    cod_postal: 'CP',
    categoria: 'Categoria',
    estado_est: 'Estado establecimiento',
    estado_loc: 'Estado localizacion',
    telefono_cod_area: 'Cod de área',
    telefono_nro: 'Nro telefono',
    email_loc: 'Email localizacion',
}

const matricula_adultos_secundaria_columns = {
    cueanexo: 'CUEanexo',
    nom_est: 'Nombre establecimiento',
    nro_est: 'Nro establecimiento',
    turno: 'Turno',
    nivel: 'Nivel',
    nro_plan_est: 'Nro plan de estudio',
    anio_plan_est: 'Año plan de estudio',
    nom_div: 'Nombre divicion',
    tipo_div: 'Tipo divicion',
    orientacion: 'Orientacion',
    total: 'Total',
    total_var: 'Total varones',
    total_rep: 'Total repitentes',
    var_rep: 'Varones repitentes',
    
    /* fecha_creac_establec: 'Fecha creacion establecimiento', */
    region: 'Region',
    sector: 'Sector',
    ambito: 'Ambito',
    ref_loc: 'Referencia localizacion',
    calle: 'Calle',
    numero: 'Numero',
    localidad: 'Localidad',
    departamento: 'Departamento',
    cod_postal: 'CP',
    categoria: 'Categoria',
    estado_est: 'Estado establecimiento',
    estado_loc: 'Estado localizacion',
    telefono_cod_area: 'Cod de área',
    telefono_nro: 'Nro telefono',
    email_loc: 'Email localizacion',
}

const matricula_especial_primaria_columns = {
    cueanexo: 'CUEanexo',
    nom_est: 'Nombre establecimiento',
    nro_est: 'Nro establecimiento',
    turno: 'Turno',
    tipo_secc: 'Tipo seccion',
    total: 'Total',
    total_var: 'Total varones',
    nom_secc: 'Nombre seccion',
    total_rep: 'Total repitentes',
    var_rep: 'Varones repitentes',
    
    /* fecha_creac_establec: 'Fecha creacion establecimiento', */
    region: 'Region',
    sector: 'Sector',
    ambito: 'Ambito',
    ref_loc: 'Referencia localizacion',
    calle: 'Calle',
    numero: 'Numero',
    localidad: 'Localidad',
    departamento: 'Departamento',
    cod_postal: 'CP',
    categoria: 'Categoria',
    estado_est: 'Estado establecimiento',
    estado_loc: 'Estado localizacion',
    telefono_cod_area: 'Cod de área',
    telefono_nro: 'Nro telefono',
    email_loc: 'Email localizacion',

}