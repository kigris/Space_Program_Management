import core
import utils
import data

# Menú principal
while(True):
    time = utils.displayTime(output=True, startText = "\n\n\t", endText="\n\n")
    auto_save_text = None
    if data.auto_save:
        auto_save_text = data.auto_save_text.format(state="encendido", bold_text=data.bold_text, end_format=data.end_format)
    else:
        auto_save_text = data.auto_save_text.format(state="apagado", bold_text=data.bold_text, end_format=data.end_format)

    info_text = data.menu_info_display.format(header_color=data.header_color,info_color=data.info_color, end_format=data.end_format, success_color=data.success_color, error_color=data.error_color, rocket_count=len(data.rockets), launch_count=len(data.launches)+len(data.launches_in_transit)+len(data.launches_delivered), launch_new_count=len(data.launches), launch_transit_count=len(data.launches_in_transit), launch_delivered_count=len(data.launches_delivered), request_count=len(data.requests)+len(data.requests_in_transit)+len(data.requests_failed)+len(data.requests_delivered), request_new_count=len(data.requests), request_assigned_count=len(data.requests_in_transit), request_failed_count=len(data.requests_failed), request_delivered_count=len(data.requests_delivered))
    # Recogemos la respuesta del +usuario y verificamos si es válida
    answer = utils.tryAnswer(data.welcomeText+info_text+auto_save_text+time+data.optionsText, data.choice_error_message, core.makeChoice, regex=data.choice_regex, args=[core.menuChoicesDict], outlineText="\t", errorTextExtra="\t")
    if answer == False: # Si la respuesta es "False"
        utils.display(data.app_exit, waitText="\t") # quiere decir que el usuario ha llamado a la función de salida
        break # rompemos el bucle y se acaba el programa