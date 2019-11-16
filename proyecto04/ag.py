#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Universaidad Nacional Autónoma de México
# Facultad de Ingeniería
# Aprendizaje (Máquina)
# Programa 04
# Algoritmo Genético
# Aguilar Enriquez Paul Sebastian
# Cabrera Lopez Oscar Emilio


# In[2]:


import random
from matplotlib import pyplot as plt


# In[3]:


# Parametros del algoritmo

## Número de genes: 16
numGenes = 16
## Metodo de selección: Ruleta
## Cruza: De 2 puntos , crossover_rate(pc) = 80%
crossover_points = 2
crossover_rate = .8
## Mutación: -, mutation_rate(pm) = 1%
mutation_rate = .01
## Tamaño de población: 50
population = 50
## Cantidad de generaciones: 20
generations = 20


# In[4]:


# Funciones de apoyo

## Verifica la suma de capital a invertir y que este se encuentre en el 
## rango valido
def inversionValida(a, b, c, d):
    inversion = a + b + c + d
    if (inversion > 0) and (inversion <= 10):
        return True
    else:
        return False
    
## Convierte de decimal a binario
def dec2bin(dec):
    bina = []
    
    # Convertimos el valor decimal a binario
    while int(dec/2) != 0:
        bina.append( int(dec%2) )
        dec = dec/2
    if dec > 0:
        bina.append(1)
    
    # Completamos los valores faltantes
    while(len(bina) < 4):
        bina.append(0)
    bina.reverse()
    return bina

## Convierte de binario a decimal
def bin2dec(bina):
    dec = []
    val = 0
    slide = 1
    
    # Recorremos los bits con una ventana de 4
    for i in range(numGenes):
        if bina[i] == 1:
            val += pow(2,(4*slide)-1-i)
        if (i+1)%4 == 0:
            dec.append(val)
            val = 0
            slide += 1
    return dec


# In[5]:


#Funcion y valores de mercado

## Valores de mercado
T1 = [0.00, 0.28, 0.45, 0.65, 0.78, 0.90, 1.02, 1.13, 1.23, 1.32, 1.38]
T2 = [0.00, 0.25, 0.41, 0.55, 0.65, 0.75, 0.80, 0.85, 0.88, 0.90, 0.90]
T3 = [0.00, 0.15, 0.25, 0.40, 0.50, 0.62, 0.73, 0.82, 0.90, 0.96, 1.00]
T4 = [0.00, 0.20, 0.33, 0.42, 0.48, 0.53, 0.56, 0.58, 0.60, 0.60, 0.60]

## Función de aptitud
def F(inv1, inv2, inv3, inv4):
    sumInversionTotal = inv1 + inv2 + inv3 + inv4;
    V = abs(sumInversionTotal - 10)
    
    # Ahora sí función de aptitud :D
    x = (T1[inv1] + T2[inv2] + T3[inv3] + T4[inv4]) / ( (500*V)+1 )
    return x


# In[6]:


#Inicialización
pobDec = []
pobBin = []

## Generador de población
def generador():
    # Creamos la cantidad de poblacion
    for i in range(population):
        # Limpiamos valores
        a = 0
        b = 0
        c = 0
        d = 0
        
        # Proponemos los valores a invertir de manera aleatoria
        # y verificamos que se encuentren en el rango de 
        # 0 <= inversion <= 10
        while(not inversionValida(a, b, c, d)):
            a = random.randint(0, 11)
            b = random.randint(0, 11 - a)
            c = random.randint(0, 11 - a - b)
            d = random.randint(0, 11 - a - b - c)
        
        # Guardamos al individuo en su formato decimal
        pobDec.append([a, b, c, d])
        # Guardamos al individuo en su formato binario
        pobBin.append(dec2bin(a) + dec2bin(b) + dec2bin(c) + dec2bin(d))

