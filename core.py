from datetime import time, timedelta, datetime
import utils
import data
import file_management

def makeChoice(args):
    '''
    Función para escoger opciones de un diccionario
        Entradas
            @args : lista que contiene el diccionario y la opción escogida por el usuario
        Salidas
            Devuelve la salida de la función llamada del diccionario
    '''
    # Se obtiene el diccionario de los argumentos
    menuChoicesDict = args[0]
    # Se obtiene la elección del usuario de los argumentos
    choice = args[1]
    # Se accede al diccionario con la elección del usuario
    return menuChoicesDict[int(choice)]()

# Menú para la creación de cohetes
def rocketMenu():
    utils.menu(data.rocket_menu_display, data.choice_error_message, data.menu_exit, makeChoice, data.choice_regex, [rocketChoicesDict], True, errorTextExtra="\t\t")

def createRocket():
    '''
    Función para crear cohetes
        Sin entradas ni salidas
    '''
    # Se obtiene el nombre del cohete
    name = utils.getAnswer(data.rocket_name_display, errorText=data.rocket_name_error, regex=data.rocket_name_regex, errorTextExtra="\t\t")
    validName = utils.checkValidEntry(name, data.rockets, data.rocket_duplicate_error, errorTextExtra="\n\t\t\t") # Se valida para ver si la entrada no está vacía o no está ya creada
    if not validName: # Si la entrada no es válida
        return # salimos de la función
    
    # Se obtiene el peso máximo de transporte
    maxWeight = utils.getAnswer(data.rocket_max_weight_display.format(name = name), errorText=data.rocket_max_weight_error, regex=data.rocket_max_weight_regex, errorTextExtra="\t\t")
    validMaxWeight = utils.checkValidEntry(maxWeight) # Se valida para ver si la entrada no está vacía o no está ya creada
    if not validMaxWeight: # Si la entrada no es válida
        return # salimos de la función

    # Finalmente, tras haber comprobado que toda la información es válida,
    data.rockets[name] = int(maxWeight) # y se crea el cohete nuevo
    
    # Se compone y guarda la información
    file_rockets_data = {}
    file_rockets_data["rockets"] = data.rockets
    file_management.saveData(file_rockets_data)

    utils.display(data.rocket_create_success.format(name=name, weight=maxWeight), successMessage=True, waitText="\t\t") # se muestra el mensaje de éxito en pantalla

# Menú para la creación de peticiones
def requestMenu():
    utils.menu(data.request_menu_display, data.choice_error_message, data.menu_exit, makeChoice, data.choice_regex, [requestChoicesDict], True, errorTextExtra="\t\t")

def request():
    '''
    Función para crear peticiones
        Sin entradas ni salidas
    '''
    # Se obtiene el nombre de la petición
    name = utils.getAnswer(data.request_name_display, errorText=data.request_name_error, regex=data.request_name_regex, errorTextExtra="\t\t")
    validName = utils.checkValidEntry(name, data.requests, data.request_new_duplicate_error, errorTextExtra="\t\t\t") # Se valida para ver si la entrada no está vacía o no está ya creada
    if not validName: # Si la entrada no es válida
        return # salimos de la función

    validName = utils.checkValidEntry(name, data.requests_in_transit, data.request_assigned_duplicate_error, errorTextExtra="\t\t") # Se valida para ver si la entrada no está vacía o no está ya creada
    if not validName: # Si la entrada no es válida
        return # salimos de la función

    validName = utils.checkValidEntry(name, data.requests_failed, data.request_failed_duplicate_error, errorTextExtra="\t\t") # Se valida para ver si la entrada no está vacía o no está ya creada
    if not validName: # Si la entrada no es válida
        return # salimos de la función

    # Se obtiene la descripción
    description = utils.getAnswer(data.request_description_display.format(name=name), errorText=data.request_description_error, regex=data.request_description_regex, errorTextExtra="\t\t")
    validDescription = utils.checkValidEntry(description) # Se valida para ver si la entrada no está vacía o no está ya creada
    if not validDescription: # Si la entrada no es válida
        return # salimos de la función
    
    # Se obtiene el peso de la petición
    weight = utils.getAnswer(data.request_weight_display.format(name=name), errorText=data.request_weight_error, regex=data.request_weight_regex, errorTextExtra="\t\t")
    validWeight = utils.checkValidEntry(weight) # Se valida para ver si la entrada no está vacía o no está ya creada
    if not validWeight: # Si la entrada no es válida
        return # salimos de la función
    
    # Se obtiene los días máximos en los que debería llegar
    maxDays = utils.getAnswer(data.request_max_days_display.format(name=name), errorText=data.request_max_days_error, regex=data.request_max_days_regex, errorTextExtra="\t\t")
    validMaxDays = utils.checkValidEntry(maxDays) # Se valida para ver si la entrada no está vacía o no está ya creada
    if not validMaxDays: # Si la entrada no es válida
        return # salimos de la función

    # Finalmente, tras haber comprobado que toda la información es válida,
    data.requests[name] = [description, int(maxDays), float(weight)] # y se crea la petición

    # Se compone y guarda la información
    file_requests_data = {}
    file_requests_data["requests"] = data.requests
    file_management.saveData(file_requests_data)

    utils.display(data.request_create_succes.format(name=name, description=description, max_days=maxDays, weight=weight), successMessage=True, waitText="\t\t") # se muestra el mensaje de éxito en pantalla
    
