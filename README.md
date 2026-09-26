# Log Analyzer

## Descripción

Log Analyzer es un script desarrollado en Python que permite analizar archivos de texto que contienen registros simulados de sistemas.

El programa identifica el nivel de severidad de cada registro, valida las fechas y determina si las líneas cumplen con las reglas establecidas.

El proyecto fue desarrollado utilizando inteligencia artificial como herramienta de apoyo, manteniendo las decisiones de validación y comportamiento bajo criterio del desarrollador.

---

## Objetivo

Desarrollar una solución funcional en Python que permita:

- Leer un archivo de texto seleccionado por el usuario.
- Analizar cada línea del archivo.
- Identificar los niveles `INFO`, `WARNING` y `ERROR`.
- Validar las fechas.
- Detectar líneas malformadas o incompletas.
- Continuar procesando el archivo aunque existan líneas con errores.
- Generar un resumen estadístico de los resultados.

---

## Reglas de validación

Las reglas fueron definidas antes de solicitar a la IA la implementación del código.

### Nivel de severidad

Solamente se reconocen los siguientes niveles:

- `INFO`
- `WARNING`
- `ERROR`

Cualquier otro nivel, por ejemplo `DEBUG`, se considera inválido.

### Fecha

La fecha debe cumplir exactamente con el formato:

`YYYY-MM-DD`

Además, debe representar una fecha real del calendario.

Por ejemplo:

- `2025-01-10` → válida
- `2025-02-30` → inválida
- `2025-99-99` → inválida
- `10-01-2025` → inválida

### Mensaje

Cada registro debe contener un mensaje.

Si el mensaje está ausente o vacío, la línea se considera malformada.

### Información faltante

Cuando una línea contiene información faltante o inválida, se marca como malformada, pero el programa continúa procesando las demás líneas.

### Conteo de eventos

Se considera evento cualquier línea que contenga un nivel de severidad reconocido (`INFO`, `WARNING` o `ERROR`), aunque posteriormente la fecha o el mensaje resulten inválidos.

Por ejemplo:

`[ERROR] 2025-99-99 Error de conexión`

Se contabiliza como:

- 1 evento
- 1 ERROR
- 1 línea malformada

Una línea con un nivel desconocido no se contabiliza como evento, pero sí como malformada.

---

## Estructura del proyecto

Log_Analyzer/
├── src/
│   └── log_analyzer.py
├── tests/
│   ├── log_bien_formado.txt
│   └── log_formato_malo.txt
├── docs/
│   └── reflexion_tecnica.md
└── README.md