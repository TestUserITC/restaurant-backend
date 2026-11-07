## HU-024: Interfaz Principal del POS

### Descripción
Como usuario (Owner o Cajero), quiero una interfaz de punto de venta clara y eficiente para tomar pedidos rápidamente y sin errores durante el servicio a clientes.

### Criterios de Aceptación

**Layout Principal:**
- La interfaz está dividida en 2 secciones principales:
  - Izquierda (60-65%): Catálogo de productos
  - Derecha (35-40%): Carrito de compra y resumen
- Diseño optimizado para tablet (landscape) y desktop
- Sin distracciones: interfaz limpia enfocada en velocidad

**Sección Izquierda: Catálogo de Productos**
- Título "Productos" en la parte superior
- Filtros por categoría en tabs o pills horizontales:
  - "Todas" (muestra todos los productos)
  - Cada categoría activa del sistema
- Barra de búsqueda rápida con placeholder "Buscar producto..."
- Grid de productos con cards:
  - Imagen del producto (o placeholder si no tiene)
  - Nombre del producto
  - Precio
  - Badge "No disponible" si el producto no está disponible
- Cards clickeables para agregar al carrito
- Scroll vertical si hay muchos productos

**Sección Derecha: Carrito y Resumen**
- Título "Orden actual" en la parte superior
- Lista de productos agregados mostrando:
  - Nombre del producto
  - Precio unitario
  - Controles de cantidad (-, cantidad, +)
  - Subtotal (precio × cantidad)
  - Botón eliminar (X o ícono de basura)
- Si el carrito está vacío, mostrar mensaje: "No hay productos agregados"
- Resumen de totales al final:
  - Subtotal
  - Impuesto (% y monto)
  - Total (destacado, grande)
- Botón principal "Procesar pago" (grande, color primario)
- Botón secundario "Limpiar carrito"

**Filtro por Categoría:**
- Al hacer clic en una categoría, mostrar solo productos de esa categoría
- La categoría activa se destaca visualmente
- "Todas" muestra todos los productos disponibles

**Búsqueda de Productos:**
- Búsqueda en tiempo real mientras se escribe (debounce de 300ms)
- Busca en nombre del producto
- Muestra solo productos que coincidan con la búsqueda
- Botón X para limpiar búsqueda

**Estado de Productos No Disponibles:**
- Productos marcados como "No disponible" se muestran con opacidad reducida
- Badge "No disponible" sobre la card
- No son clickeables (no se pueden agregar al carrito)
- Tooltip al hacer hover: "Este producto no está disponible actualmente"

**Productos de Categorías Inactivas:**
- No mostrar productos de categorías inactivas
- Solo mostrar productos de categorías activas

**Responsive Design:**
- Desktop (>1024px): Layout de 2 columnas (60/40)
- Tablet landscape (768px-1024px): Layout de 2 columnas ajustado
- Tablet portrait/Mobile (<768px): Carrito en modal que se abre con botón flotante "Ver carrito (X items)"

**Estados de Carga:**
- Al cargar el POS, mostrar skeleton loaders en grid de productos
- Al cargar categorías, mostrar skeleton en filtros
- La carga debe completarse en menos de 2 segundos

**Manejo de Errores:**
- Si hay error al cargar productos, mostrar: "Error al cargar productos" con botón "Reintentar"
- Si no hay productos disponibles, mostrar: "No hay productos disponibles para vender"

**Permisos:**
- Tanto Owner como Cajero tienen acceso completo al POS

### Escenarios

1. **POS con productos cargados**: Usuario accede a `/pos`, ve grid con 15 productos organizados por categorías, carrito vacío a la derecha con mensaje "No hay productos agregados"
2. **Filtrar por categoría Bebidas**: Usuario hace clic en tab "Bebidas", el grid muestra solo 8 productos de esa categoría
3. **Volver a ver todas las categorías**: Usuario hace clic en "Todas", el grid vuelve a mostrar todos los productos disponibles
4. **Buscar producto**: Usuario escribe "ham" en búsqueda, el grid muestra solo "Hamburguesa Clásica" y "Hamburguesa con Queso"
5. **Limpiar búsqueda**: Usuario hace clic en X del campo de búsqueda, el grid vuelve a mostrar todos los productos
6. **Producto no disponible**: Producto "Coca Cola" está marcado como no disponible, aparece con opacidad reducida y badge "No disponible", no se puede hacer clic
7. **Hover en producto no disponible**: Usuario hace hover sobre producto no disponible, ve tooltip "Este producto no está disponible actualmente"
8. **Carrito vacío**: Usuario ve mensaje "No hay productos agregados" en sección derecha, el botón "Procesar pago" está deshabilitado
9. **Vista en tablet landscape**: Usuario accede desde iPad en horizontal, ve layout de 2 columnas optimizado para pantalla
10. **Vista en mobile**: Usuario accede desde teléfono, ve grid de productos en pantalla completa, botón flotante "Ver carrito (0 items)" en parte inferior
11. **Error al cargar productos**: Hay error de red, usuario ve mensaje "Error al cargar productos" con botón "Reintentar", hace clic y los productos cargan correctamente
12. **Sin productos disponibles**: Todos los productos están marcados como no disponibles o eliminados, usuario ve mensaje "No hay productos disponibles para vender"
13. **Categorías inactivas ocultas**: Categoría "Promociones" está inactiva, no aparece en los filtros del POS y sus productos no se muestran

---