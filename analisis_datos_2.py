"""SEGUNDA PARTE DEL PIA. DATASET DE VENTAS USADO"""

import pandas as pd
import matplotlib.pyplot as plt
import time

archivo = 'ventas_dataset.csv' #Desde aquí definimos el path del archivo.
"""--- MENSAJES DE SISTEMA ---"""
def limpiar_consola():
    """Puramente estética, para limpiar la consola en algunas ocasiones. Cómo al inicio del programa"""
    for i in range(20):
        print("\n")

def info_message(type: int, texto:str):
    """
    Función para mandar información sobre el sistema al usuario usando un print customizado.
    Tipo 1: Error
    Tipo 2: Información del sistema
    """
    hora_actual = time.strftime('%H:%M:%S')

    if type == 1:
        print(f"[{hora_actual}] [ERROR]: {texto}")
    elif type == 2:
        print(f"[{hora_actual}] [INFO]: {texto}")
    else:
        print(f"[{hora_actual}]: {texto}")
    return
"""--- PREGUNTAR SI DESEA GUARDAR EL REPORTE EN UN .TXT"""
def save_file():
    """Pregunta si deseas ver una gráfica o no. Dado que iba a ser muy repetitivo colocarlo en cada funcion de análisis de datos, cree una función."""
    dialog = input(str('¿Deseas guardar el reporte en un archivo? (SI/NO): '))
    if dialog.lower() == 'si' or dialog.lower() == 'sí' : #Convertimos a LowerCase para que no importe "SI" o "si"
        info_message(2, "Seleccionaste SI guardar el reporte, creando.....")
        return True #Retorna TRUE, si se guardará.
    elif dialog.lower() == 'no':
        info_message(2, "Seleccionaste NO guardar el reporte.")
        return False #Retorna FALSE, NO se enseñará se guardará
    else:
        info_message(1, "Solamente puedes elegir entre SI o NO!")
        info_message(1, "No seleccionaste una opción válida, se tomará cómo un NO.")
        return False

"""--- PREGUNTAR SI DESEA VER LA GRÁFICA O NO"""
def ask_grafica():
    """Pregunta si deseas ver una gráfica o no. Dado que iba a ser muy repetitivo colocarlo en cada funcion de análisis de datos, cree una función."""
    dialog = input(str('¿Deseas ver una gráfica para visualizar los datos? (SI/NO): '))
    if dialog.lower() == 'si' or dialog.lower() == 'sí' : #Convertimos a LowerCase para que no importe "SI" o "si"
        info_message(2, "Seleccionaste SI ver la gráfica, construyendo gráfica...")
        return True #Retorna TRUE, si se mostrará la gráfica.
    elif dialog.lower() == 'no':
        info_message(2, "Seleccionaste NO ver la gráfica.")
        return False #Retorna FALSE, NO se enseñará la grafica
    else:
        info_message(1, "Solamente puedes elegir entre SI o NO!")
        info_message(1, "No seleccionaste una opción válida, se tomará cómo un NO.")
        return False

"""--- PREGUNTAR SI SE DESEA GUARDAR LA GRÁFICA O NO ---"""
def save_grafica():
    "Función para preguntar si el usuario desea guardar la gráfica. No hay más."""
    dialog = input(str('Antes de visualizar la grafica, ¿deseas guardarla?: '))
    if dialog.lower() == 'si' or dialog.lower() == 'sí' : #Convertimos a LowerCase para que no importe "SI" o "si"
        info_message(2, "Seleccionaste SI guardar la gráfica..")
        return True #Retorna TRUE, si se mostrará la gráfica.
    elif dialog.lower() == 'no':
        info_message(2, "Seleccionaste NO guardar la gráfica.")
        return False #Retorna FALSE, NO se enseñará la grafica
    else:
        info_message(1, "Solamente puedes elegir entre SI o NO!")
        info_message(1, "No seleccionaste una opción válida, se tomará cómo un NO.")
        return False

"""--- CREAR UN NUEVO ARCHIVO Y VERFICAR QUE SE CREÓ CORRECTAMENTE"""

