#importamos la libreria para poder graficar
import matplotlib.pyplot as plt
#Preguntamos por medio de un mensaje porque metodo se va a resolver
#1 Algoritmo DDA
#2 Algoritmo Bresenhams
respuesta = int( input("Coloca 1 Si deceas ocupar el ALgoritmo DDA O 2 de Bresenhams para dibujar el Poligono Regular") )
#Si la respuesta es 1 entrara al primer if y se se graficara por DDA
if respuesta == 1:
    print("Algoritmo DDA")
    lados = int(input("Ingresa el numero de lado del poligonos regular a graficar: "))
    if lados == 3:
        print("Triangulo Equilatero")
        x1=3
        y1=1
        x2=9
        y2=1
        #calculamos la diferencia
        dx = x2-x1
        dy = y2-y1
        #calculamos la pendiente
        if dx !=0 :
            m = dy / dx
        else:
            print("")
        #calculamos el valor de steps
        if(dx > dy):
            steps = dx
        else:
            steps = dy
        #Calculamos el incremento
        xinc = dx / steps
        yinc = dy / steps
        print(x1,y1)
        plt.scatter(x1,y1)
        #calculamos los nuevos valores de x y y
        i=1
        while(i<=steps):
            x1 = x1 + xinc
            y1 = y1 + yinc
            #Redondeamos los valores con el metodo round 
            x=round(x1)
            y=round(y1)
            i+=1
            print(x,y)
            plt.scatter(x,y)
        ###***************************************************************************************
        x1=3
        y1=1
        x2=6
        y2=4
        #calculamos la diferencia
        dx = x2-x1
        dy = y2-y1
        #calculamos la pendiente
        if dx !=0 :
            m = dy / dx
        else:
            print("")
        #calculamos el valor de steps
        if(dx > dy):
            steps = dx
        else:
            steps = dy
        #Calculamos el incremento
        xinc = dx / steps
        yinc = dy / steps
        print(x1,y1)
        plt.scatter(x1,y1)
        #calculamos los nuevos valores de x y y
        i=1
        while(i<=steps):
            x1 = x1 + xinc
            y1 = y1 + yinc
            #Redondeamos los valores con el metodo round 
            x=round(x1)
            y=round(y1)
            i+=1
            print(x,y)
            plt.scatter(x,y)
        #********************************************************************************************
        x1=6
        y1=4
        x2=9
        y2=1
        #calculamos la diferencia
        dx = x2-x1
        dy = y2-y1
        #calculamos la pendiente
        if dx !=0 :
            m = dy / dx
        else:
            print("")
        #calculamos el valor de steps
        if(dx > dy):
            steps = dx
        else:
            steps = dy
        #Calculamos el incremento
        xinc = dx / steps
        yinc = dy / steps
        print(x1,y1)
        plt.scatter(x1,y1)
        #calculamos los nuevos valores de x y y
        i=1
        while(i<=steps):
            x1 = x1 + xinc
            y1 = y1 + yinc
            #Redondeamos los valores con el metodo round 
            x=round(x1)
            y=round(y1)
            i+=1
            print(x,y)
            plt.scatter(x,y)
        plt.show()
    if lados == 4:
        print("Cuadrilatero")
        x1=3
        y1=2
        x2=3
        y2=4
        #calculamos la diferencia
        dx = x2-x1
        dy = y2-y1
        #calculamos la pendiente
        if dx !=0 :
            m = dy / dx
        else:
            print("")
        #calculamos el valor de steps
        if(dx > dy):
            steps = dx
        else:
            steps = dy
        #Calculamos el incremento
        xinc = dx / steps
        yinc = dy / steps
        print(x1,y1)
        plt.scatter(x1,y1)
        #calculamos los nuevos valores de x y y
        i=1
        while(i<=steps):
            x1 = x1 + xinc
            y1 = y1 + yinc
            #Redondeamos los valores con el metodo round 
            x=round(x1)
            y=round(y1)
            i+=1
            print(x,y)
            plt.scatter(x,y)
        ###***************************************************************************************
        x1=3
        y1=4
        x2=5
        y2=4
        #calculamos la diferencia
        dx = x2-x1
        dy = y2-y1
        #calculamos la pendiente
        if dx !=0 :
            m = dy / dx
        else:
            print("")
        #calculamos el valor de steps
        if(dx > dy):
            steps = dx
        else:
            steps = dy
        #Calculamos el incremento
        xinc = dx / steps
        yinc = dy / steps
        print(x1,y1)
        plt.scatter(x1,y1)
        #calculamos los nuevos valores de x y y
        i=1
        while(i<=steps):
            x1 = x1 + xinc
            y1 = y1 + yinc
            #Redondeamos los valores con el metodo round 
            x=round(x1)
            y=round(y1)
            i+=1
            print(x,y)
            plt.scatter(x,y)
        #********************************************************************************************
        x1=3
        y1=2
        x2=5
        y2=2
        #calculamos la diferencia
        dx = x2-x1
        dy = y2-y1
        #calculamos la pendiente
        if dx !=0 :
            m = dy / dx
        else:
            print("")
        #calculamos el valor de steps
        if(dx > dy):
            steps = dx
        else:
            steps = dy
        #Calculamos el incremento
        xinc = dx / steps
        yinc = dy / steps
        print(x1,y1)
        plt.scatter(x1,y1)
        #calculamos los nuevos valores de x y y
        i=1
        while(i<=steps):
            x1 = x1 + xinc
            y1 = y1 + yinc
            #Redondeamos los valores con el metodo round 
            x=round(x1)
            y=round(y1)
            i+=1
            print(x,y)
            plt.scatter(x,y)
        #********************************************************************************************
        x1=5
        y1=2
        x2=5
        y2=4
        #calculamos la diferencia
        dx = x2-x1
        dy = y2-y1
        #calculamos la pendiente
        if dx !=0 :
            m = dy / dx
        else:
            print("")
        #calculamos el valor de steps
        if(dx > dy):
            steps = dx
        else:
            steps = dy
        #Calculamos el incremento
        xinc = dx / steps
        yinc = dy / steps
        print(x1,y1)
        plt.scatter(x1,y1)
        #calculamos los nuevos valores de x y y
        i=1
        while(i<=steps):
            x1 = x1 + xinc
            y1 = y1 + yinc
            #Redondeamos los valores con el metodo round 
            x=round(x1)
            y=round(y1)
            i+=1
            print(x,y)
            plt.scatter(x,y)
        plt.show()
    if lados == 5:
        print("Pentagono")
        x1=1
        y1=0
        x2=3
        y2=0
        #calculamos la primera parte del cuadrado
        #calculamos la diferencia
        dx = x2-x1
        dy = y2-y1
        #calculamos la pendiente
        if dx !=0 :
            m = dy / dx
        else:
            print("")
        #calculamos el valor de steps
        if(dx > dy):
            steps = dx
        else:
            steps = dy
        #Calculamos el incremento
        xinc = dx / steps
        yinc = dy / steps
        print(x1,y1)
        plt.scatter(x1,y1)
        #calculamos los nuevos valores de x y y
        i=1
        while(i<=steps):
            x1 = x1 + xinc
            y1 = y1 + yinc
            #Redondeamos los valores con el metodo round 
            x=round(x1)
            y=round(y1)
            i+=1
            print(x,y)
            plt.scatter(x,y)
        #**********************************************************************************************
        x1=1
        y1=0
        x2=0
        y2=2
        #calculamos la primera parte del cuadrado
        #calculamos la diferencia
        dx = x2-x1
        dy = y2-y1
        #calculamos la pendiente
        if dx !=0 :
            m = dy / dx
        else:
            print("")
        #calculamos el valor de steps
        if(dx > dy):
            steps = dx
        else:
            steps = dy
        #Calculamos el incremento
        xinc = dx / steps
        yinc = dy / steps
        if xinc !=0 :
            print("Se puede")
        else:
            print("No se puede realizar una operacion entre cero")
        if yinc !=0 :
            print("Se puede")
        else:
            print("No se puede realizar una operacion entre cero")
        print(x1,y1)
        plt.scatter(x1,y1)
        #calculamos los nuevos valores de x y y
        i=1
        while(i<=steps):
            x1 = x1 + xinc
            y1 = y1 + yinc
            #Redondeamos los valores con el metodo round 
            x=round(x1)
            y=round(y1)
            i+=1
            print(x,y)
            plt.scatter(x,y)
        #**********************************************************************************************
        x1=0
        y1=2
        x2=2
        y2=3
        #calculamos la primera parte del cuadrado
        #calculamos la diferencia
        dx = x2-x1
        dy = y2-y1
        #calculamos la pendiente
        if dx !=0 :
            m = dy / dx
        else:
            print("")
        #calculamos el valor de steps
        if(dx > dy):
            steps = dx
        else:
            steps = dy
        #Calculamos el incremento
        xinc = dx / steps
        yinc = dy / steps
        print(x1,y1)
        plt.scatter(x1,y1)
        #calculamos los nuevos valores de x y y
        i=1
        while(i<=steps):
            x1 = x1 + xinc
            y1 = y1 + yinc
            #Redondeamos los valores con el metodo round 
            x=round(x1)
            y=round(y1)
            i+=1
            print(x,y)
            plt.scatter(x,y)
        #**********************************************************************************************
        x1=2
        y1=3
        x2=4
        y2=2
        #calculamos la primera parte del cuadrado
        #calculamos la diferencia
        dx = x2-x1
        dy = y2-y1
        #calculamos la pendiente
        if dx !=0 :
            m = dy / dx
        else:
            print("")
        #calculamos el valor de steps
        if(dx > dy):
            steps = dx
        else:
            steps = dy
        #Calculamos el incremento
        xinc = dx / steps
        yinc = dy / steps
        print(x1,y1)
        plt.scatter(x1,y1)
        #calculamos los nuevos valores de x y y
        i=1
        while(i<=steps):
            x1 = x1 + xinc
            y1 = y1 + yinc
            #Redondeamos los valores con el metodo round 
            x=round(x1)
            y=round(y1)
            i+=1
            print(x,y)
            plt.scatter(x,y)
        #**********************************************************************************************
        x1=3
        y1=0
        x2=4
        y2=2
        #calculamos la primera parte del cuadrado
        #calculamos la diferencia
        dx = x2-x1
        dy = y2-y1
        #calculamos la pendiente
        if dx !=0 :
            m = dy / dx
        else:
            print("")
        #calculamos el valor de steps
        if(dx > dy):
            steps = dx
        else:
            steps = dy
        #Calculamos el incremento
        xinc = dx / steps
        yinc = dy / steps
        print(x1,y1)
        plt.scatter(x1,y1)
        #calculamos los nuevos valores de x y y
        i=1
        while(i<=steps):
            x1 = x1 + xinc
            y1 = y1 + yinc
            #Redondeamos los valores con el metodo round 
            x=round(x1)
            y=round(y1)
            i+=1
            print(x,y)
            plt.scatter(x,y)
        plt.show()
    if lados == 6:
        print("Hexagono")    
        x1=4
        y1=0
        x2=0
        y2=4
        #calculamos la diferencia
        dx = x2-x1
        dy = y2-y1
        #calculamos la pendiente
        if dx !=0 :
            m = dy / dx
        else:
            print("")
        #calculamos el valor de steps
        if(dx > dy):
            steps = dx
        else:
            steps = dy
        #Calculamos el incremento
        xinc = dx / steps
        yinc = dy / steps
        print(x1,y1)
        plt.scatter(x1,y1)
        #calculamos los nuevos valores de x y y
        i=1
        while(i<=steps):
            x1 = x1 + xinc
            y1 = y1 + yinc
            #Redondeamos los valores con el metodo round 
            x=round(x1)
            y=round(y1)
            i+=1
            print(x,y)
            plt.scatter(x,y)
        #**********************************************************************************************
        x1=4
        y1=0
        x2=8
        y2=0
        #calculamos la diferencia
        dx = x2-x1
        dy = y2-y1
        #calculamos la pendiente
        if dx !=0 :
            m = dy / dx
        else:
            print("")
        #calculamos el valor de steps
        if(dx > dy):
            steps = dx
        else:
            steps = dy
        #Calculamos el incremento
        xinc = dx / steps
        yinc = dy / steps
        print(x1,y1)
        plt.scatter(x1,y1)
        #calculamos los nuevos valores de x y y
        i=1
        while(i<=steps):
            x1 = x1 + xinc
            y1 = y1 + yinc
            #Redondeamos los valores con el metodo round 
            x=round(x1)
            y=round(y1)
            i+=1
            print(x,y)
            plt.scatter(x,y)
        #**********************************************************************************************
        x1=8
        y1=0
        x2=12
        y2=4
        #calculamos la diferencia
        dx = x2-x1
        dy = y2-y1
        #calculamos la pendiente
        if dx !=0 :
            m = dy / dx
        else:
            print("")
        #calculamos el valor de steps
        if(dx > dy):
            steps = dx
        else:
            steps = dy
        #Calculamos el incremento
        xinc = dx / steps
        yinc = dy / steps
        print(x1,y1)
        plt.scatter(x1,y1)
        #calculamos los nuevos valores de x y y
        i=1
        while(i<=steps):
            x1 = x1 + xinc
            y1 = y1 + yinc
            #Redondeamos los valores con el metodo round 
            x=round(x1)
            y=round(y1)
            i+=1
            print(x,y)
            plt.scatter(x,y)
       #***********************************************************************************
        x1=0
        y1=4
        x2=4
        y2=8
        #calculamos la diferencia
        dx = x2-x1
        dy = y2-y1
        #calculamos la pendiente
        if dx !=0 :
            m = dy / dx
        else:
            print("")
        #calculamos el valor de steps
        if(dx > dy):
            steps = dx
        else:
            steps = dy
        #Calculamos el incremento
        xinc = dx / steps
        yinc = dy / steps
        print(x1,y1)
        plt.scatter(x1,y1)
        #calculamos los nuevos valores de x y y
        i=1
        while(i<=steps):
            x1 = x1 + xinc
            y1 = y1 + yinc
            #Redondeamos los valores con el metodo round 
            x=round(x1)
            y=round(y1)
            i+=1
            print(x,y)
            plt.scatter(x,y)
        #**********************************************************************************************
        x1=4
        y1=8
        x2=8
        y2=8
        #calculamos la diferencia
        dx = x2-x1
        dy = y2-y1
        #calculamos la pendiente
        if dx !=0 :
            m = dy / dx
        else:
            print("")
        #calculamos el valor de steps
        if(dx > dy):
            steps = dx
        else:
            steps = dy
        #Calculamos el incremento
        xinc = dx / steps
        yinc = dy / steps
        print(x1,y1)
        plt.scatter(x1,y1)
        #calculamos los nuevos valores de x y y
        i=1
        while(i<=steps):
            x1 = x1 + xinc
            y1 = y1 + yinc
            #Redondeamos los valores con el metodo round 
            x=round(x1)
            y=round(y1)
            i+=1
            print(x,y)
            plt.scatter(x,y)
        #**********************************************************************************************
        x1=8
        y1=8
        x2=12
        y2=4
        #calculamos la diferencia
        dx = x2-x1
        dy = y2-y1
        #calculamos la pendiente
        if dx !=0 :
            m = dy / dx
        else:
            print("")
        #calculamos el valor de steps
        if(dx > dy):
            steps = dx
        else:
            steps = dy
        #Calculamos el incremento
        xinc = dx / steps
        yinc = dy / steps
        print(x1,y1)
        plt.scatter(x1,y1)
        #calculamos los nuevos valores de x y y
        i=1
        while(i<=steps):
            x1 = x1 + xinc
            y1 = y1 + yinc
            #Redondeamos los valores con el metodo round 
            x=round(x1)
            y=round(y1)
            i+=1
            print(x,y)
            plt.scatter(x,y)
        plt.show()
    if lados == 7:
        print("Heptágono") 
        x1=3.3
        y1=0
        x2=0
        y2=2
        #calculamos la primera parte del cuadrado
        #calculamos la diferencia
        dx = x2-x1
        dy = y2-y1
        #calculamos la pendiente
        if dx !=0 :
            m = dy / dx
        else:
            print("")
        #calculamos el valor de steps
        if(dx > dy):
            steps = dx
        else:
            steps = dy
        #Calculamos el incremento
        xinc = dx / steps
        yinc = dy / steps
        print(x1,y1)
        plt.scatter(x1,y1)
        #calculamos los nuevos valores de x y y
        i=1
        while(i<=steps):
            x1 = x1 + xinc
            y1 = y1 + yinc
            #Redondeamos los valores con el metodo round 
            x=x1
            y=y1
            i+=1
            print(x,y)
            plt.scatter(x,y)
        #**********************************************************************************************
        x1=0
        y1=2
        x2=0
        y2=5.9
        #calculamos la primera parte del cuadrado
        #calculamos la diferencia
        dx = x2-x1
        dy = y2-y1
        #calculamos la pendiente
        if dx !=0 :
            m = dy / dx
        else:
            print("")
        #calculamos el valor de steps
        if(dx > dy):
            steps = dx
        else:
            steps = dy
        #Calculamos el incremento
        xinc = dx / steps
        yinc = dy / steps
        if xinc !=0 :
            print("Se puede")
        else:
            print("No se puede realizar una operacion entre cero")
        if yinc !=0 :
            print("Se puede")
        else:
            print("No se puede realizar una operacion entre cero")
        print(x1,y1)
        plt.scatter(x1,y1)
        #calculamos los nuevos valores de x y y
        i=1
        while(i<=steps):
            x1 = x1 + xinc
            y1 = y1 + yinc
            #Redondeamos los valores con el metodo round 
            x=x1
            y=y1
            i+=1
            print(x,y)
            plt.scatter(x,y)
        #**********************************************************************************************
        x1=0
        y1=5.9
        x2=3
        y2=8
        #calculamos la primera parte del cuadrado
        #calculamos la diferencia
        dx = x2-x1
        dy = y2-y1
        #calculamos la pendiente
        if dx !=0 :
            m = dy / dx
        else:
            print("")
        #calculamos el valor de steps
        if(dx > dy):
            steps = dx
        else:
            steps = dy
        #Calculamos el incremento
        xinc = dx / steps
        yinc = dy / steps
        print(x1,y1)
        plt.scatter(x1,y1)
        #calculamos los nuevos valores de x y y
        i=1
        while(i<=steps):
            x1 = x1 + xinc
            y1 = y1 + yinc
            #Redondeamos los valores con el metodo round 
            x=x1
            y=y1
            i+=1
            print(x,y)
            plt.scatter(x,y)
        #**********************************************************************************************
        x1=3
        y1=8
        x2=6.9
        y2=7
        #calculamos la primera parte del cuadrado
        #calculamos la diferencia
        dx = x2-x1
        dy = y2-y1
        #calculamos la pendiente
        if dx !=0 :
            m = dy / dx
        else:
            print("")
        #calculamos el valor de steps
        if(dx > dy):
            steps = dx
        else:
            steps = dy
        #Calculamos el incremento
        xinc = dx / steps
        yinc = dy / steps
        print(x1,y1)
        plt.scatter(x1,y1)
        #calculamos los nuevos valores de x y y
        i=1
        while(i<=steps):
            x1 = x1 + xinc
            y1 = y1 + yinc
            #Redondeamos los valores con el metodo round 
            x=x1
            y=y1
            i+=1
            print(x,y)
            plt.scatter(x,y)
        #**********************************************************************************************
        x1=8
        y1=4
        x2=6.9
        y2=7
        #calculamos la primera parte del cuadrado
        #calculamos la diferencia
        dx = x2-x1
        dy = y2-y1
        #calculamos la pendiente
        if dx !=0 :
            m = dy / dx
        else:
            print("")
        #calculamos el valor de steps
        if(dx > dy):
            steps = dx
        else:
            steps = dy
        #Calculamos el incremento
        xinc = dx / steps
        yinc = dy / steps
        print(x1,y1)
        plt.scatter(x1,y1)
        #calculamos los nuevos valores de x y y
        i=1
        while(i<=steps):
            x1 = x1 + xinc
            y1 = y1 + yinc
            #Redondeamos los valores con el metodo round 
            x=x1
            y=y1
            i+=1
            print(x,y)
            plt.scatter(x,y)
        #**********************************************************************************************
        x1=6.4
        y1=0.4
        x2=8
        y2=4
        #calculamos la primera parte del cuadrado
        #calculamos la diferencia
        dx = x2-x1
        dy = y2-y1
        #calculamos la pendiente
        if dx !=0 :
            m = dy / dx
        else:
            print("")
        #calculamos el valor de steps
        if(dx > dy):
            steps = dx
        else:
            steps = dy
        #Calculamos el incremento
        xinc = dx / steps
        yinc = dy / steps
        print(x1,y1)
        plt.scatter(x1,y1)
        #calculamos los nuevos valores de x y y
        i=1
        while(i<=steps):
            x1 = x1 + xinc
            y1 = y1 + yinc
            #Redondeamos los valores con el metodo round 
            x=x1
            y=y1
            i+=1
            print(x,y)
            plt.scatter(x,y)
        #**********************************************************************************************
        x1=3.3
        y1=0
        x2=6.5
        y2=.5
        #calculamos la primera parte del cuadrado
        #calculamos la diferencia
        dx = x2-x1
        dy = y2-y1
        #calculamos la pendiente
        if dx !=0 :
            m = dy / dx
        else:
            print("")
        #calculamos el valor de steps
        if(dx > dy):
            steps = dx
        else:
            steps = dy
        #Calculamos el incremento
        xinc = dx / steps
        yinc = dy / steps
        print(x1,y1)
        plt.scatter(x1,y1)
        #calculamos los nuevos valores de x y y
        i=1
        while(i<=steps):
            x1 = x1 + xinc
            y1 = y1 + yinc
            #Redondeamos los valores con el metodo round 
            x=x1
            y=y1
            i+=1
            print(x,y)
            plt.scatter(x,y)
        plt.show()
    if lados == 8:
        print("Octògono")
        x1=5
        y1=3
        x2=5
        y2=6
        #calculamos la diferencia
        dx = x2-x1
        dy = y2-y1
        #calculamos la pendiente
        if dx !=0 :
            m = dy / dx
        else:
            print("")
        #calculamos el valor de steps
        if(dx > dy):
            steps = dx
        else:
            steps = dy
        #Calculamos el incremento
        xinc = dx / steps
        yinc = dy / steps
        print(x1,y1)
        plt.scatter(x1,y1)
        #calculamos los nuevos valores de x y y
        i=1
        while(i<=steps):
            x1 = x1 + xinc
            y1 = y1 + yinc
            #Redondeamos los valores con el metodo round 
            x=round(x1)
            y=round(y1)
            i+=1
            print(x,y)
            plt.scatter(x,y)
        #**********************************************************************************************
        x1=5
        y1=3
        x2=6
        y2=1
        #calculamos la diferencia
        dx = x2-x1
        dy = y2-y1
        #calculamos la pendiente
        if dx !=0 :
            m = dy / dx
        else:
            print("")
        #calculamos el valor de steps
        if(dx > dy):
            steps = dx
        else:
            steps = dy
        #Calculamos el incremento
        xinc = dx / steps
        yinc = dy / steps
        if xinc !=0 :
            print("Se puede")
        else:
            print("No se puede realizar una operacion entre cero")
        if yinc !=0 :
            print("Se puede")
        else:
            print("No se puede realizar una operacion entre cero")
        print(x1,y1)
        plt.scatter(x1,y1)
        #calculamos los nuevos valores de x y y
        i=1
        while(i<=steps):
            x1 = x1 + xinc
            y1 = y1 + yinc
            #Redondeamos los valores con el metodo round 
            x=round(x1)
            y=round(y1)
            i+=1
            print(x,y)
            plt.scatter(x,y)
        #**********************************************************************************************
        x1=6
        y1=1
        x2=9
        y2=1
        #calculamos la diferencia
        dx = x2-x1
        dy = y2-y1
        #calculamos la pendiente
        if dx !=0 :
            m = dy / dx
        else:
            print("")
        #calculamos el valor de steps
        if(dx > dy):
            steps = dx
        else:
            steps = dy
        #Calculamos el incremento
        xinc = dx / steps
        yinc = dy / steps
        print(x1,y1)
        plt.scatter(x1,y1)
        #calculamos los nuevos valores de x y y
        i=1
        while(i<=steps):
            x1 = x1 + xinc
            y1 = y1 + yinc
            #Redondeamos los valores con el metodo round 
            x=round(x1)
            y=round(y1)
            i+=1
            print(x,y)
            plt.scatter(x,y)
        #**********************************************************************************************
        x1=9
        y1=1
        x2=11
        y2=3
        #calculamos la diferencia
        dx = x2-x1
        dy = y2-y1
        #calculamos la pendiente
        if dx !=0 :
            m = dy / dx
        else:
            print("")
        #calculamos el valor de steps
        if(dx > dy):
            steps = dx
        else:
            steps = dy
        #Calculamos el incremento
        xinc = dx / steps
        yinc = dy / steps
        print(x1,y1)
        plt.scatter(x1,y1)
        #calculamos los nuevos valores de x y y
        i=1
        while(i<=steps):
            x1 = x1 + xinc
            y1 = y1 + yinc
            #Redondeamos los valores con el metodo round 
            x=round(x1)
            y=round(y1)
            i+=1
            print(x,y)
            plt.scatter(x,y)
        #**********************************************************************************************
        x1=11
        y1=3
        x2=11
        y2=6
        #calculamos la diferencia
        dx = x2-x1
        dy = y2-y1
        #calculamos la pendiente
        if dx !=0 :
            m = dy / dx
        else:
            print("")
        #calculamos el valor de steps
        if(dx > dy):
            steps = dx
        else:
            steps = dy
        #Calculamos el incremento
        xinc = dx / steps
        yinc = dy / steps
        print(x1,y1)
        plt.scatter(x1,y1)
        #calculamos los nuevos valores de x y y
        i=1
        while(i<=steps):
            x1 = x1 + xinc
            y1 = y1 + yinc
            #Redondeamos los valores con el metodo round 
            x=round(x1)
            y=round(y1)
            i+=1
            print(x,y)
            plt.scatter(x,y)
        #**********************************************************************************************
        x1=5
        y1=6
        x2=6
        y2=8
        #calculamos la diferencia
        dx = x2-x1
        dy = y2-y1
        #calculamos la pendiente
        if dx !=0 :
            m = dy / dx
        else:
            print("")
        #calculamos el valor de steps
        if(dx > dy):
            steps = dx
        else:
            steps = dy
        #Calculamos el incremento
        xinc = dx / steps
        yinc = dy / steps
        print(x1,y1)
        plt.scatter(x1,y1)
        #calculamos los nuevos valores de x y y
        i=1
        while(i<=steps):
            x1 = x1 + xinc
            y1 = y1 + yinc
            #Redondeamos los valores con el metodo round 
            x=round(x1)
            y=round(y1)
            i+=1
            print(x,y)
            plt.scatter(x,y)
        #**********************************************************************************************
        x1=6
        y1=8
        x2=9
        y2=8
        #calculamos la diferencia
        dx = x2-x1
        dy = y2-y1
        #calculamos la pendiente
        if dx !=0 :
            m = dy / dx
        else:
            print("")
        #calculamos el valor de steps
        if(dx > dy):
            steps = dx
        else:
            steps = dy
        #Calculamos el incremento
        xinc = dx / steps
        yinc = dy / steps
        print(x1,y1)
        plt.scatter(x1,y1)
        #calculamos los nuevos valores de x y y
        i=1
        while(i<=steps):
            x1 = x1 + xinc
            y1 = y1 + yinc
            #Redondeamos los valores con el metodo round 
            x=round(x1)
            y=round(y1)
            i+=1
            print(x,y)
            plt.scatter(x,y)
        #**********************************************************************************************
        x1=9
        y1=8
        x2=11
        y2=6
        #calculamos la diferencia
        dx = x2-x1
        dy = y2-y1
        #calculamos la pendiente
        if dx !=0 :
            m = dy / dx
        else:
            print("")
        #calculamos el valor de steps
        if(dx > dy):
            steps = dx
        else:
            steps = dy
        #Calculamos el incremento
        xinc = dx / steps
        yinc = dy / steps
        print(x1,y1)
        plt.scatter(x1,y1)
        #calculamos los nuevos valores de x y y
        i=1
        while(i<=steps):
            x1 = x1 + xinc
            y1 = y1 + yinc
            #Redondeamos los valores con el metodo round 
            x=round(x1)
            y=round(y1)
            i+=1
            print(x,y)
            plt.scatter(x,y)
        plt.show()
    if lados == 9:
        print("Eneàgono")
        x1=5.7
        y1=0.3
        x2=2.5
        y2=0.7
        #calculamos la primera parte del cuadrado
        #calculamos la diferencia
        dx = x2-x1
        dy = y2-y1
        #calculamos la pendiente
        if dx !=0 :
            m = dy / dx
        else:
            print("")
        #calculamos el valor de steps
        if(dx > dy):
            steps = dx
        else:
            steps = dy
        #Calculamos el incremento
        xinc = dx / steps
        yinc = dy / steps
        print(x1,y1)
        plt.scatter(x1,y1)
        #calculamos los nuevos valores de x y y
        i=1
        while(i<=steps):
            x1 = x1 + xinc
            y1 = y1 + yinc
            #Redondeamos los valores con el metodo round 
            x=x1
            y=y1
            i+=1
            print(x,y)
            plt.scatter(x,y)
        #**********************************************************************************************
        x1=2.5
        y1=0.7
        x2=0.9
        y2=3
        #calculamos la primera parte del cuadrado
        #calculamos la diferencia
        dx = x2-x1
        dy = y2-y1
        #calculamos la pendiente
        if dx !=0 :
            m = dy / dx
        else:
            print("")
        #calculamos el valor de steps
        if(dx > dy):
            steps = dx
        else:
            steps = dy
        #Calculamos el incremento
        xinc = dx / steps
        yinc = dy / steps
        if xinc !=0 :
            print("Se puede")
        else:
            print("No se puede realizar una operacion entre cero")
        if yinc !=0 :
            print("Se puede")
        else:
            print("No se puede realizar una operacion entre cero")
        print(x1,y1)
        plt.scatter(x1,y1)
        #calculamos los nuevos valores de x y y
        i=1
        while(i<=steps):
            x1 = x1 + xinc
            y1 = y1 + yinc
            #Redondeamos los valores con el metodo round 
            x=x1
            y=y1
            i+=1
            print(x,y)
            plt.scatter(x,y)
        #**********************************************************************************************
        x1=0.9
        y1=3
        x2=1
        y2=5.4
        #calculamos la primera parte del cuadrado
        #calculamos la diferencia
        dx = x2-x1
        dy = y2-y1
        #calculamos la pendiente
        if dx !=0 :
            m = dy / dx
        else:
            print("")
        #calculamos el valor de steps
        if(dx > dy):
            steps = dx
        else:
            steps = dy
        #Calculamos el incremento
        xinc = dx / steps
        yinc = dy / steps
        print(x1,y1)
        plt.scatter(x1,y1)
        #calculamos los nuevos valores de x y y
        i=1
        while(i<=steps):
            x1 = x1 + xinc
            y1 = y1 + yinc
            #Redondeamos los valores con el metodo round 
            x=x1
            y=y1
            i+=1
            print(x,y)
            plt.scatter(x,y)
        #**********************************************************************************************
        x1=1
        y1=5.4
        x2=3
        y2=7.3
        #calculamos la primera parte del cuadrado
        #calculamos la diferencia
        dx = x2-x1
        dy = y2-y1
        #calculamos la pendiente
        if dx !=0 :
            m = dy / dx
        else:
            print("")
        #calculamos el valor de steps
        if(dx > dy):
            steps = dx
        else:
            steps = dy
        #Calculamos el incremento
        xinc = dx / steps
        yinc = dy / steps
        print(x1,y1)
        plt.scatter(x1,y1)
        #calculamos los nuevos valores de x y y
        i=1
        while(i<=steps):
            x1 = x1 + xinc
            y1 = y1 + yinc
            #Redondeamos los valores con el metodo round 
            x=x1
            y=y1
            i+=1
            print(x,y)
            plt.scatter(x,y)
        #**********************************************************************************************
        x1=3
        y1=7.3
        x2=5.8
        y2=7.8
        #calculamos la primera parte del cuadrado
        #calculamos la diferencia
        dx = x2-x1
        dy = y2-y1
        #calculamos la pendiente
        if dx !=0 :
            m = dy / dx
        else:
            print("")
        #calculamos el valor de steps
        if(dx > dy):
            steps = dx
        else:
            steps = dy
        #Calculamos el incremento
        xinc = dx / steps
        yinc = dy / steps
        print(x1,y1)
        plt.scatter(x1,y1)
        #calculamos los nuevos valores de x y y
        i=1
        while(i<=steps):
            x1 = x1 + xinc
            y1 = y1 + yinc
            #Redondeamos los valores con el metodo round 
            x=x1
            y=y1
            i+=1
            print(x,y)
            plt.scatter(x,y)
        #**********************************************************************************************
        x1=5.8
        y1=7.8
        x2=8.2
        y2=6.5
        #calculamos la primera parte del cuadrado
        #calculamos la diferencia
        dx = x2-x1
        dy = y2-y1
        #calculamos la pendiente
        if dx !=0 :
            m = dy / dx
        else:
            print("")
        #calculamos el valor de steps
        if(dx > dy):
            steps = dx
        else:
            steps = dy
        #Calculamos el incremento
        xinc = dx / steps
        yinc = dy / steps
        print(x1,y1)
        plt.scatter(x1,y1)
        #calculamos los nuevos valores de x y y
        i=1
        while(i<=steps):
            x1 = x1 + xinc
            y1 = y1 + yinc
            #Redondeamos los valores con el metodo round 
            x=x1
            y=y1
            i+=1
            print(x,y)
            plt.scatter(x,y)
        #**********************************************************************************************
        x1=8.2
        y1=6.5
        x2=9
        y2=4
        #calculamos la primera parte del cuadrado
        #calculamos la diferencia
        dx = x2-x1
        dy = y2-y1
        #calculamos la pendiente
        if dx !=0 :
            m = dy / dx
        else:
            print("")
        #calculamos el valor de steps
        if(dx > dy):
            steps = dx
        else:
            steps = dy
        #Calculamos el incremento
        xinc = dx / steps
        yinc = dy / steps
        print(x1,y1)
        plt.scatter(x1,y1)
        #calculamos los nuevos valores de x y y
        i=1
        while(i<=steps):
            x1 = x1 + xinc
            y1 = y1 + yinc
            #Redondeamos los valores con el metodo round 
            x=x1
            y=y1
            i+=1
            print(x,y)
            plt.scatter(x,y)
        #**********************************************************************************************
        x1=9
        y1=4
        x2=8.2
        y2=1.5
        #calculamos la primera parte del cuadrado
        #calculamos la diferencia
        dx = x2-x1
        dy = y2-y1
        #calculamos la pendiente
        if dx !=0 :
            m = dy / dx
        else:
            print("")
        #calculamos el valor de steps
        if(dx > dy):
            steps = dx
        else:
            steps = dy
        #Calculamos el incremento
        xinc = dx / steps
        yinc = dy / steps
        print(x1,y1)
        plt.scatter(x1,y1)
        #calculamos los nuevos valores de x y y
        i=1
        while(i<=steps):
            x1 = x1 + xinc
            y1 = y1 + yinc
            #Redondeamos los valores con el metodo round 
            x=x1
            y=y1
            i+=1
            print(x,y)
            plt.scatter(x,y)
        #**********************************************************************************************
        x1=5.4
        y1=0.3
        x2=8.2
        y2=1.5
        #calculamos la primera parte del cuadrado
        #calculamos la diferencia
        dx = x2-x1
        dy = y2-y1
        #calculamos la pendiente
        if dx !=0 :
            m = dy / dx
        else:
            print("")
        #calculamos el valor de steps
        if(dx > dy):
            steps = dx
        else:
            steps = dy
        #Calculamos el incremento
        xinc = dx / steps
        yinc = dy / steps
        print(x1,y1)
        plt.scatter(x1,y1)
        #calculamos los nuevos valores de x y y
        i=1
        while(i<=steps):
            x1 = x1 + xinc
            y1 = y1 + yinc
            #Redondeamos los valores con el metodo round 
            x=x1
            y=y1
            i+=1
            print(x,y)
            plt.scatter(x,y)
        plt.show()
    if lados == 10:
        print("Decàgono")
        x1=0.8
        y1=4
        x2=1.8
        y2=1.8
        #calculamos la diferencia
        dx = x2-x1
        dy = y2-y1
        #calculamos la pendiente
        if dx !=0 :
            m = dy / dx
        else:
            print("")
        #calculamos el valor de steps
        if(dx > dy):
            steps = dx
        else:
            steps = dy
        #Calculamos el incremento
        xinc = dx / steps
        yinc = dy / steps
        print(x1,y1)
        plt.scatter(x1,y1)
        #calculamos los nuevos valores de x y y
        i=1
        while(i<=steps):
            x1 = x1 + xinc
            y1 = y1 + yinc
            #Redondeamos los valores con el metodo round 
            x=x1
            y=y1
            i+=1
            print(x,y)
            plt.scatter(x,y)
        #************************************************************************************************
        x1=0.8
        y1=4
        x2=1.8
        y2=6.3
        #calculamos la diferencia
        dx = x2-x1
        dy = y2-y1
        #calculamos la pendiente
        if dx !=0 :
            m = dy / dx
        else:
            print("")
        #calculamos el valor de steps
        if(dx > dy):
            steps = dx
        else:
            steps = dy
        #Calculamos el incremento
        xinc = dx / steps
        yinc = dy / steps
        print(x1,y1)
        plt.scatter(x1,y1)
        #calculamos los nuevos valores de x y y
        i=1
        while(i<=steps):
            x1 = x1 + xinc
            y1 = y1 + yinc
            #Redondeamos los valores con el metodo round 
            x=x1
            y=y1
            i+=1
            print(x,y)
            plt.scatter(x,y)
        #************************************************************************************************
        x1=1.8
        y1=6.3
        x2=3.6
        y2=7.8
        #calculamos la diferencia
        dx = x2-x1
        dy = y2-y1
        #calculamos la pendiente
        if dx !=0 :
            m = dy / dx
        else:
            print("")
        #calculamos el valor de steps
        if(dx > dy):
            steps = dx
        else:
            steps = dy
        #Calculamos el incremento
        xinc = dx / steps
        yinc = dy / steps
        print(x1,y1)
        plt.scatter(x1,y1)
        #calculamos los nuevos valores de x y y
        i=1
        while(i<=steps):
            x1 = x1 + xinc
            y1 = y1 + yinc
            #Redondeamos los valores con el metodo round 
            x=x1
            y=y1
            i+=1
            print(x,y)
            plt.scatter(x,y)
        #************************************************************************************************
        x1=3.6
        y1=7.8
        x2=5.8
        y2=7.8
        #calculamos la diferencia
        dx = x2-x1
        dy = y2-y1
        #calculamos la pendiente
        if dx !=0 :
            m = dy / dx
        else:
            print("")
        #calculamos el valor de steps
        if(dx > dy):
            steps = dx
        else:
            steps = dy
        #Calculamos el incremento
        xinc = dx / steps
        yinc = dy / steps
        print(x1,y1)
        plt.scatter(x1,y1)
        #calculamos los nuevos valores de x y y
        i=1
        while(i<=steps):
            x1 = x1 + xinc
            y1 = y1 + yinc
            #Redondeamos los valores con el metodo round 
            x=x1
            y=y1
            i+=1
            print(x,y)
            plt.scatter(x,y)
        #************************************************************************************************
        x1=3.8
        y=0.4
        x2=1.8
        y2=1.8
        #calculamos la diferencia
        dx = x2-x1
        dy = y2-y1
        #calculamos la pendiente
        if dx !=0 :
            m = dy / dx
        else:
            print("")
        #calculamos el valor de steps
        if(dx > dy):
            steps = dx
        else:
            steps = dy
        #Calculamos el incremento
        xinc = dx / steps
        yinc = dy / steps
        print(x1,y1)
        plt.scatter(x1,y1)
        #calculamos los nuevos valores de x y y
        i=1
        while(i<=steps):
            x1 = x1 + xinc
            y1 = y1 + yinc
            #Redondeamos los valores con el metodo round 
            x=x1
            y=y1
            i+=1
            print(x,y)
            plt.scatter(x,y)
        #************************************************************************************************
        x1=3.8
        y1=0.4
        x2=6.3
        y2=0.4
        #calculamos la diferencia
        dx = x2-x1
        dy = y2-y1
        #calculamos la pendiente
        if dx !=0 :
            m = dy / dx
        else:
            print("")
        #calculamos el valor de steps
        if(dx > dy):
            steps = dx
        else:
            steps = dy
        #Calculamos el incremento
        xinc = dx / steps
        yinc = dy / steps
        print(x1,y1)
        plt.scatter(x1,y1)
        #calculamos los nuevos valores de x y y
        i=1
        while(i<=steps):
            x1 = x1 + xinc
            y1 = y1 + yinc
            #Redondeamos los valores con el metodo round 
            x=x1
            y=y1
            i+=1
            print(x,y)
            plt.scatter(x,y)
        #************************************************************************************************
        x1=6.3
        y1=0.4
        x2=8.5
        y2=1.9
        #calculamos la diferencia
        dx = x2-x1
        dy = y2-y1
        #calculamos la pendiente
        if dx !=0 :
            m = dy / dx
        else:
            print("")
        #calculamos el valor de steps
        if(dx > dy):
            steps = dx
        else:
            steps = dy
        #Calculamos el incremento
        xinc = dx / steps
        yinc = dy / steps
        print(x1,y1)
        plt.scatter(x1,y1)
        #calculamos los nuevos valores de x y y
        i=1
        while(i<=steps):
            x1 = x1 + xinc
            y1 = y1 + yinc
            #Redondeamos los valores con el metodo round 
            x=x1
            y=y1
            i+=1
            print(x,y)
            plt.scatter(x,y)
        #************************************************************************************************
        x1=8.5
        y1=1.9
        x2=9.2
        y2=4
        #calculamos la diferencia
        dx = x2-x1
        dy = y2-y1
        #calculamos la pendiente
        if dx !=0 :
            m = dy / dx
        else:
            print("")
        #calculamos el valor de steps
        if(dx > dy):
            steps = dx
        else:
            steps = dy
        #Calculamos el incremento
        xinc = dx / steps
        yinc = dy / steps
        print(x1,y1)
        plt.scatter(x1,y1)
        #calculamos los nuevos valores de x y y
        i=1
        while(i<=steps):
            x1 = x1 + xinc
            y1 = y1 + yinc
            #Redondeamos los valores con el metodo round 
            x=x1
            y=y1
            i+=1
            print(x,y)
            plt.scatter(x,y)
        #************************************************************************************************
        x1=8.5
        y1=6.2
        x2=9.2
        y2=4
        #calculamos la diferencia
        dx = x2-x1
        dy = y2-y1
        #calculamos la pendiente
        if dx !=0 :
            m = dy / dx
        else:
            print("")
        #calculamos el valor de steps
        if(dx > dy):
            steps = dx
        else:
            steps = dy
        #Calculamos el incremento
        xinc = dx / steps
        yinc = dy / steps
        print(x1,y1)
        plt.scatter(x1,y1)
        #calculamos los nuevos valores de x y y
        i=1
        while(i<=steps):
            x1 = x1 + xinc
            y1 = y1 + yinc
            #Redondeamos los valores con el metodo round 
            x=x1
            y=y1
            i+=1
            print(x,y)
            plt.scatter(x,y)
        #************************************************************************************************
        x1=6.5
        y1=7.8
        x2=8.5
        y2=6.2
        #calculamos la diferencia
        dx = x2-x1
        dy = y2-y1
        #calculamos la pendiente
        if dx !=0 :
            m = dy / dx
        else:
            print("")
        #calculamos el valor de steps
        if(dx > dy):
            steps = dx
        else:
            steps = dy
        #Calculamos el incremento
        xinc = dx / steps
        yinc = dy / steps
        print(x1,y1)
        plt.scatter(x1,y1)
        #calculamos los nuevos valores de x y y
        i=1
        while(i<=steps):
            x1 = x1 + xinc
            y1 = y1 + yinc
            #Redondeamos los valores con el metodo round 
            x=x1
            y=y1
            i+=1
            print(x,y)
            plt.scatter(x,y)
        plt.show()
    else:
        print(lados,"Esa figura no se puede construir por el tamaño")