# Menú para la creación de lanzamientos
def launchMenu():
    utils.menu(data.launch_menu_display, data.choice_error_message, data.menu_exit, makeChoice, data.choice_regex, [launchesChoicesDict], True, errorTextExtra="\t\t")

def launch():
    '''
    Función para crear lanzamientos
        Sin entradas ni salidas
    '''
    
    # Si no hay ningún cohete creado
    if len(data.rockets) == 0:
        utils.display(data.launch_no_rockets, infoMessage=True, waitText="\t\t")
        return

    # Se obtiene una lista de los cohetes disponibles
    rocketList = []
    # Se itera sobre las claves de los cohetes
    for k in data.rockets.keys():
        # Se guarda en una lista el nombre y la información del cohete actual
        rocketList.append([k, data.rockets[k]])

    # Se imprime un salto de línea
    print()
    # Se itera sobre la lista de los cohetes disponibles
    for i in range(0, len(rocketList)):
        # Se imprime en pantalla el cohete actual disponible
        utils.display(data.launch_rocket_pick.format(bold_text=data.bold_text, end_format=data.end_format,index=i, name=rocketList[i][0], weight=rocketList[i][1]), wait=False, mainColor=False)
    
    # Se obtiene el nombre del cohete a elegir
    rocketNumber = utils.getAnswer(data.launch_rocket_display, errorText=data.launch_rocket_error, regex=data.launch_rocket_regex, errorTextExtra="\t\t")
    validRocketNumber = utils.checkValidEntry(rocketNumber) # Se valida para ver si la entrada no está vacía o no está ya creada
    if not validRocketNumber: # Si la entrada no es válida
        return # salimos de la función

    # Se convierte a entero el número obtenido
    rocketNumber = int(rocketNumber)
    # Se comprueba que el cohete exista
    if not (0 <= rocketNumber < len(rocketList)):
        # Si no existe, se muestra el mensaje de error en pantalla
        utils.display(data.launch_no_rocket_error, errorMessage=True, waitText="\t\t")
        return
    
    # Se obtiene el cohete actual a utilizar
    rocket = rocketList[rocketNumber][0]
    # Se obtiene los días de la misión
    days = utils.getAnswer(data.launch_days_display, errorText=data.launch_days_error, regex=data.launch_days_regex, errorTextExtra="\t\t")
    validDays = utils.checkValidEntry(days)  # Se valida para ver si la entrada no está vacía o no está ya creada
    if not validDays: # Si la entrada no es válida
        return # salimos de la función

    weight = data.rockets[rocket] # obtenemos peso máximo del cohete
    # Finalmente, tras haber comprobado que toda la información es válida,
    data.launches.append([rocket, int(days), weight, []]) # y se crea la petición

    # Se compone y guarda la información
    file_launches_data = {}
    file_launches_data["launches"] = data.launches
    file_management.saveData(file_launches_data)

    utils.display(data.launch_create_success.format(rocket=rocket, days=days), successMessage=True, waitText="\t\t") # se muestra el mensaje de éxito en pantalla

# Menú para asignar
def assignMenu():
    utils.menu(data.assign_menu_display, data.choice_error_message, data.menu_exit, makeChoice, data.choice_regex, [assignChoicesDict], True, errorTextExtra="\t\t")

