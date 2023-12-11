import turtle as t


def dibujo_estrella(puntas):
    window=t.Screen()
       
    #ángulo para girar según el número de puntas    
    angulo=180-(180/puntas)
    
    #dibujar la estrella
    for _ in range(puntas):
            t.forward(200)  #longitud  de cada punta
            t.left(angulo)
            
    #completar
    t.goto(0,0)
       
    #mostrar el dibujo y cerrar al hacer clic y 
        
    window.exitonclick()
puntas=int(input('¿Cuántas puntas quiere que tenga tu estrella?: ')) 
dibujo_estrella(puntas)
