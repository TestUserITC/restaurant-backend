## HU-027: Eliminar Productos del Carrito

### Descripción
Como usuario (Owner o Cajero), quiero eliminar productos del carrito para corregir errores o cuando el cliente cambia su orden.

### Criterios de Aceptación

**Botón Eliminar:**
- Cada producto en el carrito tiene un botón "Eliminar"
- Representado con ícono X o de basura
- Posicionado a la derecha de la fila del producto
- Color distintivo (rojo o neutral según diseño)

**Comportamiento al Eliminar:**
- Al hacer clic en "Eliminar", el producto desaparece inmediatamente del carrito
- Animación de salida (fade out, slide out) para transición suave
- Los totales se recalculan automáticamente
- No mostrar confirmación (acción debe ser rápida)

**Actualización de Totales:**
- Al eliminar producto, recalcular:
  - Subtotal general
  - Impuesto
  - Total final
- Si era el único producto, el carrito queda vacío

**Carrito Vacío:**
- Si se eliminan todos los productos, mostrar mensaje: "No hay productos agregados"
- El botón "Procesar pago" se deshabilita
- Los totales muestran $0.00

**Botón Limpiar Carrito:**
- Incluir botón "Limpiar carrito" en la parte inferior del carrito
- Color secundario o texto (menos prominente que "Procesar pago")
- Al hacer clic, eliminar todos los productos del carrito
- Mostrar modal de confirmación: "¿Limpiar el carrito?"

**Modal de Confirmación Limpiar Carrito:**
- Título: "¿Limpiar el carrito?"
- Mensaje: "Se eliminarán todos los productos. Esta acción no se puede deshacer."
- Botones:
  - "Cancelar" (secundario)
  - "Limpiar" (destructivo/rojo)

**Feedback Visual:**
- Al eliminar producto individual, animación de salida
- Al limpiar carrito completo, todos los productos desaparecen con animación
- Toast de confirmación: "Carrito limpiado" (opcional)

**Alternativa: Decrementar a 0:**
- Reducir cantidad a 0 con el botón "-" también elimina el producto
- El comportamiento es idéntico a hacer clic en "Eliminar"

### Escenarios

1. **Eliminar producto individual**: Usuario tiene 3 productos en carrito, hace clic en "Eliminar" de Coca Cola, el producto desaparece con animación, quedan 2 productos, totales se actualizan
2. **Eliminar último producto**: Usuario tiene solo 1 producto en carrito, lo elimina, el carrito muestra "No hay productos agregados", botón "Procesar pago" se deshabilita, totales en $0.00
3. **Limpiar carrito completo**: Usuario tiene 5 productos, hace clic en "Limpiar carrito", ve modal de confirmación, hace clic en "Limpiar", todos los productos desaparecen, carrito queda vacío
4. **Cancelar limpiar carrito**: Usuario hace clic en "Limpiar carrito", ve modal, hace clic en "Cancelar", el modal se cierra, todos los productos permanecen en el carrito
5. **Eliminar vía decrementar**: Usuario tiene Hamburguesa con cantidad 1, hace clic en "-", la cantidad llega a 0, el producto se elimina automáticamente
6. **Actualización de totales al eliminar**: Usuario tiene orden de $50 total, elimina producto de $10, el total se actualiza inmediatamente a $40 + impuestos recalculados
7. **Animación de salida**: Usuario elimina producto, la fila del producto hace fade out durante 0.3 segundos antes de desaparecer
8. **Múltiples eliminaciones rápidas**: Usuario hace clic en "Eliminar" de 3 productos consecutivamente, todos se eliminan correctamente con sus animaciones
9. **Carrito vacío después de limpiar**: Usuario limpia carrito, el mensaje "No hay productos agregados" aparece en el área del carrito

---