"""--- CARGAR Y VERIFICAR EL ARCHIVO ---"""
def cargar_datos(csv: str):
    """Función para verificar que el .csv cargue correctamente"""
    if not csv.endswith('.csv'): #Simple verificación para comprobar la extensión .csv.
        info_message(1, 'El archivo no tiene el formato .csv!')
        return
    try:
        global df
        df = pd.read_csv(csv)
        info_message(2, 'Archivo cargado correctamente!')
    except FileNotFoundError: #Archivo no encontrado
        info_message(1, 'No se encontró el archivo!')
        return
    except Exception as e: #Cualquier otra excepción
        info_message(1, f'Hubo un error desconocido! {e}')
        return
    
"""--- OPCIONES DEL MENÚ ---"""

def menu():
    while True:
        limpiar_consola()
        print("--- ¡HOLA DE NUEVO! ---")
        print("1. Información de costos por unidad")
        print("2. Información de costos totales por item")
        print("3. Items más populares por región.")
        print("4. Generar un reporte sobre un Item.")
        print("5. Salir")
        try:
            opcion = int(input('Selecciona una opción del menú: '))
        except ValueError:
            info_message(1, "No se introdujo un valor válido.")
            info_message (2, "Regresando al menú...")
            time.sleep(5)
            return menu()
        except Exception as e:
            info_message(1, f'Ocurrió un error desconocido: {e}. Si el error persiste, reinicia el programa.')
            info_message(2, 'Regresando al menú...')
            return menu()
        match opcion:
            case 1:
                return opcion_1()
            case 2:
                return opcion_2()
            case 3:
                chart_avg_items_country()
            case 4:
                generar_reporte_item()
            case 5:
                print("Gracias por tu preferencia!")
                print("Saliendo del programa...")
                time.sleep(3)
                break
            case _any:
                info_message(1, "Solo puedes escoger un número de los presentados en el menú!")
                info_message (2, "Regresando al menú...")
                time.sleep(5)
    

def opcion_1():
    while True:
        limpiar_consola()
        print('\n')
        print('¿Qué información quieres ver relacionada a los costos por unidad?')
        print('1. Ranking de Unidades Vendidas')
        print('2. Ranking del precio por Unidad')
        print('3. Ranking del costo por unidad')
        print('4. Promedio de Unidades Vendidas')
        print('5. Top 5 Unidades MEJOR vendida.')
        print('6. Top 5 Unidades PEOR vendida.')
        print('7. Cambie de opinión. Volver al menú principal.')
        try:
            opcion = int(input('Selecciona una opción del menú: '))
        except ValueError:
            info_message(1, "No se introdujo un valor válido.")
            info_message (2, "Regresando al menú...")
            time.sleep(5)
            return opcion_1()
        except Exception as e:
            info_message(1, f'Ocurrió un error desconocido: {e}. Si el error persiste, reinicia el programa.')
            info_message(2, 'Regresando al menú...')
            return opcion_1()
        match opcion:
            case 1:
                rank_units_sold()
            case 2:
                rank_units_price()
            case 3:
                rank_units_cost()
            case 4:
                prom_units_sold()
            case 5:
                max_unit_sales()
            case 6:
                min_unit_sales()
                
            case 7:
                info_message (2, "Regresando al menú principal...")
                time.sleep(5)
                return menu()
            case _any:
                info_message(1, "Solo puedes escoger un número de los presentados en el menú!")
                info_message (2, "Regresando al menú...")
                time.sleep(5)


