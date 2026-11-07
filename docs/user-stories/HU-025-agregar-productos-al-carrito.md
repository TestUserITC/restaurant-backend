## HU-025: Agregar Productos al Carrito

### Descripción
Como usuario (Owner o Cajero), quiero agregar productos al carrito de forma rápida e intuitiva para construir la orden del cliente eficientemente.

### Criterios de Aceptación

**Agregar Producto desde Catálogo:**
- Al hacer clic en una card de producto, agregar el producto al carrito
- Cantidad inicial: 1 unidad
- Si el producto ya está en el carrito, incrementar cantidad en 1
- Feedback visual al agregar: animación breve en la card (ej: flash, bounce)
- Reproducir sonido de confirmación (opcional, debe poder desactivarse)

**Producto Agregado al Carrito:**
- El producto aparece en la lista de carrito con:
  - Nombre del producto
  - Precio unitario
  - Cantidad inicial: 1
  - Subtotal: precio × cantidad
  - Controles +/- para ajustar cantidad
  - Botón eliminar (X)
- Si ya existía, solo incrementar cantidad (no duplicar fila)

**Feedback Visual:**
- Al agregar producto, mostrar animación sutil en la card del producto
- El número de items en el carrito se actualiza inmediatamente
- En mobile, el badge del botón flotante se actualiza (ej: "Ver carrito (3 items)")

**Orden de Productos en Carrito:**
- Los productos aparecen en el orden en que fueron agregados
- Mantener orden consistente mientras se modifican cantidades

**Cálculo Automático de Subtotal:**
- Al agregar producto, el subtotal de ese item se calcula automáticamente (precio × cantidad)
- El subtotal total del carrito se actualiza inmediatamente

**Agregar Múltiples Unidades:**
- Al hacer múltiples clicks en el mismo producto, incrementar cantidad
- Cada click agrega 1 unidad

**Límite de Cantidad (Opcional):**
- Límite máximo de 99 unidades por producto
- Si se alcanza el límite, no permitir agregar más
- Mostrar mensaje temporal: "Cantidad máxima alcanzada"

**Estados de Carga:**
- No hay loading al agregar productos (acción instantánea)
- Solo actualización visual del carrito

**Validaciones:**
- No permitir agregar productos marcados como "No disponible"
- No permitir agregar productos de categorías inactivas

### Escenarios

1. **Agregar primer producto**: Usuario hace clic en "Hamburguesa Clásica" ($10), el producto aparece en el carrito con cantidad 1, subtotal $10.00, el total general muestra $10.00 + impuesto
2. **Agregar segundo producto diferente**: Usuario agrega "Coca Cola" ($3), aparece en el carrito debajo de Hamburguesa, el total se actualiza a $13.00 + impuesto
3. **Agregar mismo producto dos veces**: Usuario hace clic en "Hamburguesa" dos veces, la cantidad en el carrito aumenta de 1 a 2, el subtotal cambia a $20.00
4. **Feedback visual al agregar**: Usuario hace clic en producto, la card hace una animación breve (flash o bounce) confirmando la acción
5. **Badge de carrito actualizado en mobile**: Usuario en mobile agrega 3 productos diferentes, el botón flotante muestra "Ver carrito (3 items)"
6. **Agregar hasta límite máximo**: Usuario hace clic 99 veces en "Coca Cola", la cantidad llega a 99, el siguiente click muestra mensaje temporal "Cantidad máxima alcanzada"
7. **Intento de agregar producto no disponible**: Usuario hace clic en producto con badge "No disponible", no pasa nada, el producto no se agrega al carrito
8. **Cálculo automático de totales**: Usuario agrega 2 Hamburguesas ($10 c/u) y 1 Refresco ($3), el subtotal muestra $23.00, impuesto 18% muestra $4.14, total muestra $27.14
9. **Productos en orden de agregado**: Usuario agrega Pizza, luego Coca Cola, luego Tacos, el carrito muestra los productos en ese mismo orden
10. **Agregar producto rápidamente**: Usuario hace 5 clicks rápidos en "Hamburguesa", la cantidad aumenta a 5 sin lag o errores

---