## HU-018: Ver Lista de Órdenes en Tiempo Real

### Descripción
Como usuario (Owner o Cajero), quiero ver todas las órdenes del restaurante en tiempo real para monitorear el flujo de trabajo y gestionar los pedidos activos eficientemente.

### Criterios de Aceptación

**Estructura de la Página:**
- La página muestra un título "Órdenes" en la parte superior
- Incluye un botón primario "Nueva orden" en la esquina superior derecha
- Incluye filtros rápidos por estado en la parte superior (tabs o pills)
- El contenido principal muestra una tabla/lista de órdenes
- Si no hay órdenes, mostrar estado vacío con mensaje "No hay órdenes registradas" y botón "Crear primera orden"

**Filtros por Estado:**
- Tabs/pills horizontales:
  - "Todas" (por defecto, muestra todas las órdenes)
  - "Pendiente" (badge con número de órdenes pendientes)
  - "Preparación" (badge con número en preparación)
  - "Lista" (badge con número listas)
  - "Cerrada" (órdenes completadas)
- Al hacer clic en un filtro, la lista se actualiza mostrando solo órdenes de ese estado
- El filtro activo se destaca visualmente

**Tabla/Lista de Órdenes:**
- Columnas visibles:
  - Número de orden (ej: #001, #002)
  - Estado (badge con color distintivo)
  - Hora (hora de creación, formato 12h: "10:30 AM")
  - Items (número de productos, ej: "3 items")
  - Total (formato moneda)
  - Notas (ícono si tiene notas)
  - Acciones (botón ver detalle)
- Cada fila es clickeable para abrir el detalle
- Las órdenes se ordenan por hora de creación (más reciente primero)

**Badges de Estado:**
- Pendiente: Color naranja/amarillo
- Preparación: Color azul
- Lista: Color verde
- Cerrada: Color gris

**Actualización en Tiempo Real:**
- Las órdenes se actualizan automáticamente cada 10-15 segundos
- Cuando hay un cambio (nueva orden, cambio de estado), mostrar actualización suave sin recargar toda la página
- Indicador visual discreto cuando se actualiza (pequeño ícono pulsante o texto "Actualizado hace X segundos")

**Botón de Actualización Manual:**
- Incluir botón de refresh en la parte superior
- Al hacer clic, actualizar inmediatamente la lista de órdenes
- Mostrar animación de loading durante la actualización

**Detalle Rápido en Fila:**
- Cada fila muestra información resumida
- Número de items: "3 items"
- Total: "$45.50"
- Si tiene notas, mostrar ícono de nota con tooltip del contenido al hacer hover

**Estados de Carga:**
- Al cargar la página por primera vez, mostrar skeleton loader con estructura de tabla
- La carga inicial debe completarse en menos de 2 segundos

**Manejo de Errores:**
- Si hay error al cargar órdenes, mostrar mensaje: "Error al cargar órdenes" con botón "Reintentar"
- Si falla la actualización automática, seguir mostrando datos anteriores y permitir actualización manual

**Paginación:**
- Si hay más de 50 órdenes, implementar paginación
- Mostrar selector de "Elementos por página": 25, 50, 100
- Mostrar información: "Mostrando 1-25 de 100 órdenes"
- Por defecto, mostrar últimas 50 órdenes

**Filtro por Fecha:**
- Dropdown para filtrar por fecha:
  - "Hoy" (por defecto)
  - "Ayer"
  - "Últimos 7 días"
  - "Este mes"
  - "Personalizado" (abre selector de rango de fechas)
- Al cambiar fecha, actualizar la lista de órdenes

**Búsqueda Rápida:**
- Campo de búsqueda con placeholder "Buscar orden..."
- Búsqueda por número de orden (ej: "001", "#001")
- Búsqueda en tiempo real mientras se escribe (debounce de 300ms)
- Limpiar búsqueda con botón X dentro del campo

**Responsive Design:**
- En desktop (>1024px): Tabla completa con todas las columnas
- En tablet (768px-1024px): Tabla con scroll horizontal
- En mobile (<768px): Convertir en cards verticales, cada card muestra número, estado, hora, total y botón ver detalle

**Permisos:**
- Esta página es accesible tanto para Owner como para Cajero
- Ambos roles ven la misma información

### Escenarios

1. **Ver lista con órdenes activas**: Usuario accede a `/orders`, ve tabla con 12 órdenes mostrando número, estado, hora, items, total y botones de acción
2. **Estado vacío sin órdenes**: Usuario accede por primera vez en el día, ve mensaje "No hay órdenes registradas" con botón "Crear primera orden"
3. **Filtrar por Pendiente**: Usuario hace clic en tab "Pendiente", la lista muestra solo 5 órdenes con estado Pendiente
4. **Filtrar por Preparación**: Usuario hace clic en tab "Preparación", ve 3 órdenes en preparación
5. **Volver a ver Todas**: Usuario hace clic en tab "Todas", la lista vuelve a mostrar todas las órdenes
6. **Actualización automática**: Usuario tiene lista abierta, después de 15 segundos aparece una nueva orden automáticamente sin refresh manual
7. **Actualización manual**: Usuario hace clic en botón de refresh, ve animación de loading por 1 segundo, la lista se actualiza con datos frescos
8. **Buscar orden por número**: Usuario escribe "005" en búsqueda, la lista muestra solo la orden #005
9. **Limpiar búsqueda**: Usuario hace clic en X del campo de búsqueda, la búsqueda se limpia, vuelve a mostrar todas las órdenes
10. **Filtrar por fecha - Hoy**: Usuario selecciona "Hoy" en filtro de fecha, ve solo órdenes del día actual
11. **Filtrar por fecha - Últimos 7 días**: Usuario selecciona "Últimos 7 días", ve órdenes de la última semana
12. **Click en fila abre detalle**: Usuario hace clic en cualquier parte de la fila de orden #008, es redirigido a página de detalle `/orders/008`
13. **Ver tooltip de notas**: Orden #003 tiene notas, usuario hace hover sobre ícono de nota, ve tooltip con el contenido de la nota
14. **Paginación con muchas órdenes**: Hay 150 órdenes, la tabla muestra primeras 25 con paginación, usuario hace clic en página 2, ve órdenes 26-50
15. **Error al cargar**: Hay error de red, usuario ve mensaje "Error al cargar órdenes" con botón "Reintentar", hace clic y los datos cargan correctamente
16. **Vista en mobile**: Usuario accede desde teléfono, ve órdenes como cards verticales con información resumida
17. **Badge de estado con conteo**: Tab "Pendiente" muestra badge "5" indicando hay 5 órdenes pendientes
18. **Indicador de actualización**: En esquina superior aparece texto "Actualizado hace 10 segundos" que se actualiza continuamente
19. **Click en Nueva orden**: Usuario hace clic en "Nueva orden", es redirigido al POS `/pos`

---