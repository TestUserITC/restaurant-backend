# Historias de Usuario - Historial de Ventas
## MVP SaaS Administración de Restaurantes

---

## HU-033: Ver Lista de Ventas

### Descripción
Como usuario Owner, quiero ver un listado completo de todas las ventas realizadas para tener control sobre los ingresos del restaurante y poder consultar transacciones específicas.

### Criterios de Aceptación

**Estructura de la Página:**
- La página muestra un título "Historial de Ventas" en la parte superior
- Incluye filtro de fecha en la parte superior
- Incluye botón "Exportar CSV" en la esquina superior derecha
- El contenido principal muestra una tabla con las ventas
- Si no hay ventas en el periodo seleccionado, mostrar estado vacío con mensaje "No hay ventas en este periodo"

**Filtro por Fecha:**
- Dropdown con opciones predefinidas:
  - "Hoy" (por defecto)
  - "Ayer"
  - "Últimos 7 días"
  - "Este mes"
  - "Mes anterior"
  - "Personalizado" (abre date picker de rango)
- Al cambiar el filtro, actualizar la tabla automáticamente

**Date Picker Personalizado:**
- Al seleccionar "Personalizado", abrir selector de rango de fechas
- Permite seleccionar fecha inicial y fecha final
- Validar que fecha final >= fecha inicial
- Botones:
  - "Cancelar" (cierra sin aplicar)
  - "Aplicar" (ejecuta el filtro)

