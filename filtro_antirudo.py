# Make sure to have the server side running in CoppeliaSim: 
# in a child script of a CoppeliaSim scene, add following command
# to be executed just once, at simulation start:
#
# simRemoteApi.start(19999)
#
# then start simulation, and run this program.
#
# IMPORTANT: for each successful call to simxStart, there
# should be a corresponding call to simxFinish at the end!
try:
    import sim
except:
    print ('--------------------------------------------------------------')
    print ('"sim.py" could not be imported. This means very probably that')
    print ('either "sim.py" or the remoteApi library could not be found.')
    print ('Make sure both are in the same folder as this file,')
    print ('or appropriately adjust the file "sim.py"')
    print ('--------------------------------------------------------------')
    print ('')

import time
import random
import matplotlib.pyplot as plt
from robot_filtro import Robot


def obtener_los_manejadores(clientID):
    manejadores=[0,0,0,0,0,0,0,0,0,0,0,0,0]
    returnCode,manejadores[0]=sim.simxGetObjectHandle(clientID,'Pioneer_p3dx_nuevo',sim.simx_opmode_blocking)
    if(returnCode!=sim.simx_return_ok): print("Pioneer_p3dx_nuevo! no encontrado")

    returnCode,manejadores[1]=sim.simxGetObjectHandle(clientID,'robot_pose',sim.simx_opmode_blocking)
    if(returnCode!=sim.simx_return_ok): print("robot_pose! no encontrado")

    returnCode,manejadores[2]=sim.simxGetObjectHandle(clientID,'Pioneer_p3dx_leftMotor',sim.simx_opmode_blocking)
    if(returnCode!=sim.simx_return_ok): print("Pioneer_p3dx_leftMotor! no encontrado")

    returnCode,manejadores[3]=sim.simxGetObjectHandle(clientID,'Pioneer_p3dx_rightMotor',sim.simx_opmode_blocking)
    if(returnCode!=sim.simx_return_ok): print("Pioneer_p3dx_rightMotor! no encontrado")

    #returnCode,manejadores[4]=sim.simxGetObjectHandle(clientID,'GPS_version_actual',sim.simx_opmode_blocking)
    #if(returnCode!=sim.simx_return_ok): print("GPS_version_actual! no encontrado")

    returnCode,manejadores[5]=sim.simxGetObjectHandle(clientID,'Pioneer_p3dx_caster_freeJoint1',sim.simx_opmode_blocking)
    if(returnCode!=sim.simx_return_ok): print("Pioneer_p3dx_caster_freeJoint1! no encontrado")

    returnCode,manejadores[6]=sim.simxGetObjectHandle(clientID,'fastHokuyo',sim.simx_opmode_blocking)
    if(returnCode!=sim.simx_return_ok): print("fastHokuyo! no encontrado")

    returnCode,manejadores[7]=sim.simxGetObjectHandle(clientID,'Pioneer_p3dx_visible',sim.simx_opmode_blocking)
    if(returnCode!=sim.simx_return_ok): print("fastHokuyo! no encontrado")

    returnCode,manejadores[8]=sim.simxGetObjectHandle(clientID,'Pioneer_p3dx_leftWheel',sim.simx_opmode_blocking)
    if(returnCode!=sim.simx_return_ok): print("Pioneer_p3dx_leftWheel! no encontrado")

    returnCode,manejadores[9]=sim.simxGetObjectHandle(clientID,'Pioneer_p3dx_rightWheel',sim.simx_opmode_blocking)
    if(returnCode!=sim.simx_return_ok): print("Pioneer_p3dx_righttWheel! no encontrado")

    returnCode,manejadores[10]=sim.simxGetObjectHandle(clientID,'Pioneer_p3dx_caster_link',sim.simx_opmode_blocking)
    if(returnCode!=sim.simx_return_ok): print("Pioneer_p3dx_leftWheel! no encontrado")

    returnCode,manejadores[11]=sim.simxGetObjectHandle(clientID,'Pioneer_p3dx_caster_wheel',sim.simx_opmode_blocking)
    if(returnCode!=sim.simx_return_ok): print("Pioneer_p3dx_caster_wheel! no encontrado")

    return manejadores