def opcion_2():
    while True:
        limpiar_consola()
        print('\n')
        print('¿Qué información quieres ver relacionada a costos totales?')
        print('1. Ranking de Items por ganancia neta.')
        print('2. Ranking de Items por costo total.')
        print('3. Ranking de Items por ganancia total.')
        print('4. Items con la MAYOR ganancia total.')
        print('5. Items con la PEOR ganancia total.')
        print('6. Cambie de opinión. Volver al menú principal')
        try:
            opcion = int(input('Selecciona una opción del menú: '))
        except ValueError:
            info_message(1, "No se introdujo un valor válido.")
            info_message (2, "Regresando al menú...")
            time.sleep(5)
            return opcion_2()
        except Exception as e:
            info_message(1, f'Ocurrió un error desconocido: {e}. Si el error persiste, reinicia el programa.')
            info_message(2, 'Regresando al menú...')
            return opcion_2()
        match opcion:
            case 1:
                rank_item_net_revenue()
            case 2:
                rank_item_net_cost()
            case 3:
                rank_item_total_gain()
            case 4:
                max_total_profit_item()
            case 5:
                min_total_profit_item()
                
            case 6:
                info_message (2, "Regresando al menú principal...")
                time.sleep(5)
                return menu()
            case _any:
                info_message(1, "Solo puedes escoger un número de los presentados en el menú!")
                info_message (2, "Regresando al menú...")
                time.sleep(5)

"""--- OPCIÓN 1 --- """

def rank_units_sold():
    """Ranking de Unidades Vendidas"""
    info_message(2, 'Seleccionaste ver el ranking de unidades vendidas!')
    info_message(2, 'Cargando información...')
    time.sleep(5)
    mostrar_info = df.groupby('Item Type')['Units Sold'].sum().sort_values(ascending=False).reset_index()#.sort_values(by='Units Sold', ascending=False) #Primero, obtenemos la suma de todo lo vendido por Item, y después lo ordenamos.
    #IMPORTANTE: Aqui use reset_index para mostrar la información de una manera más ordenada en la consola.
    # Una consecuencia de esto es que, ahora mostrar_info es un nuevo DataFrame
    # Y es por ello que más abajo, al momento de crear la gráfica de barras, 1en vez de usar
    # mostrar_info.values, se tiene que usar mostrar_info['Item Type']1
    
    print(mostrar_info)
    if ask_grafica() is False: #Si se eligió "NO" simplemente salimos de la función.
        return
    
    # Aqui empieza la gráfica
    colores = ['green' if v>=45000 else 'red' for v in mostrar_info['Units Sold']] #Asignamos colores si el valor es menor a 45000
    plt.figure(figsize=(20,10))
    bars = plt.barh(mostrar_info['Item Type'], mostrar_info['Units Sold'], color=colores) #Dado que tenemos muchos Items, haremos una barra horizontal
    for bar in bars:
        w = bar.get_width()
        plt.text(w + (mostrar_info['Units Sold'].max() * 0.01), 
                bar.get_y() + bar.get_height()/2, 
                f'{w:.1f}', 
                va='center', fontsize=10)
    plt.title('Volumen Total de Ventas Por Item', fontsize=14)
    plt.xlabel('Item')
    plt.ylabel('Total de Ventas')
    plt.axvline(x=45000, color='orange', linestyle='dashed', label='Más de $45000') #Creamos una linea de referencia
    plt.legend()
    plt.tight_layout() #Evita que se corten etiquetas
    if save_grafica() is True:
        plt.savefig('grafica.png', dpi=250)
    plt.show()
    
def rank_units_cost():
    """Ranking de Costo Por Unidad"""
    info_message(2, 'Seleccionaste ver el ranking de Costo por Unidad!')
    info_message(2, 'Cargando información...')
    time.sleep(5)
    mostrar_info = df.groupby('Item Type')['Unit Cost'].sum().sort_values(ascending=False).reset_index() #Primero, obtenemos la suma de todo lo vendido por Item, y después lo ordenamos.
    print(mostrar_info)

    if ask_grafica() is False: #Si se eligió "NO" simplemente salimos de la función.
        return
    
    # Aqui empieza la gráfica
    colores = ['green' if v<=700 else 'red' for v in mostrar_info['Unit Cost']] #Asignamos colores si el valor es menor a 45000
    plt.figure(figsize=(20,10))
    bars = plt.barh(mostrar_info['Item Type'], mostrar_info['Unit Cost'], color=colores) #Dado que tenemos muchos Items, haremos una barra horizontal
    for bar in bars:
        w = bar.get_width()
        plt.text(w + (mostrar_info['Unit Cost'].max() * 0.01), 
                bar.get_y() + bar.get_height()/2, 
                f'{w:.1f}', 
                va='center', fontsize=10)
    plt.title('Costo total por Unidad', fontsize=14)
    plt.xlabel('Unidad')
    plt.ylabel('Costo total')
    plt.axvline(x=700, color='orange', linestyle='dashed', label='Más de $700') #Creamos una linea de referencia
    plt.legend()
    plt.tight_layout() #Evita que se corten etiquetas
    if save_grafica() is True:
        plt.savefig('grafica.png', dpi=250)
    plt.show()

