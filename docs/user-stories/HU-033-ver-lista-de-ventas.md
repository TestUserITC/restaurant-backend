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