def obtener_posicion_inicial(manejadores):
    position=[0,0,0,0,0,0,0,0,0,0,0,0,0]

    returnCode,position[0]=sim.simxGetObjectPosition(clientID,manejadores[0],-1, sim.simx_opmode_blocking)
    if(returnCode!=sim.simx_return_ok): print("Pioneer_p3dx_nuevo! posicion no obtenida")

    returnCode,position[1]=sim.simxGetObjectPosition(clientID,manejadores[1],manejadores[0], sim.simx_opmode_blocking)
    if(returnCode!=sim.simx_return_ok): print("robot_pose! posicion no obtenida")

    returnCode,position[2]=sim.simxGetObjectPosition(clientID,manejadores[2],manejadores[0], sim.simx_opmode_blocking)
    if(returnCode!=sim.simx_return_ok): print("Pioneer_p3dx_leftMotor! posicion no obtenida")

    returnCode,position[3]=sim.simxGetObjectPosition(clientID,manejadores[3],manejadores[0], sim.simx_opmode_blocking)
    if(returnCode!=sim.simx_return_ok): print("Pioneer_p3dx_rightMotor! posicion no obtenida")

    returnCode,position[4]=sim.simxGetObjectPosition(clientID,manejadores[4],manejadores[0], sim.simx_opmode_blocking)
    if(returnCode!=sim.simx_return_ok): print("GPS_version_actual! posicion no obtenida")

    returnCode,position[5]=sim.simxGetObjectPosition(clientID,manejadores[5],manejadores[0], sim.simx_opmode_blocking)
    if(returnCode!=sim.simx_return_ok): print("Pioneer_p3dx_caster_freeJoint1! posicion no obtenida")

    returnCode,position[6]=sim.simxGetObjectPosition(clientID,manejadores[6],manejadores[0], sim.simx_opmode_blocking)
    if(returnCode!=sim.simx_return_ok): print("fastHokuyo! posicion no obtenida")

    returnCode,position[7]=sim.simxGetObjectPosition(clientID,manejadores[7],manejadores[0], sim.simx_opmode_blocking)
    if(returnCode!=sim.simx_return_ok): print("fastHokuyo! posicion no obtenida")

    returnCode,position[8]=sim.simxGetObjectPosition(clientID,manejadores[8],manejadores[0], sim.simx_opmode_blocking)
    if(returnCode!=sim.simx_return_ok): print("Pioneer_p3dx_leftWheel! posicion no obtenida")

    returnCode,position[9]=sim.simxGetObjectPosition(clientID,manejadores[9],manejadores[0], sim.simx_opmode_blocking)
    if(returnCode!=sim.simx_return_ok): print("Pioneer_p3dx_rightWheel! posicion no obtenida")

    returnCode,position[10]=sim.simxGetObjectPosition(clientID,manejadores[10],manejadores[0], sim.simx_opmode_blocking)
    if(returnCode!=sim.simx_return_ok): print("Pioneer_p3dx_caster_link! posicion no obtenida")

    returnCode,position[11]=sim.simxGetObjectPosition(clientID,manejadores[11],manejadores[0], sim.simx_opmode_blocking)
    if(returnCode!=sim.simx_return_ok): print("Pioneer_p3dx_caster_wheel! posicion no obtenida")

    returnCode,position[12]=sim.simxGetObjectOrientation(clientID,manejadores[0],-1,sim.simx_opmode_blocking)

    return position

def inicializar_poblacion(tamanio,rango_q,rango_c,rango_r,rango_e):
    #robots=[0,0,0,0,0,0,0,0,0,0]
    robots=[]
    for i in range(tamanio):
        robots.append(Robot(rango_q,rango_c,rango_r,rango_e))
    return robots

def escojer_el_mejor(robots):
    #print("-----------------------comprobando que escojemos el mejor indice--------------------------")
    menor_fitness = robots[0].get_fitness_actual_del_robot()
    indice_de_mayor_fitness=0
    #print("inicializamos el menor fitness por defecto como el primero :",robots[0].fitness)
    for i in range(len(robots)):
        #print("robots[",i,"].fitness :",robots[i].fitness)
        #print("menor_fitness",menor_fitness)
        if(robots[i].get_fitness_actual_del_robot() < menor_fitness ):
            indice_de_mayor_fitness=i
            menor_fitness=robots[i].get_fitness_actual_del_robot()

    return indice_de_mayor_fitness

def escojer_individuo_con_mejor_media(robots,cantidad_de_fitness_pasados_almacenados):
    #La mejor media es la media mas pequeña
    mejor_media=0
    indice_de_la_mejor_media=0
    #inicializamos como mejor media la primera media que encontremos
    for i in range(len(robots)):
        if(robots[i].indice_actual_fitness==(cantidad_de_fitness_pasados_almacenados-1)):
            mejor_media=robots[i].media_de_fitness()
            indice_de_la_mejor_media=i
            break
    #seguimos buscando para verificar si hay una media mejor que la que inicializamos
    while i <len(robots):
        if(robots[i].indice_actual_fitness==(cantidad_de_fitness_pasados_almacenados-1)):
            media=robots[i].media_de_fitness()
            print("media de robots[",i,"] :",media)
            if(media<mejor_media):
                indice_de_la_mejor_media=i
                mejor_media=media
        i=i+1
    return indice_de_la_mejor_media

