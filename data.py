# Colores
main_color = '\033[95m'
submain_color = '\33[35m'
header_color = '\033[96m'
time_color = '\033[93m'
info_color = '\033[94m'
bold_text = '\033[1m'
error_color = '\033[91m'
success_color = '\033[92m'
end_format = '\033[0m'

# Fecha
watch = None

# Autoguardado
auto_save = None

# Texto principal
welcomeText = f"\n{bold_text}Bienvenido al programa de estación espacial Gamma\n¿Que desea hacer?\n\n{end_format}"
optionsText = f"{submain_color}\t1) Tipos cohetes\n\t2) Peticiones estación\n\t3) Lanzamientos disponibles\n\t4) Asignar\n\t5) Días\n\t6) Info sistema\n\t7) Archivos\n\t8) Salir\n\t\tElige: {end_format}"
menu_info_display = "{header_color}Cohetes({rocket_count}){end_format}\t{header_color}Lanzamientos({launch_count}):{end_format} {launch_new_count} sin desplegar, {success_color}{launch_transit_count} desplegados{end_format}, {info_color}{launch_delivered_count} entregados{end_format}\t{header_color}Peticiones({request_count}):{end_format} {request_new_count} sin asignar, {success_color}{request_assigned_count} asignadas{end_format}, {error_color}{request_failed_count} no asignadas{end_format}, {info_color}{request_delivered_count} entregadas{end_format}\n\n"
choice_error_message = "No has introducido una opción válida. Por favor, introduzca un número correspondiente a una acción."
menu_exit = "\n\tSaliendo al menú principal..."
app_exit = "\n\tSaliendo del programa..."
continue_message = f"{header_color}Pulse 'Enter' para continuar...{end_format}"
all_regex = r"^(?!\s*$).+"
choice_regex = r'^[1-9][0-9]*$'
unknown_error = "\n\t\tError crítico."
auto_save_text = "{bold_text}Autoguardado {state}{end_format}"

# Texto de cohetes
rocket_menu_display = "\n\tTipos cohete\n\t\t1) Crear cohete\n\t\t2) Salir\n\t\t\tElige: "
rocket_name_display = "\n\t\tIntroduzca el nombre del cohete: "
rocket_name_error = "El nombre introducido no es correcto. Debe tener una longitud entre 3-20 carácteres, contener carácteres alfanuméricos pero comenzar por una letra."
rocket_duplicate_error = "Ya existe un cohete con ese nombre. Introduzca otro..."
rocket_max_weight_display = "\t\tIntroduzca la capacidad de carga del cohete {name} (en kg): "
rocket_max_weight_error = "Peso inválido. Debe ser un número entero mayor que 0..."
rocket_create_success = "\n\t\t¡Cohete creado con éxito!\n\t\t\tNombre: {name}\n\t\t\tPeso: {weight}kg"
rocket_name_regex = r'^[a-zA-Z][a-zA-Z0-9-_]{2,30}'
rocket_max_weight_regex = r'^[1-9][0-9]*$'

# Texto de peticiones
request_menu_display = "\n\tPeticiones estación\n\t\t1) Crear petición\n\t\t2) Salir\n\t\t\tElige: "
request_name_display = "\n\t\tIntroduzca el nombre de la petición: "
request_name_error = "El nombre introducido no es correcto. Debe tener una longitud entre 3-20 carácteres, contener carácteres alfanuméricos pero comenzar por una letra."
request_new_duplicate_error = "Ya existe una petición sin asignar con ese nombre. Introduzca otra..."
request_assigned_duplicate_error = "Ya existe una petición asignada con ese nombre. Introduzca otra..."
request_failed_duplicate_error = "Ya existe una petición fallida con ese nombre. Introduzca otra..."
request_description_display = "\t\tIntroduzca la descripción de la petición {name}: "
request_description_error = "La descripción introducida no es correcta. Debe tener una longitud entre 8-60 carácteres y contener carácteres alfanuméricos. Se pueden utilizar los carácteres especiales: '-', '.', '(', ')'."
request_weight_display = "\t\tIntroduzca el peso de la petición {name} (en kg): "
request_weight_error = "Peso inválido. Debe ser un número real mayor que 0..."
request_max_days_display =  "\t\tIntroduzca los días de llegada máximos de la petición {name}: "
request_max_days_error = "Número máximo de días inválido. Debe ser un número natural..."
request_create_succes = "\n\t\t¡Petición creada con éxito!\n\t\t\tNombre: {name}\n\t\t\tDescripción: {description}\n\t\t\tPeso: {weight}kg\n\t\t\tDías de llegada máximos: {max_days}"
request_name_regex = r'^[a-zA-Z][a-zA-Z0-9-_]{2,30}'
request_description_regex = r'[a-zA-Z0-9-,.() ]{8,60}'
request_weight_regex = r'^[1-9][0-9.]*$'
request_max_days_regex = r'^[1-9]*[0-9]+$'

