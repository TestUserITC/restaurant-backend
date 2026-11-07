## HU-010: Ver Lista de Categorías

### Descripción
Como usuario Owner, quiero ver todas las categorías del menú del restaurante para tener una visión organizada de cómo está estructurado mi menú y poder gestionar las categorías fácilmente.

### Criterios de Aceptación

**Estructura de la Página:**
- La página muestra un título "Categorías" en la parte superior
- Incluye un botón primario "Nueva categoría" en la esquina superior derecha
- El contenido principal muestra una tabla con las categorías existentes
- Si no hay categorías, mostrar estado vacío con mensaje "No hay categorías creadas" y botón "Crear primera categoría"

**Tabla de Categorías:**
- Columnas visibles:
  - Nombre (texto, ordenable)
  - Productos (número de productos en la categoría)
  - Estado (badge: Activa/Inactiva)
  - Acciones (botones de editar y toggle estado)
- Las filas se pueden ordenar por nombre (A-Z o Z-A) haciendo clic en el encabezado de columna
- Cada fila muestra:
  - Nombre de la categoría con icono representativo si existe
  - Número de productos asociados (ej: "12 productos")
  - Badge de estado: "Activa" (verde) o "Inactiva" (gris)
  - Botón "Editar" (ícono de lápiz)
  - Toggle switch para activar/desactivar

**Ordenamiento por Defecto:**
- Las categorías se muestran ordenadas alfabéticamente (A-Z) por defecto
- Al cargar la página, el encabezado "Nombre" muestra un indicador de orden ascendente

**Acciones Rápidas:**
- Al hacer clic en el toggle de estado, la categoría cambia inmediatamente entre Activa/Inactiva
- Al cambiar estado, mostrar toast de confirmación: "Categoría actualizada correctamente"
- Al hacer clic en "Editar", abrir modal de edición de categoría
- Al hacer clic en el botón "Nueva categoría", abrir modal de creación

**Estados de Categoría:**
- Activa: La categoría y sus productos están disponibles para selección en el POS
- Inactiva: La categoría y sus productos NO están disponibles en el POS pero se mantienen en el sistema

**Conteo de Productos:**
- Si la categoría tiene 0 productos, mostrar "Sin productos"
- Si tiene 1 producto, mostrar "1 producto"
- Si tiene más de 1, mostrar "X productos"
- El conteo incluye todos los productos (disponibles y no disponibles)

**Estados de Carga:**
- Al cargar la página, mostrar skeleton loader con estructura de tabla
- Al cambiar estado de categoría, mostrar spinner en el toggle mientras se procesa
- La carga inicial debe completarse en menos de 2 segundos

**Manejo de Errores:**
- Si hay error al cargar categorías, mostrar mensaje: "Error al cargar categorías" con botón "Reintentar"
- Si hay error al cambiar estado, mostrar toast de error: "No se pudo actualizar la categoría. Intenta de nuevo"
- El toggle vuelve a su estado anterior si falla la actualización

**Responsive Design:**
- En desktop (>1024px): Mostrar tabla completa con todas las columnas
- En tablet (768px-1024px): Tabla con scroll horizontal si es necesario
- En mobile (<768px): Convertir tabla en cards, cada card muestra nombre, conteo productos, estado y botones de acción

**Permisos:**
- Esta página solo es accesible para usuarios con rol Owner
- Si un Cajero intenta acceder, ver página 403

### Escenarios

1. **Ver lista con categorías existentes**: Owner accede a `/menu/categorias`, ve tabla con 5 categorías ordenadas alfabéticamente con sus nombres, conteo de productos, estados y botones de acción
2. **Estado vacío sin categorías**: Owner accede a página por primera vez, ve mensaje "No hay categorías creadas" con botón "Crear primera categoría"
3. **Cambiar estado de categoría a Inactiva**: Owner hace clic en toggle de categoría "Bebidas" (actualmente Activa), el toggle muestra spinner, la categoría cambia a Inactiva, badge cambia a gris, aparece toast "Categoría actualizada correctamente"
4. **Cambiar estado de categoría a Activa**: Owner hace clic en toggle de categoría "Postres" (actualmente Inactiva), la categoría cambia a Activa, badge cambia a verde
5. **Ordenar por nombre descendente**: Owner hace clic en encabezado "Nombre", la tabla se reordena de Z-A, el indicador cambia a orden descendente
6. **Ordenar por nombre ascendente nuevamente**: Owner hace clic nuevamente en "Nombre", la tabla vuelve al orden A-Z
7. **Ver categoría sin productos**: Categoría "Promociones" muestra "Sin productos" en columna de productos
8. **Ver categoría con múltiples productos**: Categoría "Platos Fuertes" muestra "23 productos"
9. **Click en Nueva categoría**: Owner hace clic en botón "Nueva categoría", se abre modal de creación de categoría
10. **Click en Editar**: Owner hace clic en botón "Editar" de categoría "Entradas", se abre modal de edición con los datos de esa categoría
11. **Error al cargar categorías**: Hay error de red al cargar la página, Owner ve mensaje "Error al cargar categorías" con botón "Reintentar", hace clic y los datos cargan correctamente
12. **Error al cambiar estado**: Owner intenta cambiar estado de categoría pero hay error de red, toggle vuelve a posición original, aparece toast "No se pudo actualizar la categoría. Intenta de nuevo"
13. **Vista en mobile**: Owner accede desde teléfono, ve categorías como cards apiladas verticalmente, cada card muestra nombre, estado, conteo y botones
14. **Cajero intenta acceder**: Usuario con rol Cajero intenta navegar a `/menu/categorias`, ve página 403 con mensaje "No tienes permisos para acceder a esta sección"

---