def rank_units_price():
    """Ranking de Unidades por Precio"""
    info_message(2, 'Seleccionaste ver el ranking de Precio Por Unidad!')
    info_message(2, 'Cargando información...')
    time.sleep(5)
    mostrar_info = df.groupby('Item Type')['Unit Price'].sum().sort_values(ascending=False).reset_index() #Primero, obtenemos la suma de todo lo vendido por Item, y después lo ordenamos.
    print(mostrar_info)

    if ask_grafica() is False: #Si se eligió "NO" simplemente salimos de la función.
        return
    
    # Aqui empieza la gráfica
    colores = ['green' if v>=4000 else 'red' for v in mostrar_info['Unit Price']] #Asignamos colores si el valor es menor a 45000
    plt.figure(figsize=(20,10))
    bars = plt.barh(mostrar_info['Item Type'], mostrar_info['Unit Price'], color=colores) #Dado que tenemos muchos Items, haremos una barra horizontal
    for bar in bars:
        w = bar.get_width()
        plt.text(w + (mostrar_info['Unit Price'].max() * 0.01), 
                bar.get_y() + bar.get_height()/2, 
                f'{w:.1f}', 
                va='center', fontsize=10)
    plt.title('Precio (al consumidor) por Unidad', fontsize=14)
    plt.xlabel('Unidad')
    plt.ylabel('Precio')
    plt.axvline(x=4000, color='orange', linestyle='dashed', label='Más de $4000') #Creamos una linea de referencia
    plt.legend()
    plt.tight_layout() #Evita que se corten etiquetas
    if save_grafica() is True:
        plt.savefig('grafica.png', dpi=250)
    plt.show()

def prom_units_sold():
    """Promedio Total de Unidades Vendidas"""
    info_message(2, 'Seleccionaste ver el promedio total de Unidades Vendidas!')
    info_message(2, 'Cargando información...')
    time.sleep(5)
    mostrar_info = df.groupby('Item Type')['Units Sold'].mean().sort_values(ascending=False).reset_index() #Primero, obtenemos la suma de todo lo vendido por Item, y después lo ordenamos.
    print(mostrar_info)

    if ask_grafica() is False: #Si se eligió "NO" simplemente salimos de la función.
        return

    # Aqui empieza la gráfica
    plt.figure(figsize=(20,10))
    bars = plt.barh(mostrar_info['Item Type'], mostrar_info['Units Sold'], color='green') #Dado que tenemos muchos Items, haremos una barra horizontal
    for bar in bars:
        w = bar.get_width()
        plt.text(w + (mostrar_info['Units Sold'].max() * 0.01), 
                bar.get_y() + bar.get_height()/2, 
                f'{w:.1f}', 
                va='center', fontsize=10)
    plt.title('Promedio Total de Unidades Vendidas', fontsize=14)
    plt.xlabel('Unidad')
    plt.ylabel('Promedio')
    plt.tight_layout() #Evita que se corten etiquetas
    if save_grafica() is True:
        plt.savefig('grafica.png', dpi=250)
    plt.show()

