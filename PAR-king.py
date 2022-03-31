# Codigo Creado por: David Ruiz Velazquez T2 #
# Codigo Creado por: David Ruiz Velazquez T2 #

#El programa esta hecho para que cuente tanto movimientos correctos como erroneos, pero los errorenos no se ejecutaran, en cambio estos si que saldran reflejados en la puntuacion
#El programa esta hecho para que cuente tanto movimientos correctos como erroneos, pero los errorenos no se ejecutaran, en cambio estos si que saldran reflejados en la puntuacion

#asignaccion de variables principales para la construccion de los bordes de los coches


from email import message_from_binary_file


LH  = u'\u2500' # ─ 
LV  = u'\u2502' # │ 
E1  = u'\u250C' # ┌ 
E2  = u'\u2510' # ┐ 
E3  = u'\u2514' # └ 
E4  = u'\u2518' # ┘ 
CBLH = u'\u2550' # ═ 
CBLV = u'\u2551' # ║ 
celda = u'\u2592' # ▒ 

otraPartida = True #variable de control para reiniciar o no todo el juego
empezar1 = False #variable de control para repetir si desea crear o no el fichero records

#obtiene el fichero (si no existe, o si se desea reiniciar el archivo desde 0)
def ObtencionRecords():
    f = open("records.txt","w")
    f.close()

#Se encarga de decidir si es una nueva partida o no para actualizar el archivo de records
while empezar1 != True:
    print ("si deseas emepezar desde 0 o no has jugado nunca, pulse 's' en caso contrario 'n' ")
    print("pero recuerda que si deseas comenzar de 0, se borrara todo tu progreso anterior \n")
    empezar0 = input()
    if empezar0 == 's' or empezar0 == 'n' or empezar0 == 'S' or empezar0 == 'N':
        if empezar0 == 's' or  empezar0 == 'S' :
            ObtencionRecords() #obtiene "records.txt" (en el caso de que este no exista)
            print("Bienvenido \n")
            empezar1 = True
        else: 
            print("Bienvenido de nuevo \n")
            empezar1 = True
    else: print("porfavor introduzca un valor adecuado")
    
# Funcion que lee el archivo, remueve los "\n" , y guarda el contenido en uan losta para que sea mas facil acceder
def Lectura():
    f = open("niveles.txt","r")
    listaNiveles = f.read().splitlines()
    f.close()
    return listaNiveles 

#lee el fichero record y obtiene sus elementos en una lista
def LecturaRecord():
    f = open("records.txt","r")
    listaRecords = f.read().split()
    f.close
    return listaRecords

#un salto de linea en la escritura al acabar el nivel 
def SaltoRecords(): 
    f= open("records.txt","a+")
    f.write(" ""\n") #recordar que el ultimo digito de cada record es null asi que restar -1 para no tenerlo usarlo
    f.close()

#pone al principio de la escritura la marca del nivel en el que se encuentra
def MarcaNivel():  
    f = open("records.txt","a+")
    f.write(str(nivel)) #escribe los movmientos en el record
    f.close

#Funcion que se va a encargar de escribir los records
def EscribirRecords(movimientos): 
    f = open("records.txt","a+")
    f.write(str(movimientos)) #escribe los movmientos en el record
    f.close()

#comprueba en el archivo records cual es la cabecera de nivel mas grande y decide los niveles desbloqueados

def ComprobarNivelMax():
    listado = LecturaRecord()
    cabeceraNivel = []
    if int(len(listado)) == 0:
        return 0 #si no existe la lista o esta vacia, retorna 0 al maximo nivel para que no salte un error
    for i in listado:
        cabeceraNivel.append(i[0])    #obtiene todas las cabeceras, las mete en una lista y coje el maximo nivel que se puede jugar
    lvlMax = (max(cabeceraNivel))

    return int(lvlMax)

#input para elejir el nivel que jugar

def SeleccionNivel():
    lvlTope = int(Lectura()[0])
    lvlMax = ComprobarNivelMax()+1
    continuar = False
    if lvlMax >=lvlTope: lvlMax=lvlTope #evita que deje pasar de mas niveles de los que exixten
    while continuar != True : 
        try:  #este try, se encarga de que si ponen una letra no salte un error y el programa siga normal
            nivelSelec  = int(input("Que nivel deseas jugar entre el 1 y el "+ str(lvlMax)+" \n"))
            if nivelSelec >= 1 and nivelSelec <= lvlMax :
                continuar = True
            else:  
                print("Porfavor introduzca el valor adecuado \n")
        except ValueError:
            print("Porfavor introduzca el valor adecuado \n")

    return nivelSelec