def crossover_delta(indice_del_mejor,robots,tasa_de_mutacion,rango_q,rango_c,rango_r,rango_e):
    robots_nueva_generacion=[0,0,0,0,0,0,0,0,0,0]
    suma_o_resta=[1,-1]
    for i in range(len(robots)):
        if(indice_del_mejor!=i):
            delta_q=abs(robots[indice_del_mejor].epsilon_q-robots[i].epsilon_q)/2
            delta_c=abs(robots[indice_del_mejor].epsilon_c-robots[i].epsilon_c)/2
            delta_r=abs(robots[indice_del_mejor].epsilon_r-robots[i].epsilon_r)/2
            delta_e=abs(robots[indice_del_mejor].e-robots[i].e)/2
            #print("robots[indice_del_mejor].epsilon_q : ",robots[indice_del_mejor].epsilon_q,"robots[",i,"].epsilon_q",robots[i].epsilon_q)
            #print("robots[indice_del_mejor].epsilon_c : ",robots[indice_del_mejor].epsilon_c,"robots[",i,"].epsilon_c",robots[i].epsilon_c)
            #print("robots[indice_del_mejor].epsilon_r : ",robots[indice_del_mejor].epsilon_r,"robots[",i,"].epsilon_r",robots[i].epsilon_r)
            #print("robot cruzado : epsilon_q ->",q," , epsilon_c ->",c," , epsilon_r ->",r)
            #print("hago crossover en la posicion : ", i)
            #print("nuevo individiduo despues de pasarle los valores -> robots[i].epsilon_q :",robots[i].epsilon_q,"robots[i].epsilon_c:",robots[i].epsilon_c,"robots[i].epsilon_r",robots[i].epsilon_r)

            #si es menor a 0.9 sumamos o restamos el delta a la madre, el porcentaje para la madre es mas grande porque el padre siempre sera
            #el mismo, por lo que tendra un mayor numero de oportunidades de salir elegido
            if(random.random()<0.9):
                q=robots[i].epsilon_q+(random.choice(suma_o_resta)*delta_q)
                c=robots[i].epsilon_c+(random.choice(suma_o_resta)*delta_c)
                r=robots[i].epsilon_r+(random.choice(suma_o_resta)*delta_r)
                e=robots[i].e+(random.choice(suma_o_resta)*delta_e)
            #si es mayor a 0.5 sumamos o restamos el delta al padre (consideraremos al padre como el mejor de todos)
            else:
                q=robots[indice_del_mejor].epsilon_q+(random.choice(suma_o_resta)*delta_q)
                c=robots[indice_del_mejor].epsilon_c+(random.choice(suma_o_resta)*delta_c)
                r=robots[indice_del_mejor].epsilon_r+(random.choice(suma_o_resta)*delta_r)
                e=robots[indice_del_mejor].e+(random.choice(suma_o_resta)*delta_e)

            #----------------------------------------------------------mutacion---------------------------------------------------------------
            probabilidad=[1,1,1,1,1,1,1,1,2,2]
            cantidad_de_genes_a_mutar=random.choice(probabilidad)
            elegir_cual_mutar=[1,2,3,4]
            for i in range(cantidad_de_genes_a_mutar):
                    eleccion=random.choice(elegir_cual_mutar)
                    #muta epsilon_q
                    if(eleccion==1):
                        q=q+(tasa_de_mutacion*rango_q*random.choice(suma_o_resta))
                        elegir_cual_mutar.remove(1)
                    #muta epsilon_c
                    elif(eleccion==2):
                        c=c+(tasa_de_mutacion*rango_c*random.choice(suma_o_resta))
                        elegir_cual_mutar.remove(2)
                    #muta epsilon_r
                    elif(eleccion==3):
                        r=r+(tasa_de_mutacion*rango_r*random.choice(suma_o_resta))
                        elegir_cual_mutar.remove(3)
                    elif(eleccion==3):
                        e=e+(tasa_de_mutacion*rango_e*random.choice(suma_o_resta))
                        elegir_cual_mutar.remove(4)

            robots[i].pasar_valores_de_crossover(q,c,r,e)
        else:
            print("No hago nada en el mejor de esta generacion: ", i)
            #print("El mejor individiduo no cambia -> robots[",i,"].epsilon_q :",robots[i].epsilon_q,"robots[",i,"].epsilon_c:",robots[i].epsilon_c,"robots[",i,"].epsilon_r",robots[i].epsilon_r)

    return robots