## Imprime la poblacion feliz de nuestro universo :D
def imprimirPoblacion():
    print("\n\n# Poblacion #")
    for i in range(population):
        print("Individuo " , i, ": ", pobDec[i])
        print("Binario ", i, ": ", pobBin[i])


# In[7]:


# Evaluación
pobAptitud = []
sumAptitud = 0

def evaluacion():
    global pobAptitud
    pobAptitud = []
    global sumAptitud
    sumAptitud = 0
    
    for i in range(population):
        # Evaluamos con la función de aptitud dada
        pobAptitud.append(F(pobDec[i][0], pobDec[i][1], pobDec[i][2], pobDec[i][3]))
        # Vamos calculando la suma de las aptitudes, se necesitara en la seleccion
        sumAptitud += pobAptitud[i]
    
def imprimirEvaluacion():
    print("\n\n# Aptitud de la población #")
    for i in range(population):
        print("Aptitud ", i, ": ", pobAptitud[i])
    print("Suma de la aptitud: ", sumAptitud)


# In[8]:


# Seleccion
promedio = 0
pobPromedio = []
pobVe = []
sumVe = 0
pobAcum = []
pobR = []
pobSelec = []

def seleccion():
    global promedio
    promedio = 0
    global pobPromedio
    global pobVe
    pobVe = []
    global sumVe
    sumVe = 0
    global pobAcum
    pobAcum = []
    global pobR
    pobR = []
    global pobSelec
    pobSelec = []
    
    # calculamos el promedio de las aptitudes
    promedio = sumAptitud / population
    pobPromedio.append(promedio)
    
    # Calculamos los valores esperados para cada individuo
    for i in range(population):
        pobVe.append(pobAptitud[i]/promedio)
        sumVe += pobVe[i];
        pobAcum.append(sumVe)
    
    # Aquí empieza la ruleta!
    for i in range(population):
        # Generamos una r aleatoria
        pobR.append(random.uniform(0,sumVe))
        # Buscamos el primer elementos que es mayor o igual en su acumulado
        # que la r generada
        for j in range(population):
            if pobAcum[j] >= pobR[i]:
                pobSelec.append(j)
                break

def imprimirSeleccion():
    print("\n\n# Calculo de valores para la seleccion de la población #")
    for i in range(population):
        print("Ve ", i, ": ", pobVe[i])
        print("Acumulado ", i, ": ", pobAcum[i])
    print("\nPromedio: ", promedio)
    print("Sum Ve: ", sumVe)
    
    print("\n\n# Seleccion de la población #")
    for i in range(population):
        print("r ", i, ": ", pobR[i])
        print("Ind. seleccionado: ", pobSelec[i])
    
# Es para cargar la población despues de la selección, así podemos
# operar sobre de ella ya con los individuos seleccionados
def configurarPoblacionSeleccionada():
    global pobDec
    global pobBin
    pobDecN = []
    pobBinN = []
    
    for i in range(population):
        pobDecN.append(pobDec[pobSelec[i]])
        pobBinN.append(pobBin[pobSelec[i]])
    
    pobDec = pobDecN
    pobBin = pobBinN


# In[9]:


# Cruza
pobK = [] # Valores de K
pobKI = [] # Indices seleccionados para hacer la cruza

