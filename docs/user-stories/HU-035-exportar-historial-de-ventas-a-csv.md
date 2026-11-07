## HU-035: Exportar Historial de Ventas a CSV

### Descripción
Como usuario Owner, quiero exportar el historial de ventas a formato CSV para poder analizar los datos en Excel, hacer reportes externos o compartir información con mi contador.

### Criterios de Aceptación

**Botón Exportar CSV:**
- Ubicado en la esquina superior derecha de la página de historial
- Texto: "Exportar CSV" o ícono de descarga + "Exportar"
- Color secundario o neutral
- Habilitado solo si hay ventas en el periodo filtrado

**Alcance de la Exportación:**
- Exportar todas las ventas del periodo actualmente filtrado
- Si hay filtro de fecha activo, exportar solo ese periodo
- Si hay búsqueda activa, exportar solo resultados filtrados
- Ignorar la paginación (exportar todas, no solo la página visible)

**Contenido del CSV:**
- Columnas incluidas:
  - Número de orden
  - Fecha (formato: YYYY-MM-DD)
  - Hora (formato: HH:MM)
  - Método de pago
  - Número de items
  - Subtotal
  - Impuesto
  - Total
  - Notas (si existen)
- Primera fila: Encabezados de columnas
- Datos: Una fila por venta

**Ejemplo de Contenido:**
```
Número de Orden,Fecha,Hora,Método de Pago,Items,Subtotal,Impuesto,Total,Notas
#001,2026-01-26,10:30,Efectivo,3,23.00,4.14,27.14,Sin cebolla
#002,2026-01-26,11:15,Tarjeta,5,45.00,8.10,53.10,
#003,2026-01-26,12:00,Efectivo,2,15.00,2.70,17.70,Para llevar
```

**Nombre del Archivo:**
- Formato: `ventas_[fecha_inicio]_[fecha_fin].csv`
- Si es período predefinido: `ventas_hoy.csv`, `ventas_ayer.csv`, `ventas_mes_enero.csv`
- Si es personalizado: `ventas_2026-01-01_2026-01-15.csv`
- Incluir fecha en nombre para fácil identificación

**Codificación del Archivo:**
- UTF-8 con BOM (para correcta visualización en Excel)
- Separador: Coma (,)
- Delimitador de texto: Comillas dobles (") cuando necesario
- Escape de comillas dentro del texto

**Formato de Números:**
- Usar punto (.) como separador decimal
- No usar separador de miles en el CSV
- Ejemplo: 1250.50 (no $1,250.50)

**Proceso de Descarga:**
- Al hacer clic en "Exportar CSV", generar archivo inmediatamente
- Mostrar indicador de carga: "Generando archivo..."
- Descargar automáticamente al navegador
- Mostrar toast de confirmación: "Archivo CSV descargado exitosamente"

**Límites de Exportación:**
- Si hay más de 10,000 ventas, mostrar advertencia: "Estás exportando X ventas. Esto puede tardar unos segundos."
- Límite máximo: 50,000 ventas (si se excede, sugerir filtrar por periodos más cortos)

**Estados de Carga:**
- Durante la generación, mostrar spinner en el botón
- Cambiar texto a "Generando..."
- Deshabilitar botón mientras se genera

**Manejo de Errores:**
- Si hay error al generar CSV, mostrar toast: "Error al generar archivo. Por favor, intenta de nuevo"
- Si el periodo tiene demasiadas ventas, mostrar error: "El periodo seleccionado tiene demasiadas ventas. Por favor, selecciona un rango más corto"

**Campos con Caracteres Especiales:**
- Si las notas contienen comillas, escaparlas correctamente
- Si contienen saltos de línea, mantenerlos dentro de comillas
- Asegurar compatibilidad con Excel y Google Sheets

**Información de Periodo en el Archivo (Opcional):**
- Incluir comentario en primera línea: `# Ventas del 2026-01-01 al 2026-01-31`
- O incluir metadatos en las primeras filas antes de los datos

### Escenarios

1. **Exportar ventas del día**: Owner filtra por "Hoy" (25 ventas), hace clic en "Exportar CSV", ve spinner "Generando...", descarga archivo "ventas_hoy.csv" con 25 filas + encabezados
2. **Exportar periodo personalizado**: Owner filtra del 1 al 15 de enero (150 ventas), exporta, descarga archivo "ventas_2026-01-01_2026-01-15.csv" con 150 ventas
3. **Exportar con búsqueda activa**: Owner busca "005", solo aparece 1 resultado, exporta, el CSV contiene solo esa venta
4. **Exportar mes completo**: Owner filtra por "Este mes" (287 ventas), hace clic en "Exportar", ve advertencia "Estás exportando 287 ventas. Esto puede tardar unos segundos", confirma, descarga exitosamente
5. **Nombre de archivo correcto**: Owner exporta ventas de ayer, el archivo descargado se llama "ventas_ayer.csv" con la fecha correspondiente
6. **Toast de confirmación**: Owner exporta CSV, ve toast "Archivo CSV descargado exitosamente" durante 3 segundos
7. **Abrir en Excel**: Owner abre el CSV descargado en Excel, todas las columnas se ven correctamente, tildes y caracteres especiales se muestran bien (UTF-8 BOM)
8. **Ventas con notas complejas**: Venta tiene notas con comillas y saltos de línea, el CSV exporta correctamente con escapes apropiados, Excel lo muestra bien
9. **Exportar sin ventas**: Owner filtra un día sin ventas, el botón "Exportar CSV" está deshabilitado
10. **Formato de números**: Owner abre CSV y ve totales como "27.14", "1250.50" (sin símbolo de moneda, con punto decimal)
11. **Error al generar**: Owner intenta exportar pero hay error de red, ve toast "Error al generar archivo. Por favor, intenta de nuevo"
12. **Periodo muy largo**: Owner intenta exportar 2 años completos (60,000 ventas), ve error "El periodo seleccionado tiene demasiadas ventas. Por favor, selecciona un rango más corto"
13. **Exportar e importar en Google Sheets**: Owner descarga CSV, lo abre en Google Sheets, todos los datos se importan correctamente con formato adecuado
14. **Indicador de carga**: Owner hace clic en "Exportar", el botón muestra spinner y texto "Generando..." durante 2 segundos, luego se descarga el archivo

---