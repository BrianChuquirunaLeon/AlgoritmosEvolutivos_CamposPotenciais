import sim
import random
import time
class Robot:
    
    def __init__(self,rango_q,rango_c,rango_r,rango_e):
        self.epsilon_q=random.uniform(0,rango_q)
        self.epsilon_c=random.uniform(0,rango_c)
        self.epsilon_r=random.uniform(0,rango_r)
        self.e=random.uniform(0,rango_e)
        self.array_fitness_anteriores=[0,0,0,0,0]
        self.indice_actual_fitness=0
        self.cantidad_de_fitness_pasados_almacenados=5

    def resetar_todos_los_fitness(self):
        self.array_fitness_anteriores=[0,0,0,0,0]
        self.indice_actual_fitness=-1

    def pasar_valores_de_crossover(self,epsilon_q,epsilon_c,epsilon_r,e):
        self.epsilon_q=epsilon_q
        self.epsilon_c=epsilon_c
        self.epsilon_r=epsilon_r
        self.e=e
        self.resetar_todos_los_fitness()
        print("hace crossover y resetea los valores de los fitness")
        
    #devuelve la distancia entre el punto actual y el destino
    def fitness_robot(self,destino,puntuacion_extra,clientID):
        returnCode,self.x=sim.simxGetFloatSignal(clientID,"X_actual",sim.simx_opmode_blocking)
        returnCode,self.y=sim.simxGetFloatSignal(clientID,"Y_actual",sim.simx_opmode_blocking)
        delta_x = self.x - destino[0]
        delta_y = self.y - destino[1]

        if(self.indice_actual_fitness<5):
            self.array_fitness_anteriores[self.indice_actual_fitness]=((delta_x**2 + delta_y**2)**0.5)+puntuacion_extra
        else:
            self.array_fitness_anteriores.pop(0)
            self.indice_actual_fitness=self.indice_actual_fitness-1
            self.array_fitness_anteriores.append(((delta_x**2 + delta_y**2)**0.5)+puntuacion_extra)
        
        return self.array_fitness_anteriores[self.indice_actual_fitness]

    def incrementar_indice_del_vector_de_fitness(self):   
        if(self.indice_actual_fitness<5):
            self.indice_actual_fitness=self.indice_actual_fitness+1

    def ver_fitness_actual_del_robot(self):
        print("Fitness actual del robot : ",self.array_fitness_anteriores[self.indice_actual_fitness])

    def get_fitness_actual_del_robot(self):
        return self.array_fitness_anteriores[self.indice_actual_fitness]

    def ver_todos_los_fitness(self):    
        print("todos los fitness : ",self.array_fitness_anteriores,"self.indice_actual_fitness",self.indice_actual_fitness)


    def media_de_fitness(self):
        if(self.indice_actual_fitness==(self.cantidad_de_fitness_pasados_almacenados-1)):
            media=0
            for fitness_actual in self.array_fitness_anteriores:
                media=media+fitness_actual
            media=media/self.cantidad_de_fitness_pasados_almacenados

            return media
        else:
            print("no sacamos la media ya que no tiene los 5 fitness llenos")


    def girar_robot(self,manejadores,clientID):
        #gira el robot para la derecha o la izquierda
        #girar=[1,-1]
        #elige_lado = random.choice(girar)
        #startTime=time.time()
        #while time.time()-startTime < 2:
        returnCode=sim.simxSetFloatSignal(clientID,"girar",1,sim.simx_opmode_blocking)
        returnCode=sim.simxSetJointTargetVelocity(clientID,manejadores[2],2, sim.simx_opmode_oneshot)
        returnCode=sim.simxSetJointTargetVelocity(clientID,manejadores[3],-2, sim.simx_opmode_oneshot)
        time.sleep(0.5)
        returnCode=sim.simxSetFloatSignal(clientID,"girar",0,sim.simx_opmode_blocking)

    def resetear(self,position,manejadores,clientID):

        #empieza con velocidad inicial de referencia en 2 igual que el script en lua dentro de coppelia
        #startTime=time.time()
        #while time.time()-startTime < 2:
        returnCode=sim.simxSetJointTargetVelocity(clientID,manejadores[2],0, sim.simx_opmode_oneshot)
        returnCode=sim.simxSetJointTargetVelocity(clientID,manejadores[3],0, sim.simx_opmode_oneshot)

        returnCode=sim.simxSetObjectPosition(clientID,manejadores[0],-1,position[0],sim.simx_opmode_oneshot)
        #if(returnCode!=sim.simx_return_ok): print("Pioneer_p3dx_nuevo! posicion NO reseteada")

        returnCode=sim.simxSetObjectPosition(clientID,manejadores[1],manejadores[0],position[1],sim.simx_opmode_oneshot)
        #if(returnCode!=sim.simx_return_ok): print("robot_pose! posicion NO reseteada")

        returnCode=sim.simxSetObjectPosition(clientID,manejadores[2],manejadores[0],position[2],sim.simx_opmode_oneshot)
        #if(returnCode!=sim.simx_return_ok): print("Pioneer_p3dx_leftMotor! posicion NO reseteada")

        returnCode=sim.simxSetObjectPosition(clientID,manejadores[3],manejadores[0],position[3],sim.simx_opmode_oneshot)
        #if(returnCode!=sim.simx_return_ok): print("Pioneer_p3dx_rightMotor! posicion NO reseteada")

        returnCode=sim.simxSetObjectPosition(clientID,manejadores[4],manejadores[0],position[4],sim.simx_opmode_oneshot)
        #if(returnCode!=sim.simx_return_ok): print("GPS_version_actual! posicion NO reseteada")

        returnCode=sim.simxSetObjectPosition(clientID,manejadores[5],manejadores[0],position[5],sim.simx_opmode_oneshot)
        #if(returnCode!=sim.simx_return_ok): print("Pioneer_p3dx_caster_freeJoint1! posicion NO reseteada")

        returnCode=sim.simxSetObjectPosition(clientID,manejadores[6],manejadores[0],position[6],sim.simx_opmode_oneshot)
        #if(returnCode!=sim.simx_return_ok): print("fastHokuyo! posicion NO reseteada")

        returnCode=sim.simxSetObjectPosition(clientID,manejadores[7],manejadores[0],position[7],sim.simx_opmode_oneshot)

        returnCode=sim.simxSetObjectPosition(clientID,manejadores[8],manejadores[0],position[8],sim.simx_opmode_oneshot)

        returnCode=sim.simxSetObjectPosition(clientID,manejadores[9],manejadores[0],position[9],sim.simx_opmode_oneshot)

        returnCode=sim.simxSetObjectPosition(clientID,manejadores[10],manejadores[0],position[10],sim.simx_opmode_oneshot)

        returnCode=sim.simxSetObjectPosition(clientID,manejadores[11],manejadores[0],position[11],sim.simx_opmode_oneshot)

        returnCode=sim.simxSetObjectOrientation(clientID,manejadores[0],-1,position[12],sim.simx_opmode_oneshot)

        startTime=time.time()
        while time.time()-startTime < 5:
            returnCode=sim.simxSetFloatSignal(clientID,"reiniciar_fuerzas",1,sim.simx_opmode_blocking)
        returnCode=sim.simxSetFloatSignal(clientID,"reiniciar_fuerzas",0,sim.simx_opmode_blocking)

    