def assign():
    '''
    Función para asignar
        Sin entradas ni salidas
    '''

    def subAssign(requestsDict, failed=False):
        # Ordenamos peticiones y lanzamientos
        sortedRequests = sorted(requestsDict.items(), key=lambda x:x[1][1])
        data.launches = sorted(data.launches, key=lambda x:x[1])

        print() # se imprime un salto de línea
        # Si no hay peticiones que procesar
        if len(sortedRequests) > 0:
            if not failed: # Si se llama la función para peticiones nuevas
                # Se muestra en pantalla en pantalla el texto de inicio para peticiones nuevas
                utils.display(data.assign_new_requests_start, mainColor=False, waitText="\t\t")
            else: # Si se llama la función para peticiones fallidas
                # Se muestra en pantalla en pantalla el texto de inicio para peticiones fallidas
                utils.display(data.assign_failed_requests_start, mainColor=False, waitText="\t\t")
            success_counter = 0 # Contador para contar las peticiones asignadas
            failed_counter = 0 # Contador para contar las peticiones fallidas
            # Iteramos sobre cada petición ordenada
            for j in range(0, len(sortedRequests)):
                # Iteramos sobre cada lanzamiento ordenado
                assigned = False
                for i in range(0, len(data.launches)):
                    # Si los días máximos de la petición son mayores a los del lanzamiento
                    if sortedRequests[j][1][1] >= data.launches[i][1]:
                        # Si el peso de la petición es menor que el del lanzamiento
                        if sortedRequests[j][1][2] <= data.launches[i][2]:
                            success_counter += 1 # Se incrementa en 1 cada vez que se asigna una petición a un lanzamiento
                            data.launches[i][2] -= sortedRequests[j][1][2] # Se resta el peso
                            data.launches[i][2] = round(data.launches[i][2], 3) # Se redondea el resultado
                            # Se añade la petición a la lista de peticiones en tránsito
                            data.requests_in_transit[sortedRequests[j][0]] = sortedRequests[j][1]
                            # Se añade la petición al lanzamiento
                            data.launches[i][3].append(sortedRequests[j][0])
                            # Se elimina del diccionario original la petición actual
                            requestsDict.pop(sortedRequests[j][0]) 
                            assigned = True # Se pone la variable en True para confirmar que la hemos podido asignar
                            if not failed: # Si se llama la función para peticiones nuevas
                                # Se muestra en pantalla la asignación exitosa
                                utils.display(data.assign_new_feedback.format(request_name=sortedRequests[j][0], launch_name=data.launches[i][0]), wait=False, successMessage=True,)
                            else: # Si se llama la función para peticiones fallidas
                                # Se muestra en pantalla la reasignación exitosa
                                utils.display(data.assign_failed_feedback.format(request_name=sortedRequests[j][0], launch_name=data.launches[i][0]), wait=False, successMessage=True)
                            break
                # Si no ha sido asignado y si se trata de una petición nueva
                if not assigned and not failed:
                    # Se añade la petición a la lista de las fallidas
                    data.requests_failed[sortedRequests[j][0]] = sortedRequests[j][1]
                    # Se elimina del diccionario original la petición actual
                    requestsDict.pop(sortedRequests[j][0])
                    # Se muestra en pantalla el feedback del fracaso de intentar asignar la petición nueva actual
                    utils.display(data.assign_new_fail_feedback.format(request_name=sortedRequests[j][0]), wait=False, errorMessage=True)
                    failed_counter += 1 # Se incrementa el contador de las peticiones fallidas
                # Si no ha sido asignado y si se trata de una petición fallida
                elif failed and not assigned:
                    # Se muestra en pantalla el feedback del fracaso de intentar asignar la petición fallida actual
                    utils.display(data.assign_fail_feedback.format(request_name=sortedRequests[j][0]), wait=False, errorMessage=True)
                    failed_counter += 1 # Se incrementa el contador de las peticiones fallidas
            if not failed: # Si se llama la función para peticiones nuevas
                # Se muestra en pantalla la información final de las peticiones nuevas
                utils.display(data.assign_new_feedback_all.format(success_color=data.success_color, error_color=data.error_color, end_format=data.end_format, success_counter=success_counter, failed_counter=failed_counter), infoMessage=True, waitText="\t\t")
            else: # Si se llama la función para peticiones fallidas
                # Se muestra en pantalla la información final de las peticiones fallidas
                utils.display(data.assign_failed_feedback_all.format(success_color=data.success_color, error_color=data.error_color, end_format=data.end_format, success_counter=success_counter, failed_counter=failed_counter), infoMessage=True, waitText="\t\t")

        elif not failed: # Si se llama la función para peticiones nuevas
            # Se informa en pantalla de que no hay peticionnes nuevas que procesar
            utils.display(data.assign_no_new, mainColor=False, waitText="\t\t")
        else: # Si se llama la función para peticiones fallidas
            # Se informa en pantalla de que no hay peticionnes fallidas que procesar
            utils.display(data.assign_no_failed, mainColor=False, waitText="\t\t")

    # Se llama la función de arriba sobre las peticiones fallidas
    subAssign(data.requests_failed, failed=True)

    # Se llama la función de arriba sobre las peticiones
    subAssign(data.requests)

    # Información para guardar en fichero
    file_general_data = {}
    file_general_data["requests"] = data.requests
    file_general_data["requests_in_transit"] = data.requests_in_transit
    file_general_data["requests_failed"] = data.requests_failed
    file_general_data["launches"] = data.launches
    file_management.saveData(file_general_data)