def crossover_mejor_transa_con_todos(indice_del_mejor,robots,tasa_de_mutacion,rango_q,rango_c,rango_r,rango_e):
    robots_nueva_generacion=[0,0,0,0,0,0,0,0,0,0]
    suma_o_resta=[1,-1]
    for i in range(len(robots)):
        if(indice_del_mejor!=i):
            q=(robots[indice_del_mejor].epsilon_q+robots[i].epsilon_q)/2
            c=(robots[indice_del_mejor].epsilon_c+robots[i].epsilon_c)/2
            r=(robots[indice_del_mejor].epsilon_r+robots[i].epsilon_r)/2
            e=(robots[indice_del_mejor].e+robots[i].e)/2
            #----------------------------------------------------------mutacion---------------------------------------------------------------
            probabilidad=[1,1,1,1,1,1,1,1,2,2]
            cantidad_de_genes_a_mutar=random.choice(probabilidad)
            elegir_cual_mutar=[1,2,3,4]
            for j in range(cantidad_de_genes_a_mutar):
                    eleccion=random.choice(elegir_cual_mutar)
                    #muta epsilon_q
                    if(eleccion==1):
                        q=q+(tasa_de_mutacion*rango_q*random.choice(suma_o_resta))
                        elegir_cual_mutar.remove(1)
                    #muta epsilon_c
                    elif(eleccion==2):
                        c=c+(tasa_de_mutacion*rango_c*random.choice(suma_o_resta))
                        elegir_cual_mutar.remove(2)
                    #muta epsilon_r
                    elif(eleccion==3):
                        r=r+(tasa_de_mutacion*rango_r*random.choice(suma_o_resta))
                        elegir_cual_mutar.remove(3)
                    elif(eleccion==4):
                        e=e+(tasa_de_mutacion*rango_e*random.choice(suma_o_resta))
                        elegir_cual_mutar.remove(4)

            robots[i].pasar_valores_de_crossover(q,c,r,e)
        else:
            print("No hago nada en el mejor de esta generacion: ", i)
            #print("El mejor individiduo no cambia -> robots[",i,"].epsilon_q :",robots[i].epsilon_q,"robots[",i,"].epsilon_c:",robots[i].epsilon_c,"robots[",i,"].epsilon_r",robots[i].epsilon_r)

    return robots

def crossover_mejor_transa_con_todos_con_filtro(indice_de_la_mejor_media,robots,tasa_de_mutacion,rango_q,rango_c,rango_r,rango_e):
    robots_nueva_generacion=[0,0,0,0,0,0,0,0,0,0]
    suma_o_resta=[1,-1]
    mejor_media=robots[indice_de_la_mejor_media].media_de_fitness()
    for i in range(len(robots)):
        if(mejor_media<robots[i].get_fitness_actual_del_robot() and i!=indice_de_la_mejor_media):
            q=(robots[indice_de_la_mejor_media].epsilon_q+robots[i].epsilon_q)/2
            c=(robots[indice_de_la_mejor_media].epsilon_c+robots[i].epsilon_c)/2
            r=(robots[indice_de_la_mejor_media].epsilon_r+robots[i].epsilon_r)/2
            e=(robots[indice_de_la_mejor_media].e+robots[i].e)/2
            #----------------------------------------------------------mutacion---------------------------------------------------------------
            probabilidad=[1,1,1,1,1,1,1,1,2,2]
            cantidad_de_genes_a_mutar=random.choice(probabilidad)
            elegir_cual_mutar=[1,2,3,4]
            for j in range(cantidad_de_genes_a_mutar):
                    eleccion=random.choice(elegir_cual_mutar)
                    #muta epsilon_q
                    if(eleccion==1):
                        q=q+(tasa_de_mutacion*rango_q*random.choice(suma_o_resta))
                        elegir_cual_mutar.remove(1)
                    #muta epsilon_c
                    elif(eleccion==2):
                        c=c+(tasa_de_mutacion*rango_c*random.choice(suma_o_resta))
                        elegir_cual_mutar.remove(2)
                    #muta epsilon_r
                    elif(eleccion==3):
                        r=r+(tasa_de_mutacion*rango_r*random.choice(suma_o_resta))
                        elegir_cual_mutar.remove(3)
                    elif(eleccion==4):
                        e=e+(tasa_de_mutacion*rango_e*random.choice(suma_o_resta))
                        elegir_cual_mutar.remove(4)

            robots[i].pasar_valores_de_crossover(q,c,r,e)
            print("Si transa : ", i)
            print("probamos ver si se reseteo el array de fitness",robots[i].array_fitness_anteriores)
        else:
            print("No transa ya que su fitness actual es mejor que la media del mejor o talves es la mejor media: ", i)
            print("debe quedarse con todo el array de fitness",robots[i].array_fitness_anteriores)
            #print("El mejor individiduo no cambia -> robots[",i,"].epsilon_q :",robots[i].epsilon_q,"robots[",i,"].epsilon_c:",robots[i].epsilon_c,"robots[",i,"].epsilon_r",robots[i].epsilon_r)

    return robots