# Texto de lanzamientos
launch_menu_display = "\n\tLanzamientos disponibles\n\t\t1) Crear lanzamiento\n\t\t2) Salir\n\t\t\tElige: "
launch_no_rockets = "\n\t\tNo hay ningún cohete creado para poder crear un lanzamiento. Debe crear uno..."
launch_rocket_display = "\n\t\tIntroduzca el número correspondiente al cohete a utilizar: "
launch_rocket_error = "Debes introducir un número correspondiente al cohete a utilizar."
launch_no_rocket_error = "No existe ningún cohete con el número seleccionado. Inténtalo otra vez..."
launch_days_display = "\t\tIntroduzca el número de días de llegada: "
launch_days_error = "Número de días de llegada inválido. Debe ser un número natural..."
launch_create_success = "\n\t\t¡Lanzamiento añadido con éxito!\n\t\t\tCohete asignado: {rocket}\n\t\t\tDías de llegada: {days}"
launch_rocket_regex = r'^[0-9]+$'
launch_days_regex = r'^[1-9]*[0-9]+$'
launch_rocket_pick = "\t\t\t{index} - Nombre: {bold_text}{name}{end_format}\tCapacidad de carga: {bold_text}{weight}{end_format}kg"

# Texto de asignar
assign_menu_display = "\n\tAsignar\n\t\t1) Comenzar proceso de asignación\n\t\t2) Salir\n\t\t\tElige: "
assign_new_requests_start = "\t\tAsignando peticiones nuevas..."
assign_failed_requests_start = "\t\tReasignando peticiones fallidas..."
assign_new_feedback = "\t\tSe ha asignado con éxito la petición nueva \"{request_name}\" al lanzamiento \"{launch_name}\""
assign_new_fail_feedback = "\t\tNo se ha podido asignar la petición nueva \"{request_name}\" a ningún lanzamiento actual"
assign_fail_feedback = "\t\tNo se ha podido reasignar la petición fallida \"{request_name}\" a ningún lanzamiento actual"
assign_failed_feedback = "\t\tSe ha reasignado con éxito la petición fallida \"{request_name}\" al lanzamiento \"{launch_name}\""
assign_new_feedback_all = "\t\t{success_color}Peticiones nuevas asignadas: {success_counter}{end_format}\n\t\t{error_color}Peticiones nuevas no asignadas(fallidas): {failed_counter}{end_format}\n\n\t\tAsignación completada"
assign_failed_feedback_all = "\t\t{success_color}Peticiones fallidas reasignadas: {success_counter}{end_format}\n\t\t{error_color}Peticiones fallidas no asignadas: {failed_counter}{end_format}\n\n\t\tAsignación completada"
assign_no_new = "\t\tNo hay peticiones nuevas que asignar"
assign_no_failed = "\t\tNo hay peticiones fallidas que reasignar"

# Texto de días
days_menu_display = "\n\tDías\n\t\t1) Avanzar días\n\t\t2) Salir\n\t\t\tElige: "
days_input_text = "\n\t\tIntroduzca el número de días a transcurrir: "
days_error = "Número de días a transcurrir inválido. Debe ser un número entero mayor que 0..."
days_regex = r"^[1-9]+[0-9]*$"