def Puntuacion():
    listado = LecturaRecord()
    puntuacion = len(listado[-1]) #-1 para empezar desde el ultimo valor escrito
    return puntuacion-1

# Obtiene donde empieza el nivel , y guarda la cantidad de coches que este contiene 

def InfoBasica(nivel):  #nivel = en el que te encuentras, se obtiene preguntando a "Seleccion de nivel()"
    lvl = nivel
    continuar = False
    veces = 0
    posicion = 1
    while continuar != True :             
        coches = int(Lectura()[posicion])
        posicion += coches + 1
        veces += 1
        if veces == lvl : 
            continuar = True
            posicion -= (coches+1)
    Info = [coches,posicion]
    return Info                   #Genera una lista, el "0" es la cantidad de coches de ese nivel, y el "1" es la posicion donde empieza ese nivel en el fichero

#Obtiene una lista con los tipos de coches que existen en el nivel seleccionado

def InfoCoches(nivel):
    lvl = nivel
    posicion = InfoBasica(lvl)[1]+1 #le sumo 1 ya que necesito la posicion del primer coche no la posicion donde empieza esta parte del fichero
    numCoches = InfoBasica(lvl)[0]
    tiposCoches = []
    tiposCoches = Lectura()[posicion:posicion+numCoches:1]
    return tiposCoches

# Se encarga de crear el tablero en forma de matriz
def GenerarTablero():
    tableroParking = []
    ladoAbajo = 23
    tamFilas = 24
    for i in range(tamFilas): #Tamaño de las filas.
        tableroParking.append([]) #LLenamos la Matriz de valores en blanco
        for j in range(40): #Tamaño de las columnas
            #El valor de las celdas tomaran el valor de "celda" que corresponde al codigo de los bordes 
            # dependiendo de las posibilidades o tamaño estas se incluyen en el if, al final hay un "else para que el resto de casos este en blanco"
            valorCelda = celda if i in [0,tamFilas] or i in [1,tamFilas] or i in [2,tamFilas] or i in [ladoAbajo,tamFilas] or i in [ladoAbajo-1,tamFilas] or i in [ladoAbajo-2,tamFilas] or j in [0,40] or j in [1,40] or j in [2,40] or j in [3,40] or j in [4,40] or j in [39,40] or j in [38,40] or j in [37,40] or j in [36,40] or j in [35,40]  else " "
            tableroParking[i].append(valorCelda) #Sustiye o escribe el valor de celda correspondiente
    #Retirar el hueco de salida, i= de col 5 a 40 , j de fila 9 a 12 para dejar justo un recuadro vacio

    for i in range(35,40):
        for j in range(9,12):  
            tableroParking[j][i] = " " 
    return tableroParking

# Se encarga de imprimir la matriz que se le asigne    
def ImprimirTablero(matriz):
    for i in matriz:
            for j in i:
                print(j, end="")
            print()

# Generar los objetos y sus elementos.
def GenElem(lista):
    tableroParking = GenerarTablero()
    Series = 0  #contador que se encargara de ver en que letra se encuentra cada coche
    for i in ListaCoches: 
        if i[0] == 'H':  #Generacion horizontal
            columnaInicioH = int(i[1])*5 #obtienen los valor de la posicion de cada coche
            tamanoH = int(i[3])*5
            finalH = tamanoH + columnaInicioH
            filaInicioH = int(i[2])*3
            for j in range(columnaInicioH+1,finalH-1):  #sumando 1 y restando 1, conseguimos dejar un hueco para las esquinas 
                tableroParking[filaInicioH][columnaInicioH] = E1  
                tableroParking[filaInicioH][finalH-1] = E2
                tableroParking[filaInicioH+2][columnaInicioH] = E3
                tableroParking[filaInicioH+2][finalH-1] = E4
                tableroParking[filaInicioH][j] = LH  # linea de arriba
                tableroParking[filaInicioH+2][j] = LH #linea de abajo
                tableroParking[filaInicioH+1][columnaInicioH] = LV  # linea izquiera
                tableroParking[filaInicioH+1][finalH-1] = LV # linea derecha
                tableroParking[filaInicioH+1][columnaInicioH+1] = numerosSerie[Series] # pone la letra mayuscula
                tableroParking[filaInicioH+1][columnaInicioH+tamanoH-2] = numerosSerie[Series+1]   #pone la letra minuscula
        else:   #Generacion vertical
            columnaInicioV  = int(i[1])*5
            tamanoV = int(i[3])*3
            filaInicioV = int(i[2])*3
            finalV = tamanoV + filaInicioV
            for j in range(filaInicioV+1,finalV-1):   #sumando 1 y restando 1, conseguimos dejar un hueco para las esquinas
                tableroParking[filaInicioV][columnaInicioV] = E1
                tableroParking[filaInicioV][columnaInicioV+4] = E2
                tableroParking[finalV-1][columnaInicioV] = E3
                tableroParking[finalV-1][columnaInicioV+4] = E4
                tableroParking[finalV-1][columnaInicioV+1] = LH
                tableroParking[finalV-1][columnaInicioV+2] = LH
                tableroParking[finalV-1][columnaInicioV+3] = LH
                tableroParking[filaInicioV][columnaInicioV+1] = LH
                tableroParking[filaInicioV][columnaInicioV+2] = LH
                tableroParking[filaInicioV][columnaInicioV+3] = LH
                tableroParking[j][columnaInicioV] = LV #linea de arriba
                tableroParking[j][columnaInicioV+4] = LV # linea de abajo
                tableroParking[filaInicioV+1][columnaInicioV+2] = numerosSerie[Series] # pone la letra mayuscula
                tableroParking[finalV-2][columnaInicioV+2] = numerosSerie[Series+1]   #pone la letra minuscula

        Series +=2 # avanca 2 posiciones en el identificador del coche para pasar al siguiente par de letras
    return tableroParking