#Si la respuesta es 2 entrara al segundo if y se se graficara por Bresenham
if respuesta == 2:
    print("Algoritmo Bresenham")
    lados = int(input("Ingresa el numero de lado del pologinos a graficar: "))
    if lados == 3:
        print("Triangulo Equilatero")
        #Declaramos las variables que recibiran los valores
        x1=3
        y1=1
        x2=9
        y2=1
        #calculamos la diferencia
        dx = x2-x1
        dy = y2-y1
        #calculamos a p
        p = 2*dy - dx
        plt.scatter(x2,y2)
        #calculamos los nuevos valores de x y y
        while(x1<x2):
            plt.scatter(x1,y1)
            x1=x1+1
            if dy<0:
                if p<0:
                    p=p+2*dy
                    y1=y1-1
                else:
                    p=p + (2*dy)-(2*dx)
            else:
                if p<0:
                    p=p+2*dy
                else:
                    p = p + (2*dy)-(2*dx)
                    y1=y1+1
            print(x1,y1)
        #D************************************************************************************************
        x1=3
        y1=1
        x2=6
        y2=4
        #calculamos la diferencia
        dx = x2-x1
        dy = y2-y1
        #calculamos a p
        p = 2*dy - dx
        plt.scatter(x2,y2)
        #calculamos los nuevos valores de x y y
        while(x1<x2):
            plt.scatter(x1,y1)
            x1=x1+1
            if dy<0:
                if p<0:
                    p=p+2*dy
                    y1=y1-1
                else:
                    p=p + (2*dy)-(2*dx)
            else:
                if p<0:
                    p=p+2*dy
                else:
                    p = p + (2*dy)-(2*dx)
                    y1=y1+1
            print(x1,y1)
        #D************************************************************************************************
        x1=6
        y1=4
        x2=9
        y2=1
        #calculamos la diferencia
        dx = x2-x1
        dy = y2-y1
        #calculamos a p
        p = 2*dy - dx
        plt.scatter(x2,y2)
        #calculamos los nuevos valores de x y y
        while(x1<x2):
            plt.scatter(x1,y1)
            x1=x1+1
            if dy<0:
                if p<0:
                    p=p+2*dy
                    y1=y1-1
                else:
                    p=p + (2*dy)-(2*dx)
            else:
                if p<0:
                    p=p+2*dy
                else:
                    p = p + (2*dy)-(2*dx)
                    y1=y1+1
            print(x1,y1)
        plt.show()
    if lados == 4:
        print("Cuadrilatero")
        #Declaramos las variables que recibiran los valores
        x1=0
        y1=0
        x2=0
        y2=1
        #calculamos la diferencia
        dx = x2-x1
        dy = y2-y1
        #calculamos a p
        p = 2*dy - dx
        plt.scatter(x2,y2)
        #calculamos los nuevos valores de x y y
        while(x1<x2):
            plt.scatter(x1,y1)
            x1=x1+1
            if dy<0:
                if p<0:
                    p=p+2*dy
                    y1=y1-1
                else:
                    p=p + (2*dy)-(2*dx)
            else:
                if p<0:
                    p=p+2*dy
                else:
                    p = p + (2*dy)-(2*dx)
                    y1=y1+1
            print(x1,y1)
        #D************************************************************************************************
        x1=0
        y1=1
        x2=1
        y2=1
        #calculamos la diferencia
        dx = x2-x1
        dy = y2-y1
        #calculamos a p
        p = 2*dy - dx
        plt.scatter(x2,y2)
        #calculamos los nuevos valores de x y y
        while(x1<x2):
            plt.scatter(x1,y1)
            x1=x1+1
            if dy<0:
                if p<0:
                    p=p+2*dy
                    y1=y1-1
                else:
                    p=p + (2*dy)-(2*dx)
            else:
                if p<0:
                    p=p+2*dy
                else:
                    p = p + (2*dy)-(2*dx)
                    y1=y1+1
            print(x1,y1)
        #D************************************************************************************************
        x1=0
        y1=0
        x2=1
        y2=0
        #calculamos la diferencia
        dx = x2-x1
        dy = y2-y1
        #calculamos a p
        p = 2*dy - dx
        plt.scatter(x2,y2)
        #calculamos los nuevos valores de x y y
        while(x1<x2):
            plt.scatter(x1,y1)
            x1=x1+1
            if dy<0:
                if p<0:
                    p=p+2*dy
                    y1=y1-1
                else:
                    p=p + (2*dy)-(2*dx)
            else:
                if p<0:
                    p=p+2*dy
                else:
                    p = p + (2*dy)-(2*dx)
                    y1=y1+1
            print(x1,y1)
        #D************************************************************************************************
        x1=1
        y1=0
        x2=1
        y2=1
        #calculamos la diferencia
        dx = x2-x1
        dy = y2-y1
        #calculamos a p
        p = 2*dy - dx
        plt.scatter(x2,y2)
        #calculamos los nuevos valores de x y y
        while(x1<x2):
            plt.scatter(x1,y1)
            x1=x1+1
            if dy<0:
                if p<0:
                    p=p+2*dy
                    y1=y1-1
                else:
                    p=p + (2*dy)-(2*dx)
            else:
                if p<0:
                    p=p+2*dy
                else:
                    p = p + (2*dy)-(2*dx)
                    y1=y1+1
            print(x1,y1)
        plt.show()
    if lados == 5:
        print("Pentagono")
        #Declaramos las variables que recibiran los valores
        x1=1
        y1=0
        x2=3
        y2=0
        #calculamos la diferencia
        dx = x2-x1
        dy = y2-y1
        #calculamos a p
        p = 2*dy - dx
        plt.scatter(x2,y2)
        #calculamos los nuevos valores de x y y
        while(x1<x2):
            plt.scatter(x1,y1)
            x1=x1+1
            if dy<0:
                if p<0:
                    p=p+2*dy
                    y1=y1-1
                else:
                    p=p + (2*dy)-(2*dx)
            else:
                if p<0:
                    p=p+2*dy
                else:
                    p = p + (2*dy)-(2*dx)
                    y1=y1+1
            print(x1,y1)
        #*********************************************************************************************
        x1=1
        y1=0
        x2=0
        y2=2
        #calculamos la diferencia
        dx = x2-x1
        dy = y2-y1
        #calculamos a p
        p = 2*dy - dx
        plt.scatter(x2,y2)
        #calculamos los nuevos valores de x y y
        while(x1<x2):
            plt.scatter(x1,y1)
            x1=x1+1
            if dy<0:
                if p<0:
                    p=p+2*dy
                    y1=y1-1
                else:
                    p=p + (2*dy)-(2*dx)
            else:
                if p<0:
                    p=p+2*dy
                else:
                    p = p + (2*dy)-(2*dx)
                    y1=y1+1
            print(x1,y1)
        #*********************************************************************************************
        x1=0
        y1=2
        x2=2
        y2=3
        #calculamos la diferencia
        dx = x2-x1
        dy = y2-y1
        #calculamos a p
        p = 2*dy - dx
        plt.scatter(x2,y2)
        #calculamos los nuevos valores de x y y
        while(x1<x2):
            plt.scatter(x1,y1)
            x1=x1+1
            if dy<0:
                if p<0:
                    p=p+2*dy
                    y1=y1-1
                else:
                    p=p + (2*dy)-(2*dx)
            else:
                if p<0:
                    p=p+2*dy
                else:
                    p = p + (2*dy)-(2*dx)
                    y1=y1+1
            print(x1,y1)
        #*********************************************************************************************
        x1=2
        y1=3
        x2=4
        y2=2
        #calculamos la diferencia
        dx = x2-x1
        dy = y2-y1
        #calculamos a p
        p = 2*dy - dx
        plt.scatter(x2,y2)
        #calculamos los nuevos valores de x y y
        while(x1<x2):
            plt.scatter(x1,y1)
            x1=x1+1
            if dy<0:
                if p<0:
                    p=p+2*dy
                    y1=y1-1
                else:
                    p=p + (2*dy)-(2*dx)
            else:
                if p<0:
                    p=p+2*dy
                else:
                    p = p + (2*dy)-(2*dx)
                    y1=y1+1
            print(x1,y1)
        #*********************************************************************************************
        x1=3
        y1=0
        x2=4
        y2=2
        #calculamos la diferencia
        dx = x2-x1
        dy = y2-y1
        #calculamos a p
        p = 2*dy - dx
        plt.scatter(x2,y2)
        #calculamos los nuevos valores de x y y
        while(x1<x2):
            plt.scatter(x1,y1)
            x1=x1+1
            if dy<0:
                if p<0:
                    p=p+2*dy
                    y1=y1-1
                else:
                    p=p + (2*dy)-(2*dx)
            else:
                if p<0:
                    p=p+2*dy
                else:
                    p = p + (2*dy)-(2*dx)
                    y1=y1+1
            print(x1,y1)
        plt.show()
    if lados == 6:
        print("Hexagono")
        #Declaramos las variables que recibiran los valores
        x1=0
        y1=4
        x2=4
        y2=0
        #calculamos la diferencia
        dx = x2-x1
        dy = y2-y1
        #calculamos a p
        p = 2*dy - dx
        plt.scatter(x2,y2)
        #calculamos los nuevos valores de x y y
        while(x1<x2):
            plt.scatter(x1,y1)
            x1=x1+1
            if dy<0:
                if p<0:
                    p=p+2*dy
                    y1=y1-1
                else:
                    p=p + (2*dy)-(2*dx)
            else:
                if p<0:
                    p=p+2*dy
                else:
                    p = p + (2*dy)-(2*dx)
                    y1=y1+1
            print(x1,y1)
        #D************************************************************************************************
        x1=0
        y1=4
        x2=4
        y2=8
        #calculamos la diferencia
        dx = x2-x1
        dy = y2-y1
        #calculamos a p
        p = 2*dy - dx
        plt.scatter(x2,y2)
        #calculamos los nuevos valores de x y y
        while(x1<x2):
            plt.scatter(x1,y1)
            x1=x1+1
            if dy<0:
                if p<0:
                    p=p+2*dy
                    y1=y1-1
                else:
                    p=p + (2*dy)-(2*dx)
            else:
                if p<0:
                    p=p+2*dy
                else:
                    p = p + (2*dy)-(2*dx)
                    y1=y1+1
            print(x1,y1)
        #D************************************************************************************************
        x1=4
        y1=8
        x2=8
        y2=8
        #calculamos la diferencia
        dx = x2-x1
        dy = y2-y1
        #calculamos a p
        p = 2*dy - dx
        plt.scatter(x2,y2)
        #calculamos los nuevos valores de x y y
        while(x1<x2):
            plt.scatter(x1,y1)
            x1=x1+1
            if dy<0:
                if p<0:
                    p=p+2*dy
                    y1=y1-1
                else:
                    p=p + (2*dy)-(2*dx)
            else:
                if p<0:
                    p=p+2*dy
                else:
                    p = p + (2*dy)-(2*dx)
                    y1=y1+1
            print(x1,y1)
        #D************************************************************************************************
        x1=4
        y1=0
        x2=8
        y2=0
        #calculamos la diferencia
        dx = x2-x1
        dy = y2-y1
        #calculamos a p
        p = 2*dy - dx
        plt.scatter(x2,y2)
        #calculamos los nuevos valores de x y y
        while(x1<x2):
            plt.scatter(x1,y1)
            x1=x1+1
            if dy<0:
                if p<0:
                    p=p+2*dy
                    y1=y1-1
                else:
                    p=p + (2*dy)-(2*dx)
            else:
                if p<0:
                    p=p+2*dy
                else:
                    p = p + (2*dy)-(2*dx)
                    y1=y1+1
            print(x1,y1)
        #D************************************************************************************************
        x1=8
        y1=0
        x2=12
        y2=4
        #calculamos la diferencia
        dx = x2-x1
        dy = y2-y1
        #calculamos a p
        p = 2*dy - dx
        plt.scatter(x2,y2)
        #calculamos los nuevos valores de x y y
        while(x1<x2):
            plt.scatter(x1,y1)
            x1=x1+1
            if dy<0:
                if p<0:
                    p=p+2*dy
                    y1=y1-1
                else:
                    p=p + (2*dy)-(2*dx)
            else:
                if p<0:
                    p=p+2*dy
                else:
                    p = p + (2*dy)-(2*dx)
                    y1=y1+1
            print(x1,y1)
        #D************************************************************************************************
        x1=8
        y1=8
        x2=12
        y2=4
        #calculamos la diferencia
        dx = x2-x1
        dy = y2-y1
        #calculamos a p
        p = 2*dy - dx
        plt.scatter(x2,y2)
        #calculamos los nuevos valores de x y y
        while(x1<x2):
            plt.scatter(x1,y1)
            x1=x1+1
            if dy<0:
                if p<0:
                    p=p+2*dy
                    y1=y1-1
                else:
                    p=p + (2*dy)-(2*dx)
            else:
                if p<0:
                    p=p+2*dy
                else:
                    p = p + (2*dy)-(2*dx)
                    y1=y1+1
            print(x1,y1)
        plt.show()
    if lados == 7:
        print("Heptágono") 
        #Declaramos las variables que recibiran los valores
        x1=3.3
        y1=0
        x2=0
        y2=2
        #calculamos la diferencia
        dx = x2-x1
        dy = y2-y1
        #calculamos a p
        p = 2*dy - dx
        plt.scatter(x2,y2)
        #calculamos los nuevos valores de x y y
        while(x1<x2):
            plt.scatter(x1,y1)
            x1=x1+1
            if dy<0:
                if p<0:
                    p=p+2*dy
                    y1=y1-1
                else:
                    p=p + (2*dy)-(2*dx)
            else:
                if p<0:
                    p=p+2*dy
                else:
                    p = p + (2*dy)-(2*dx)
                    y1=y1+1
            print(x1,y1)
        #*********************************************************************************************
        x1=0
        y1=2
        x2=0
        y2=5.9
        #calculamos la diferencia
        dx = x2-x1
        dy = y2-y1
        #calculamos a p
        p = 2*dy - dx
        plt.scatter(x2,y2)
        #calculamos los nuevos valores de x y y
        while(x1<x2):
            plt.scatter(x1,y1)
            x1=x1+1
            if dy<0:
                if p<0:
                    p=p+2*dy
                    y1=y1-1
                else:
                    p=p + (2*dy)-(2*dx)
            else:
                if p<0:
                    p=p+2*dy
                else:
                    p = p + (2*dy)-(2*dx)
                    y1=y1+1
            print(x1,y1)
        #*********************************************************************************************
        x1=0
        y1=5.9
        x2=3
        y2=8
        #calculamos la diferencia
        dx = x2-x1
        dy = y2-y1
        #calculamos a p
        p = 2*dy - dx
        plt.scatter(x2,y2)
        #calculamos los nuevos valores de x y y
        while(x1<x2):
            plt.scatter(x1,y1)
            x1=x1+1
            if dy<0:
                if p<0:
                    p=p+2*dy
                    y1=y1-1
                else:
                    p=p + (2*dy)-(2*dx)
            else:
                if p<0:
                    p=p+2*dy
                else:
                    p = p + (2*dy)-(2*dx)
                    y1=y1+1
            print(x1,y1)
        #*********************************************************************************************
        x1=3
        y1=8
        x2=6.9
        y2=7
        #calculamos la diferencia
        dx = x2-x1
        dy = y2-y1
        #calculamos a p
        p = 2*dy - dx
        plt.scatter(x2,y2)
        #calculamos los nuevos valores de x y y
        while(x1<x2):
            plt.scatter(x1,y1)
            x1=x1+1
            if dy<0:
                if p<0:
                    p=p+2*dy
                    y1=y1-1
                else:
                    p=p + (2*dy)-(2*dx)
            else:
                if p<0:
                    p=p+2*dy
                else:
                    p = p + (2*dy)-(2*dx)
                    y1=y1+1
            print(x1,y1)
        #*********************************************************************************************
        x1=8
        y1=4
        x2=6.9
        y2=7
        #calculamos la diferencia
        dx = x2-x1
        dy = y2-y1
        #calculamos a p
        p = 2*dy - dx
        plt.scatter(x2,y2)
        #calculamos los nuevos valores de x y y
        while(x1<x2):
            plt.scatter(x1,y1)
            x1=x1+1
            if dy<0:
                if p<0:
                    p=p+2*dy
                    y1=y1-1
                else:
                    p=p + (2*dy)-(2*dx)
            else:
                if p<0:
                    p=p+2*dy
                else:
                    p = p + (2*dy)-(2*dx)
                    y1=y1+1
            print(x1,y1)
        #*********************************************************************************************
        x1=6.4
        y1=0.4
        x2=8
        y2=4
        #calculamos la diferencia
        dx = x2-x1
        dy = y2-y1
        #calculamos a p
        p = 2*dy - dx
        plt.scatter(x2,y2)
        #calculamos los nuevos valores de x y y
        while(x1<x2):
            plt.scatter(x1,y1)
            x1=x1+1
            if dy<0:
                if p<0:
                    p=p+2*dy
                    y1=y1-1
                else:
                    p=p + (2*dy)-(2*dx)
            else:
                if p<0:
                    p=p+2*dy
                else:
                    p = p + (2*dy)-(2*dx)
                    y1=y1+1
            print(x1,y1)
        #*********************************************************************************************
        x1=3.3
        y1=0
        x2=6.5
        y2=.5
        #calculamos la diferencia
        dx = x2-x1
        dy = y2-y1
        #calculamos a p
        p = 2*dy - dx
        plt.scatter(x2,y2)
        #calculamos los nuevos valores de x y y
        while(x1<x2):
            plt.scatter(x1,y1)
            x1=x1+1
            if dy<0:
                if p<0:
                    p=p+2*dy
                    y1=y1-1
                else:
                    p=p + (2*dy)-(2*dx)
            else:
                if p<0:
                    p=p+2*dy
                else:
                    p = p + (2*dy)-(2*dx)
                    y1=y1+1
            print(x1,y1)
        plt.show()
    if lados == 8:
        print("Octògono")
        #Declaramos las variables que recibiran los valores
        x1=5
        y1=3
        x2=5
        y2=6
        #calculamos la diferencia
        dx = x2-x1
        dy = y2-y1
        #calculamos a p
        p = 2*dy - dx
        plt.scatter(x2,y2)
        #calculamos los nuevos valores de x y y
        while(x1<x2):
            plt.scatter(x1,y1)
            x1=x1+1
            if dy<0:
                if p<0:
                    p=p+2*dy
                    y1=y1-1
                else:
                    p=p + (2*dy)-(2*dx)
            else:
                if p<0:
                    p=p+2*dy
                else:
                    p = p + (2*dy)-(2*dx)
                    y1=y1+1
            print(x1,y1)
        #*********************************************************************************************
        x1=5
        y1=3
        x2=6
        y2=1
        #calculamos la diferencia
        dx = x2-x1
        dy = y2-y1
        #calculamos a p
        p = 2*dy - dx
        plt.scatter(x2,y2)
        #calculamos los nuevos valores de x y y
        while(x1<x2):
            plt.scatter(x1,y1)
            x1=x1+1
            if dy<0:
                if p<0:
                    p=p+2*dy
                    y1=y1-1
                else:
                    p=p + (2*dy)-(2*dx)
            else:
                if p<0:
                    p=p+2*dy
                else:
                    p = p + (2*dy)-(2*dx)
                    y1=y1+1
            print(x1,y1)
        #*********************************************************************************************
        x1=6
        y1=1
        x2=9
        y2=1
        #calculamos la diferencia
        dx = x2-x1
        dy = y2-y1
        #calculamos a p
        p = 2*dy - dx
        plt.scatter(x2,y2)
        #calculamos los nuevos valores de x y y
        while(x1<x2):
            plt.scatter(x1,y1)
            x1=x1+1
            if dy<0:
                if p<0:
                    p=p+2*dy
                    y1=y1-1
                else:
                    p=p + (2*dy)-(2*dx)
            else:
                if p<0:
                    p=p+2*dy
                else:
                    p = p + (2*dy)-(2*dx)
                    y1=y1+1
            print(x1,y1)
        #*********************************************************************************************
        x1=9
        y1=1
        x2=11
        y2=3
        #calculamos la diferencia
        dx = x2-x1
        dy = y2-y1
        #calculamos a p
        p = 2*dy - dx
        plt.scatter(x2,y2)
        #calculamos los nuevos valores de x y y
        while(x1<x2):
            plt.scatter(x1,y1)
            x1=x1+1
            if dy<0:
                if p<0:
                    p=p+2*dy
                    y1=y1-1
                else:
                    p=p + (2*dy)-(2*dx)
            else:
                if p<0:
                    p=p+2*dy
                else:
                    p = p + (2*dy)-(2*dx)
                    y1=y1+1
            print(x1,y1)
        #*********************************************************************************************
        x1=11
        y1=3
        x2=11
        y2=6
        #calculamos la diferencia
        dx = x2-x1
        dy = y2-y1
        #calculamos a p
        p = 2*dy - dx
        plt.scatter(x2,y2)
        #calculamos los nuevos valores de x y y
        while(x1<x2):
            plt.scatter(x1,y1)
            x1=x1+1
            if dy<0:
                if p<0:
                    p=p+2*dy
                    y1=y1-1
                else:
                    p=p + (2*dy)-(2*dx)
            else:
                if p<0:
                    p=p+2*dy
                else:
                    p = p + (2*dy)-(2*dx)
                    y1=y1+1
            print(x1,y1)
        #*********************************************************************************************
        x1=5
        y1=6
        x2=6
        y2=8
        #calculamos la diferencia
        dx = x2-x1
        dy = y2-y1
        #calculamos a p
        p = 2*dy - dx
        plt.scatter(x2,y2)
        #calculamos los nuevos valores de x y y
        while(x1<x2):
            plt.scatter(x1,y1)
            x1=x1+1
            if dy<0:
                if p<0:
                    p=p+2*dy
                    y1=y1-1
                else:
                    p=p + (2*dy)-(2*dx)
            else:
                if p<0:
                    p=p+2*dy
                else:
                    p = p + (2*dy)-(2*dx)
                    y1=y1+1
            print(x1,y1)
        #*********************************************************************************************
        x1=6
        y1=8
        x2=9
        y2=8
        #calculamos la diferencia
        dx = x2-x1
        dy = y2-y1
        #calculamos a p
        p = 2*dy - dx
        plt.scatter(x2,y2)
        #calculamos los nuevos valores de x y y
        while(x1<x2):
            plt.scatter(x1,y1)
            x1=x1+1
            if dy<0:
                if p<0:
                    p=p+2*dy
                    y1=y1-1
                else:
                    p=p + (2*dy)-(2*dx)
            else:
                if p<0:
                    p=p+2*dy
                else:
                    p = p + (2*dy)-(2*dx)
                    y1=y1+1
            print(x1,y1)
        #*********************************************************************************************
        x1=9
        y1=8
        x2=11
        y2=6
        #calculamos la diferencia
        dx = x2-x1
        dy = y2-y1
        #calculamos a p
        p = 2*dy - dx
        plt.scatter(x2,y2)
        #calculamos los nuevos valores de x y y
        while(x1<x2):
            plt.scatter(x1,y1)
            x1=x1+1
            if dy<0:
                if p<0:
                    p=p+2*dy
                    y1=y1-1
                else:
                    p=p + (2*dy)-(2*dx)
            else:
                if p<0:
                    p=p+2*dy
                else:
                    p = p + (2*dy)-(2*dx)
                    y1=y1+1
            print(x1,y1)
        plt.show()
    if lados == 9:
        print("Eneàgono")
        #Declaramos las variables que recibiran los valores
        x1=5.7
        y1=0.3
        x2=2.5
        y2=0.7
        #calculamos la diferencia
        dx = x2-x1
        dy = y2-y1
        #calculamos a p
        p = 2*dy - dx
        plt.scatter(x2,y2)
        #calculamos los nuevos valores de x y y
        while(x1<x2):
            plt.scatter(x1,y1)
            x1=x1+1
            if dy<0:
                if p<0:
                    p=p+2*dy
                    y1=y1-1
                else:
                    p=p + (2*dy)-(2*dx)
            else:
                if p<0:
                    p=p+2*dy
                else:
                    p = p + (2*dy)-(2*dx)
                    y1=y1+1
            print(x1,y1)
        #*********************************************************************************************
        x1=2.5
        y1=0.7
        x2=0.9
        y2=3
        #calculamos la diferencia
        dx = x2-x1
        dy = y2-y1
        #calculamos a p
        p = 2*dy - dx
        plt.scatter(x2,y2)
        #calculamos los nuevos valores de x y y
        while(x1<x2):
            plt.scatter(x1,y1)
            x1=x1+1
            if dy<0:
                if p<0:
                    p=p+2*dy
                    y1=y1-1
                else:
                    p=p + (2*dy)-(2*dx)
            else:
                if p<0:
                    p=p+2*dy
                else:
                    p = p + (2*dy)-(2*dx)
                    y1=y1+1
            print(x1,y1)
        #*********************************************************************************************
        x1=.9
        y1=3
        x2=1
        y2=5.4
        #calculamos la diferencia
        dx = x2-x1
        dy = y2-y1
        #calculamos a p
        p = 2*dy - dx
        plt.scatter(x2,y2)
        #calculamos los nuevos valores de x y y
        while(x1<x2):
            plt.scatter(x1,y1)
            x1=x1+1
            if dy<0:
                if p<0:
                    p=p+2*dy
                    y1=y1-1
                else:
                    p=p + (2*dy)-(2*dx)
            else:
                if p<0:
                    p=p+2*dy
                else:
                    p = p + (2*dy)-(2*dx)
                    y1=y1+1
            print(x1,y1)
        #*********************************************************************************************
        x1=1
        y1=5.4
        x2=3
        y2=7.3
        #calculamos la diferencia
        dx = x2-x1
        dy = y2-y1
        #calculamos a p
        p = 2*dy - dx
        plt.scatter(x2,y2)
        #calculamos los nuevos valores de x y y
        while(x1<x2):
            plt.scatter(x1,y1)
            x1=x1+1
            if dy<0:
                if p<0:
                    p=p+2*dy
                    y1=y1-1
                else:
                    p=p + (2*dy)-(2*dx)
            else:
                if p<0:
                    p=p+2*dy
                else:
                    p = p + (2*dy)-(2*dx)
                    y1=y1+1
            print(x1,y1)
        #*********************************************************************************************
        x1=3
        y1=7.3
        x2=5.8
        y2=7.8
        #calculamos la diferencia
        dx = x2-x1
        dy = y2-y1
        #calculamos a p
        p = 2*dy - dx
        plt.scatter(x2,y2)
        #calculamos los nuevos valores de x y y
        while(x1<x2):
            plt.scatter(x1,y1)
            x1=x1+1
            if dy<0:
                if p<0:
                    p=p+2*dy
                    y1=y1-1
                else:
                    p=p + (2*dy)-(2*dx)
            else:
                if p<0:
                    p=p+2*dy
                else:
                    p = p + (2*dy)-(2*dx)
                    y1=y1+1
            print(x1,y1)
        #*********************************************************************************************
        x1=5.8
        y1=7.8
        x2=8.2
        y2=6.5
        #calculamos la diferencia
        dx = x2-x1
        dy = y2-y1
        #calculamos a p
        p = 2*dy - dx
        plt.scatter(x2,y2)
        #calculamos los nuevos valores de x y y
        while(x1<x2):
            plt.scatter(x1,y1)
            x1=x1+1
            if dy<0:
                if p<0:
                    p=p+2*dy
                    y1=y1-1
                else:
                    p=p + (2*dy)-(2*dx)
            else:
                if p<0:
                    p=p+2*dy
                else:
                    p = p + (2*dy)-(2*dx)
                    y1=y1+1
            print(x1,y1)
        #*********************************************************************************************
        x1=8.2
        y1=6.5
        x2=9
        y2=4
        #calculamos la diferencia
        dx = x2-x1
        dy = y2-y1
        #calculamos a p
        p = 2*dy - dx
        plt.scatter(x2,y2)
        #calculamos los nuevos valores de x y y
        while(x1<x2):
            plt.scatter(x1,y1)
            x1=x1+1
            if dy<0:
                if p<0:
                    p=p+2*dy
                    y1=y1-1
                else:
                    p=p + (2*dy)-(2*dx)
            else:
                if p<0:
                    p=p+2*dy
                else:
                    p = p + (2*dy)-(2*dx)
                    y1=y1+1
            print(x1,y1)
        #*********************************************************************************************
        x1=9
        y1=4
        x2=8.2
        y2=1.5
        #calculamos la diferencia
        dx = x2-x1
        dy = y2-y1
        #calculamos a p
        p = 2*dy - dx
        plt.scatter(x2,y2)
        #calculamos los nuevos valores de x y y
        while(x1<x2):
            plt.scatter(x1,y1)
            x1=x1+1
            if dy<0:
                if p<0:
                    p=p+2*dy
                    y1=y1-1
                else:
                    p=p + (2*dy)-(2*dx)
            else:
                if p<0:
                    p=p+2*dy
                else:
                    p = p + (2*dy)-(2*dx)
                    y1=y1+1
            print(x1,y1)
        #*********************************************************************************************
        x1=5.4
        y1=0.3
        x2=8.2
        y2=1.5
        #calculamos la diferencia
        dx = x2-x1
        dy = y2-y1
        #calculamos a p
        p = 2*dy - dx
        plt.scatter(x2,y2)
        #calculamos los nuevos valores de x y y
        while(x1<x2):
            plt.scatter(x1,y1)
            x1=x1+1
            if dy<0:
                if p<0:
                    p=p+2*dy
                    y1=y1-1
                else:
                    p=p + (2*dy)-(2*dx)
            else:
                if p<0:
                    p=p+2*dy
                else:
                    p = p + (2*dy)-(2*dx)
                    y1=y1+1
            print(x1,y1)
        plt.show()
    if lados == 10:
        print("Decàgono")
        #Declaramos las variables que recibiran los valores
        x1=0.8
        y1=4
        x2=1.8
        y2=1.8
        #calculamos la diferencia
        dx = x2-x1
        dy = y2-y1
        #calculamos a p
        p = 2*dy - dx
        plt.scatter(x2,y2)
        #calculamos los nuevos valores de x y y
        while(x1<x2):
            plt.scatter(x1,y1)
            x1=x1+1
            if dy<0:
                if p<0:
                    p=p+2*dy
                    y1=y1-1
                else:
                    p=p + (2*dy)-(2*dx)
            else:
                if p<0:
                    p=p+2*dy
                else:
                    p = p + (2*dy)-(2*dx)
                    y1=y1+1
            print(x1,y1)
        #*********************************************************************************************
        x1=0.8
        y1=4
        x2=1.8
        y2=6.3
        #calculamos la diferencia
        dx = x2-x1
        dy = y2-y1
        #calculamos a p
        p = 2*dy - dx
        plt.scatter(x2,y2)
        #calculamos los nuevos valores de x y y
        while(x1<x2):
            plt.scatter(x1,y1)
            x1=x1+1
            if dy<0:
                if p<0:
                    p=p+2*dy
                    y1=y1-1
                else:
                    p=p + (2*dy)-(2*dx)
            else:
                if p<0:
                    p=p+2*dy
                else:
                    p = p + (2*dy)-(2*dx)
                    y1=y1+1
            print(x1,y1)
        #*********************************************************************************************
        x1=1.8
        y1=6.3
        x2=3.6
        y2=7.8
        #calculamos la diferencia
        dx = x2-x1
        dy = y2-y1
        #calculamos a p
        p = 2*dy - dx
        plt.scatter(x2,y2)
        #calculamos los nuevos valores de x y y
        while(x1<x2):
            plt.scatter(x1,y1)
            x1=x1+1
            if dy<0:
                if p<0:
                    p=p+2*dy
                    y1=y1-1
                else:
                    p=p + (2*dy)-(2*dx)
            else:
                if p<0:
                    p=p+2*dy
                else:
                    p = p + (2*dy)-(2*dx)
                    y1=y1+1
            print(x1,y1)
        #*********************************************************************************************
        x1=3.6
        y1=7.8
        x2=5.8
        y2=7.8
        #calculamos la diferencia
        dx = x2-x1
        dy = y2-y1
        #calculamos a p
        p = 2*dy - dx
        plt.scatter(x2,y2)
        #calculamos los nuevos valores de x y y
        while(x1<x2):
            plt.scatter(x1,y1)
            x1=x1+1
            if dy<0:
                if p<0:
                    p=p+2*dy
                    y1=y1-1
                else:
                    p=p + (2*dy)-(2*dx)
            else:
                if p<0:
                    p=p+2*dy
                else:
                    p = p + (2*dy)-(2*dx)
                    y1=y1+1
            print(x1,y1)
        #*********************************************************************************************
        x1=3.8
        y1=0.4
        x2=1.8
        y2=1.8
        #calculamos la diferencia
        dx = x2-x1
        dy = y2-y1
        #calculamos a p
        p = 2*dy - dx
        plt.scatter(x2,y2)
        #calculamos los nuevos valores de x y y
        while(x1<x2):
            plt.scatter(x1,y1)
            x1=x1+1
            if dy<0:
                if p<0:
                    p=p+2*dy
                    y1=y1-1
                else:
                    p=p + (2*dy)-(2*dx)
            else:
                if p<0:
                    p=p+2*dy
                else:
                    p = p + (2*dy)-(2*dx)
                    y1=y1+1
            print(x1,y1)
        #*********************************************************************************************
        x1=3.8
        y1=0.4
        x2=6.3
        y2=0.4
        #calculamos la diferencia
        dx = x2-x1
        dy = y2-y1
        #calculamos a p
        p = 2*dy - dx
        plt.scatter(x2,y2)
        #calculamos los nuevos valores de x y y
        while(x1<x2):
            plt.scatter(x1,y1)
            x1=x1+1
            if dy<0:
                if p<0:
                    p=p+2*dy
                    y1=y1-1
                else:
                    p=p + (2*dy)-(2*dx)
            else:
                if p<0:
                    p=p+2*dy
                else:
                    p = p + (2*dy)-(2*dx)
                    y1=y1+1
            print(x1,y1)
        #*********************************************************************************************
        x1=6.3
        y1=0.4
        x2=8.5
        y2=1.9
        #calculamos la diferencia
        dx = x2-x1
        dy = y2-y1
        #calculamos a p
        p = 2*dy - dx
        plt.scatter(x2,y2)
        #calculamos los nuevos valores de x y y
        while(x1<x2):
            plt.scatter(x1,y1)
            x1=x1+1
            if dy<0:
                if p<0:
                    p=p+2*dy
                    y1=y1-1
                else:
                    p=p + (2*dy)-(2*dx)
            else:
                if p<0:
                    p=p+2*dy
                else:
                    p = p + (2*dy)-(2*dx)
                    y1=y1+1
            print(x1,y1)
        #*********************************************************************************************
        x1=8.5
        y1=1.9
        x2=9.2
        y2=4
        #calculamos la diferencia
        dx = x2-x1
        dy = y2-y1
        #calculamos a p
        p = 2*dy - dx
        plt.scatter(x2,y2)
        #calculamos los nuevos valores de x y y
        while(x1<x2):
            plt.scatter(x1,y1)
            x1=x1+1
            if dy<0:
                if p<0:
                    p=p+2*dy
                    y1=y1-1
                else:
                    p=p + (2*dy)-(2*dx)
            else:
                if p<0:
                    p=p+2*dy
                else:
                    p = p + (2*dy)-(2*dx)
                    y1=y1+1
            print(x1,y1)
        #*********************************************************************************************
        x1=8.5
        y1=6.2
        x2=9.2
        y2=4
        #calculamos la diferencia
        dx = x2-x1
        dy = y2-y1
        #calculamos a p
        p = 2*dy - dx
        plt.scatter(x2,y2)
        #calculamos los nuevos valores de x y y
        while(x1<x2):
            plt.scatter(x1,y1)
            x1=x1+1
            if dy<0:
                if p<0:
                    p=p+2*dy
                    y1=y1-1
                else:
                    p=p + (2*dy)-(2*dx)
            else:
                if p<0:
                    p=p+2*dy
                else:
                    p = p + (2*dy)-(2*dx)
                    y1=y1+1
            print(x1,y1)
        #*********************************************************************************************
        x1=6.5
        y1=7.8
        x2=8.5
        y2=6.2
        #calculamos la diferencia
        dx = x2-x1
        dy = y2-y1
        #calculamos a p
        p = 2*dy - dx
        plt.scatter(x2,y2)
        #calculamos los nuevos valores de x y y
        while(x1<x2):
            plt.scatter(x1,y1)
            x1=x1+1
            if dy<0:
                if p<0:
                    p=p+2*dy
                    y1=y1-1
                else:
                    p=p + (2*dy)-(2*dx)
            else:
                if p<0:
                    p=p+2*dy
                else:
                    p = p + (2*dy)-(2*dx)
                    y1=y1+1
            print(x1,y1)
        plt.show()
    else:
        print(lados,"Esa figura no se puede construir por el tamaño")