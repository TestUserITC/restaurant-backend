## HU-017: Eliminar Producto

### Descripción
Como usuario Owner, quiero eliminar productos del menú que ya no ofrezco para mantener el catálogo actualizado y limpio.

### Criterios de Aceptación

**Trigger de Eliminación:**
- En la tabla de productos, columna "Acciones" incluye botón "Eliminar" (ícono de basura)
- El botón está siempre habilitado (no hay restricción por ventas históricas)
- Al hacer clic, abrir modal de confirmación

**Modal de Confirmación:**
- Título: "¿Eliminar producto?"
- Mensaje: "¿Estás seguro de que deseas eliminar '[Nombre del producto]'? Este producto ya no estará disponible en el menú."
- Submensaje: "Nota: Las ventas históricas de este producto se mantendrán."
- El nombre del producto se muestra en negrita
- Botones:
  - "Cancelar" (secundario, izquierda)
  - "Eliminar" (destructivo/rojo, derecha)

**Comportamiento de Eliminación:**
- Al hacer clic en "Eliminar", mostrar spinner en el botón y cambiar texto a "Eliminando..."
- Deshabilitar ambos botones durante el proceso
- Si la eliminación es exitosa:
  - Cerrar el modal automáticamente
  - Remover el producto de la lista con animación de salida
  - Mostrar toast de éxito: "Producto eliminado exitosamente"

**Preservación de Datos Históricos:**
- La eliminación es "soft delete" (desactivación)
- Las ventas históricas que incluyen este producto se mantienen intactas
- En reportes históricos, el producto sigue apareciendo con su nombre original
- El producto simplemente deja de estar disponible para nuevas ventas

**Manejo de Errores:**
- Si hay error al eliminar, mostrar toast: "No se pudo eliminar el producto. Por favor, intenta de nuevo"
- El modal permanece abierto para permitir reintentos

**Impacto en Categoría:**
- Al eliminar un producto, el conteo de productos de su categoría se actualiza automáticamente
- Si era el último producto de la categoría, la categoría ahora muestra "Sin productos" y puede ser eliminada

**Estado Vacío Después de Eliminar:**
- Si después de eliminar no quedan más productos, mostrar estado vacío: "No hay productos creados" con botón "Crear primer producto"

**Cierre del Modal:**
- Al hacer clic en "Cancelar", cerrar modal sin eliminar
- Al hacer clic en X, cerrar modal sin eliminar
- Al hacer clic fuera del modal (overlay), cerrar sin eliminar
- Al presionar ESC, cerrar sin eliminar

### Escenarios

1. **Eliminar producto exitosamente**: Owner hace clic en "Eliminar" de producto "Tacos", ve modal de confirmación con nombre "Tacos" en negrita, hace clic en "Eliminar", ve spinner, el modal se cierra, la fila desaparece con animación, aparece toast "Producto eliminado exitosamente"
2. **Cancelar eliminación**: Owner hace clic en "Eliminar", ve modal, hace clic en "Cancelar", el modal se cierra sin eliminar, el producto permanece en la lista
3. **Cerrar modal con X**: Owner abre modal de eliminación, hace clic en X, el modal se cierra sin eliminar
4. **Mantener ventas históricas**: Owner elimina producto "Pizza" que tiene 50 ventas del mes pasado, el producto se elimina pero las ventas del mes pasado siguen mostrando "Pizza" correctamente
5. **Actualizar conteo de categoría**: Categoría "Bebidas" tiene 5 productos, Owner elimina "Coca Cola", el conteo de "Bebidas" ahora muestra "4 productos"
6. **Último producto de categoría**: Categoría "Promociones" tiene solo 1 producto, Owner lo elimina, la categoría ahora muestra "Sin productos" y su botón "Eliminar" se habilita
7. **Estado vacío después de eliminar todo**: Owner tiene 3 productos, los elimina todos, ve estado vacío "No hay productos creados" con botón "Crear primer producto"
8. **Error al eliminar**: Owner intenta eliminar producto, hay error de red, aparece toast "No se pudo eliminar el producto", el modal permanece abierto
9. **Eliminar con filtro activo**: Filtro activo en "Bebidas" que tiene 5 productos, Owner elimina uno, la lista ahora muestra 4 productos de Bebidas
10. **Cerrar con ESC**: Owner abre modal de confirmación, presiona tecla ESC, el modal se cierra sin eliminar

---

## Resumen de Navegación en Gestión de Menú

**Estructura de URLs:**
- `/menu` → Redirige a `/menu/categorias` (página principal)
- `/menu/categorias` → Lista de categorías
- `/menu/productos` → Lista de productos

**Navegación en Menú Lateral:**
- Ítem "Menú" con sub-ítems:
  - Categorías
  - Productos
- Al hacer clic en "Menú", expandir sub-menú
- Marcar como activo el sub-ítem de la página actual

**Breadcrumb:**
- `/menu/categorias`: Dashboard > Menú > Categorías
- `/menu/productos`: Dashboard > Menú > Productos

---

## Notas Técnicas

**Imágenes:**
- Almacenar en storage/CDN
- Generar thumbnails automáticamente (60x60, 200x200)
- Optimizar al subir (comprimir, convertir a WebP si es posible)
- Lazy loading de imágenes en la lista

**Validación de Nombres:**
- Validar unicidad case-insensitive
- Trimear espacios al inicio y final
- No permitir solo espacios

**Performance:**
- Cargar productos con paginación o virtual scrolling si hay muchos
- Caché de lista de categorías (usada en múltiples lugares)
- Optimizar queries con índices en nombre, categoría, estado

**Soft Delete:**
- Productos eliminados no se borran físicamente
- Campo deleted_at para marcar como eliminado
- Queries excluyen productos eliminados por defecto
- Mantener integridad referencial con órdenes históricas

**Estados de Producto:**
- Disponible: Activo y visible en POS
- No disponible: Existe pero no se puede vender (temporalmente agotado)
- Eliminado (soft delete): No aparece en ningún lado excepto historial

**Formatos de Moneda:**
- Usar la moneda configurada en settings
- Todos los precios en formato consistente
- Validar que precio > 0