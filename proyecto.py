import psutil
import time

def obtener_informacion_rendimiento():
    # Obtener datos de uso de memoria y almacenamiento
    uso_memoria = psutil.virtual_memory().percent
    uso_almacenamiento = psutil.disk_usage('/').percent

    return uso_memoria, uso_almacenamiento

def analizar_rendimiento(uso_memoria, uso_almacenamiento):
    sugerencias = {}

    if uso_memoria > 80:
        sugerencias['Memoria'] = 'El uso de memoria es alto. Considera ajustes.'

    if uso_almacenamiento > 80:
        sugerencias['Almacenamiento'] = 'El espacio de almacenamiento está casi lleno. Realiza limpieza.'

    return sugerencias

def aplicar_sugerencias(sugerencias):
    # Implementar lógica para aplicar ajustes sugeridos
    # Esto podría incluir acciones como la eliminación de archivos temporales, ajustes de configuración, etc.
    pass

def main():
    while True:
        uso_memoria, uso_almacenamiento = obtener_informacion_rendimiento()
        sugerencias = analizar_rendimiento(uso_memoria, uso_almacenamiento)

        if sugerencias:
            print("Sugerencias de Optimización:")
            for recurso, mensaje in sugerencias.items():
                print(f"{recurso}: {mensaje}")

            # Aplicar ajustes (descomentar la línea siguiente para activar)
            # aplicar_sugerencias(sugerencias)

        time.sleep(300)  # Esperar 5 minutos antes de volver a verificar

if __name__ == "__main__":
    main()