def max_unit_sales():
    """Top 5 Unidades Más Vendidas"""
    info_message(2, 'Seleccionaste ver el top 5 de Unidades más Vendidas!')
    info_message(2, 'Cargando información...')
    time.sleep(5)
    mostrar_info = df.groupby('Item Type')['Units Sold'].sum().nlargest(5).sort_values(ascending=False).reset_index()
    #Primero, obtenemos la suma de todo lo vendido por Item, y con nlargest obtenemos los mejores 5.
    print(mostrar_info)

    if ask_grafica() is False: #Si se eligió "NO" simplemente salimos de la función.
        return

    colores = ['#1F6F5F', '#2FA084', '#6FCF97','#9AD872' , '#B5E18B',]
    plt.figure(figsize=(8,5)) # Tamaño del lienzo (ancho por alto)
    bars = plt.bar(mostrar_info['Item Type'], mostrar_info['Units Sold'], color=colores)
    #Etiqueta con el valor encima de cada barra
    for bar in bars:
        h = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, h+1, f'{h:.1f}', ha='center', fontsize=10)

    plt.title('Top 5 de Unidades Más Vendidas', fontsize=14)
    plt.xlabel('Unidad')
    plt.ylabel('Cantidad Vendida')
    plt.tight_layout()
    if save_grafica() is True:
        plt.savefig('grafica.png', dpi=250)
    plt.show()

def min_unit_sales():
    """Top 5 Unidades PEOR Vendidas"""
    info_message(2, 'Seleccionaste ver el top 5 de Unidades peor vendidas.')
    info_message(2, 'Cargando información...')
    time.sleep(5)
    mostrar_info = df.groupby('Item Type')['Units Sold'].sum().nsmallest(5).sort_values(ascending=True).reset_index()
    
    #Primero, obtenemos la suma de todo lo vendido por Item, y con nsmallest obtenemos los 5 peores.
    print(mostrar_info)

    if ask_grafica() is False: #Si se eligió "NO" simplemente salimos de la función.
        return

    colores = ['#a70000', '#ff0000', '#ff5252','#ff7b7b' , '#ffbaba',]
    plt.figure(figsize=(8,5)) # Tamaño del lienzo (ancho por alto)
    bars = plt.bar(mostrar_info['Item Type'], mostrar_info['Units Sold'], color=colores)
    #Etiqueta con el valor encima de cada barra
    for bar in bars:
        h = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, h+1, f'{h:.1f}', ha='center', fontsize=10)

    plt.title('Top 5 de Unidades PEOR Vendidas', fontsize=14)
    plt.xlabel('Unidad')
    plt.ylabel('Cantidad Vendida')
    plt.tight_layout()
    if save_grafica() is True:
        plt.savefig('grafica.png', dpi=250)
    plt.show()

"""--- OPCION 2 ---"""
def rank_item_net_revenue():
    """Ranking de Items por Ganancia Neta"""
    info_message(2, 'Seleccionaste ver el ranking de Items por Ganancia Neta!')
    info_message(2, 'Cargando información...')
    time.sleep(5)
    mostrar_info = df.groupby('Item Type')['Total Revenue'].sum().sort_values(ascending=True).reset_index() #Primero, obtenemos la suma de todo lo vendido por Item, y después lo ordenamos.
    print(mostrar_info)

    if ask_grafica() is False: #Si se eligió "NO" simplemente salimos de la función.
        return
    
    # Aqui empieza la gráfica
    colores = ['#5B7E3C','#468432' ,'#9AD872' , '#A2CB8B', '#CCD67F'] #Asignamos colores si el valor es menor a 45000
    plt.figure(figsize=(20,10))
    bars = plt.barh(mostrar_info['Item Type'], mostrar_info['Total Revenue'], color=colores) #Dado que tenemos muchos Items, haremos una barra horizontal
    for bar in bars:
        w = bar.get_width()
        plt.text(w + (mostrar_info['Total Revenue'].max() * 0.01), 
                bar.get_y() + bar.get_height()/2, 
                f'{w:.1f}', 
                va='center', fontsize=10)
    plt.title('Ganancia Neta por Item', fontsize=14)
    plt.xlabel('Item')
    plt.ylabel('Ganancia Neta')
    plt.tight_layout() #Evita que se corten etiquetas
    if save_grafica() is True:
        plt.savefig('grafica.png', dpi=250)
    plt.show()
    return