# Menú para el paso de los días 
def daysMenu():
    utils.menu(data.days_menu_display, data.choice_error_message, data.menu_exit, makeChoice, data.choice_regex, [daysChoicesDict], True, errorTextExtra="\t\t")

def days():
    # Se obtienen los días a transcurrir
    days = utils.getAnswer(data.days_input_text, errorText=data.days_error, regex=data.days_regex, errorTextExtra="\t\t")
    # Se comprueba que no se haya obtenido una entrada vacía
    validDays = utils.checkValidEntry(days)
    if not validDays:
        return
    
    # Se convierten los días a número entero
    days = int(days)

    # Se muestra la fecha de inicio
    utils.displayTime(startText="\n\t\t")

    # Se suman los días a pasar
    days_sum = timedelta(days=days)
    # Se suman los días a la fecha actual
    data.watch = data.watch+days_sum

    file_watch = {}
    file_watch["watch"] = data.watch
    file_management.saveData(file_watch)

    launches_temp = []
    # Si hay lanzamientos que procesar se van a poner todos en tránsito
    if len(data.launches) != 0:
        # Bucle que itera sobre los lanzamientos
        for i in range(0, len(data.launches)):
            requestsCount = len(data.launches[i][3])
            if requestsCount != 0: # Si el lanzamiento actual tiene peticiones asignadas
                data.launches_in_transit.append(data.launches[i]) # Se ponen en tránsito
            else:
                launches_temp.append(data.launches[i])
        # Se vacía la lista de los lanzamientos normales
        data.launches = launches_temp

    # Lista temporal de los lanzamientos en tránsito
    new_launches_in_transit = []

    # Contadores para contar los lanzamientos y peticiones entregadas
    launches_counter = 0
    requests_counter = 0

    # Se imprime en pantalla el inicio de la secuencia de conteo de días
    utils.display(f"\t\tTranscurre el tiempo...\n\t\t{days} días restantes",  mainColor=False, waitText="\t\t")

    # Si hay lanzamientos en tránsito
    if len(data.launches_in_transit) > 0:
        # Iteramos sobre ellos
        for i in range(0, len(data.launches_in_transit)):
            # Se restan los días del lanzamiento actual
            data.launches_in_transit[i][1] -= days
            # Si nos quedan días menores que 1 quiere decir que se ha podido entregar
            if data.launches_in_transit[i][1] < 1:
                # Se obtiene el tiempo de entrega
                timeNow = data.watch+(timedelta(days=data.launches_in_transit[i][1]))
                # Se muestra en pantalla la fecha actual de entrega
                utils.display(f"\n\t\t{data.time_color}Fecha: {timeNow}{data.end_format}\n\t\t{data.success_color}El lanzamiento \"{data.launches_in_transit[i][0]}\" ha llegado a la estación espacial.{data.end_format}\n\t\tPeticiones:", wait=False, successMessage=True)
                launches_counter += 1 # Se incrementa el contador de lanzamientos entregados
                requests_counter += len(data.launches_in_transit[i][3]) # Se incrementa el contador de peticiones entregadas
                # Bucle que itera sobre todas las peticiones del lanzamiento actual
                for j in range(0, len(data.launches_in_transit[i][3])):
                    # Se muestra en pantalla las peticiones entregadas
                    utils.display(f"\t\t\t\"{data.launches_in_transit[i][3][j]}\" entregada", successMessage=True, wait=False)
                    # Se compone la información correspondiente a la petición actual
                    requestInfo = data.requests_in_transit[data.launches_in_transit[i][3][j]]
                    requestInfo[1] = timeNow # Se guarda en la información de la petición actual la fecha de entrega
                    # Se añade la petición entrega a la lista de las peticiones entregadas
                    data.requests_delivered.append([data.launches_in_transit[i][3][j], requestInfo])
                    # Se borra la petición actual de la lista de las que están en tránsito
                    del data.requests_in_transit[data.launches_in_transit[i][3][j]]
                data.launches_in_transit[i][1] = timeNow # Se guarda en la información del lanzamiento la fecha de entrega
                data.launches_delivered.append(data.launches_in_transit[i]) # Se añade el lanzamiento entregado a la lista correspondiente
                utils.display("", waitText="\t\t") # Se pausa el tiempo de ejecución para que el usuario pueda apreciar lo que está pasando
            else: # sino
                # Se añade a la lista temporal de los lanzamientos en tránsito el lanzamiento actual
                new_launches_in_transit.append(data.launches_in_transit[i])

    data.launches_in_transit = new_launches_in_transit # Se asigna la lista temporal de los lanzamientos en tránsito a la definitiva

    # Información para guardar en fichero
    file_general_data = {}
    file_historic_data = {}
    file_general_data["requests_in_transit"] = data.requests_in_transit
    file_general_data["launches"] = data.launches
    file_general_data["launches_in_transit"] = data.launches_in_transit
    file_historic_data["requests_delivered"] = data.requests_delivered
    file_historic_data["launches_delivered"] = data.launches_delivered
    file_management.saveData(file_general_data)
    file_management.saveData(file_historic_data, historic=True)

    utils.displayTime(startText="\n\t\t") # Se muesta la fecha final cuando han transcurrido los días introducidos
    utils.display(f"\t\tHan transcurrido los {days} días...",  infoMessage=True, wait=False) # Se imprime la cantidad de días transcurridos
    # Se informa de los eventos ocurridos durante los días transcurridos
    utils.display(f"\t\tLanzamientos entregados: {launches_counter}\n\t\tPeticiones entregadas: {requests_counter}", waitText="\t\t", successMessage=True)

