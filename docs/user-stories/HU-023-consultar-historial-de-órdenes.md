## HU-023: Consultar Historial de Órdenes

### Descripción
Como usuario Owner, quiero consultar el historial completo de órdenes para revisar pedidos anteriores, analizar ventas o recuperar información de órdenes específicas.

### Criterios de Aceptación

**Acceso al Historial:**
- Desde la página de órdenes, el filtro de fecha permite seleccionar periodos anteriores
- Por defecto, la vista muestra "Hoy"
- Owner puede cambiar a "Ayer", "Últimos 7 días", "Este mes", o rango personalizado

**Filtro de Fecha Personalizado:**
- Al seleccionar "Personalizado", abrir date picker de rango
- Permite seleccionar fecha inicial y fecha final
- Botón "Aplicar" para ejecutar la búsqueda
- Botón "Limpiar" para volver a la vista de hoy

**Órdenes Históricas:**
- Mostrar todas las órdenes del periodo seleccionado
- Incluir órdenes en todos los estados (Pendiente, Preparación, Lista, Cerrada)
- Ordenar por fecha/hora de creación (más reciente primero)

**Información Visible:**
- Las mismas columnas que la vista principal
- Todas las órdenes históricas muestran su estado final
- Click en una orden abre su detalle completo

**Búsqueda en Historial:**
- El campo de búsqueda funciona también en historial
- Permite buscar por número de orden en cualquier fecha
- Buscar orden específica sin importar el rango de fecha activo

**Exportación de Historial (Opcional):**
- Botón "Exportar" para descargar historial en CSV
- El CSV incluye: número orden, fecha, hora, estado, items, total, notas
- El nombre del archivo incluye el rango de fechas (ej: "ordenes_2026-01-20_2026-01-26.csv")

**Paginación en Historial:**
- Si hay muchas órdenes, implementar paginación
- Mostrar selector de elementos por página: 25, 50, 100
- Información de paginación: "Mostrando 1-25 de 200 órdenes"

**Estados de Carga:**
- Al cambiar rango de fecha, mostrar loading mientras se cargan órdenes
- Skeleton loaders durante la carga

**Manejo de Errores:**
- Si hay error al cargar historial, mostrar: "Error al cargar historial de órdenes" con botón "Reintentar"
- Si el rango de fechas es inválido (fecha final antes de inicial), mostrar error: "Rango de fechas inválido"

**Estadísticas Rápidas del Periodo:**
- Mostrar resumen del periodo seleccionado:
  - Total de órdenes
  - Total de ventas
  - Ticket promedio
- Este resumen aparece en la parte superior de la lista

**Permisos:**
- Solo Owner puede acceder a historial completo
- Cajero solo puede ver órdenes del día actual

### Escenarios

1. **Ver órdenes de ayer**: Owner selecciona "Ayer" en filtro de fecha, ve todas las órdenes del día anterior con sus estados finales
2. **Ver últimos 7 días**: Owner selecciona "Últimos 7 días", ve todas las órdenes de la última semana, hay 150 órdenes con paginación
3. **Rango personalizado**: Owner selecciona "Personalizado", elige del 1 al 15 de enero, hace clic en "Aplicar", ve todas las órdenes de ese periodo
4. **Búsqueda en historial**: Owner está viendo historial de último mes, busca "025", encuentra orden #025 del 15 de enero
5. **Click en orden histórica**: Owner hace clic en orden #018 de hace 3 días, ve detalle completo con todos los productos y estado final "Cerrada"
6. **Estadísticas del periodo**: Owner selecciona "Últimos 7 días", ve en parte superior: "150 órdenes, $3,250.00 total ventas, $21.67 ticket promedio"
7. **Exportar historial**: Owner selecciona "Este mes", hace clic en "Exportar", descarga archivo "ordenes_2026-01-01_2026-01-26.csv" con todas las órdenes del mes
8. **Volver a vista de hoy**: Owner está viendo historial, hace clic en "Hoy" en filtro de fecha, vuelve a ver solo órdenes del día actual
9. **Rango inválido**: Owner selecciona fecha final antes de fecha inicial, ve error "Rango de fechas inválido", no se ejecuta la búsqueda
10. **Paginación en historial grande**: Owner selecciona "Este mes" con 500 órdenes, ve primeras 25 con paginación, navega a página 5 para ver órdenes 101-125
11. **Error al cargar historial**: Owner selecciona periodo, hay error de red, ve mensaje "Error al cargar historial de órdenes" con botón "Reintentar"
12. **Cajero intenta ver historial**: Usuario Cajero intenta cambiar a "Ayer", el sistema no permite o muestra mensaje "Solo puedes ver órdenes de hoy"

---

## Resumen de Estados de Órdenes

**Estados Disponibles:**
1. **Pendiente** - Orden creada, esperando preparación (Color: Naranja/Amarillo)
2. **Preparación** - Orden en proceso de preparación (Color: Azul)
3. **Lista** - Orden lista para entregar (Color: Verde)
4. **Cerrada** - Orden completada y entregada (Color: Gris)

**Flujo de Estados:**
```
Pendiente → Preparación → Lista → Cerrada
```

**Restricciones:**
- No se puede saltar estados
- No se puede retroceder estados
- Cerrada es estado final (no cambia)

---

## Navegación en Módulo de Órdenes

**URLs:**
- `/orders` → Lista de órdenes
- `/orders/[id]` → Detalle de orden específica

**Breadcrumbs:**
- `/orders`: Dashboard > Órdenes
- `/orders/[id]`: Dashboard > Órdenes > Orden #XXX

**Acciones desde Órdenes:**
- "Nueva orden" → Redirige a `/pos`
- Click en fila → Redirige a `/orders/[id]`
- "Volver a órdenes" → Redirige a `/orders`

---

## Notas Técnicas

**Actualización en Tiempo Real:**
- Implementar WebSocket o polling (cada 10-15 segundos)
- Actualizar lista cuando hay cambios en órdenes
- Notificar cambios si usuario tiene detalle abierto
- Optimizar para no hacer requests innecesarios

**Numeración de Órdenes:**
- Generar número secuencial automático
- Formato: #001, #002, #003...
- Considerar reinicio diario o secuencia continua
- Asegurar unicidad con índice en base de datos

**Cálculo de Totales:**
- Subtotal: Suma de (precio × cantidad) de todos los productos
- Impuesto: Subtotal × (% impuesto configurado)
- Total: Subtotal + Impuesto
- Almacenar totales calculados en la orden (no recalcular cada vez)

**Performance:**
- Índices en: estado, fecha_creacion, numero_orden
- Paginación para listas grandes
- Caché de órdenes activas (Pendiente, Preparación, Lista)
- Lazy loading de órdenes históricas

**Timestamps:**
- created_at: Fecha/hora de creación
- updated_at: Última actualización
- Timestamp por cada cambio de estado (opcional)
- Zona horaria del restaurante

**Soft Delete:**
- No implementar eliminación de órdenes
- Todas las órdenes se mantienen en el sistema
- Estado "Cerrada" es el estado final

**Permisos:**
- Owner: Acceso completo (crear, ver, editar, historial)
- Cajero: Crear, ver y cambiar estados (solo órdenes del día)
- Validar permisos en frontend y backend

**Canal:**
- Para MVP: Solo "Mostrador" (fijo)
- Preparar estructura para futuros canales (Delivery, Para llevar, etc.)