def rank_item_net_cost():
    """Ranking de Items por Costo Neto"""
    info_message(2, 'Seleccionaste ver el ranking de Items por Costo Neto!')
    info_message(2, 'Cargando información...')
    time.sleep(5)
    mostrar_info = df.groupby('Item Type')['Total Cost'].sum().sort_values(ascending=False).reset_index() #Primero, obtenemos la suma de todo lo vendido por Item, y después lo ordenamos.
    print(mostrar_info)

    if ask_grafica() is False: #Si se eligió "NO" simplemente salimos de la función.
        return
    
    # Aqui empieza la gráfica
    colores = ['#5E0006','#980404' , '#9B0F06', '#C00707', ] #Asignamos colores si el valor es menor a 45000
    plt.figure(figsize=(20,10))
    bars = plt.barh(mostrar_info['Item Type'], mostrar_info['Total Cost'], color=colores) #Dado que tenemos muchos Items, haremos una barra horizontal
    for bar in bars:
        w = bar.get_width()
        plt.text(w + (mostrar_info['Total Cost'].max() * 0.01), 
                bar.get_y() + bar.get_height()/2, 
                f'{w:.1f}', 
                va='center', fontsize=10)
    plt.title('Costo Neto por Item', fontsize=14)
    plt.xlabel('Item')
    plt.ylabel('Costo Neto')
    plt.tight_layout() #Evita que se corten etiquetas
    if save_grafica() is True:
        plt.savefig('grafica.png', dpi=250)
    plt.show()
    return

def rank_item_total_gain():
    """Ranking de Items por Ganancia total (Ganancia Neta - Costo Neto)"""
    info_message(2, 'Seleccionaste ver el ranking de Items por Ganancia total!')
    info_message(2, 'Cargando información...')
    time.sleep(5)
    mostrar_info = df.groupby('Item Type')['Total Profit'].sum().sort_values(ascending=False).reset_index() #Primero, obtenemos la suma de todo lo vendido por Item, y después lo ordenamos.
    print(mostrar_info)

    if ask_grafica() is False: #Si se eligió "NO" simplemente salimos de la función.
        return
    
    # Aqui empieza la gráfica
    colores = [ '#E87F24', '#FFA02E','#FFAA00' ,'#FFC81E' , '#FFC85C', ] #Asignamos colores si el valor es menor a 45000
    plt.figure(figsize=(20,10))
    bars = plt.barh(mostrar_info['Item Type'], mostrar_info['Total Profit'], color=colores) #Dado que tenemos muchos Items, haremos una barra horizontal
    for bar in bars:
        w = bar.get_width()
        plt.text(w + (mostrar_info['Total Profit'].max() * 0.01), 
                bar.get_y() + bar.get_height()/2, 
                f'{w:.1f}', 
                va='center', fontsize=10)
    plt.title('Ganancia Total Por Items (Ganancia Neta - Costo Neto)', fontsize=14)
    plt.xlabel('Item')
    plt.ylabel('Ganancia Total')
    plt.tight_layout() #Evita que se corten etiquetas
    if save_grafica() is True:
        plt.savefig('grafica.png', dpi=250)
    plt.show()
    return

def max_total_profit_item():
    """Top 5 Items con más Ganancia Total"""
    info_message(2, 'Seleccionaste ver el top 5 de Items con más ganancia total!')
    info_message(2, 'Cargando información...')
    time.sleep(5)
    mostrar_info = df.groupby('Item Type')['Total Profit'].sum().nlargest(5).sort_values(ascending=False).reset_index()
    #Primero, obtenemos la suma de todo lo vendido por Item, y con nlargest obtenemos los mejores 5.
    print(mostrar_info)

    if ask_grafica() is False: #Si se eligió "NO" simplemente salimos de la función.
        return

    colores = ['#1F6F5F', '#2FA084', '#6FCF97','#9AD872' , '#B5E18B',]
    plt.figure(figsize=(8,5)) # Tamaño del lienzo (ancho por alto)
    bars = plt.bar(mostrar_info['Item Type'], mostrar_info['Total Profit'], color=colores)
    #Etiqueta con el valor encima de cada barra
    for bar in bars:
        h = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, h+1, f'{h:.1f}', ha='center', fontsize=10)

    plt.title('Top 5 Items con más Ganancias Totales', fontsize=14)
    plt.xlabel('Item')
    plt.ylabel('Ganancia Total')
    plt.tight_layout()
    if save_grafica() is True:
        plt.savefig('grafica.png', dpi=250)
    plt.show()
    return

