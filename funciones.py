import random

def encontrar_menores(diccionario,letra):
    """Dado un diccionario de palabras, y una letra, esta funciÃ³n devuelve la lista de palabras que empiezan por una letra que alfabÃ©ticamente estÃ¡ antes que la indicada.
    Args:
      diccionario
      letra
    Returns:
      resultado: ej. ['AUNQUE','ABINAR']
    """
    for clave in diccionario:
        for palabra in diccionario[clave]:
            if palabra[0] < letra:
                resultado=[]
                resultado.append(palabra)
    return resultado

def add_client(clients_list,nif,name,address,phone,email):
    """Dado un diccionario de clientes y datos de un nuevo cliente, esta funciÃ³n inserta estos datos como un nuevo cliente.
    Args:
      diccionario
      nif
      name 
      address
      phone
      email
    """
    #anteriormente, teniamos puesto que en el diccionario clients_list, en la clave nif, se guardaba un diccionario con la clave nif, donde 
    #se guardaba a su vez otro diccionario con la clave nif, por lo tanto se repetia dos veces nif, si eliminamos lo que seria nif:{},
    #ahora si que esta funcion realiza loq ue se supone que deberia de realizar
    clients_list[nif] = {
        'name': name,
        'address': address,
        'phone': phone,
        'email': email
        
    }

def repartir_cartas(cartas_iniciales,repeticiones):
    """Dada una baraja de cartas iniciales y un nÃºmero de repeticiones, esta funciÃ³n selecciona 5 cartas aleatorias de esta baraja y las mete en un diccionario llamado combinaciones. El proceso se repite tantas veces como repeticiones se indiquen.
    Args:
      cartas_iniciales
      repeticiones
    Returns:
      combinaciones: ej. {'repeticion1': ['contable', 'alguacil', 'asesino', 'cardenal', 'obispo']}
    """    
    combinaciones={}
    for i in range(1,repeticiones+1):
        cartas_aleatorias = cartas_iniciales 
        combinaciones["repeticion"+str(i)]=[]
        for j in range(0,5):
            carta=random.choice(cartas_aleatorias)
            #anteriormente se guardaba en la clave del diccionario, la posicion de la carta que se habia seleccionado enel random,
            #ya que se hacia .append de carta
            #de forma que solo se guardaba la posicion de las cartas elegidas de la lista cartas_aleatorias, si lo cambiamos por castas_aleatorias[carta]
            #estaremos guardando el valor de la carta seleccionada y no su posicion
            combinaciones["repeticion"+str(i)].append(cartas_aleatorias[carta])
            cartas_aleatorias.remove(carta)

    return combinaciones

    