**Tabla de Ventas:**
- Columnas visibles:
  - Número de orden (ej: #001, #002)
  - Fecha (formato: "26 ene 2026")
  - Hora (formato 12h: "10:30 AM")
  - Método de pago (badge: Efectivo/Tarjeta)
  - Items (número de productos diferentes, ej: "3 items")
  - Total (formato moneda)
  - Acciones (botón "Ver detalle")
- Las ventas se ordenan por fecha y hora (más reciente primero)
- Cada fila es clickeable para abrir el detalle

**Badges de Método de Pago:**
- Efectivo: Badge con color distintivo (ej: verde)
- Tarjeta: Badge con color distintivo (ej: azul)

**Formato de Totales:**
- Usar símbolo de moneda configurado en el sistema
- Formato con separador de miles y 2 decimales (ej: "$1,250.00")

**Resumen del Periodo:**
- En la parte superior de la tabla, mostrar resumen del periodo filtrado:
  - Total de ventas (número de transacciones)
  - Monto total vendido
  - Venta promedio
- Este resumen se actualiza según el filtro de fecha activo

**Ejemplo de Resumen:**
- "150 ventas | $3,250.00 total | $21.67 promedio"
- O en cards separadas:
  - "150 Ventas"
  - "$3,250.00 Total"
  - "$21.67 Promedio"

**Paginación:**
- Si hay más de 50 ventas, implementar paginación
- Mostrar selector de "Elementos por página": 25, 50, 100
- Mostrar información: "Mostrando 1-25 de 150 ventas"
- Botones: Anterior, 1, 2, 3, ..., Siguiente

**Búsqueda Rápida:**
- Campo de búsqueda con placeholder "Buscar por número de orden..."
- Búsqueda en tiempo real (debounce de 300ms)
- Busca por número de orden
- Botón X para limpiar búsqueda

**Estados de Carga:**
- Al cargar la página o cambiar filtro, mostrar skeleton loader con estructura de tabla
- La carga debe completarse en menos de 2 segundos

**Manejo de Errores:**
- Si hay error al cargar ventas, mostrar: "Error al cargar historial de ventas" con botón "Reintentar"
- Si el rango de fechas es inválido, mostrar error: "Rango de fechas inválido"

**Responsive Design:**
- En desktop (>1024px): Tabla completa con todas las columnas
- En tablet (768px-1024px): Tabla con scroll horizontal
- En mobile (<768px): Convertir en cards, cada card muestra orden, fecha/hora, método, total y botón ver

**Permisos:**
- Esta página solo es accesible para usuarios con rol Owner
- Si un Cajero intenta acceder, ver página 403 "No tienes permisos para acceder a esta sección"

### Escenarios

1. **Ver ventas del día**: Owner accede a `/sales`, ve filtro en "Hoy", la tabla muestra 25 ventas del día actual con toda la información
2. **Estado vacío sin ventas**: Owner accede por primera vez en el día, no hay ventas todavía, ve mensaje "No hay ventas en este periodo"
3. **Filtrar por Ayer**: Owner selecciona "Ayer" en filtro de fecha, la tabla se actualiza mostrando todas las ventas del día anterior
4. **Filtrar por Últimos 7 días**: Owner selecciona "Últimos 7 días", ve todas las ventas de la última semana, el resumen muestra "150 ventas | $3,250.00 total"
5. **Rango personalizado**: Owner selecciona "Personalizado", elige del 1 al 15 de enero, hace clic en "Aplicar", ve todas las ventas de ese periodo específico
6. **Rango inválido**: Owner selecciona fecha final antes de fecha inicial, ve error "Rango de fechas inválido", no se ejecuta el filtro
7. **Buscar orden específica**: Owner escribe "025" en búsqueda, la tabla filtra y muestra solo orden #025
8. **Limpiar búsqueda**: Owner hace clic en X del campo de búsqueda, la búsqueda se limpia, vuelve a mostrar todas las ventas del periodo
9. **Click en fila abre detalle**: Owner hace clic en cualquier parte de la fila de orden #012, es redirigido a página de detalle de venta
10. **Click en Ver detalle**: Owner hace clic en botón "Ver detalle" de orden #008, es redirigido al detalle de esa venta
11. **Resumen del periodo**: Owner filtra por "Este mes", ve en la parte superior "287 ventas | $6,500.00 total | $22.65 promedio"
12. **Paginación**: Owner filtra por "Este mes" con 150 ventas, ve primeras 25 con paginación "1-25 de 150 ventas", hace clic en página 2, ve ventas 26-50
13. **Cambiar elementos por página**: Owner cambia selector a "100 elementos por página", la tabla muestra 100 ventas (si hay tantas)
14. **Error al cargar**: Hay error de red al cargar ventas, Owner ve mensaje "Error al cargar historial de ventas" con botón "Reintentar", hace clic y los datos cargan
15. **Vista en mobile**: Owner accede desde teléfono, ve ventas como cards verticales con información resumida
16. **Badges de método de pago**: Owner ve en la tabla que orden #001 tiene badge verde "Efectivo" y orden #002 tiene badge azul "Tarjeta"
17. **Cajero intenta acceder**: Usuario Cajero intenta navegar a `/sales`, ve página 403 "No tienes permisos para acceder a esta sección"

---

## HU-034: Ver Detalle de Venta

### Descripción
Como usuario Owner, quiero ver el detalle completo de una venta específica para conocer todos los productos vendidos, el método de pago y otra información relevante de la transacción.

### Criterios de Aceptación

**Estructura de la Página:**
- La página muestra un título "Detalle de Venta - Orden #XXX" en la parte superior
- Incluye breadcrumb: Dashboard > Historial de Ventas > Orden #XXX
- Botón "Volver al historial" en la esquina superior izquierda
- Botón "Imprimir ticket" en la esquina superior derecha
- El contenido está dividido en secciones claramente definidas

**Sección: Información General**
- Card con información de la venta:
  - Número de orden (grande y destacado)
  - Estado: "Cerrada" (con badge gris)
  - Fecha y hora completa (formato: "26 de enero, 2026 - 10:30 AM")
  - Canal: "Mostrador" (fijo para MVP)
  - Método de pago (badge con color según tipo)
  - Información adicional según método de pago:
    - Efectivo: Monto recibido y cambio entregado
    - Tarjeta: Solo indicador de pago autorizado

**Ejemplo Información Efectivo:**
- "Método de pago: Efectivo"
- "Monto recibido: $50.00"
- "Cambio entregado: $15.78"

**Sección: Productos Vendidos**
- Lista detallada de productos con:
  - Nombre del producto
  - Cantidad (ej: "x2")
  - Precio unitario
  - Subtotal (cantidad × precio unitario)
- Si un producto fue eliminado del menú, mostrar su nombre original
- Los productos aparecen en el mismo orden que fueron agregados

**Sección: Resumen de Totales**
- Al final de la lista de productos:
  - Subtotal de productos
  - Impuesto (% y monto)
  - Total final (destacado, grande, en negrita)

**Formato de Moneda:**
- Usar moneda configurada en el sistema
- Formato con separador de miles y 2 decimales
- Consistente en toda la página

**Sección: Notas**
- Si la venta tiene notas, mostrarlas en un área destacada
- Título: "Notas"
- Contenido de las notas con formato (respetando saltos de línea)
- Si no hay notas, mostrar: "Sin notas adicionales"

**Botón Imprimir Ticket:**
- Al hacer clic, abrir vista de impresión optimizada
- La vista incluye:
  - Nombre del restaurante
  - Número de orden
  - Fecha y hora
  - Lista de productos con cantidades y precios
  - Totales
  - Método de pago
  - Notas (si existen)
  - Mensaje de agradecimiento (opcional)

**Vista de Impresión:**
- Formato optimizado para impresora de tickets (58mm o 80mm)
- Texto alineado correctamente
- Sin elementos de navegación
- Sin colores (blanco y negro)
- Fuente legible

**Navegación:**
- Al hacer clic en "Volver al historial", redirigir a `/sales`
- Mantener el filtro de fecha activo antes de abrir el detalle

**Estados de Carga:**
- Al cargar la página, mostrar skeleton loaders en cada sección
- La carga debe completarse en menos de 2 segundos

**Manejo de Errores:**
- Si la venta no existe, mostrar página 404: "Venta no encontrada" con botón "Volver al historial"
- Si hay error al cargar, mostrar: "Error al cargar detalle de venta" con botón "Reintentar"

**Información Inmutable:**
- Toda la información mostrada es de solo lectura
- No hay opciones de edición (la venta está cerrada y completada)
- Los datos son un registro histórico permanente

**Responsive Design:**
- En desktop: Layout organizado en cards y secciones claras
- En tablet/mobile: Secciones apiladas verticalmente con buen espaciado

**Permisos:**
- Solo Owner puede ver detalle de ventas
- Si Cajero intenta acceder, ver página 403

### Escenarios

1. **Ver detalle de venta completa**: Owner hace clic en orden #012 desde lista, ve página de detalle con toda la información: fecha/hora, método de pago "Efectivo", 5 productos, totales, y notas
2. **Venta con pago en efectivo**: Owner ve detalle de orden #008, método "Efectivo", muestra "Monto recibido: $50.00" y "Cambio entregado: $15.78"
3. **Venta con pago en tarjeta**: Owner ve detalle de orden #015, método "Tarjeta", muestra "Pago autorizado" sin detalles de cambio
4. **Venta sin notas**: Owner ve detalle de venta que no tiene notas, la sección "Notas" muestra "Sin notas adicionales"
5. **Venta con notas**: Owner ve detalle con notas "Sin cebolla, para llevar", las notas aparecen en área destacada respetando el formato
6. **Producto eliminado del menú**: Owner ve venta de hace 1 mes que incluye "Pizza Especial" (producto ya eliminado), el nombre aparece correctamente en la lista
7. **Cálculo de totales**: Venta tiene 2 Hamburguesas ($10 c/u = $20) y 1 Refresco ($3), detalle muestra Subtotal: $23.00, IVA 18%: $4.14, Total: $27.14
8. **Click en Volver al historial**: Owner hace clic en "Volver al historial", es redirigido a `/sales` manteniendo el filtro de fecha activo
9. **Click en Imprimir ticket**: Owner hace clic en "Imprimir", se abre vista de impresión optimizada con todos los detalles en formato de ticket
10. **Vista de impresión**: La vista muestra nombre del restaurante "Restaurante El Sabor", orden #012, fecha, productos con cantidades, totales, método de pago, y "¡Gracias por su compra!"
11. **Venta no encontrada**: Owner intenta acceder a `/sales/999` (no existe), ve página 404 "Venta no encontrada" con botón "Volver al historial"
12. **Error al cargar**: Hay error de red al cargar detalle, Owner ve mensaje "Error al cargar detalle de venta" con botón "Reintentar"
13. **Vista en mobile**: Owner accede desde teléfono, ve información apilada verticalmente con buen espaciado y legibilidad
14. **Producto con cantidad alta**: Venta incluye "Coca Cola x 12", el detalle muestra correctamente cantidad, precio unitario $3.00, subtotal $36.00
15. **Cajero intenta acceder**: Usuario Cajero intenta navegar a `/sales/001`, ve página 403 "No tienes permisos para acceder a esta sección"

---

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

## HU-036: Análisis Rápido del Periodo

### Descripción
Como usuario Owner, quiero ver indicadores visuales y estadísticas rápidas del periodo seleccionado para tener una visión general del rendimiento de ventas sin necesidad de exportar datos.

### Criterios de Aceptación

**Ubicación de Estadísticas:**
- Mostrar cards de estadísticas en la parte superior de la página, antes de la tabla
- 3 cards principales en fila:
  - Total de ventas (cantidad)
  - Monto total vendido
  - Venta promedio

**Card: Total de Ventas**
- Ícono representativo (ej: recibo, documento)
- Número grande: cantidad de ventas del periodo
- Label: "Ventas" o "Total ventas"
- Ejemplo: "150 Ventas"

**Card: Monto Total Vendido**
- Ícono representativo (ej: dinero, billete)
- Monto en formato moneda, grande y destacado
- Label: "Total vendido" o "Ingresos"
- Ejemplo: "$3,250.00 Total"

**Card: Venta Promedio**
- Ícono representativo (ej: ticket, promedio)
- Monto promedio en formato moneda
- Label: "Venta promedio" o "Ticket promedio"
- Cálculo: Total vendido ÷ Número de ventas
- Ejemplo: "$21.67 Promedio"

**Actualización Automática:**
- Las estadísticas se actualizan automáticamente al cambiar el filtro de fecha
- Al buscar una orden específica, las estadísticas NO cambian (siguen mostrando todo el periodo)
- Mostrar indicador de carga en las cards mientras se actualizan

**Comparación con Periodo Anterior (Opcional):**
- Incluir pequeño indicador de cambio porcentual vs periodo anterior
- Flecha verde arriba si aumentó, flecha roja abajo si disminuyó
- Ejemplo: "↑ 15% vs periodo anterior"
- Tooltip explicando el periodo de comparación

**Desglose por Método de Pago:**
- Incluir card adicional o sección mostrando:
  - Ventas en efectivo (cantidad y monto)
  - Ventas con tarjeta (cantidad y monto)
- Formato visual: mini-gráfica de barras o números con porcentajes

**Ejemplo de Desglose:**
- "Efectivo: 85 ventas ($1,850.00) - 57%"
- "Tarjeta: 65 ventas ($1,400.00) - 43%"

**Periodo Sin Ventas:**
- Si no hay ventas en el periodo, mostrar cards con valores en $0.00
- Mensaje adicional: "No hay ventas registradas en este periodo"

**Formato Visual:**
- Cards con buen contraste y legibilidad
- Números grandes y destacados
- Íconos claros y representativos
- Colores consistentes con el diseño del sistema

**Responsive Design:**
- En desktop: 3 cards en fila horizontal
- En tablet: 3 cards con menor espaciado
- En mobile: 3 cards apilados verticalmente

**Estados de Carga:**
- Al cambiar filtro de fecha, mostrar skeleton loaders en las cards
- Actualización debe completarse en menos de 2 segundos

**Manejo de Errores:**
- Si hay error al calcular estadísticas, mostrar: "Error al cargar estadísticas"
- No bloquear el resto de la página, permitir ver la tabla de ventas

### Escenarios

1. **Ver estadísticas del día**: Owner filtra por "Hoy" con 25 ventas totalizando $575.00, ve cards: "25 Ventas", "$575.00 Total", "$23.00 Promedio"
2. **Estadísticas de periodo largo**: Owner filtra "Este mes" con 287 ventas y $6,500.00, ve estadísticas correctamente calculadas con promedio de $22.65
3. **Actualización al cambiar filtro**: Owner cambia de "Hoy" a "Últimos 7 días", las cards muestran skeleton loaders por 1 segundo, luego actualizan con nuevos valores
4. **Periodo sin ventas**: Owner filtra un día sin actividad, ve cards con "0 Ventas", "$0.00 Total", "$0.00 Promedio" y mensaje "No hay ventas registradas en este periodo"
5. **Desglose por método de pago**: Owner ve desglose: "Efectivo: 85 ventas ($1,850.00) - 57%" y "Tarjeta: 65 ventas ($1,400.00) - 43%"
6. **Comparación con periodo anterior**: Owner ve en card de Total: "↑ 15% vs periodo anterior", hace hover y tooltip explica "Comparado con los 7 días anteriores"
7. **Búsqueda no afecta estadísticas**: Owner busca orden #005, ve solo 1 resultado en tabla, pero las estadísticas siguen mostrando datos del periodo completo
8. **Vista en mobile**: Owner accede desde teléfono, ve 3 cards apilados verticalmente con buen espaciado y números legibles
9. **Error al cargar estadísticas**: Hay error de red al calcular estadísticas, Owner ve "Error al cargar estadísticas" en el área de cards, pero la tabla de ventas se muestra normalmente
10. **Venta promedio con 1 venta**: Owner tiene solo 1 venta de $27.14, ve "1 Venta", "$27.14 Total", "$27.14 Promedio" (cálculo correcto)
11. **Formato de números grandes**: Owner filtra periodo con $15,250.50 total, ve "$15,250.50" con separador de miles correctamente formateado

---

## Resumen de Funcionalidad de Historial de Ventas

**Información Incluida por Venta:**
- Número de orden (secuencial)
- Fecha y hora de la venta
- Método de pago (Efectivo/Tarjeta)
- Lista de productos vendidos
- Cantidades y precios
- Subtotal, impuesto y total
- Notas (si existen)
- Canal: Mostrador (fijo para MVP)

**Filtros Disponibles:**
- Hoy (por defecto)
- Ayer
- Últimos 7 días
- Este mes
- Mes anterior
- Personalizado (rango de fechas)

**Acciones Principales:**
- Ver lista de ventas
- Filtrar por fecha
- Buscar orden específica
- Ver detalle de venta
- Imprimir ticket
- Exportar CSV

**Estadísticas Calculadas:**
- Total de ventas (cantidad)
- Monto total vendido
- Venta promedio
- Desglose por método de pago

---

## Navegación en Historial de Ventas

**URLs:**
- `/sales` → Lista de ventas (historial)
- `/sales/[id]` → Detalle de venta específica

**Breadcrumbs:**
- `/sales`: Dashboard > Historial de Ventas
- `/sales/[id]`: Dashboard > Historial de Ventas > Orden #XXX

**Acceso:**
- Desde menú lateral: "Ventas" o "Historial"
- Desde dashboard (Owner): Card o enlace a ventas
- Volver desde detalle: Botón "Volver al historial"

---

## Notas Técnicas

**Permisos:**
- Solo Owner tiene acceso a historial de ventas
- Cajero NO puede acceder (recibe 403)
- Validar permisos en frontend y backend

**Performance:**
- Índices en: fecha, numero_orden, metodo_pago
- Paginación obligatoria para queries grandes
- Caché de estadísticas del día actual (TTL 5 minutos)
- Lazy loading en detalle de ventas

**Cálculos:**
- Venta promedio: Total vendido ÷ Número de ventas
- Redondear a 2 decimales
- Manejar división por cero (0 ventas = $0.00 promedio)

**Exportación CSV:**
- Generar en backend (no frontend)
- Limitar a 50,000 registros por exportación
- UTF-8 con BOM para compatibilidad con Excel
- Streaming para archivos grandes (evitar timeout)

**Datos Inmutables:**
- Las ventas son registros históricos inmutables
- No se pueden editar o eliminar (solo consultar)
- Preservar información incluso si productos/categorías se eliminan
- Soft delete no aplica (ventas siempre visibles para Owner)

**Timezone:**
- Usar zona horaria configurada en settings del restaurante
- Todas las fechas/horas en timezone local
- En CSV, incluir timezone o usar formato local

**Búsqueda:**
- Búsqueda por número de orden (exacto o parcial)
- Case-insensitive
- Soportar con o sin "#" (ej: "001" o "#001")

**Métodos de Pago:**
- Efectivo: Registrar monto recibido y cambio
- Tarjeta: Solo registro de autorización
- Preparar estructura para futuros métodos (Transferencia, etc.)

**Relación con Órdenes:**
- Una venta = Una orden en estado "Cerrada"
- Ventas provienen del POS (cierre directo)
- Órdenes de cocina que se cierran también son ventas
- Mismo ID de orden para venta y orden

**Formato de Impresión:**
- Optimizado para impresora térmica de tickets
- Ancho: 58mm o 80mm
- Fuente monoespaciada para alineación
- Incluir logo o nombre del restaurante (configurable)