def min_total_profit_item():
    """Top 5 de Items con la PEOR ganancia total"""
    info_message(2, 'Seleccionaste ver el top 5 de Items con la peor ganancia total.')
    info_message(2, 'Cargando información...')
    time.sleep(5)
    mostrar_info = df.groupby('Item Type')['Total Profit'].sum().nsmallest(5).sort_values(ascending=True).reset_index()
    
    #Primero, obtenemos la suma de todo lo vendido por Item, y con nsmallest obtenemos los 5 peores.
    print(mostrar_info)

    if ask_grafica() is False: #Si se eligió "NO" simplemente salimos de la función.
        return

    colores = ['#a70000', '#ff0000', '#ff5252','#ff7b7b' , '#ffbaba',]
    plt.figure(figsize=(8,5)) # Tamaño del lienzo (ancho por alto)
    bars = plt.bar(mostrar_info['Item Type'], mostrar_info['Total Profit'], color=colores)
    #Etiqueta con el valor encima de cada barra
    for bar in bars:
        h = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, h+1, f'{h:.1f}', ha='center', fontsize=10)

    plt.title('Top 5 de Items con la PEOR ganancia total', fontsize=14)
    plt.xlabel('Item')
    plt.ylabel('Ganancia Total')
    plt.tight_layout()
    if save_grafica() is True:
        plt.savefig('grafica.png', dpi=250)
    plt.show()
    return

"""--- OPCIÓN 3 ---"""
def chart_avg_items_country():
    """Crea un gráfico de 'pie' para mostrar el porcentaje de items por región."""
    limpiar_consola()
    info_message(2, 'Seleccionaste ver un gráfico mostrando el porcentaje de cada item por región')
    info_message(2, 'A continuación, selecciona una región: ')

    #Esta parte provocó un montón de busquedas en Google.
    print('--- MENU DE REGIONES ---')
    paises = df['Region'].unique()
    for i, pais in enumerate(paises, 1): #Generamos la lista de opciones usando enumerate
        print(f'{i}. {pais}')
    while True:
        try:
            opcion = int(input("Selecciona una de las ID de las regiones mostrados en la lista: "))
            break
        except ValueError:
            info_message(1, "No seleccionaste un valor válido. Solamente puedes ingresar IDs!\n")
            time.sleep(5)
        except Exception as e:
            info_message(1, f"Ocurrió un error desconocido: {e}\n")
            time.sleep(5)
    
    #Ahora verificamos que el país SI exista.
    if opcion >=1 and opcion <= len(paises):
        info_message(2, 'La región SI existe en los registros..')
        pais_elegido = paises[opcion-1]
        info_message(2, f'Región elegida: {pais_elegido}')
    else:
        info_message(1, "La región NO existe en los registros. Intentalo de nuevo.")
        time.sleep(5)
        return chart_avg_items_country()

    #Ahora si, empezamos a construir la gráfica.
    datos_pais = df[df['Region'] == pais_elegido] #Filtramos y construimos un DataFrame solo con los datos del país elegido.
    sales_item = datos_pais.groupby('Item Type')['Units Sold'].sum() #Ahora si, agrupamos todo por su tipo de Item y que tanto se vendió.

    #GRAFICA
    plt.figure(figsize=(8, 8))
    plt.pie(sales_item.values, labels=sales_item.index, autopct='%1.1f%%', startangle=90, colors=['#FF9999','#66B3FF','#99FF99','#FFCC99'])
    plt.title(f'Porcentaje de Ventas por Item en {pais_elegido}')
    plt.tight_layout()
    if save_grafica() is True:
        plt.savefig('grafica.png', dpi=250)
    plt.show()
    return

