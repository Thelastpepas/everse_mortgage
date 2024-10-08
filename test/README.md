# Reverse Mortgage Calculator

## ¿Quién hizo esto?
Autor:Yonatan Calimeño
## ¿Qué es y para qué es?
Este proyecto es una aplicación para calcular los pagos mensuales de una hipoteca inversa, considerando factores como el valor de la propiedad, el estado de la propiedad, el estado civil, las edades del propietario y del cónyuge, y la tasa de interés.

## ¿Cómo lo hago funcionar?

### Prerrequisitos
Asegúrate de tener Python instalado en tu sistema. No se requieren dependencias externas adicionales para ejecutar el proyecto.

### Ejecución
Para ejecutar el programa fuera del entorno de desarrollo:

1. Navega a la carpeta :
 Una vez clonado el archivo, abres cd o prompt anaconda, y te direjes haciendo tienes el archivo guarado por ejemplo:

    ```
     cd C:\Users\yonatan\Desktop\lenguaje dos\mimanera_tarea2\Practica_Hipoteca-main\homework
    
    ```

2. Ejecuta el script principal:
    ```
    python src/console/console.py
    ```
 

## ¿Cómo está hecho?

### Arquitectura del Proyecto
El proyecto está organizado en dos carpetas principales:

- **src**: Contiene el código fuente de la aplicación.
  - **console**: Contiene el script principal `console.py` para la interacción con el usuario.
  - **logic**: Contiene la lógica de cálculo de la hipoteca inversa (`reverse_mortgage.py`).
- **tests**: Contiene las pruebas unitarias para validar el funcionamiento del código.

### Organización de los Módulos
- `src/console/console.py`: Archivo principal para la interacción con el usuario. Recoge entradas del usuario y muestra los resultados.
- `src/logic/reverse_mortgage.py`: Contiene las funciones de lógica para el cálculo de la hipoteca inversa, incluida la validación de entradas y el cálculo de pagos.

### Dependencias
- `unittest`: Biblioteca estándar de Python para pruebas unitarias.

## Uso
Para ejecutar las pruebas unitarias desde la carpeta test usa el siguiente comando:
   python test/Prueba_Unitaria.py 