# Menu para visualizar la información
def infoMenu():
    utils.menu(data.info_menu_display, data.choice_error_message, data.menu_exit, makeChoice, data.choice_regex, [infoChoicesDict], True, errorTextExtra="\t\t")

def general_info():
    # Información general de los cohetes
    # Se muestra en pantalla una información breve de los cohetes
    rockets_length = len(data.rockets)
    utils.display(data.info_general_rockets.format(count=rockets_length), wait=False, infoMessage=True)
    if rockets_length > 0:
        # Se itera sobre todos ellos
        for key in data.rockets:
            # Se muestra la información detalllada del cohete actual
            utils.display(data.info_general_rockets_all.format(bold_text=data.bold_text, end_format=data.end_format, name=key, weight=data.rockets[key]), mainColor=False, wait=False)
    utils.display("", waitText="\t\t") # Se hace una pausa en el tiempo de ejecución para que el usuario no se pierda

    # Información general de los lanzamientos
    # Se obtiene la cantidad de lanzamientos sin desplegar y desplegados
    launches_count = len(data.launches)+len(data.launches_in_transit)
    # Se muestra en pantalla una información breve de los lanzamientos
    utils.display(data.info_general_launches.format(count=launches_count, standby_count=len(data.launches), transit_count=len(data.launches_in_transit)), wait=False, infoMessage=True)
    if launches_count > 0: # Si hay lanzamientos sin desplegar o desplegados
        if len(data.launches) > 0: # Si hay lanzamientos sin desplegar
            # Se muestra en pantalla una información breve de los lanzamientos sin desplegar
            utils.display(data.info_general_launches_new.format(count=len(data.launches)), wait=False)
            # Se itera sobre todos ellos
            for i in range(0, len(data.launches)):
                # Se muestra la información detallada del lanzamiento sin desplegar actual
                utils.display(data.info_general_launches_all.format(bold_text=data.bold_text, end_format=data.end_format, index=i, rocket=data.launches[i][0], days=data.launches[i][1], weight=data.launches[i][2]), mainColor=False, wait=False)
                if len(data.launches[i][3]) > 0: # Si el lanzamiento actual tiene peticiones asignadas
                    # Se muestra en pantalla una información breve de los peticiones del lanzamientos sin desplegar actual
                    utils.display(data.info_general_launches_requests.format(count=len(data.launches[i][3])), wait=False, infoMessage=True)
                    # Se itera sobre todas sus peticiones
                    for j in range(0, len(data.launches[i][3])):
                        # Se muestra el nombre de la petición actual del lanzamiento sin desplegar actual
                        utils.display(data.info_general_launches_request_info.format(name=data.launches[i][3][j]), wait=False, mainColor=False)
                else: # sino
                    # Se informa en pantalla de que el lanzamiento sin desplegar actual no tiene peticiones asignadas
                    utils.display(data.info_general_launches_no_requests, wait=False, mainColor=False)
            utils.display("", waitText="\t\t") # Se hace una pausa en el tiempo de ejecución para que el usuario no se pierda

        if len(data.launches_in_transit) > 0: # Si hay lanzamientos desplegados
            # Se muestra en pantalla una información breve de los lanzamientos desplegados
            utils.display(data.info_general_launches_transit.format(count=len(data.launches_in_transit)), wait=False)
            # Se itera sobre todos ellos
            for i in range(0, len(data.launches_in_transit)):
                 # Se muestra la información detallada del lanzamiento desplegado actual
                utils.display(data.info_general_launches_all.format(bold_text=data.bold_text, end_format=data.end_format, index=i, rocket=data.launches_in_transit[i][0], days=data.launches_in_transit[i][1], weight=data.launches_in_transit[i][2]), mainColor=False, wait=False)
                # Se muestra en pantalla una información breve de los peticiones del lanzamientos desplegado actual
                utils.display(data.info_general_launches_requests.format(count=len(data.launches_in_transit[i][3])), wait=False, infoMessage=True)
                # Se itera sobre todas sus peticiones
                for j in range(0, len(data.launches_in_transit[i][3])):
                    # Se muestra el nombre de la petición actual del lanzamiento desplegado actual
                    utils.display(data.info_general_launches_request_info.format(name=data.launches_in_transit[i][3][j]), wait=False, mainColor=False)
            utils.display("", waitText="\t\t") # Se hace una pausa en el tiempo de ejecución para que el usuario no se pierda
    else:
        utils.display("", waitText="\t\t") # Se hace una pausa en el tiempo de ejecución para que el usuario no se pierda

    # Información general de las peticiones
    # Se obtiene la cantidad de peticiones sin asignar, asignadas y fallidas
    request_count = len(data.requests)+len(data.requests_in_transit)+len(data.requests_failed)
    # Se muestra en pantalla una información breve de las peticiones
    utils.display(data.info_general_requests.format(count=request_count, new_count = len(data.requests), transit_count = len(data.requests_in_transit), failed_count=len(data.requests_failed)), wait=False, infoMessage=True)
    if request_count > 0: # Si hay peticiones sin asignar o asignadas o fallidas
        if len(data.requests) > 0: # Si hay peticiones sin asignar
            # Se muestra en pantalla una información breve de las peticiones sin asignar
            utils.display(data.info_general_requests_new.format(count=len(data.requests)), wait=False)
            # Se itera sobre todas ellas
            for key in data.requests:
                # Se muestra la información detallada de la petición sin asignar actual
                utils.display(data.info_general_requests_all.format(bold_text=data.bold_text, end_format=data.end_format, name=key, description=data.requests[key][0], days=data.requests[key][1], weight=data.requests[key][2]), mainColor=False, wait=False)
            utils.display("", waitText="\t\t") # Se hace una pausa en el tiempo de ejecución para que el usuario no se pierda

        if len(data.requests_in_transit) > 0: # Si hay peticiones asignadas
            # Se muestra en pantalla una información breve de las peticiones asignadas
            utils.display(data.info_general_requests_assigned.format(count=len(data.requests_in_transit)), wait=False)
            # Se itera sobre todas ellas
            for key in data.requests_in_transit:
                # Se muestra la información detallada de la petición asignada actual
                utils.display(data.info_general_requests_all.format(bold_text=data.bold_text, end_format=data.end_format, name=key, description=data.requests_in_transit[key][0], days=data.requests_in_transit[key][1], weight=data.requests_in_transit[key][2]), mainColor=False, wait=False)
            utils.display("", waitText="\t\t") # Se hace una pausa en el tiempo de ejecución para que el usuario no se pierda

        if len(data.requests_failed) > 0: # Si hay peticiones fallidas
            # Se muestra en pantalla una información breve de las peticiones fallidas
            utils.display(data.info_general_requests_failed.format(count=len(data.requests_failed)), wait=False)
            # Se itera sobre todas ellas
            for key in data.requests_failed:
                # Se muestra la información detallada de la petición fallida actual
                utils.display(data.info_general_requests_all.format(bold_text=data.bold_text, end_format=data.end_format, name=key, description=data.requests_failed[key][0], days=data.requests_failed[key][1], weight=data.requests_failed[key][2]), mainColor=False, wait=False)
            utils.display("", waitText="\t\t") # Se hace una pausa en el tiempo de ejecución para que el usuario no se pierda
    else:
        utils.display("", waitText="\t\t") # Se hace una pausa en el tiempo de ejecución para que el usuario no se pierda