"""--- OPCIÓN 4: REPORTE --- """
def generar_reporte_item():
    """Creamos un reporte a partir de un item selccionado."""
    info_message(2, 'Seleccionaste crear un reporte en base a un item seleccionado.')
    info_message(2, 'A continuación, selecciona un Item: \n')
    time.sleep(5)
    print('--- MENU DE ITEMS ---')
    items = df['Item Type'].unique()
    for i, pais in enumerate(items, 1): #Generamos la lista de opciones usando enumerate
        print(f'{i}. {pais}')
    while True:
        try:
            opcion = int(input("Selecciona una de las ID de los Items mostrados en la lista: "))
            break
        except ValueError:
            info_message(1, "No seleccionaste un valor válido. Solamente puedes ingresar IDs!\n")
            time.sleep(5)
        except Exception as e:
            info_message(1, f"Ocurrió un error desconocido: {e}\n")
            time.sleep(5)
    
    #Ahora verificamos que el país SI exista.
    if opcion >=1 and opcion <= len(items):
        info_message(2, 'El Item SI existe en los registros..')
        item_elegido = items[opcion-1]
        info_message(2, f'Item elegido: {item_elegido}')
    else:
        info_message(1, "El Item NO existe en los registros. Intentalo de nuevo.")
        time.sleep(5)
        return generar_reporte_item()

    info_message(2, 'Creando reporte...')
    time.sleep(5)
    datos_item = df[df['Item Type'] == item_elegido]
    # Ahora si, creamos el reporte:
    total_ventas = datos_item['Units Sold'].sum()
    avg_precio_unidad = datos_item['Unit Price'].mean()
    avg_costo_unidad = datos_item['Unit Cost'].mean()
    costo_total = datos_item['Total Cost'].sum()
    ganancia_neta = datos_item['Total Revenue'].sum()
    ganancia_total = datos_item['Total Profit'].sum()

    # Asignamos el texto a una variable, porque lo vamos a usar dos veces. Una para PRINT y otro para el reporte.
    reporte_texto = (
        f'\n --- REPORTE FINANCIERO: {item_elegido.upper()} ---\n'
        f'Total Ventas: {total_ventas}\n'
        f'Costo por Unidad (Promedio): ${avg_costo_unidad}\n'
        f'Precio por Unidad (Promedio): ${avg_precio_unidad}\n'
        f'Costo Total: ${costo_total}\n'
        f'Ganancia Neta: ${ganancia_neta}\n'
        f'Ganancia Total: ${ganancia_total}\n'
        f'--- REPORTE FINALIZADO ---\n')

    print(reporte_texto)
    if save_file() is False:
        return
    try:
        with open(f'reporte {item_elegido}.txt', 'w', encoding='utf-8',) as reporte:
            reporte.write(reporte_texto)
            info_message(2, 'El reporte se creó con exito!')
            info_message(2, f'Nombre del archivo: "reporte {item_elegido}"')
    except Exception as e:
        info_message(1, "Ocurrió un error inesperado al intentar crear el archivo!: {e}")
    return

cargar_datos(archivo)
menu()

# FAQ:
"""
¿Porqué hay tantos time.sleep(5):
- Para que el usuario no reciba toda la información de golpe y se confunda/quede abrumado

¿Porqué el dataset está en inglés?:
- Porque fue el primer dataset que encontré.

¿Porqué hay un info_message, que es solo un print pero con más formato?
- Exactamente para eso, para darle más formato. Y sabiendo a que hora fue enviado por la consola el mensaje, el usuario no se pierda.

Nota:
- El Dataset tiene tantas entradas que tuve que usar, principalmente, barras de gráfica horizontales.
- Al obtener los .sum() de los costos, ganancia, y profit totales, la suma era tan grande que está en notación cientifica.
No me di cuenta de eso, solo me dí cuenta cuando en las gráficas aparecía 1.5+e
"""