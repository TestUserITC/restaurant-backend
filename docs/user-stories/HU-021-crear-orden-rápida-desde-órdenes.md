## HU-021: Crear Orden Rápida desde Órdenes

### Descripción
Como usuario (Owner o Cajero), quiero poder crear una nueva orden rápidamente desde la página de órdenes para agilizar el flujo de trabajo sin necesariamente ir al POS completo.

### Criterios de Aceptación

**Trigger de Creación:**
- Botón "Nueva orden" en la esquina superior derecha de la página de órdenes
- Al hacer clic, redirigir al POS (`/pos`)
- Alternativamente, el botón puede abrir un mini-POS modal (versión simplificada)

**Redirección al POS:**
- Al hacer clic en "Nueva orden", redirigir a `/pos`
- El POS está vacío y listo para agregar productos
- Después de crear y cerrar la orden en el POS, volver automáticamente a `/orders`

**Mini-POS Modal (Alternativa):**
- Si se implementa modal en lugar de redirección:
  - Título: "Nueva orden"
  - Selector de productos con búsqueda rápida
  - Lista de productos agregados con cantidad y subtotal
  - Campo opcional para notas
  - Total calculado en tiempo real
  - Botones: "Cancelar" y "Crear orden"

**Funcionalidad del Mini-POS:**
- Búsqueda de productos por nombre
- Click en producto lo agrega a la orden
- Botones +/- para ajustar cantidad
- Botón eliminar para quitar producto
- Campo de notas opcional
- Cálculo automático de subtotal, impuesto y total

**Creación de Orden:**
- Al hacer clic en "Crear orden", validar que haya al menos 1 producto
- La orden se crea con estado "Pendiente"
- Canal: "Mostrador" (fijo)
- Cerrar el modal automáticamente
- Actualizar la lista de órdenes mostrando la nueva orden
- Mostrar toast: "Orden creada exitosamente"

**Validaciones:**
- Si no hay productos agregados, deshabilitar botón "Crear orden"
- Si no hay productos disponibles en el menú, mostrar mensaje: "No hay productos disponibles para crear órdenes"

**Manejo de Errores:**
- Si hay error al crear orden, mostrar toast: "No se pudo crear la orden. Por favor, intenta de nuevo"
- El modal permanece abierto con los datos ingresados

**Número de Orden Automático:**
- Generar número de orden automáticamente de forma secuencial
- Formato: #001, #002, #003, etc.
- Reiniciar numeración cada día (opcional) o mantener secuencia continua

### Escenarios

1. **Redirección al POS**: Usuario hace clic en "Nueva orden", es redirigido a `/pos`, crea orden con 3 productos, al finalizar vuelve automáticamente a `/orders` donde ve la nueva orden
2. **Mini-POS: crear orden simple**: Usuario hace clic en "Nueva orden", se abre modal, busca "Hamburguesa", la agrega, ajusta cantidad a 2, agrega "Coca Cola", escribe nota "Sin cebolla", hace clic en "Crear orden", el modal se cierra, la nueva orden aparece en la lista con estado Pendiente
3. **Mini-POS: ajustar cantidades**: Usuario agrega Hamburguesa, hace clic en botón "+" dos veces, la cantidad aumenta a 3, el subtotal se actualiza automáticamente
4. **Mini-POS: eliminar producto**: Usuario agrega 3 productos, elimina uno con botón "X", quedan 2 productos en la lista
5. **Mini-POS: búsqueda de productos**: Usuario escribe "piz" en búsqueda, aparecen resultados "Pizza Margarita", "Pizza Pepperoni", hace clic en "Pizza Margarita", se agrega a la orden
6. **Mini-POS: validación sin productos**: Usuario abre modal, no agrega productos, el botón "Crear orden" está deshabilitado
7. **Mini-POS: cancelar creación**: Usuario agrega productos, hace clic en "Cancelar", el modal se cierra sin crear orden, los datos se descartan
8. **Crear orden sin notas**: Usuario crea orden con productos pero sin escribir notas, la orden se crea exitosamente, en detalle aparece "Sin notas adicionales"
9. **Error al crear orden**: Usuario completa orden, hace clic en "Crear orden", hay error de red, aparece toast "No se pudo crear la orden", el modal permanece abierto
10. **Orden aparece al inicio de la lista**: Usuario crea nueva orden, al cerrar modal la orden aparece al inicio de la lista (más reciente primero)
11. **Número de orden automático**: Usuario crea orden, se le asigna automáticamente #012 (siguiente número secuencial)
12. **Nueva orden con estado Pendiente**: Usuario crea orden, la orden aparece con badge naranja/amarillo indicando estado Pendiente

---