def cruza():
    global pobK
    pobK = []
    global ponKI
    pobKI = []
    global pobDec
    global pobBin
    
    # Generamos el valor K para los individuos a cruzar de
    # entre los seleccionados
    for i in range(population):
        pobK.append(random.uniform(0,1))
        
        # Si el valor K generado es menor al pc
        # seleccionamos al individuo para cruzar
        if pobK[i] < crossover_rate:
            pobKI.append(i)
        
    # Ahora procedemos a hacer la cruza
    pobCruzada = [] # Población hija o resultante
    
    # Imprimimos las cruzas seleccionadas ;@
    print("\n\n# Cruza! #")
    for i in range(population):
        print("k ", i, ": ", pobK[i])
    
    print("\nIndividuos a cruzar de los seleccionados: ", pobKI)
    print("\nTotal de individuos a cruzar de los seleccionados: ", len(pobKI))
    
    print("\nProceso de cruza")
    for i in range(len(pobKI)):
        # Va de 1 a 14, excluimos el 0 y el 15 porque son las orillas
        p1 = random.randint(1,15)
        p2 = random.randint(1,15)
        
        # Validamos el orden de los indices en los puntos
        # Si el primer punto es mayor que el segundo, esta mas lejos
        # en el indice de posiciones, hay que intercambiarlos
        if p1 > p2:
            temp = p1
            p1 = p2
            p2 = temp
        
        # Ahora si va la cruza!
        # Tomamos las orillas del primero y el centro del segundo
        print("punto1: ", p1, " punto2: ", p2)
        print("\tPadre1: ", pobBin[pobKI[i]])
        if i < len(pobKI) - 1:
            print("\tPadre2:\t", pobBin[pobKI[i+1]])
            pobCruzada.append(pobBin[pobKI[i]][0:p1] + pobBin[pobKI[i+1]][p1:p2] + pobBin[pobKI[i]][p2:numGenes])
        else:
            print("\tPadre2:\t", pobBin[pobKI[0]])
            pobCruzada.append(pobBin[pobKI[i]][0:p1] + pobBin[pobKI[0]][p1:p2] + pobBin[pobKI[i]][p2:numGenes])
        print("\tHijo:\t", pobCruzada[i])
    
    # Guardamos las combinaciones resultantes en la poblacion
    for i in range(len(pobKI)):
        pobBin[pobKI[i]] = pobCruzada[i]
        pobDec[pobKI[i]] = bin2dec(pobCruzada[i])


# In[10]:


# Mutación

def mutacion():
    global pobDec
    global pobBin
    
    # Calculamos el número de mutaciones
    total_gen = numGenes * population
    # Le sumamos 2 para asegurar que por lo menos haya un par
    # de genes a mutar ya que el mutation_rate es muy pequeño
    num_mutation = int(mutation_rate * total_gen) + 2
    
    print("\n\n# Mutacion! #")
    print("Total de mutaciones: ", num_mutation)
    
    # Aqui almacenaremos los indices de los genes a mutar
    mutationIndex = []
    
    # Calculamos los genes a mutar
    for i in range(num_mutation):
        mutationIndex.append(random.randint(0,total_gen-1))
    
    print("Genes a mutar: ", mutationIndex)
    
    # Comenzamos la mutación
    for i in range(num_mutation-1):
        # Calculamos los individuos y el gen de ese individuo
        # a intercambiar
        ind1 = int(mutationIndex[i]/numGenes)
        gen1 = mutationIndex[i]-int(ind1*numGenes)
        ind2 = int(mutationIndex[i+1]/numGenes)
        gen2 = mutationIndex[i+1]-int(ind2*numGenes)
        
        print("Se mutara individuo", ind1, "gen", gen1, " e individuo", ind2, "gen", gen2)
        print("\tAntes de mutar:")
        print("\t\tIndividuo ", ind1, ": ", pobBin[ind1])
        print("\t\tIndividuo ", ind2, ": ", pobBin[ind2])
        
        # Hacemos un swap
        temp = pobBin[ind1][gen1]
        pobBin[ind1][gen1] = pobBin[ind2][gen2]
        pobBin[ind2][gen2] = temp
        
        # Convertimos cada individuo mutado a su versión en decimal
        pobDec[ind1] = bin2dec(pobBin[ind1])
        pobDec[ind2] = bin2dec(pobBin[ind2])
        
        print("\tDespues de mutar:")
        print("\t\tIndividuo ", ind1, ": ", pobBin[ind1])
        print("\t\tIndividuo ", ind2, ": ", pobBin[ind2])
        
        # Damos un paso extra para que realmente el ciclo avance
        # de dos en dos
        i += 1


# In[11]:


# Determinamos al mejor individuo para esta generación

mejorInd = 0
mejorApt = 0