#Actualiza la antigual lista con los valores de los coches por una nueva
def MovCol(numerosSerie): #Introducimos el abecedario 
    esLetra = False
    while esLetra != True:
        movimiento = input("Indique el siguiente movimiento = ")
        coches = InfoBasica(nivel)
        SerieCocreta = numerosSerie[0:int(coches[0])*2:1]
        for i in range(len(movimiento)):
            if movimiento[i] in SerieCocreta or movimiento[i] == '*': #deja pasar los asteriscos y los coches posibles que hay en el nivel actualmente
                esLetra = True
            else: 
                print("Alguno de los movimiento que has introducido no se corresponde con ningun coche \n")
                print("Recuerde que todos los movimientos que escribas deben de estar relacionados con alguno de los coches posibles \n")
                esLetra = False

    EscribirRecords(movimiento)


    tamano = len(movimiento)  #tamño de la secuencia de movimientos
    print("")
    BucleDeMovimiento = (x for x in range(tamano)) #asigno el tamaño a otra variable para que si la cierro se cierre el bucle sin usar break
    for i in BucleDeMovimiento:  #realiza tantos mov como caracteres tenga el input (de tamaño la nueva vaaribale para poder cerrarla en caso de mov inv)
        movimientoT = movimiento[i] #obtiene el movimiento que toque por orden de escritura.
        if movimiento[i] == '*':
            a = lista.pop()
            if a == '*':
                a = lista.pop()
            a= a.lower() if a.isupper() else a.upper()
            movimientoT = a 
            BucleDeMovimiento.close()

        if movimientoT.isupper() == False:  #Minuscula : derecha,abajo
            lista.append(movimiento[i])
            indice = int(numerosSerie.index(movimientoT)/2) #indice en el abecedario de parejas, corresponde con la lista de coches
            if indice <= len(ListaCoches): 
                cocheElej = ListaCoches[indice] #obtengo el coche en concreto para trabajar mejor con el de forma
                orientacion = cocheElej[0]
            if orientacion == 'H': #horizontal, derecha
                Hcol = int(cocheElej[1])+1 #aumenta la columan avanza
                Hlon = int(cocheElej[3]) 
                Hfil = int(cocheElej[2])
                if (Hcol+Hlon) == 8:            #colision borde derecho
                    if Hfil == 3 and Hlon ==2:
                        Hcol = int(cocheElej[1])+1  #hace que el a no colisione para que pueda salir
                        cocheSustituto =(orientacion,Hcol,Hfil,Hlon)
                        ListaCoches[indice] = cocheSustituto
                        return ListaCoches #hace return a la lista para luego decir al bucle que el coche a esta en la salida y que acabe el juego
                        BucleDeMovimiento.close()
                        
                    else: 
                        Hcol -=1  #reduce uno en el muro para no atravesarlo  <--
                        print("movimiento ",movimiento[i]," invalido, se anularan el resto escritos \n")
                        BucleDeMovimiento.close()    #para no utlizar break cierro la variable que tiene el tamaño del for por asi decirlo
                
    #Colisiones hacia la derecha
                for l in range(int(len(ListaCoches))):
                    cocheComprobar = ListaCoches[l]
                    if (Hcol+Hlon)-1 == int(cocheComprobar[1]):
                        if cocheComprobar[0] == 'H': #comprobado es horizontal
                            if Hfil == int(cocheComprobar[2]):
                                Hcol -=1
                    
                        else: # comprobado es vertical
                            if Hfil >= int(cocheComprobar[2]) and Hfil <= (int(cocheComprobar[2])+ int(cocheComprobar[3])) -1 : # -1 porque sino se pasaria uno de lon
                                Hcol -=1
                                print("movimiento ",movimiento[i]," invalido, se anularan el resto escritos \n")
                                BucleDeMovimiento.close()    #para no utlizar break cierro la variable que tiene el tamaño del for por asi decirlo

                                
                cocheSustituto =(orientacion,Hcol,Hfil,Hlon)
                ListaCoches[indice] = cocheSustituto

            else: #vertical , abajo
                Vcol = int(cocheElej[1])
                Vfil = int(cocheElej[2])+1  #aumenta la fila, baja
                Vlon = int(cocheElej[3]) 
                
                if (Vfil+Vlon) == 8:       #colision borde abajo
                    Vfil -=1  #reduce uno en el muro para no atravesarlo abajo
                    print("movimiento ",movimiento[i]," invalido, se anularan el resto escritos \n")
                    BucleDeMovimiento.close()    #para no utlizar break cierro la variable que tiene el tamaño del for por asi decirlo
        

    #Colsiones hacia abajo
                for l in range(int(len(ListaCoches))): 
                    cocheComprobar = ListaCoches[l]   
                    if (Vfil+Vlon)-1 == int(cocheComprobar[2]): #compruba si esta en la misma fila
                        if cocheComprobar[0] == 'H':
                            if Vcol >= int(cocheComprobar[1]) and Vcol <= int(cocheComprobar[1])+int(cocheComprobar[3])-1:  #compruba si misma col+long-1 ya que estaria en un valor pasado de largo)            
                                    Vfil = Vfil-1
                                    print("movimiento ",movimiento[i]," invalido, se anularan el resto escritos \n")
                                    BucleDeMovimiento.close()

                        elif Vcol == int(cocheComprobar[1]):
                            Vfil = Vfil-1
                            print("movimiento ",movimiento[i]," invalido, se anularan el resto escritos \n")
                            BucleDeMovimiento.close()
                            
                
                cocheSustituto =(orientacion,Vcol,Vfil,Vlon)
                ListaCoches[indice] = cocheSustituto


        else: #Mayuscula, izquiera, arriba
            lista.append(movimiento[i])
            indice = int(numerosSerie.index(movimientoT)/2) #indice en el abecedario de parejas, corresponde con la lista de coches
            cocheElej = ListaCoches[indice]
            orientacion = cocheElej[0]
            if orientacion == 'H': #horizontal, izquierda
                Hcol = int(cocheElej[1])-1 # disminuye la columa, retrocede
                Hfil = int(cocheElej[2])
                Hlon = int(cocheElej[3])
                if Hcol == 0:   #colision borde izquierdo
                    Hcol =+1   #añade 1 para no atravesarlo
                    print("movimiento ",movimiento[i]," invalido, se anularan el resto escritos \n")
                    BucleDeMovimiento.close()    #para no utlizar break cierro la variable que tiene el tamaño del for por asi decirlo

                for l in range(int(len(ListaCoches))): 
                    cocheComprobar = ListaCoches[l]
                    if cocheComprobar[0] == 'H':
                        if Hfil == int(cocheComprobar[2]):
                            if Hcol == int(cocheComprobar[1])+int(cocheComprobar[3])-1:
                                if cocheComprobar != cocheElej:
                                    Hcol +=1
                                    print("movimiento ",movimiento[i]," invalido, se anularan el resto escritos \n")
                                    BucleDeMovimiento.close()

                    else:
                        if Hcol == int(cocheComprobar[1]):
                            if Hfil >= int(cocheComprobar[2]) and Hfil <= int(cocheComprobar[2])+int(cocheComprobar[3])-1:    
                                Hcol +=1
                                print("movimiento ",movimiento[i]," invalido, se anularan el resto escritos \n")
                                BucleDeMovimiento.close()

                cocheSustituto =(orientacion,Hcol,Hfil,Hlon)
                ListaCoches[indice] = cocheSustituto
            else: #vertical, arriba
                Vcol = int(cocheElej[1])
                Vfil = int(cocheElej[2])-1 #disminuye la fila, sube
                Vlon = int(cocheElej[3]) 

                if Vfil == 0:  #colision borde arriba
                    Vfil =+ 1  #añade 1 para no atravesar el muro
                    print("movimiento ",movimiento[i]," invalido, se anularan el resto escritos \n")
                    BucleDeMovimiento.close()    #para no utlizar break cierro la variable que tiene el tamaño del for por asi decirlo
            
    #Colisones hacia Arriba 
                for l in range(int(len(ListaCoches))): 
                    cocheComprobar = ListaCoches[l]
                    if (cocheComprobar[0]) == 'H':
                        if Vfil == int(cocheComprobar[2]):
                            if Vcol >= int(cocheComprobar[1]) and Vcol <= int(cocheComprobar[1])+ int(cocheComprobar[3])-1:
                                Vfil +=1
                                print("movimiento ",movimiento[i]," invalido, se anularan el resto escritos \n")
                                BucleDeMovimiento.close()
                    else:
                        if Vfil == int(cocheComprobar[2]) + int(cocheComprobar[3])-1:
                            if Vcol == int(cocheComprobar[1]):
                                Vfil +=1
                                print("movimiento ",movimiento[i]," invalido, se anularan el resto escritos \n")
                                BucleDeMovimiento.close() 

                    


                cocheSustituto =(orientacion,Vcol,Vfil,Vlon)
                ListaCoches[indice] = cocheSustituto

    return ListaCoches
    # A partir de este punto comienza las ejecuciones del programa, es resto Son funciones,clases......