# Texto de información
info_menu_display = "\n\tInfo sistema\n\t\t1) Ver información\n\t\t2) Ver historial\n\t\t3) Salir\n\t\t\tElige: "
info_general_rockets = "\n\t\tCohetes({count})"
info_general_rockets_all = "\t\t\tNombre: {bold_text}{name}{end_format}\tCapacidad de carga: {bold_text}{weight}{end_format}kg"
info_general_requests = "\n\t\tPeticiones({count}) - {new_count} sin asignar, {transit_count} asignadas, {failed_count} fallidas"
info_general_requests_new = "\t\t\tPeticiones sin asignar({count})"
info_general_requests_assigned = "\t\t\tPeticiones asignadas({count})"
info_general_requests_failed = "\t\t\tPeticiones fallidas({count})"
info_general_requests_all = "\t\t\t\tNombre: {bold_text}{name}{end_format}\tDescripción: {bold_text}{description}{end_format}\tDías máximos: {bold_text}{days}{end_format}\tPeso: {bold_text}{weight}{end_format}kg"
info_general_launches = "\n\t\tLanzamientos({count}) - {standby_count} no desplegados, {transit_count} desplegados"
info_general_launches_new = "\t\t\tLanzamientos no desplegados({count})"
info_general_launches_transit = "\n\t\t\tLanzamientos desplegados({count})"
info_general_launches_all = "\t\t\t\tNº: {bold_text}{index}{end_format}\tCohete utilizado: {bold_text}{rocket}{end_format}\tDías de llegada: {bold_text}{days}{end_format}\tCapacidad de carga restante: {bold_text}{weight}{end_format}"
info_general_launches_requests = "\t\t\t\tPeticiones({count})"
info_general_launches_request_info = "\t\t\t\t\t{name}"
info_general_launches_no_requests = "\t\t\t\t\tNo hay peticiones asignadas a este lanzamiento"

info_historic_requests = "\n\t\tPeticiones entregadas({count})"
info_historic_requests_all = "\t\t\tNº: {bold_text}{index}{end_format}\tNombre: {bold_text}{name}{end_format}\tDescripción: {bold_text}{description}{end_format}\tPeso: {bold_text}{weight}{end_format}kg\tEntregado: {bold_text}{date}{end_format}"
info_historic_launches = "\t\tLanzamientos entregados({count})"
info_historic_launches_all = "\t\t\tNº: {bold_text}{index}{end_format}\tCohete utilizado: {bold_text}{rocket}{end_format}\tEntregado: {bold_text}{date}{end_format}"
info_historic_launches_requests = "\t\t\t\tPeticiones entregadas({count})"

# Texto de archivos
files_menu_display = "\n\tGestión de archivos\n\n\t\t{info_color}Copias de seguridad: {count}{end_format}\n\n\t\t{bold_text}Autoguardado {state}{end_format}\n\n\t\t{main_color}1) Guardar copia de seguridad\n\t\t2) Cargar copia de seguridad\n\t\t3) Borrar copia de seguridad\n\t\t4) Guardar datos existentes\n\t\t5) Limpiar datos existentes\n\t\t6) {state_toggle} autoguardado\n\t\t7) Salir\n\t\t\tElige: {end_format}"
files_save_backup_success = "\n\t\tSe ha guardado con éxito la copia de seguridad: {info_color}{file_name}{end_format}"
file_no_backups_error = "\n\t\tNo hay ninguna copia de seguridad creada... Debe crear una..."
file_backup_pick = "\t\t\t{index} - Nombre: {bold_text}{name}{end_format}"
file_pick_display = "\n\t\tIntroduzca el número correspondiente a la copia de seguridad a cargar: "
file_backup_error = "Debes introducir un número correspondiente a la copia de seguridad a restaurar."
file_backup_range_error = "\n\t\tNo existe ninguna copia de seguridad con el número seleccionado. Inténtalo otra vez..."
file_load_backup_feeback_text = "\n\t\t¡Se ha cargado con éxito la copia de seguridad {file}!"
file_delete_display = "\n\t\tIntroduzca el número correspondiente a la copia de seguridad a borrar: "
file_delete_backup_feeback_text = "\n\t\t¡Se ha borrado con éxito la copia de seguridad {file}!"
auto_save_feedback_text = "\n\t\t¡Se ha {state_text} el autoguardado!"
file_save_data_feedback_text = "\n\t\t¡Se ha guardado con éxito el estado actual!"
file_clear_data_feedback_text = "\n\t\t¡Se han limpiado con éxito todos los datos existentes!"
file_critical_write_error = "\n\t\tHa habido un problema al intentar escribir en la ruta: {path}"
file_critical_read_error = "\n\t\tHa habido un problema al intentar leer en la ruta: {path}"

# Colecciones
rockets = {}
requests = {}
launches = []
requests_failed = {}
requests_in_transit = {}
requests_delivered = []
launches_in_transit = []
launches_delivered = []