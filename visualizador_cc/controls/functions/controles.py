

from ast import Constant


class Constant:
    NO_ERROR = 0
    ERROR = 1
    WARNING = 2


class MatriculaComunIncialControl():

    def precocidad(row): 

        if(row['sala'] == "Sala de 3 años"):
            if(row["menos_1_anio"] > 0
                or row["un_anio"] > 0
                    or row["dos_anios"] > 0): 
                        return Constant.ERROR

        if(row['sala'] == "Sala de 4 años"):
            if(row["menos_1_anio"] > 0
                or row["un_anio"] > 0
                    or row["dos_anios"] > 0                               
                        or row["tres_anios"] > 0):
                            return Constant.ERROR

        if(row['sala'] == "Sala de 5 años"):
            if(row["menos_1_anio"] > 0
                or row["un_anio"] > 0
                    or row["dos_anios"] > 0                               
                        or row["tres_anios"] > 0
                            or row["cuatro_anios"] > 0):                                     
                                return Constant.ERROR


        return Constant.NO_ERROR 

    def sobreedad(row):

        count = 0

        if(row['sala'] == "Sala de 3 anios"):
            if(row["cuatro_anios"] > 0
                or row["cinco_anios"] > 0
                    or row["seis_anios"] > 0):
                        return Constant.WARNING

        if(row['sala'] == "Sala de 4 anios"):
            if(row["cinco_anios"] > 0
                or row["seis_anios"] > 0):
                    return Constant.WARNING

        if(row['sala'] == "Sala de 5 anios"):
            if(row["seis_anios"] > 0):
                return Constant.WARNING


        return Constant.NO_ERROR


class MatriculaComunPrimariaControl():

    def precocidad(row): 

        if(row['grado_anio'] == "1er Año/Grado"):#6
            if(row["edad_5"] > 0): 
                return Constant.ERROR

        if(row['grado_anio'] == "2do Año/Grado"):#7
            if(row["edad_5"] > 0
                or row["edad_6"] > 0):                 
                    return Constant.ERROR

        if(row['grado_anio'] == "3er Año/Grado"):#8
            if(row["edad_5"] > 0
                or row["edad_6"] > 0
                    or row["edad_7"] > 0):             
                        return Constant.ERROR

        if(row['grado_anio'] == "4to Año/Grado"):#9
            if(row["edad_5"] > 0
                or row["edad_6"] > 0
                    or row["edad_7"] > 0                
                        or row["edad_8"] > 0):             
                            return Constant.ERROR

        if(row['grado_anio'] == "5to Año/Grado"):#10
            if(row["edad_5"] > 0
                or row["edad_6"] > 0
                  or row["edad_7"] > 0
                    or row["edad_8"] > 0
                        or row["edad_9"] > 0):             
                            return Constant.ERROR

        if(row['grado_anio'] == "6to Año/Grado"):#11
            if(row["edad_5"] > 0
                or row["edad_6"] > 0
                    or row["edad_7"] > 0
                        or row["edad_8"] > 0
                            or row["edad_9"] > 0
                                or row["edad_10"] > 0):             
                                    return Constant.ERROR

        if(row['grado_anio'] == "7mo Año/Grado"):#12
            if(row["edad_5"] > 0
                or row["edad_6"] > 0
                    or row["edad_7"] > 0
                        or row["edad_8"] > 0
                            or row["edad_9"] > 0
                                or row["edad_10"] > 0
                                    or row["edad_11"] > 0):             
                                        return Constant.ERROR



        return Constant.NO_ERROR 

    def sobreedad(row):
      
        if(row['grado_anio'] == "1er Año/Grado"):#6
            if(row["edad_7"] > 0
                or row["edad_8"] > 0
                    or row["edad_9"] > 0
                        or row["edad_10"] > 0
                            or row["edad_11"] > 0
                                or row["edad_12"] > 0
                                    or row["edad_13"] > 0
                                        or row["edad_14"] > 0
                                            or row["edad_15"] > 0
                                                or row["edad_16"] > 0
                                                    or row["edad_17"] > 0
                                                        or row["edad_18_y_mas"] > 0):                 
                                                            return Constant.WARNING

        if(row['grado_anio'] == "2do Año/Grado"):#7
            if(row["edad_8"] > 0
                or row["edad_9"] > 0
                    or row["edad_10"] > 0
                        or row["edad_11"] > 0
                            or row["edad_12"] > 0
                                or row["edad_13"] > 0
                                    or row["edad_14"] > 0
                                        or row["edad_15"] > 0
                                            or row["edad_16"] > 0
                                                or row["edad_17"] > 0
                                                    or row["edad_18_y_mas"] > 0):                 
                                                        return Constant.WARNING

        if(row['grado_anio'] == "3er Año/Grado"):#8
            if(row["edad_9"] > 0
                or row["edad_10"] > 0
                    or row["edad_11"] > 0
                        or row["edad_12"] > 0
                            or row["edad_13"] > 0
                                or row["edad_14"] > 0
                                    or row["edad_15"] > 0
                                        or row["edad_16"] > 0
                                            or row["edad_17"] > 0
                                                or row["edad_18_y_mas"] > 0):                 
                                                    return Constant.WARNING

        if(row['grado_anio'] == "4to Año/Grado"):#9
            if(row["edad_10"] > 0
                or row["edad_11"] > 0
                    or row["edad_12"] > 0
                        or row["edad_13"] > 0
                            or row["edad_14"] > 0
                                or row["edad_15"] > 0
                                    or row["edad_16"] > 0
                                        or row["edad_17"] > 0
                                            or row["edad_18_y_mas"] > 0):                 
                                                return Constant.WARNING

        if(row['grado_anio'] == "5to Año/Grado"):#10
            if(row["edad_11"] > 0
                or row["edad_12"] > 0
                    or row["edad_13"] > 0
                        or row["edad_14"] > 0
                            or row["edad_15"] > 0
                                or row["edad_16"] > 0
                                    or row["edad_17"] > 0
                                        or row["edad_18_y_mas"] > 0):                 
                                            return Constant.WARNING


        if(row['grado_anio'] == "6to Año/Grado"):#11
            if(row["edad_12"] > 0
                or row["edad_13"] > 0
                    or row["edad_14"] > 0
                        or row["edad_15"] > 0
                            or row["edad_16"] > 0
                                or row["edad_17"] > 0
                                    or row["edad_18_y_mas"] > 0):                 
                                        return Constant.WARNING

        if(row['grado_anio'] == "7mo Año/Grado"):#12
            if(row["edad_13"] > 0
                or row["edad_14"] > 0
                    or row["edad_15"] > 0
                        or row["edad_16"] > 0
                            or row["edad_17"] > 0
                                or row["edad_18_y_mas"] > 0):                 
                                    return Constant.WARNING

        return Constant.NO_ERROR

    def repitencia(row):
      
        if(row['grado_anio'] == "1er Año/Grado"):#6
            if(row["total_rep"] > 0):
                Constant.ERROR       

        if(row['grado_anio'] == "2do Año/Grado"):#7
            if(row["total_rep"] > 0):
                Constant.ERROR   

        if(row['grado_anio'] == "3er Año/Grado"):#7
            if(row["total_rep"] > 0):
                Constant.ERROR  

        return Constant.NO_ERROR