def predacion_randomica(indice_de_individuo_con_mejor_media,robots,rango_q,rango_c,rango_r,rango_e):
    #el mayor fitnes es el peor fitness
    
    if(indice_de_individuo_con_mejor_media==0):
        mayor_fitness = robots[1].get_fitness_actual_del_robot()
        indice_de_mayor_fitness=1
    else:
        mayor_fitness = robots[0].get_fitness_actual_del_robot()
        indice_de_mayor_fitness=0

    
    for i in range(len(robots)):
        if(robots[i].get_fitness_actual_del_robot() > mayor_fitness and i!=indice_de_individuo_con_mejor_media):
            indice_de_mayor_fitness=i
            mayor_fitness=robots[i].get_fitness_actual_del_robot()

    epsilon_q=random.uniform(0,rango_q)
    epsilon_c=random.uniform(0,rango_c)
    epsilon_r=random.uniform(0,rango_r)
    e=random.uniform(0,rango_e)
    robots[indice_de_mayor_fitness].pasar_valores_de_crossover(epsilon_q,epsilon_c,epsilon_r,e)
    return robots

    #tirar punos en cada colision
    #parametro que mide cuanta iteraciones que el llego para llegar al destino f(x)=numero de generaciones -numero de colisiones+tiempo
    #

sim.simxFinish(-1) # just in case, close all opened connections
#clientID=sim.simxStart('127.0.0.1',19999,True,True,5000,5) # Connect to CoppeliaSim
#print('clienteID : ',clientID)
clientID=0
if clientID!=-1:
    print ('Connected to remote API server')