def historic_info():
    # Información general de los lanzamientos entregados
    # Se muestra en pantalla una información breve de los lanzamientos entregados
    utils.display(data.info_historic_launches.format(count=len(data.launches_delivered)), wait=False, infoMessage=True)
    # Se itera sobre ellos
    for i in range(0, len(data.launches_delivered)):
        # Se muestra la información detallada del lanzamiento entregado actual
        utils.display(data.info_historic_launches_all.format(bold_text=data.bold_text, end_format=data.end_format, index=i, rocket=data.launches_delivered[i][0], date=data.launches_delivered[i][1]), mainColor=False, wait=False)
        # Se muestra en pantalla una información breve de los peticiones del lanzamientos entregado actual
        utils.display(data.info_historic_launches_requests.format(count=len(data.launches_delivered[i][3])), wait=False, infoMessage=True)
        # Se itera sobre todas ellas
        for j in range(0, len(data.launches_delivered[i][3])):
            # Se muestra el nombre de la petición actual del lanzamiento entregado actual
            utils.display(data.info_general_launches_request_info.format(name=data.launches_delivered[i][3][j]), wait=False, mainColor=False)
    utils.display("", waitText="\t\t") # Se hace una pausa en el tiempo de ejecución para que el usuario no se pierda

    # Información general de las peticiones entregadas
    # Se muestra en pantalla una información breve de las peticiones entregadas
    utils.display(data.info_historic_requests.format(count=len(data.requests_delivered)), wait=False, infoMessage=True)
    # Se itera sobre todas ellas
    for i in range(0, len(data.requests_delivered)):
        # Se muestra en pantalla una información detalla de la petición actual 
        utils.display(data.info_historic_requests_all.format(bold_text=data.bold_text, end_format=data.end_format, index=i, name=data.requests_delivered[i][0], description=data.requests_delivered[i][1][0], weight=data.requests_delivered[i][1][2], date=data.requests_delivered[i][1][1]), mainColor=False, wait=False)
    utils.display("", waitText="\t\t") # Se hace una pausa en el tiempo de ejecución para que el usuario no se pierda

