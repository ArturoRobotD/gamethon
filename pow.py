
# coding: utf-8

# In[3]:


from datetime import datetime
import hashlib

string = input('Escriba el mensaje: ')

n = input('Escriba el nivel de dificultad: ')        
while int(n) < 1 or int(n) > 64:  
    n=input('El nivel de dificultad tiene que ser un numero mayor o igual a 1 y menor o igual a 63: ') 
    
zeros = bin(0)[2:].zfill(int(n))


#complete es una variable que indica cuando el ciclo termina
complete = False
#la variable n va guardando el numero de ciclos para calcular el nonce
n = 0
start=datetime.now()
while complete == False:
        #curr_string es la concatenacion de mensaje y nonce actual
        curr_string = string + str(n)
        #message es para convertir curr_string a mensaje codficado, esto es necesario para aplicar el algoritmo sha256
        message = str(curr_string).encode()
        #curr_hash es la variable que guarda el primer hash generado
        curr_hash = hashlib.sha256(message).hexdigest()
        #message_hash convierte el primer hash generado en mensaje codificado para poder aplicar un segundo hash
        message_hash = str(curr_hash).encode()
        #double_hash es el resultado de aplicar el algoritmo sha256 sobre el primer hash
        double_hash = hashlib.sha256(message_hash).hexdigest()
        n = n + 1
        if double_hash.startswith(zeros):
            print ('PoW Hash: ',double_hash)
            print ('Nonce descubierto: ',n)
            complete = True

print ('Tiempo de Ejecucion', datetime.now()-start ,' Segundos')


# In[ ]:





# In[ ]:




