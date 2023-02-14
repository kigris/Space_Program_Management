import json
import os
from utils import display
import data
from datetime import date, datetime

# Variables para los directorios
current_dir = os.path.dirname(os.path.realpath(__file__))
data_dir = os.path.join(current_dir, "data")
backup_dir = os.path.join(data_dir, "backup")
data_general_file = os.path.join(data_dir, "general.json")
data_historic_file = os.path.join(data_dir, "historic.json")

# Función para crear un archivo nuevo
def makeFile(path, data_in="{}"):
    try: # Se intenta abrir el archivo de la ruta indicada
        with open(path, 'w') as f: # Se abre el archivo para escribir
            json.dump(json.loads(data_in), f, indent=4) # Se escribe la información al archivo
    except IOError: # Se atrapa el error
        display(data.file_critical_write_error.format(path=path), errorMessage=True, waitText="\t\t")
    except Exception as e: # de tratarse de otro error
        print(f"\n\t\t{data.error_color}{type(e).__name__}: {e}") # mostramos el error por defecto de python
        display(f"\t\t{data.unknown_error}", errorMessage=True, waitText="\t\t") # y mostramos en pantalla el mensaje de error desconocido

# Función para obtener
def getData(path):
    try: # Se intenta abrir el archivo de la ruta indicada
        with open(path, 'r') as f: # Se abre el archivo para leer
            json_data = json.load(f) # Se carga la información del archivo
    except: # Se atrapa el error
        display(data.file_critical_read_error.format(path=path), errorMessage=True, waitText="\t\t")
    return json_data

# Función que actualiza un ficher
def updateFile(path, data_in=None):
    try: # Se intenta abrir el archivo de la ruta indicada
        with open(path, 'r') as f: # Se abre el archivo para leer
            loadedData = json.load(f) # Se carga la información del archivo
    except: # Se atrapa el error
        display(data.file_critical_read_error.format(path=path), errorMessage=True, waitText="\t\t")

    # Se actualiza la información
    loadedData.update(data_in)

    try: # Se intenta abrir el archivo de la ruta indicada
        with open(path, 'w') as f: # Se abre el archivo para escribir
            json.dump(loadedData, f, indent=4, default=str) # Se escribe la información al archivo
    except: # Se atrapa el error
        display(data.file_critical_write_error.format(path=path), errorMessage=True, waitText="\t\t")

# Función que carga la información en el programa
def populateData(data_in, backup_load=False):
    if data_in: # Si hay información que cargar
        for item in data_in: # Se itera sobre ella
            if item == "rockets":
                data.rockets = data_in[item]
            elif item == "requests":
                data.requests = data_in[item]
            elif item == "launches":
                data.launches = data_in[item]
            elif item == "requests_in_transit":
                data.requests_in_transit = data_in[item]
            elif item == "requests_failed":
                data.requests_failed = data_in[item]
            elif item == "launches_in_transit":
                data.launches_in_transit = data_in[item]
            elif item == "requests_delivered":
                data.requests_delivered = data_in[item]
            elif item == "launches_delivered":
                data.launches_delivered = data_in[item]
            elif item == "watch":
                if data_in[item]:
                    data.watch = datetime.strptime(data_in[item], '%Y-%m-%d')
                    data.watch = data.watch.date()
            elif item == "auto_save" and not backup_load:
                data.auto_save = data_in[item]
            
# Función para guardar la información
def saveData(data_in, historic=False, force_save=False):
    # Si el autoguardado está encendido o si se hace un guardado forzado
    if data.auto_save or force_save:
        if not historic: # Si no se trata de información histórica
            updateFile(data_general_file, data_in=data_in) # Se guarda en el archivo general
        else: # sino
            updateFile(data_historic_file, data_in=data_in) # Se guarda en el archivo histórico

# Función que devuelve una lista con los archivos de las copias de seguridad
def backupList():
    list = os.listdir(backup_dir)
    return list

# Función para componer la información general e histórica
def composeInfo():
    general_info = {}
    general_info["rockets"] = data.rockets
    general_info["requests"] = data.requests
    general_info["launches"] = data.launches
    general_info["requests_failed"] = data.requests_failed
    general_info["requests_in_transit"] = data.requests_in_transit
    general_info["launches_in_transit"] = data.launches_in_transit
    general_info["watch"] = data.watch

    historic_info = {}
    historic_info["requests_delivered"] = data.requests_delivered
    historic_info["launches_delivered"] = data.launches_delivered

    return (general_info, historic_info)

# Función que resetea los datos
def clearData():
    data.rockets.clear()
    data.requests.clear()
    data.launches.clear()
    data.requests_failed.clear()
    data.requests_in_transit.clear()
    data.requests_delivered.clear()
    data.launches_in_transit.clear()
    data.launches_delivered.clear()
    data.watch = date.today()

    general_info, historic_info = composeInfo()
    saveData(general_info)
    saveData(historic_info, historic=True)

# Función para hacer una copia de seguridad
def makeBackup(data_in, file_name):
    # Se obtiene la ruta del archivo
    path = os.path.join(backup_dir, file_name)
    try: # Se intenta
        makeFile(path) # Se crea el archivo 
        updateFile(path, data_in=data_in) # Se escribe la información en él
        return True
    except: # Si algo sale mal
        display(data.file_critical_write_error.format(path=path), errorMessage=True, waitText="\t\t")
        return False

# Función para cargar una copia de seguridad
def loadBackup(filename):
    # Se limpian los archivos actuales
    clearData()
    data_out = getData(os.path.join(backup_dir, filename))
    populateData(data_out, backup_load=True)

    general_info, historic_info = composeInfo()
    saveData(general_info)
    saveData(historic_info, historic=True)

def deleteBackup(filename):
    os.remove(os.path.join(backup_dir, filename))

# Si el directorio de los datos no existe
if not os.path.exists(data_dir):
    os.mkdir(data_dir) # Se crea
# Si el directorio de las copias de seguridad no existe
if not os.path.exists(backup_dir):
    os.mkdir(backup_dir) # Se crea

# Si no existe el archivo de los datos generales
if not os.path.exists(data_general_file):
    makeFile(data_general_file) # Se crea
else:
    data_out = getData(data_general_file)
    populateData(data_out)

# Si no existe el archivo de los datos históricos
if not os.path.exists(data_historic_file):
    makeFile(data_historic_file) # Se crea
else:
    data_out = getData(data_historic_file)
    populateData(data_out)

# Si el autoguardado no está definido
if data.auto_save == None:
    data.auto_save = True # Se define
    # Se guarda en el archivo
    file_auto_save = {}
    file_auto_save["auto_save"] = data.auto_save
    saveData(file_auto_save)

# Si la fecha actual no está definida
if not data.watch:
    data.watch = date.today() # Se define
    # Se guarda en el archivo
    file_watch = {}
    file_watch["watch"] = data.watch
    saveData(file_watch)
