## HU-014: Ver Lista de Productos

### Descripción
Como usuario Owner, quiero ver todos los productos del menú organizados por categoría para tener control completo sobre los items que ofrezco y poder gestionarlos fácilmente.

### Criterios de Aceptación

**Estructura de la Página:**
- La página muestra un título "Productos" en la parte superior
- Incluye un botón primario "Nuevo producto" en la esquina superior derecha
- Incluye un filtro dropdown "Todas las categorías" para filtrar por categoría específica
- El contenido principal muestra una tabla con los productos existentes
- Si no hay productos, mostrar estado vacío con mensaje "No hay productos creados" y botón "Crear primer producto"

**Filtro por Categoría:**
- Dropdown con opciones:
  - "Todas las categorías" (opción por defecto)
  - Lista de todas las categorías existentes
- Al seleccionar una categoría, la tabla muestra solo productos de esa categoría
- Al seleccionar "Todas las categorías", mostrar todos los productos

**Tabla de Productos:**
- Columnas visibles:
  - Imagen (thumbnail pequeño, 60x60px)
  - Nombre (texto, ordenable)
  - Categoría (badge con nombre de categoría)
  - Precio (formato moneda, ordenable)
  - Estado (badge: Disponible/No disponible)
  - Acciones (botones de editar y toggle estado)
- Las filas se pueden ordenar por nombre (A-Z o Z-A) o por precio (menor a mayor, mayor a menor)
- Cada fila muestra toda la información del producto de forma clara

**Imagen del Producto:**
- Si el producto tiene imagen, mostrar thumbnail de 60x60px con bordes redondeados
- Si no tiene imagen, mostrar placeholder con ícono de imagen
- La imagen es clickeable y abre preview en tamaño completo (modal lightbox)

**Badge de Categoría:**
- Muestra el nombre de la categoría en un badge con color distintivo
- Si el filtro está activo en una categoría, los badges de esa categoría se destacan visualmente

**Formato de Precio:**
- Usar símbolo de moneda configurado en el sistema (ej: "$", "€", "S/")
- Formato con separador de miles y 2 decimales (ej: "$1,250.00")

**Estados del Producto:**
- Disponible (badge verde): El producto está activo y disponible para venta en el POS
- No disponible (badge gris): El producto existe pero no está disponible para venta

**Acciones Rápidas:**
- Toggle switch para cambiar estado Disponible/No disponible
- Al cambiar estado, mostrar toast: "Producto actualizado correctamente"
- Botón "Editar" (ícono de lápiz) abre modal de edición
- Botón "Eliminar" (ícono de basura) abre modal de confirmación

**Ordenamiento por Defecto:**
- Los productos se muestran ordenados alfabéticamente (A-Z) por nombre
- Al cargar la página, el encabezado "Nombre" muestra indicador de orden ascendente

**Paginación:**
- Si hay más de 20 productos, implementar paginación
- Mostrar selector de "Elementos por página": 10, 20, 50
- Mostrar información: "Mostrando 1-20 de 45 productos"
- Botones: Anterior, 1, 2, 3, Siguiente

**Búsqueda Rápida:**
- Campo de búsqueda con placeholder "Buscar producto..."
- Búsqueda en tiempo real mientras se escribe (debounce de 300ms)
- Busca en nombre y categoría del producto
- Limpiar búsqueda con botón X dentro del campo

**Estados de Carga:**
- Al cargar la página, mostrar skeleton loader con estructura de tabla
- Al filtrar o buscar, mostrar indicador de carga
- Al cambiar estado de producto, mostrar spinner en el toggle

**Manejo de Errores:**
- Si hay error al cargar productos, mostrar mensaje: "Error al cargar productos" con botón "Reintentar"
- Si hay error al cambiar estado, mostrar toast: "No se pudo actualizar el producto. Intenta de nuevo"

**Responsive Design:**
- En desktop (>1024px): Tabla completa con todas las columnas
- En tablet (768px-1024px): Tabla con scroll horizontal
- En mobile (<768px): Convertir en cards, cada card muestra imagen, nombre, categoría, precio, estado y botones

**Permisos:**
- Esta página solo es accesible para usuarios con rol Owner
- Si un Cajero intenta acceder, ver página 403

### Escenarios

1. **Ver lista con productos existentes**: Owner accede a `/menu/productos`, ve tabla con 15 productos mostrando imagen, nombre, categoría, precio, estado y botones de acción
2. **Estado vacío sin productos**: Owner accede por primera vez, ve mensaje "No hay productos creados" con botón "Crear primer producto"
3. **Filtrar por categoría específica**: Owner selecciona "Bebidas" en el dropdown, la tabla muestra solo los 8 productos de categoría Bebidas
4. **Volver a ver todas las categorías**: Owner selecciona "Todas las categorías", la tabla vuelve a mostrar todos los productos
5. **Cambiar estado a No disponible**: Owner hace clic en toggle de producto "Coca Cola" (actualmente Disponible), el producto cambia a No disponible, badge cambia a gris
6. **Ordenar por precio ascendente**: Owner hace clic en encabezado "Precio", la tabla se reordena de menor a mayor precio
7. **Ordenar por precio descendente**: Owner hace clic nuevamente en "Precio", la tabla se reordena de mayor a menor precio
8. **Buscar producto**: Owner escribe "ham" en búsqueda, la tabla muestra solo "Hamburguesa Clásica" y "Hamburguesa con Queso"
9. **Limpiar búsqueda**: Owner hace clic en X del campo de búsqueda, la búsqueda se limpia, la tabla vuelve a mostrar todos los productos
10. **Ver imagen en grande**: Owner hace clic en thumbnail de producto, se abre modal lightbox mostrando imagen en tamaño completo
11. **Producto sin imagen**: Producto "Agua" no tiene imagen, muestra placeholder con ícono de imagen
12. **Paginación con muchos productos**: Hay 45 productos, la tabla muestra primeros 20 con paginación "1-20 de 45 productos", Owner hace clic en página 2, ve productos 21-40
13. **Cambiar elementos por página**: Owner cambia selector a "50 elementos por página", la tabla muestra todos los 45 productos sin paginación
14. **Click en Nuevo producto**: Owner hace clic en "Nuevo producto", se abre modal de creación de producto
15. **Click en Editar**: Owner hace clic en "Editar" de producto "Pizza Margarita", se abre modal de edición con los datos de ese producto
16. **Error al cargar productos**: Hay error de red, Owner ve mensaje "Error al cargar productos" con botón "Reintentar"
17. **Vista en mobile**: Owner accede desde teléfono, ve productos como cards apiladas, cada card muestra imagen, nombre, precio, categoría, estado y botones
18. **Badge de categoría destacado con filtro**: Owner filtra por "Postres", los badges "Postres" en la tabla se destacan con color más intenso
19. **Cajero intenta acceder**: Usuario Cajero intenta navegar a `/menu/productos`, ve página 403 "No tienes permisos para acceder a esta sección"

---