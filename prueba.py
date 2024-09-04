from tkinter import *
from tkinter.messagebox import *
from Diccionario import obtener_palabra_dificil
from tkinter import messagebox

#Clase
class JuegoAhorcado:
    #Constructor + interfaz
    def __init__(self):
        #Llamamos Diccionario como un atributo
        self.palabra = obtener_palabra_dificil()
        
        #Escondemos la palabra generada por la API
        self.letras_palabra_oculta = ['_' for _ in self.palabra]
        
        #Definimos las vidas
        self.vidas = 6
        
        #Definimos las letras que ingresará posteriormente el usuario
        self.letras_ingresadas = []
        
        #Ventana de la interfaz grafica 
        self.raiz = Tk()
        
        #Titulo de la ventana
        self.raiz.title("Juego Ahorcado")
        
        #Atributo para guardar las letras acertadas que va ingresando el usuario
        self.ocultar_palabra = Label(self.raiz, text=" ".join(self.letras_palabra_oculta), font=("Arial", 24))
        self.ocultar_palabra.pack()
          
        #Atributo para guardar el contador de vidas
        self.etiqueta_vidas = Label(self.raiz, text=f"Vidas: {self.vidas}", font=("Arial", 18))
        self.etiqueta_vidas.pack()
        
        #Atributo donde aparecerán las letras que ingrese el usuario
        self.etiqueta_letras_ingresadas = Label(self.raiz, text="Letras ingresadas: ", font=("Arial", 18))
        self.etiqueta_letras_ingresadas.pack()
        
        #Atributo donde el usuario pondrá la letra
        self.letra_ingresada = Entry(self.raiz, font=("Arial", 18))
        self.letra_ingresada.pack()
        
        #Botón para capturar la letra ingresada por el usuario
        self.boton_ingresar = Button(self.raiz, text="Ingresar", command=self.enviar_letra)
        self.boton_ingresar.pack()
        
        #Atributo para guardar el dibujo del ahorcado
        self.imagenes_ahorcado = []  
        self.etiqueta_ahorcado = Label(self.raiz, text="")
        self.etiqueta_ahorcado.place(x=460, y=180)
        #self.etiqueta_ahorcado.place(x=30,y=50)

   
    def enviar_letra(self):
        letra = self.letra_ingresada.get().lower()
         
        #Captura que no se haya ingresado mas de una letra
        if len(letra) != 1:
            messagebox.showerror("Error", "Debes ingresar solo una letra")
            return
        
        #captura la letra ingresada y evalua que no este repetida
        if letra in self.letras_palabra_oculta or letra in self.letras_ingresadas:
            messagebox.showerror("Error", "Ya has ingresado esta letra")
            return
        
        #Se define como False hasta que el usuario acerte
        letra_correcta = False
        
        #Iteramos sobre la palabra generada por la API
        for i in range(len(self.palabra)):
            
            #Condicional que dara la letra correcta si la ingresada por el usuario esta     
            #Contenida en la palabra
            if self.palabra[i] == letra:
                self.letras_palabra_oculta[i] = letra
                letra_correcta = True
        
        #En caso de que no le restamos una vida y empezamos a dibujar el muñeco
        if not letra_correcta:
            self.vidas -= 1
            self.etiqueta_vidas.config(text=f"Vidas: {self.vidas}")
            self.dibujar_muneco()
            messagebox.showinfo("Incorrecto", f"Letra incorrecta. Te quedan {self.vidas} vidas")
        
        #O por el contrario enhorabuena para el usuario por adivinar una letra
        else:
            messagebox.showinfo("Correcto", "Letra correcta")
        #Añade la letra ingresada a la lista
        self.letras_ingresadas.append(letra)
        #Actualiza el texto de la etiqueta letras_ingresadas separadas por comas
        self.etiqueta_letras_ingresadas.config(text=f"Letras ingresadas: {', '.join(self.letras_ingresadas)}")
        #Actualiza el texto de la ocultar_palabra
        self.ocultar_palabra.config(text=" ".join(self.letras_palabra_oculta))
        #Borramos el contenido (letra ingresada) para que podamos ingresar una nueva letra
        self.letra_ingresada.delete(0, END)
        
        #Si el usuario acerto la palabra, lo felicitamos por la victoria
        if "".join(self.letras_palabra_oculta) == self.palabra:
            messagebox.showinfo("Ganaste", "¡Has ganado! Felicidades")
            self.reiniciar_juego()
        
        #Si su contador de vidas llega a 0, pierde el juego y le mostramos la palabra oculta
        elif self.vidas == 0:
            messagebox.showinfo("Perdiste", f"¡Has perdido! La palabra era '{self.palabra}'")
            self.reiniciar_juego()


    #Funcion para dibujar nuestro ahorcado
    #Dibujará el muñeco a medida que el usuario se equivoque
    def dibujar_muneco(self):
        imagenes_ahorcado = ["1.png", "2.png", "3.png", "4.png", "5.png", "6.png", ""]
        #Creamos un objeto tipo imagen que corresponde a la cantidad de vidas
        imagen = PhotoImage(file=imagenes_ahorcado[self.vidas])
        #Actualizamos la etiqueta_muñeco para ir dibujandolo
        self.etiqueta_ahorcado.config(image=imagen)
        #Almacena la referencia a la imagen en la etiqueta misma.
        #Esto es necesario porque Tkinter puede eliminar la imagen si no se 
        # mantiene una referencia a ella.(Chat)
        self.etiqueta_ahorcado.image = imagen


    #Funcion para reiniciar el juego
    def reiniciar_juego(self):
        #Preguntamos si quiere volver a jugar
        respuesta = messagebox.askyesno("Reiniciar", "¿Quieres jugar de nuevo?")
        
        #Si es si
        if respuesta:
            #Obtenemos la palabra de la API
            self.palabra = obtener_palabra_dificil()
            #Representamos la palabra de la API con guines
            self.letras_palabra_oculta = ['_' for _ in self.palabra]
            #Restauramos las vidas
            self.vidas = 6 
            #Limpiamos la lista de letras que ingresó
            self.letras_ingresadas = [] 
            #Ocultamos la palabra a adivinar
            self.ocultar_palabra.config(text=" ".join(self.letras_palabra_oculta))
            #Actualizamos las vidas
            self.etiqueta_vidas.config(text=f"Vidas: {self.vidas}")
            #Limpiamos las letras anteriormente ingresadas
            self.etiqueta_letras_ingresadas.config(text="Letras ingresadas: ")
            #Redibujamos el muñeco desde su estado inicial
            self.dibujar_muneco() 
        
        #Respuesta no 
        else:
            #Cierra la ventana y la app
            self.raiz.destroy()

#Verificamos que el juego no sea importado de un modulo
if __name__ == "__main__":
    #Instancia para la clase que representa app del juego
    juego = JuegoAhorcado()
    #Mantenemos la ventana abierta
    juego.raiz.mainloop()
    