# Fucnión que devuelve el texto formateado del menú de los archivos
def getFilesMenuDisplay():
    state_text = None
    state_toggle_text = None
    if data.auto_save:
        state_toggle_text = "Desactivar"
        state_text = "encendido"
    else:
        state_toggle_text = "Activar"
        state_text = "apagado"
    return data.files_menu_display.format(info_color=data.info_color, end_format=data.end_format, main_color=data.main_color, count=len(file_management.backupList()), state_toggle=state_toggle_text, state=state_text, bold_text=data.bold_text)

# Menu para la gestión de archivos
def filesMenu():
    utils.menu("", data.choice_error_message, data.menu_exit, makeChoice, data.choice_regex, [filesChoiceDict], True, dynamic_text=getFilesMenuDisplay, errorTextExtra="\t\t")

# Función para guardar una copia de seguridad
def save_backup():
    timeNow = datetime.now() # Se obtiene la fecha actual
    file_name = f"{timeNow.year}{timeNow.month}{timeNow.day}{timeNow.hour}{timeNow.minute}{timeNow.second}.json" # Se compone el nombre del archivo
    # Se compone la información a guardar
    all_info = {}
    all_info["rockets"] = data.rockets
    all_info["requests"] = data.requests
    all_info["launches"] = data.launches
    all_info["requests_failed"] = data.requests_failed
    all_info["requests_in_transit"] = data.requests_in_transit
    all_info["requests_delivered"] = data.requests_delivered
    all_info["launches_in_transit"] = data.launches_in_transit
    all_info["launches_delivered"] = data.launches_delivered
    all_info["watch"] = data.watch

    # Se guarda la información
    backupStatus = file_management.makeBackup(all_info, file_name)
    if backupStatus:
        utils.display(data.files_save_backup_success.format(info_color=data.info_color, file_name=file_name, end_format=data.end_format), successMessage=True, waitText="\t\t")

# Función para cargar una copia de seguridad
def load_backup():
    # Se obtiene la lista de todas las copias de seguridad
    backup_list = file_management.backupList()

    # Si no hay ninguna copia de seguridad creada
    if len(backup_list) == 0:
        utils.display(data.file_no_backups_error, infoMessage=True, waitText="\t\t")
        return

    # Se imprime un salto de línea
    print()
    # Se itera sobre la lista de las copias de seguridad creadas
    for i in range(0, len(backup_list)):
        # Se imprime en pantalla la copia de seguridad actual
        utils.display(data.file_backup_pick.format(bold_text=data.bold_text, end_format=data.end_format,index=i, name=backup_list[i]), wait=False, mainColor=False)
    
    # Se obtiene el nombre de la copia de seguridad a elegir
    backupNumber = utils.getAnswer(data.file_pick_display, errorText=data.file_backup_error, regex=data.launch_rocket_regex, errorTextExtra="\t\t")
    backupNumberValid = utils.checkValidEntry(backupNumber) # Se valida para ver si la entrada no está vacía o no está ya creada
    if not backupNumberValid: # Si la entrada no es válida
        return # salimos de la función
        
    # Se convierte a entero el número obtenido
    backupNumber = int(backupNumber)
    # Se comprueba que la copia de seguridad exista
    if not (0 <= backupNumber < len(backup_list)):
        # Si no existe, se muestra el mensaje de error en pantalla
        utils.display(data.file_backup_range_error, errorMessage=True, waitText="\t\t")
        return

    # Finalmente se carga la copia de seguridad
    file_management.loadBackup(backup_list[backupNumber])
    utils.display(data.file_load_backup_feeback_text.format(file=backup_list[backupNumber]), successMessage=True, waitText="\t\t")

