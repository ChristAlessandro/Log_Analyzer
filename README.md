# Log Analyzer

Proyecto académico desarrollado en Python para analizar archivos de
registros (logs) y generar un resumen de los eventos encontrados.

## Objetivo

El programa permitirá seleccionar un archivo de texto y analizar cada
una de sus líneas para identificar:

- Nivel de severidad.
- Fecha.
- Mensaje.
- Líneas mal formateadas o incompletas.

## Niveles permitidos

- INFO
- WARNING
- ERROR

## Formato esperado

```text
[NIVEL] YYYY-MM-DD Mensaje

## Diseño del programa

El programa se dividirá en funciones con responsabilidades específicas.

### Funciones principales

- `seleccionar_archivo()`: solicita al usuario la ruta del archivo que desea analizar.
- `leer_archivo()`: abre el archivo y obtiene sus líneas para posteriormente analizarlas.
- `analizar_linea()`: analiza individualmente cada línea y coordina las diferentes validaciones.
- `validar_nivel()`: comprueba si el nivel de severidad pertenece a los niveles permitidos.
- `validar_fecha()`: comprueba si la fecha cumple con el formato establecido y representa una fecha real.
- `mostrar_resumen()`: presenta en consola los resultados obtenidos durante el análisis.
- `main()`: coordina el flujo general del programa.

### Decisiones de diseño

Se decidió mantener separadas las funciones de selección y lectura del archivo para separar la interacción con el usuario de la gestión del archivo.

Las validaciones de nivel y fecha también permanecerán separadas para facilitar su comprobación y pruebas independientes.

Las funciones de validación no serán responsables de mostrar información en consola ni de modificar directamente las estadísticas. Su responsabilidad será únicamente determinar si el dato analizado cumple con las reglas establecidas.

La función `analizar_linea()` será responsable de utilizar estas validaciones para determinar el estado de cada registro.