def mejorIndividuo():
    global mejorInd
    global mejorApt
    global pobAptitud
    
    pobAptitud = []
    
    for i in range(population):
        pobAptitud.append(F(pobDec[i][0], pobDec[i][1], pobDec[i][2], pobDec[i][3]))
        if pobAptitud[i] > mejorApt:
            mejorApt = pobAptitud[i]
            mejorInd = i

def imprimirMejorIndividuo():
    imprimirEvaluacion()
    print("\n\nEl mejor individuo es el individuo", mejorInd)
    print("\t", pobDec[mejorInd],"\t",pobBin[mejorInd])
            


# In[12]:


# Validamos que sigan siendo individuos validos
pobMuertes = []

def validarPoblacion():
    global pobMuertes
    global pobDec
    global pobBin
    
    pobPeor = []
    # Hacemos un ajuste, al cruzar o mutar un individuo este puede terminar
    # con una configuración que invierte más de 10 unidades de millon
    # Si esto sucede el individuo debe morir y ser reemplazado por el
    # mejor individuo ;@
    
    # Para esto primero sustuimos el individuo que ya excedio el limite de 
    # inversión con uno con valores en cero el cual no genera ganacias,
    # es un neutro, despues volvemos a evaluar la poblacion con el individuo
    # nuevo, y sustituimos con el mejor de esta poblacion
    print("\n\n# Validando poblacion tras ser modificada #")
    
    # Buscamos a los individuos que rompen la regla de inversion y los
    # sustituimos por un individuo que corresponda a no realizar inversion
    contadorMuertes = 0
    for i in range(population):
        if pobDec[i][0] + pobDec[i][1] + pobDec[i][2] + pobDec[i][3] > 10:
            pobPeor.append(i)
            print("\tEl individuo ", i, " debe morir, su inversión excede 10 millones: ", pobDec[i])
            pobDec[i] = [0,0,0,0]
            pobBin[i] = dec2bin(int(pobDec[i][0])) + dec2bin(int(pobDec[i][1])) + dec2bin(int(pobDec[i][2])) + dec2bin(int(pobDec[i][3]))
            print("\tEl individuo ", i, " fue sustituido temporalmente por: ", pobDec[i])
            contadorMuertes += 1
    
    # De la población modificada con los temporales buscamos al mejor individuo
    mejorIndividuo()
    
    # Sustituimos a los peores individuos con el mejor
    for i in range(len(pobPeor)):
        pobDec[i] = pobDec[mejorInd]
        pobBin[i] = pobBin[mejorInd]
    
    print("\tLos individuos ", pobPeor, " fueron sustituidos por el individuo ", mejorInd, ": ", pobDec[mejorInd])
    # Llevamos un contador de muertes :P
    pobMuertes.append(contadorMuertes)


# In[13]:


def main():
    print("Recordar que los indices para los elementos comienzan en cero!")
    generador()
    imprimirPoblacion()
    for i in range(generations):
        print("\n###-> Generacion ", i, " <-###")
        evaluacion()
        imprimirEvaluacion()
        seleccion()
        imprimirSeleccion()
        configurarPoblacionSeleccionada()
        imprimirPoblacion()
        cruza()
        validarPoblacion()
        imprimirPoblacion()
        mutacion()
        validarPoblacion()
        imprimirPoblacion()
        mejorIndividuo()
        imprimirMejorIndividuo()
    
    plt.plot(pobPromedio, label='Promedio')
    plt.title('Promedio de Aptitud')
    plt.ylabel('Promedio')
    plt.xlabel('Generaciones')
    plt.legend(loc = 'best')
    plt.show()
    
    plt.plot(pobMuertes, label='Sustituciones')
    plt.title('Sustituciones por exceder el limite de inversion')
    plt.ylabel('Sustituciones')
    plt.xlabel('Generaciones (Cruza y mutacion)')
    plt.legend(loc = 'best')
    plt.show()


# In[14]:


main()