#--------------------------------------Algoritmo evolutivo--------------------------------------------------------------------------------
    # Now retrieve streaming data (i.e. in a non-blocking fashion):
    
    #startTime=time.time()
    #sim.simxGetIntegerParameter(clientID,sim.sim_intparam_mouse_x,sim.simx_opmode_streaming) # Initialize streaming
    #while time.time()-startTime < 5:
        #returnCode,data=sim.simxGetIntegerParameter(clientID,sim.sim_intparam_mouse_x,sim.simx_opmode_buffer) # Try to retrieve the streamed data
        #if returnCode==sim.simx_return_ok: # After initialization of streaming, it will take a few ms before the first value arrives, so check the return code
        #    print ('Mouse position x: ',data) # Mouse position x is actualized when the cursor is over CoppeliaSim's window

    #obtenemos el destino a donde queremos llegar
    #destino=[0,0]
    #returnCode,destino[0]=sim.simxGetFloatSignal(clientID,"x_destino",sim.simx_opmode_blocking)
    #returnCode,destino[1]=sim.simxGetFloatSignal(clientID,"y_destino",sim.simx_opmode_blocking)
    #print("destino(x,y) = ",destino)

    #obtenemos los manejadores de los objetos de la escena
    #manejadores=[0,0,0,0,0,0,0,0,0,0,0]
    #manejadores=obtener_los_manejadores()
    #sim.simxFinish(clientID)
    #obtenemos la posicion de donde los robots empezaran a desplazarse
    #pos_ini=[0,0,0,0,0,0,0,0,0,0,0,0]
    #pos_ini=obtener_posicion_inicial(manejadores)
    #print(pos_ini)
    #tamanio inicial de la poblacion
    tamanio_poblacion=10

    #inicializamos la semilla para los numeros aletorios
    random.seed()

    #rango de cada gen
    rango_q=5
    rango_c=5
    rango_r=5
    rango_e=2

    #inicializamos la poblacion
    #robots=[0,0,0,0,0,0,0,0,0,0]
    robots = inicializar_poblacion(tamanio_poblacion,rango_q,rango_c,rango_r,rango_e)

    #array que guarda el mejor de cada generacion
    mejor_de_cada_generacion=[]
    lista_de_media_de_todas_las_generaciones=[]

    #enviamos la informacion para que gire o haga campos pontenciales
    #returnCode=sim.simxSetFloatSignal(clientID,"girar",0,sim.simx_opmode_oneshot)

    #tasa de mutacion inicial
    tasa_de_mutacion=0.02 #empezamos con 2% de mutacion inicial

    #almacena el indicie del mejor individuo con mejor media de cada generacion
    indice_de_individuo_con_mejor_media=-1

    #bandera le indica al algoritmo cuando debe detenerse
    bandera=0
    max_it=500
    tiempo_de_sleep=10
    periodo_de_predacion=10
    contador_para_predacion=0

    #cantidad de fitness pasados que vamos a almacenar para evitar el ruido
    cantidad_de_fitness_pasados_almacenados=5

    periodo_de_aumento_de_tasa_de_mutacion=10
    contador_para_aumentar_la_tasa_de_mutacion=0
    #suponemos el peor fitness posible para la inicializacion de la generacion -1, de tal forma que la geracion 0 sea siempre mejor que esta
    fitness_de_generacion_anterior=9999999
    q_anterior=-1
    c_anterior=-1
    e_anterior=-1
    r_anterior=-1
    #en este archivo guardaremos los datos del mejor individuo y el individuo promedio de cada 

    #---------------returnCode=sim.simxStartSimulation(clientID,sim.simx_opmode_oneshot)
    while bandera<max_it:
        media_de_la_generacion=0
        bandera=bandera+1
        print("----------------------------------------------------Generacion ",bandera,"----------------------------------------------------")
        
        #-------------Evaluamos el fitness para cada individuo dentro de una misma generacion----------------------- 
        #robots[0].resetear(pos_ini,manejadores)
        for i in range(tamanio_poblacion):
            #print("prueba de quien es la mejor media",indice_de_individuo_con_mejor_media)
            if(True):#indice_del_mejor!=i or indice_del_mejor==i):
                clientID=sim.simxStart('127.0.0.1',19999,True,True,5000,5)
                returnCode=sim.simxStartSimulation(clientID,sim.simx_opmode_blocking)
                manejadores=[0,0,0,0,0,0,0,0,0,0,0]
                manejadores=obtener_los_manejadores(clientID)
                #asignamos 0 a girar siempre porque aveces se queda guardado en la memoria el numero 1 en girar y el programa se bugea
                returnCode=sim.simxSetFloatSignal(clientID,"girar",0,sim.simx_opmode_blocking)
                destino=[0,0]
                returnCode,destino[0]=sim.simxGetFloatSignal(clientID,"x_destino",sim.simx_opmode_blocking)
                returnCode,destino[1]=sim.simxGetFloatSignal(clientID,"y_destino",sim.simx_opmode_blocking)
                #print("destino(x,y) = ",destino)
                
                returnCode=sim.simxSetFloatSignal(clientID,"resetear_simulacion",0,sim.simx_opmode_blocking)
                #robots[i].resetear(pos_ini,manejadores)
                print("Generacion",bandera,"individuo: ",i,"*************************")
                
                returnCode=sim.simxSetFloatSignal(clientID,"ep_q",robots[i].epsilon_q,sim.simx_opmode_blocking)
                #returnCode=sim.simxSetFloatSignal(clientID,"ep_q",0.9884107509984599,sim.simx_opmode_blocking)
                #print("epsilon_q ->",robots[i].epsilon_q)
                returnCode=sim.simxSetFloatSignal(clientID,"ep_c",robots[i].epsilon_c,sim.simx_opmode_blocking)
                #returnCode=sim.simxSetFloatSignal(clientID,"ep_c",3.4980021117665725,sim.simx_opmode_blocking)
                #print("epsilon_c ->",robots[i].epsilon_c)
                returnCode=sim.simxSetFloatSignal(clientID,"ep_r",robots[i].epsilon_r,sim.simx_opmode_blocking)
                #returnCode=sim.simxSetFloatSignal(clientID,"ep_r",2.8366462956165095,sim.simx_opmode_blocking)
                #print("epsilon_r ->",robots[i].epsilon_r)
                returnCode=sim.simxSetFloatSignal(clientID,"e",robots[i].e,sim.simx_opmode_blocking)
                #returnCode=sim.simxSetFloatSignal(clientID,"e",1.8394345227667335,sim.simx_opmode_blocking)
                #print("e ->",robots[i].e)
                debe_seguir=0
                debe_seguir_contador=0
                puntuacion_extra=0
                posicion_actual=[0,0]
                posicion_anterior=[0,0]
                returnCode,posicion_anterior[0]=sim.simxGetFloatSignal(clientID,"X_actual",sim.simx_opmode_oneshot)
                returnCode,posicion_anterior[1]=sim.simxGetFloatSignal(clientID,"Y_actual",sim.simx_opmode_oneshot)
                startTime_parado=time.time()
                bandera_termino_de_simulacion=False
                #and time.time()-startTime<tiempo_de_sleep
                #robots[i].fitness_robot(destino,puntuacion_extra)<30
                #while(time.time()-startTime<tiempo_de_sleep and bandera_termino_de_simulacion==False):
                tiempo_prueba=time.time()
                startTime=time.time()
                startTime_velocidad=time.time()
                resetear_simulacion=0
                puntuacion_extra_extra=0
                tiempo_maximo_de_trabado=time.time()
                bias_de_tiempo_por_defecto=5#120/24
                while(puntuacion_extra_extra<15 and bandera_termino_de_simulacion==False and time.time()-tiempo_maximo_de_trabado<120):

                    # cada 1seg verificamos que velocidad<=10 de lo contrario sumamos un puntaje proporcional la velocidad, de esta forma
                    # el algoritmo sabra que este no es un buen individuo ya que su puntaje sera alto
                    
                    #----------------------------------------------------------------------------------------------------------------
                    #*********************************************************************************************************************
                    #if(time.time()-startTime_velocidad>2):
                    #   startTime_velocidad=time.time()
                    #    returnCode,umbral_de_velocidad_1=sim.simxGetFloatSignal(clientID,"umbral_de_velocidad_1",sim.simx_opmode_oneshot)
                    #    returnCode,umbral_de_velocidad_2=sim.simxGetFloatSignal(clientID,"umbral_de_velocidad_2",sim.simx_opmode_oneshot)
                    #    if(umbral_de_velocidad_1<8 and umbral_de_velocidad_2<8):
                    #        umbral_de_velocidad=(umbral_de_velocidad_1+umbral_de_velocidad_2)/2
                    #        puntuacion_extra=puntuacion_extra-(umbral_de_velocidad*2)
                    #    else:
                    #        puntuacion_extra=puntuacion_extra+1+(umbral_de_velocidad/100)
                    #*******************************************************************************************************************
                    #-------------------------------------------------------------------------------------------------------------------

                    #si recibimos una señal de que el robot choco, entonces lo giramos para la derecha o izquierda aleatoriamente
                    returnCode,debe_seguir=sim.simxGetFloatSignal(clientID,"reiniciar",sim.simx_opmode_blocking)
                    #print("debe_seguir : ",debe_seguir)
                    if(debe_seguir==1):
                        robots[i].girar_robot(manejadores,clientID)
                        puntuacion_extra=puntuacion_extra+1

                    returnCode,llego_al_destino=sim.simxGetFloatSignal(clientID,"llego_al_destino",sim.simx_opmode_oneshot)
                    if(llego_al_destino==1):
                        bandera_termino_de_simulacion=True
                        #puntuacion_extra=puntuacion_extra-5
                        #si llegamos a la meta reescribimos el bias inicial por uno mas pequeño
                        bias_de_tiempo_por_defecto=(time.time()-tiempo_maximo_de_trabado)/24
                    
                    returnCode=sim.simxAddStatusbarMessage(clientID,str(puntuacion_extra),sim.simx_opmode_oneshot)

                    #calcula cada 2 segundos si el desplazamiento esta dentro de un margen de tolerancia
                    if(time.time()-startTime_parado>2):
                        startTime_parado=time.time()
                        returnCode,posicion_actual[0]=sim.simxGetFloatSignal(clientID,"X_actual",sim.simx_opmode_oneshot)
                        returnCode,posicion_actual[1]=sim.simxGetFloatSignal(clientID,"Y_actual",sim.simx_opmode_oneshot)
                        if(((posicion_anterior[0] - posicion_actual[0])**2 + (posicion_anterior[1] - posicion_actual[1])**2)**0.5 <0.2):
                            puntuacion_extra_extra=puntuacion_extra_extra+1
                        else:
                            puntuacion_extra_extra=0
                    
                        posicion_anterior[0]=posicion_actual[0]
                        posicion_anterior[1]=posicion_actual[1]

                    #returnCode,resetear_simulacion=sim.simxGetFloatSignal(clientID,"resetear_simulacion",sim.simx_opmode_blocking)    

                puntuacion_extra=puntuacion_extra+bias_de_tiempo_por_defecto
                robots[i].fitness_robot(destino,puntuacion_extra,clientID)
                
                returnCode=sim.simxSetFloatSignal(clientID,"resetear_simulacion",1,sim.simx_opmode_oneshot)
                #time.sleep(2)
                returnCode=sim.simxPauseSimulation(clientID,sim.simx_opmode_blocking)
                sim.simxFinish(clientID)  
                #print("tiempo",time.time()-tiempo_prueba)
                media_de_la_generacion=media_de_la_generacion+robots[i].get_fitness_actual_del_robot()
                robots[i].ver_fitness_actual_del_robot()
                robots[i].ver_todos_los_fitness()
                
             

        if(bandera>cantidad_de_fitness_pasados_almacenados-1):
            media_de_la_generacion=media_de_la_generacion/tamanio_poblacion

            #escojemos la mejor media, la mejor media es la media mas pequeña
            indice_de_individuo_con_mejor_media=escojer_individuo_con_mejor_media(robots,cantidad_de_fitness_pasados_almacenados)
            #individuo con el mejor fitnes de la generacion actual
            indice_del_mejor_actual=escojer_el_mejor(robots)
            #guardamos la media de los fitnes del mejor individuo para no tener que recalcularla a cada rato
            media_de_fitness_del_mejor=robots[indice_de_individuo_con_mejor_media].media_de_fitness()
            #guardamos los datos del mejor de esta generacion
            datos = open ('datos.txt','a')
            datos.write(str(bandera)+"\t"+str(media_de_la_generacion)+"\t"+str(media_de_fitness_del_mejor)+"\t"+str(robots[indice_de_individuo_con_mejor_media].epsilon_q)+"\t"+str(robots[indice_de_individuo_con_mejor_media].epsilon_c)+"\t"+str(robots[indice_de_individuo_con_mejor_media].epsilon_r)+"\t"+str(robots[indice_de_individuo_con_mejor_media].e)+"\t"+str(tasa_de_mutacion)+"\t"+str(robots[0].get_fitness_actual_del_robot())+"\t"+str(robots[1].get_fitness_actual_del_robot())+"\t"+str(robots[2].get_fitness_actual_del_robot())+"\t"+str(robots[3].get_fitness_actual_del_robot())+"\t"+str(robots[4].get_fitness_actual_del_robot())+"\t"+str(robots[5].get_fitness_actual_del_robot())+"\t"+str(robots[6].get_fitness_actual_del_robot())+"\t"+str(robots[7].get_fitness_actual_del_robot())+"\t"+str(robots[8].get_fitness_actual_del_robot())+"\t"+str(robots[9].get_fitness_actual_del_robot())+"\t"+str(robots[indice_de_individuo_con_mejor_media].get_fitness_actual_del_robot())+"\t"+str(robots[indice_del_mejor_actual].get_fitness_actual_del_robot())+"\n")
            datos.close()

            print("Fitness del individuo con la mejor media",media_de_fitness_del_mejor," , indice : ",indice_de_individuo_con_mejor_media,"#########################")        
            print("epsilon_q ->",robots[i].epsilon_q,"epsilon_c ->",robots[i].epsilon_c,"epsilon_r ->",robots[i].epsilon_r,"e ->",robots[i].e)
            
            # cada cierto periodo predamos, osea eliminamos al peor individuo y lo reemplazamos por un individuo totalmente aleatorio
            if(contador_para_predacion>periodo_de_predacion):
                robots = predacion_randomica(indice_de_individuo_con_mejor_media,robots,rango_q,rango_c,rango_r,rango_e)
                contador_para_predacion=0
            else:
                contador_para_predacion=contador_para_predacion+1

            robots=crossover_mejor_transa_con_todos_con_filtro(indice_de_individuo_con_mejor_media,robots,tasa_de_mutacion,rango_q,rango_c,rango_r,rango_e)
        
            # cada cierto periodo aumentamos la tasa de mutacion si la media no mejora, sabemos que mejora cuando sus parametros cambian
            # ya que cuando sus parametros cambian sabemos que se ha encontrado un individuo con una media mejor, por lo que se toma esos
            # nuevos parametros
            #if(4<abs(media_de_fitness_del_mejor-fitness_de_generacion_anterior)):
            if(robots[indice_de_individuo_con_mejor_media].epsilon_q==q_anterior and c_anterior==robots[indice_de_individuo_con_mejor_media].epsilon_c and e_anterior==robots[indice_de_individuo_con_mejor_media].e and r_anterior==robots[indice_de_individuo_con_mejor_media].epsilon_r): 
                contador_para_aumentar_la_tasa_de_mutacion=contador_para_aumentar_la_tasa_de_mutacion+1
                if(contador_para_aumentar_la_tasa_de_mutacion > periodo_de_aumento_de_tasa_de_mutacion):
                    tasa_de_mutacion=tasa_de_mutacion*2
                    contador_para_aumentar_la_tasa_de_mutacion=0
                    print("duplica la tasa_de_mutacion : ",tasa_de_mutacion)
            else:
                contador_para_aumentar_la_tasa_de_mutacion=0
                tasa_de_mutacion=0.02
                

            #fitness_de_generacion_anterior=media_de_fitness_del_mejor
            q_anterior=robots[indice_de_individuo_con_mejor_media].epsilon_q
            c_anterior=robots[indice_de_individuo_con_mejor_media].epsilon_c
            e_anterior=robots[indice_de_individuo_con_mejor_media].e
            r_anterior=robots[indice_de_individuo_con_mejor_media].epsilon_r


            print("contador_para_aumentar_la_tasa_de_mutacion : ",contador_para_aumentar_la_tasa_de_mutacion)
            print("tasa_de_mutacion : ",tasa_de_mutacion)

        
        #incrementamos los indices del vector fitness de cada robot, solo incrementa si el indice es menor a 5
        for i in range(tamanio_poblacion):
            robots[i].incrementar_indice_del_vector_de_fitness()

    
    #print("los mejores de cada generacion : ",mejor_de_cada_generacion)

    # Now send some data to CoppeliaSim in a non-blocking fashion:
    sim.simxAddStatusbarMessage(clientID,'Hello CoppeliaSim!',sim.simx_opmode_oneshot)

    # Before closing the connection to CoppeliaSim, make sure that the last command sent out had time to arrive. You can guarantee this with (for example):
    #Esta funcion devuelve el ping que tarda la conexion ciente servidor
    sim.simxGetPingTime(clientID)

    #Paramos la simulacion en CoppeliaSim
    returnCode=sim.simxStopSimulation(clientID,sim.simx_opmode_oneshot)

    # Now close the connection to CoppeliaSim
    #sim.simxFinish(clientID)

#-----------------------------------------------------------------------------------------------------------------
else:
    print ('Failed connecting to remote API server')
print ('Program ended')