import numpy as np
import matplotlib.pyplot as plt

n = int(input("cantidad de masas evaluadas:")) #se pide la cantidad de masas

m=[]
X = []
Y = []
for i in range(n) :
    m.append(float((input(f"Masa {[i+1]}:  ")))) #se crea una lista con las masas evaluadas, que ira en el eje Y
    Y.append(float((m[i])*9.81))                 #Cada masa se multiplica por la aceleración de la gravedad
    X.append(float(input(f"Elongación {[i+1]}:   "))) #se hace lo mismo para las elongaciones, que sera el eje X

print("masas evaluadas"+ str(m))
print("Pesos de cada masa evaluada" + str(X))           #se imprimen las listas de los datos ingresados
print("Elongaciones" + str(Y))
   

#se calculan las sumatorias necesarias para la formula de los minimos cuadrados    
def sumatoria(X,Y):          #sumatoria de X*Y      
    sumxy=0
    for i in range (n):
        b=X[i]*Y[i]
        sumxy+=b
    return sumxy
        
def sum (X):          #sumatoria de los valores de X
    c=0
    for i in range (n):
        c+=X[i]
    return c

def sum2(X):       #sumatoria de los valores de X al cuadrado cada valor
    c=0
    for i in range (n):
        c+=(X[i])**2
    return c

def ajustecuadrados(n,X,Y):       #formual de los minimos cuadrados con las sumatorias anteriores
    m=((n*sumatoria(X,Y))-(sum(X)*sum(Y)))/((n*sum2(X))-((sum(X))**2))
    
    b=((sum(Y)*sum2(X))-(sum(X)*sumatoria(X,Y)))/((n*sum2(X))-((sum(X))**2))
    print("El coeficiente de elasticidad del resorte es de:  " + str(m))
    print("con un intercepto de :  " + str(b))
    
    return m,b

X_linea = np.linspace(0, max(X), 100)  #se crea la linea de tendencia
Y_linea = np.zeros(len(X_linea))

pendiente, termino_i = ajustecuadrados(n,X,Y)

for i in range(len(X_linea)):        #se hace un ciclo para que tome los valores de X y los reemplace en la ecuacion de la recta
    Y_linea[i] = pendiente * X_linea[i] + termino_i
    

ajustecuadrados(n,X,Y)  # se llama a la funcion de los minimos cuadrados

plt.plot(X,Y,"g.", X_linea, Y_linea, "r-") #se dibujan los puntos y la linea de tendencia
plt.show()