def delete_backup():
    # Se obtiene la lista de todas las copias de seguridad
    backup_list = file_management.backupList()

    # Si no hay ninguna copia de seguridad creada
    if len(backup_list) == 0:
        utils.display(data.file_no_backups_error, infoMessage=True, waitText="\t\t")
        return

    # Se imprime un salto de línea
    print()
    # Se itera sobre la lista de las copias de seguridad creadas
    for i in range(0, len(backup_list)):
        # Se imprime en pantalla la copia de seguridad actual
        utils.display(data.file_backup_pick.format(bold_text=data.bold_text, end_format=data.end_format,index=i, name=backup_list[i]), wait=False, mainColor=False)
    
    # Se obtiene el nombre de la copia de seguridad a elegir
    backupNumber = utils.getAnswer(data.file_delete_display, errorText=data.file_backup_error, regex=data.launch_rocket_regex, errorTextExtra="\t\t")
    backupNumberValid = utils.checkValidEntry(backupNumber) # Se valida para ver si la entrada no está vacía o no está ya creada
    if not backupNumberValid: # Si la entrada no es válida
        return # salimos de la función
        
    # Se convierte a entero el número obtenido
    backupNumber = int(backupNumber)
    # Se comprueba que la copia de seguridad exista
    if not (0 <= backupNumber < len(backup_list)):
        # Si no existe, se muestra el mensaje de error en pantalla
        utils.display(data.file_backup_range_error, errorMessage=True, waitText="\t\t")
        return

    # Finalmente se borra la copia de seguridad
    file_management.deleteBackup(backup_list[backupNumber])
    utils.display(data.file_delete_backup_feeback_text.format(file=backup_list[backupNumber]), successMessage=True, waitText="\t\t")

# Función para guardar la información
def save_data():
    # Se compone la información a guardar
    general_info, historic_info = file_management.composeInfo()

    # Se guarda la información en los archivos
    file_management.saveData(general_info, force_save=True)
    file_management.saveData(historic_info, historic=True, force_save=True)
    # Se muestra feedback de éxito
    utils.display(data.file_save_data_feedback_text, successMessage=True, waitText="\t\t")

# Función para limpiar la información
def reset_data():
    file_management.clearData() # Se limpia la información
    utils.display(data.file_clear_data_feedback_text, successMessage=True, waitText="\t\t")

# Función para activar/desactivar el autoguardado
def toggle_autosave():
    data.auto_save = not data.auto_save # Se invierte el valor que tuviera
    # Se compone la información para guardar
    file_info = {}
    file_info["auto_save"] = data.auto_save
    # Se guarda la información
    file_management.saveData(file_info, force_save=True)

    [general_info, historic_info] = file_management.composeInfo()
    file_management.saveData(general_info)
    file_management.saveData(historic_info, historic=True)

    # Se determina el texto a mostrar
    auto_save_text = None
    if data.auto_save:
        auto_save_text = "activado"
    else:
        auto_save_text = "desactivado"

    utils.display(data.auto_save_feedback_text.format(state_text=auto_save_text), successMessage=True, waitText="\t\t")

# Función utilizada para salir del menú o del programa
def exit_out():
    return False

# Diccionarios con las funciones de cada menú
menuChoicesDict = {
    1: rocketMenu,
    2: requestMenu,
    3: launchMenu,
    4: assignMenu,
    5: daysMenu,
    6: infoMenu,
    7: filesMenu,
    8: exit_out
}

rocketChoicesDict = {
    1: createRocket,
    2: exit_out
}

requestChoicesDict = {
    1: request,
    2: exit_out
}

launchesChoicesDict = {
    1: launch,
    2: exit_out
}

assignChoicesDict = {
    1: assign,
    2: exit_out
}

daysChoicesDict = {
    1: days,
    2: exit_out
}

infoChoicesDict = {
    1: general_info,
    2: historic_info,
    3: exit_out
}

filesChoiceDict = {
    1: save_backup,
    2: load_backup,
    3: delete_backup,
    4: save_data,
    5: reset_data,
    6: toggle_autosave,
    7: exit_out
}