class MatriculaComunSecundariaControl():

    def precocidad(row):        
    
        if(row['anio_est'] == "1er Año/Grado"):#13
            if(row["edad_11_y_menos"] > 0
                or row["edad_12"] > 0):                 
                return Constant.ERROR

        if(row['anio_est'] == "2do Año/Grado"):#14
            if(row["edad_11_y_menos"] > 0
                or row["edad_12"] > 0
                    or row["edad_13"] > 0):                 
                        return Constant.ERROR    

        if(row['anio_est'] == "3er Año/Grado"):#15
            if(row["edad_11_y_menos"] > 0
                or row["edad_12"] > 0
                    or row["edad_13"] > 0
                        or row["edad_14"] > 0):                 
                            return Constant.ERROR 

        if(row['anio_est'] == "4to Año/Grado"):#16
            if(row["edad_11_y_menos"] > 0
                or row["edad_12"] > 0
                    or row["edad_13"] > 0
                        or row["edad_14"] > 0
                            or row["edad_15"] > 0):                 
                                return Constant.ERROR   

        if(row['anio_est'] == "5to Año/Grado"):#17
            if(row["edad_11_y_menos"] > 0
                or row["edad_12"] > 0
                    or row["edad_13"] > 0
                        or row["edad_14"] > 0
                            or row["edad_15"] > 0
                                or row["edad_16"] > 0):                 
                                    return Constant.ERROR                         

        return Constant.NO_ERROR 



    def sobreedad(row):  

        if(row['anio_est'] == "1er Año/Grado"):#13
            if(row["edad_14"] > 0
                or row["edad_15"] > 0
                    or row["edad_16"] > 0
                        or row["edad_17"] > 0
                            or row["edad_18"] > 0
                                or row["edad_19"] > 0
                                    or row["edad_20_24"] > 0                                    
                                        or row["edad_25_y_mas"] > 0):                 
                                            return Constant.WARNING   

        if(row['anio_est'] == "2do Año/Grado"):#14
            if(row["edad_15"] > 0
                or row["edad_16"] > 0
                    or row["edad_17"] > 0
                        or row["edad_18"] > 0
                            or row["edad_19"] > 0
                                or row["edad_20_24"] > 0
                                    or row["edad_25_y_mas"] > 0):                 
                                        return Constant.WARNING   

        if(row['anio_est'] == "3er Año/Grado"):#15
            if(row["edad_16"] > 0
                or row["edad_17"] > 0
                    or row["edad_18"] > 0
                        or row["edad_19"] > 0
                            or row["edad_20_24"] > 0
                                or row["edad_25_y_mas"] > 0):                 
                                    return Constant.WARNING          

        if(row['anio_est'] == "4to Año/Grado"):#16
            if(row["edad_17"] > 0
                or row["edad_18"] > 0
                    or row["edad_19"] > 0
                        or row["edad_20_24"] > 0
                            or row["edad_25_y_mas"] > 0):                 
                                return Constant.WARNING   

        if(row['anio_est'] == "5to Año/Grado"):#17
            if(row["edad_18"] > 0
                or row["edad_19"] > 0
                    or row["edad_20_24"] > 0
                        or row["edad_25_y_mas"] > 0):                 
                            return Constant.WARNING       

        return Constant.NO_ERROR                                      

      