while otraPartida == True:

    print("")
    print("█▀█ ▄▀█ █▀█ ▄▄ █▄▀ █ █▄ █ █▀▀")
    print("█▀▀ █▀█ █▀▄    █ █ █ █ ▀█ █▄█")
    print("codigo:David Ruiz Velazquez \n")

    lista = []
    nivel = SeleccionNivel()  #input de elejir el nivel
    ListaCoches = InfoCoches(nivel)  #lista de ese nivel
    infoLvl = InfoBasica(nivel)  #  0 -> nCoches, 1 -> posicion en el array
    MarcaNivel() #pone la marca antes de escribir el movmientos
    numerosSerie = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnÑñOoPpQqRrSsTtUuVvWwXxYyZzz" #asignacion de letras a cada objeto
    ganarNivel = False
    prueba = 0
    ImprimirTablero(GenElem(ListaCoches)) #imprime el tablero inicial
    #bucle para decidir cuando finalizar el nivel
    while ganarNivel != True:
        ListaCoches = MovCol(numerosSerie)  #actualizamos la nueva lista con los nuevos movimientos
        ImprimirTablero(GenElem(ListaCoches)) #imprime con el movimiento actualizado
        cocheP = ListaCoches[0]
        if int(cocheP[1]) == 6: 
                ganarNivel = True
                SaltoRecords()

    listaRecords = LecturaRecord()
    listaNivel = []
    for c in listaRecords:
        if c[0] == str(nivel):
         listaNivel.append(c)  
    maximaP = min(listaNivel)
    maximap2 = (len(maximaP))-1
    print("Antiguo record: ",maximap2)

    puntuacion = Puntuacion()
    if puntuacion <= maximap2:
        print("Nuevo Record! : ",puntuacion)
    else: print("su puntuaccion ha sido de: ",puntuacion)

    print("█ █ █ █▀▀ ▀█▀ █▀█ █▀█ █ ▄▀█")
    print("▀▄▀ █ █▄▄  █  █▄█ █▀▄ █ █▀█")
    print("Codigo:David Ruiz Velazquez \n")
    print("")

    #Bucle para jugar o no otra partida seguido
    oGameC = False
    while oGameC == False:
        oGame = input("Si deseas jugar de nuevo pulse 's' en caso contrario 'n': ")
        if oGame == 's' or oGame == 'N' or oGame == 'n' or oGame == 'S':
            if oGame == 'N' or oGame == 'n':
                otraPartida = False
                oGameC = True
                print("\nPartida Terminada")
            else: oGameC = True
        else:
            print("porfavor introduzca los valores adecuados")



#El programa esta hecho para que cuente tanto movimientos correctos como erroneos, pero los errorenos no se ejecutaran, en cambio estos si que saldran reflejados en la puntuacion
#El programa esta hecho para que cuente tanto movimientos correctos como erroneos, pero los errorenos no se ejecutaran, en cambio estos si que saldran reflejados en la puntuacion
            