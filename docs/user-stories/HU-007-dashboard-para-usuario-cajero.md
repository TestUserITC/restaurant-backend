## HU-007: Dashboard para Usuario Cajero

### Descripción
Como usuario con rol Cajero, quiero ver un dashboard simplificado centrado en órdenes para enfocarme en las operaciones diarias sin distracciones de KPIs financieros.

### Criterios de Aceptación

**Estructura y Contenido del Dashboard:**
- El dashboard muestra un título "Dashboard" en la parte superior
- El contenido está enfocado únicamente en órdenes operativas
- Muestra 2 secciones principales:
  - Órdenes abiertas (resumen en card)
  - Lista de órdenes pendientes de atención

**Card: Órdenes Abiertas**
- Título: "Órdenes abiertas"
- Valor principal: Número total de órdenes con estados "Pendiente", "Preparación" o "Lista"
- Desglose visual por estado:
  - Badge con número de órdenes "Pendiente" (color naranja/amarillo)
  - Badge con número de órdenes "Preparación" (color azul)
  - Badge con número de órdenes "Lista" (color verde)
- Si no hay órdenes abiertas, mostrar "Sin órdenes abiertas" con icono de checkmark
- El card es clickeable y redirige a `/orders`

**Sección: Órdenes Pendientes de Atención**
- Título: "Órdenes pendientes"
- Muestra lista de las últimas 10 órdenes con estados "Pendiente" o "Preparación" (excluye "Lista" y "Cerrada")
- Cada orden en la lista muestra:
  - Número de orden (ej: "#001")
  - Estado actual con badge de color (Pendiente/Preparación)
  - Hora de creación (ej: "10:30 AM")
  - Total de la orden (ej: "$45.00")
  - Botón rápido "Ver detalle"
- Las órdenes se ordenan por hora de creación (más reciente primero)
- Si no hay órdenes pendientes, mostrar mensaje "¡Excelente! No hay órdenes pendientes" con icono de celebración

**Interacciones:**
- Al hacer clic en el card "Órdenes abiertas", redirigir a `/orders`
- Al hacer clic en "Ver detalle" de una orden, redirigir a `/orders/[id]` (detalle de la orden)
- Al hacer clic en cualquier parte de una fila de orden (no solo el botón), también redirigir al detalle

**Estados de Carga:**
- Al cargar el dashboard, mostrar skeleton loader en el card de órdenes abiertas
- En la sección de órdenes pendientes, mostrar skeleton loaders de filas (3-4 filas)
- La carga debe completarse en menos de 2 segundos

**Actualización en Tiempo Real:**
- El dashboard se actualiza automáticamente cada 30 segundos para reflejar nuevas órdenes
- Al crear una nueva orden desde el POS, el dashboard debe actualizarse automáticamente (WebSocket o polling)
- Incluir botón de actualizar manual en la esquina superior derecha
- Mostrar indicador visual discreto cuando se actualiza automáticamente (pequeño ícono pulsante)

**Manejo de Errores:**
- Si hay error al cargar las órdenes, mostrar mensaje: "Error al cargar órdenes" con botón "Reintentar"
- El botón "Reintentar" recarga los datos sin refrescar toda la página

**Responsive Design:**
- En desktop (>1024px): Card de órdenes abiertas ocupa 1/3 del ancho, lista de órdenes pendientes ocupa 2/3
- En tablet (768px-1024px): Card arriba, lista debajo
- En mobile (<768px): Card y lista apilados verticalmente, lista muestra 5 órdenes con scroll

**Elementos NO Visibles para Cajero:**
- No mostrar KPI de ventas del día
- No mostrar ticket promedio
- No mostrar productos más vendidos
- Enfoque 100% operativo en órdenes

### Escenarios

1. **Dashboard con órdenes activas**: Cajero accede al dashboard, ve "Órdenes abiertas: 8" con badges "3 Pendiente, 4 Preparación, 1 Lista", y lista con las 8 órdenes más recientes
2. **Dashboard sin órdenes pendientes**: Cajero accede al dashboard, ve "Órdenes abiertas: 0" con mensaje "Sin órdenes abiertas", y sección de pendientes muestra "¡Excelente! No hay órdenes pendientes"
3. **Click en card de órdenes**: Cajero hace clic en el card "Órdenes abiertas", es redirigido a `/orders`
4. **Click en Ver detalle**: Cajero hace clic en "Ver detalle" de orden #005, es redirigido a `/orders/005` con el detalle completo
5. **Click en fila de orden**: Cajero hace clic en cualquier parte de la fila de orden #003, es redirigido al detalle de esa orden
6. **Actualización automática**: Cajero tiene dashboard abierto, después de 30 segundos aparecen automáticamente 2 nuevas órdenes en la lista sin necesidad de refresh
7. **Actualización manual**: Cajero hace clic en botón de refresh, ve loading por 1 segundo, la lista se actualiza con datos nuevos
8. **Nueva orden desde POS**: Otro usuario crea orden desde POS, el dashboard del cajero se actualiza en tiempo real mostrando la nueva orden
9. **Más de 10 órdenes pendientes**: Hay 15 órdenes pendientes, el dashboard muestra solo las 10 más recientes con mensaje "Mostrando últimas 10 órdenes. Ver todas en Órdenes"
10. **Error al cargar órdenes**: Hay error de red, el dashboard muestra "Error al cargar órdenes" con botón "Reintentar", cajero hace clic y los datos se cargan correctamente
11. **Dashboard en mobile**: Cajero accede desde teléfono, ve card arriba y lista de 5 órdenes debajo con scroll para ver más
12. **Badges de estado**: Dashboard muestra 2 pendientes (badge naranja), 5 en preparación (badge azul), 1 lista (badge verde)
13. **Indicador de actualización automática**: Mientras el cajero observa, cada 30 segundos aparece un pequeño icono pulsante indicando actualización, los datos se refrescan silenciosamente

---