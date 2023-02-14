import data
import re

def display(text="", waitText="", wait=True, waitMessage=True, mainColor=True, errorMessage=False, successMessage=False, infoMessage=False, inlineWait=True):
    '''
    Función para imprimir en pantalla
        Entradas
            @text : texto a imprimir en pantalla
            @wait : pausa el programa y espera que el usuario pulse 'Enter' para continuar
            @waitMessage : mensaje de espera
            @mainColor : color prederminado
            @errorMessage : color de mensaje de error
            @successMessage : color de mensaje de éxito
        Salidas
            Función no productiva
    '''
    if text:
        if errorMessage: # Si se trata de un mensaje de error
            print(f"{data.error_color}{text}{data.end_format}")
        elif successMessage: # Si se trata de un mensaje de éxito
            print(f"{data.success_color}{text}{data.end_format}")
        elif infoMessage: # Si se trata de un mensaje de información
            print(f"{data.info_color}{text}{data.end_format}")
        elif mainColor: # Si se trata de un mensaje por defecto
            print(f"{data.main_color}{text}{data.end_format}")
        else:
            print(f"{text}")

    if wait: # Si se ha de hacer una pausa en el tiempo de ejecución
        if waitMessage: # Si se tiene un mensaje de espera
            if inlineWait: # Si se trata de una espera con el cursor en línea
                input(f"{waitText}{data.continue_message}")
            else: # sino
                print(f"{waitText}{data.continue_message}")
                input()
        else: # sino
            input()

def displayTime(output=False, startText="", endText=""):
    '''
    Función para obtener la fecha actual
        Entradas
            @output : si se quiere en formato salida
            @startText : texto adicional al inicio
            @endText : texto adicional al final
        Salidas
            Si output es True devolverá un string con la fecha actual
    '''
    if not output: # Si no se quiere salida
        # Se imprimirá en pantalla la fecha
        display(f"{startText}{data.time_color}Fecha: {data.watch}{data.end_format}{endText}", wait=False)
    else: # Si se quiere salida
        # Se devolverá un string con la fecha actual
        return f"{startText}{data.time_color}Fecha: {data.watch}{data.end_format}{endText}"

def getAnswer(text, errorText=None, regex=None, inline=True, outlineText="", errorTextExtra=""):
    '''
    Función para obtener una respuesta
        Entradas
            @text : texto a imprimir para pedir la respuesta
            @errorText : mensaje de error a mostrar en pantalla
            @regex : expresión regular para validar respuesta
            @inline : cursor en línea con el texto de petición
        Salidas
            @answer : respuesta obtenida
    '''
    if inline: # Si se quiere dejar el cursor en línea con el texto para introducir la respuesta
        answer = input(f"{data.main_color}{text}{data.end_format}") # se recoge la entrada de teclado en línea con el texto de petición
    else: # sino
        display(text, wait=False, waitMessage=False) # se imprime primero el texto y se salta de línea
        answer = input(outlineText) # se recoge la respuesta
    
    if regex: # si hay una expresión regular a utilizar
        if re.search(regex, answer): # si la respuesta dada por el usuario lo cumple
            return answer # devolvemos la respuesta
        elif errorText: # si tenemos un mensaje de error
            print()
            display(f"{errorTextExtra}{errorText}", errorMessage=True, waitText=errorTextExtra) # lo mostramos
            return None # y devolvemos "None"
        else: # sino
            return None # devolvemos "None"
    return answer # si no hay expresión regular devolvemos la respuesta

def tryAnswer(text, errorText, function, args=None, regex=None, inline=True, outlineText = "", errorTextExtra=""):
    '''
    Función para obtener una respuesta e intentar llamar a una función con ella
        Entradas
            @text : texto a imprimir para pedir la respuesta
            @errorText : mensaje de error a mostrar en pantalla
            @function : función a llamar
            @args : argumentos con los que se llama a la función
            @regex : expresión regular para validar respuesta
            @inline : cursor en línea con el texto de petición
        Salidas
            @answer : la respuesta de la función, puede ser "None" en caso de que salte al except o no se cumpla la expresión regular
    '''
    answer = getAnswer(text, inline=inline, outlineText=outlineText) # obtenemos la respuesta

    try: # entramos en bloque "try"
        if regex: # si hay una expresión regular a utilizar
            if re.search(regex, answer): # si la respuesta dada por el usuario lo cumple
                arguments = args.copy() # creamos una copia de los argumentos para no modificarlos
                arguments.append(answer) # añadimos la respuesta a la nueva lista de argumentos
                return function(arguments) # llamamos a la función con los argumentos
            else: # sino
                print()
                display(f"{errorTextExtra}{errorText}", errorMessage=True, waitText=errorTextExtra) # mostramos el mensaje de error en la pantalla
        else: # sino
            arguments = args.copy() # creamos una copia de los argumentos para no modificarlos
            arguments.append(answer) # añadimos la respuesta a la nueva lista de argumentos
            return function(arguments) # llamamos a la función con los argumentos
    except (TypeError, NameError, KeyError): # manejamos éstos errores
        display(f"{errorTextExtra}{errorText}", errorMessage=True, waitText=errorTextExtra) # y mostramos el mensaje de error en pantalla
    except Exception as e: # de tratarse de otro error
        print(f"{data.error_color}{type(e).__name__}: {e}") # mostramos el error por defecto de python
        display(f"{errorTextExtra}{data.unknown_error}", errorMessage=True, waitText=errorTextExtra) # y mostramos en pantalla el mensaje de error desconocido

def menu(text, errorMessage, menuExit, function, regex, args, inline, errorTextExtra="", dynamic_text=""):
    '''
    Función para imprimir menús
        Entradas
            @text : texto del menú
            @errorMessage : mensaje de error a mostrar en pantalla en caso de equivocación
            @menuExit : función para salir del menú
            @function : función a llamar para ejecutar las diferentes opciones del menú
            @regex : expresión regular para validar respuesta
            @args : argumentos con los que se llama a la función
            @inline : cursor en línea con el texto de petición
        Salidas
            Función no productiva
    '''
    while(True): # bucle infinito
        displayText = text
        if not text:
            if dynamic_text:
                displayText = dynamic_text()
        answer = tryAnswer(displayText, errorMessage, function, regex=regex, args=args, inline=inline, errorTextExtra=errorTextExtra) # obtenemos una respuesta
        if answer == False: # si la respuesta es "False"
            display(menuExit, waitText="\t") # mostramos el mensaje de salida en pantalla
            break # rompemos el bucle

def checkValidEntry(inputToCheck, dictionary=None, errorMessage=None, errorTextExtra=""):
    '''
    Función para validar si un elemento es nulo o no está en un diccionario
        Entradas
            @inputToCheck : entrada a verificar
            @dictionary : diccionario en el que buscar
            @errorMessage : 
        Salidas
            Función no productiva
    '''
    if not inputToCheck: # si la entrada es "None" o está vacía
        return False # devolvemos "False"
    if dictionary: # si hay un diccionario en el que buscar
        if inputToCheck.lower() in [element.lower() for element in dictionary]: # miramos si la entrada está en el diccionario
            display(f"{errorTextExtra}{errorMessage}", errorMessage=True, waitText=errorTextExtra) # mostramos el mensaje de error
            return False # devolvemos "False"
    return True # devolvemos "True"