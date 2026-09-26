# Reflexión técnica

## 1. Uso de inteligencia artificial

Durante el desarrollo de Log Analyzer utilicé inteligencia artificial como herramienta de apoyo para implementar y revisar diferentes partes del proyecto.

El proceso se realizó de manera progresiva. En lugar de solicitar a la IA que desarrollara todo el programa de una sola vez, se dividió el problema en funciones y etapas.

La IA fue utilizada principalmente para:

- Proponer estructuras iniciales de funciones.
- Implementar funciones a partir de reglas previamente definidas.
- Sugerir formas de validar los niveles de severidad.
- Apoyar la implementación de la validación de fechas.
- Explicar posibles errores encontrados durante las pruebas.
- Ayudar a revisar los resultados obtenidos.
- Sugerir formas de organizar el flujo principal del programa.

La IA no fue utilizada para decidir las reglas principales del sistema.

---

## 2. Decisiones tomadas por el desarrollador

Antes de solicitar la implementación a la IA, se definieron las reglas que debía cumplir el programa.

Se decidió que solamente los niveles `INFO`, `WARNING` y `ERROR` serían reconocidos como niveles válidos.

También se estableció que la fecha debía utilizar exactamente el formato `YYYY-MM-DD` y que no era suficiente con comprobar que tuviera una estructura aparentemente correcta. La fecha debía representar un día real del calendario.

Por ejemplo, una fecha como `2025-99-99` debía considerarse inválida aunque tuviera la misma cantidad de caracteres y separadores que una fecha válida.

También se decidió que una línea con información faltante debía considerarse malformada, pero no debía detener el análisis del resto del archivo.

Otra decisión importante fue establecer qué debía considerarse un evento. Se determinó que cualquier línea con un nivel reconocido (`INFO`, `WARNING` o `ERROR`) sería contabilizada como evento, aunque tuviera una fecha inválida o un mensaje incompleto.

Por ejemplo:

`[ERROR] 2025-99-99 Error de conexión`

se contabiliza como un evento `ERROR`, pero también como una línea malformada.

Estas reglas fueron definidas por el desarrollador antes de implementar la lógica con ayuda de IA.

---

## 3. Organización del código

Se decidió dividir el programa en varias funciones con responsabilidades específicas.

La función `seleccionar_archivo()` se encarga de solicitar al usuario la ruta del archivo.

`leer_archivo()` se encarga de abrir el archivo y obtener sus líneas.

`validar_nivel()` y `validar_fecha()` realizan las validaciones correspondientes.

`analizar_linea()` coordina el análisis individual de cada registro.

`generar_estadisticas()` procesa los resultados y calcula los totales.

Finalmente, `mostrar_resumen()` presenta los resultados al usuario y `main()` coordina el flujo general.

Esta separación fue revisada durante el desarrollo porque permite probar las diferentes responsabilidades de manera independiente y facilita localizar errores.

---

## 4. Validación de las propuestas de IA

Una de las decisiones importantes durante el proyecto fue no aceptar automáticamente las respuestas generadas por la inteligencia artificial.

Cada implementación fue ejecutada y probada antes de considerarse parte del proyecto.

Durante las pruebas se encontró una diferencia entre un resultado esperado inicialmente y el comportamiento real del archivo de prueba con errores.

El archivo `log_formato_malo.txt` contiene ocho líneas. Solamente la primera línea es completamente válida. Las otras siete contienen algún tipo de problema: fecha ausente, fecha inválida, nivel desconocido, línea vacía, mensaje ausente o estructura incorrecta.

Por esta razón, el resultado correcto es:

- Total de eventos: 5
- INFO: 2
- WARNING: 1
- ERROR: 2
- Líneas malformadas: 7

La revisión manual permitió comprobar que el resultado de siete líneas malformadas era correcto.

Este caso demuestra la importancia de verificar las respuestas de la IA utilizando los datos reales del proyecto en lugar de asumir que una respuesta o resultado propuesto es correcto.

---

## 5. Aspecto de la implementación que podría mejorarse

Durante la revisión del código también se identificó un aspecto que podría mejorarse en la función `analizar_linea()`.

Cuando una línea contiene el nivel pero no proporciona explícitamente una fecha, por ejemplo:

`[ERROR] Failed to connect to database`

la implementación actual interpreta `Failed` como el posible campo de fecha y posteriormente la validación determina que no es una fecha válida.

El resultado final es correcto porque la línea se marca como malformada, pero la representación interna podría ser más precisa.

Una implementación posterior podría distinguir explícitamente entre:

- fecha ausente;
- fecha presente pero inválida;
- mensaje ausente.

No fue necesario modificar esta lógica para cumplir con los requisitos actuales, pero identificar esta situación permitió comprender mejor cómo funciona el código y qué podría mejorarse en una versión futura.

---

## 6. Pruebas y validación

Se realizaron pruebas con diferentes tipos de entradas.

### Archivo bien formado

El archivo `log_bien_formado.txt` produjo:

- 5 eventos.
- 2 eventos INFO.
- 1 evento WARNING.
- 2 eventos ERROR.
- 0 líneas malformadas.

Los resultados coincidieron con los valores esperados.

### Archivo con información inconsistente

El archivo `log_formato_malo.txt` produjo:

- 5 eventos.
- 2 eventos INFO.
- 1 evento WARNING.
- 2 eventos ERROR.
- 7 líneas malformadas.

Los resultados coincidieron con el análisis manual de las ocho líneas del archivo.

También se probó una ruta de archivo inexistente para verificar que el programa manejara esta situación sin producir un error no controlado.

---

## 7. Lecciones aprendidas

El desarrollo permitió comprender que utilizar inteligencia artificial para programar no significa aceptar directamente todo el código generado.

La definición del problema, las reglas de validación y los criterios para considerar un registro como evento o como línea malformada deben estar claros antes de implementar la solución.

También fue importante realizar pruebas con casos normales y casos incorrectos. Una solución puede ejecutarse correctamente y aun así producir resultados que deben ser revisados contra lo que realmente se esperaba.

La principal lección fue que la IA puede acelerar la implementación y ayudar a encontrar soluciones, pero el desarrollador debe comprender el código, probarlo y tomar las decisiones finales sobre el comportamiento del programa.

En este proyecto, la IA funcionó como una herramienta de apoyo y no como el autor de las decisiones técnicas.