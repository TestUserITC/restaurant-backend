## HU-026: Modificar Cantidad de Productos en Carrito

### Descripción
Como usuario (Owner o Cajero), quiero ajustar las cantidades de productos en el carrito para corregir la orden según lo que el cliente solicite.

### Criterios de Aceptación

**Controles de Cantidad:**
- Cada producto en el carrito tiene 3 controles:
  - Botón "-" (decrementar)
  - Campo de cantidad (editable, numérico)
  - Botón "+" (incrementar)
- Los botones deben ser grandes y fáciles de tocar (especialmente en tablet)

**Incrementar Cantidad (+):**
- Al hacer clic en "+", aumentar cantidad en 1
- El subtotal del producto se actualiza automáticamente
- El total general se recalcula inmediatamente
- Límite máximo: 99 unidades

**Decrementar Cantidad (-):**
- Al hacer clic en "-", reducir cantidad en 1
- Si la cantidad llega a 0, eliminar el producto del carrito automáticamente
- El subtotal y total se actualizan automáticamente
- El botón "-" está habilitado siempre (no se deshabilita en 1)

**Edición Directa de Cantidad:**
- El campo de cantidad es editable (input numérico)
- Al hacer clic, seleccionar el texto para fácil reemplazo
- Al escribir, validar que solo sean números
- Al perder focus (blur), validar y aplicar la cantidad

**Validaciones en Edición Directa:**
- Solo permitir números enteros positivos
- Si se ingresa 0 o se deja vacío, eliminar el producto del carrito
- Si se excede 99, ajustar automáticamente a 99
- Si se ingresa texto no numérico, mantener cantidad anterior

**Actualización de Totales:**
- Al cambiar cantidad, recalcular:
  - Subtotal del producto (precio × cantidad)
  - Subtotal general (suma de todos los subtotales)
  - Impuesto (subtotal × %)
  - Total final (subtotal + impuesto)
- La actualización debe ser instantánea (sin delay)

**Formato Visual:**
- Campo de cantidad centrado, fácil de leer
- Botones +/- con buen contraste y tamaño
- Subtotal actualizado en tiempo real

**Feedback Visual:**
- Al cambiar cantidad, resaltar brevemente el subtotal actualizado
- Animación suave al eliminar producto (cuando cantidad llega a 0)

**Atajos de Teclado (Opcional):**
- Al editar cantidad, permitir:
  - Enter: Aplicar cantidad y mover a siguiente campo
  - Escape: Cancelar edición y mantener cantidad anterior
  - Flechas arriba/abajo: Incrementar/decrementar

### Escenarios

1. **Incrementar cantidad**: Usuario tiene Hamburguesa (cantidad 1, $10), hace clic en "+", la cantidad cambia a 2, el subtotal actualiza a $20.00, el total general se recalcula
2. **Decrementar cantidad**: Usuario tiene Coca Cola (cantidad 3, $3 c/u, subtotal $9), hace clic en "-", la cantidad cambia a 2, subtotal actualiza a $6.00
3. **Decrementar hasta eliminar**: Usuario tiene Pizza (cantidad 1), hace clic en "-", la cantidad llega a 0, el producto desaparece del carrito con animación
4. **Edición directa de cantidad**: Usuario hace clic en campo de cantidad (actualmente 2), escribe "5", presiona Enter o hace blur, la cantidad cambia a 5, subtotal se actualiza
5. **Edición con texto inválido**: Usuario intenta escribir "abc" en cantidad, el campo no acepta letras, mantiene el valor anterior
6. **Edición con 0**: Usuario edita cantidad a "0" y presiona Enter, el producto se elimina del carrito
7. **Edición campo vacío**: Usuario borra toda la cantidad dejando campo vacío y hace blur, el producto se elimina del carrito
8. **Exceder límite máximo**: Usuario escribe "150" en cantidad, al hacer blur el sistema ajusta automáticamente a 99
9. **Incrementar hasta límite**: Usuario hace clic 98 veces en "+" de producto con cantidad 1, llega a 99, el siguiente click no hace nada o muestra mensaje
10. **Actualización instantánea de totales**: Usuario cambia cantidad de Hamburguesa de 2 a 5, inmediatamente el subtotal cambia de $20 a $50, impuesto y total se recalculan sin delay
11. **Múltiples productos con cantidades**: Usuario tiene 3 productos diferentes con cantidades 2, 5, y 3 respectivamente, cambia el segundo a 8, solo ese subtotal se actualiza, los demás permanecen igual
12. **Campo cantidad seleccionado**: Usuario hace clic en campo de cantidad, todo el texto se selecciona automáticamente, puede empezar a escribir inmediatamente
13. **Atajo Enter**: Usuario edita cantidad a 3, presiona Enter, la cantidad se aplica y el cursor se mueve al siguiente campo editable
14. **Feedback visual en actualización**: Usuario incrementa cantidad, el subtotal hace una breve animación (flash o highlight) indicando el cambio

---