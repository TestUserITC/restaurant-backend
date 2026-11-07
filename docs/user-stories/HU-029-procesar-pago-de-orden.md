## HU-029: Procesar Pago de Orden

### Descripción
Como usuario (Owner o Cajero), quiero procesar el pago de una orden de forma rápida y sencilla para completar la venta y generar el registro correspondiente.

### Criterios de Aceptación

**Botón Procesar Pago:**
- Ubicado en la parte inferior del carrito
- Color primario, grande y destacado
- Texto: "Procesar pago" o "Cobrar"
- Deshabilitado si el carrito está vacío
- Al hacer clic, abrir modal de pago

**Modal de Pago:**
- Título: "Procesar pago"
- Mostrar resumen de la orden:
  - Lista de productos con cantidades y subtotales
  - Subtotal
  - Impuesto
  - Total (destacado, grande)
- Selector de método de pago (tabs o radio buttons):
  - Efectivo
  - Tarjeta
- Campos específicos según método de pago
- Botones:
  - "Cancelar" (secundario)
  - "Completar pago" (primario, grande)

**Pago en Efectivo:**
- Campo: "Monto recibido" (input numérico)
- Placeholder: "0.00"
- Al escribir, calcular y mostrar cambio automáticamente
- "Cambio: $XX.XX" (destacado en color verde si es positivo)
- Si el monto recibido es menor al total, mostrar error: "Monto insuficiente"
- Permitir monto exacto o mayor

**Cálculo de Cambio:**
- Cambio = Monto recibido - Total
- Mostrar cambio en tiempo real mientras se escribe
- Si cambio < 0, mostrar "Monto insuficiente" en rojo
- Si cambio = 0, mostrar "Monto exacto"
- Si cambio > 0, mostrar "Cambio: $XX.XX" en verde

**Pago con Tarjeta:**
- No requiere campos adicionales (el pago se procesa externamente)
- Solo mostrar el total a cobrar
- Checkbox: "Confirmo que el pago con tarjeta fue autorizado"
- Deshabilitar botón "Completar pago" hasta marcar checkbox
- Mensaje informativo: "Procesa el pago en tu terminal y confirma"

**Validaciones:**
- Efectivo: Validar que el monto recibido sea >= total
- Tarjeta: Validar que el checkbox esté marcado
- Si hay errores, mostrar mensaje específico y deshabilitar botón

**Completar Pago:**
- Al hacer clic en "Completar pago", validar datos
- Mostrar spinner en el botón y cambiar texto a "Procesando..."
- Deshabilitar todos los campos y botones durante el proceso
- Si es exitoso:
  - Crear orden con estado "Cerrada"
  - Registrar venta con método de pago usado
  - Cerrar modal automáticamente
  - Limpiar carrito
  - Mostrar modal de confirmación de venta

**Modal de Confirmación de Venta:**
- Título: "¡Venta completada!"
- Mensaje: "Orden #XXX registrada exitosamente"
- Mostrar resumen:
  - Total cobrado
  - Método de pago
  - Cambio (si fue efectivo)
- Botones:
  - "Imprimir ticket" (opcional)
  - "Nueva venta" (primario)
- Al hacer clic en "Nueva venta", cerrar modal y dejar POS listo para siguiente orden

**Manejo de Errores:**
- Si hay error al procesar pago, mostrar toast: "Error al procesar el pago. Por favor, intenta de nuevo"
- El modal permanece abierto con los datos ingresados
- Los productos permanecen en el carrito

**Cancelar Pago:**
- Al hacer clic en "Cancelar", cerrar modal sin procesar pago
- Los productos permanecen en el carrito
- No se crea orden ni registro de venta

**Atajos de Teclado:**
- En modal de pago, Enter: Intentar completar pago
- Escape: Cancelar y cerrar modal

### Escenarios

1. **Pago en efectivo con monto exacto**: Usuario tiene orden de $34.22, hace clic en "Procesar pago", selecciona "Efectivo", ingresa $34.22, ve "Monto exacto", hace clic en "Completar pago", ve modal de confirmación "¡Venta completada!"
2. **Pago en efectivo con cambio**: Usuario tiene orden de $34.22, selecciona "Efectivo", ingresa $50.00, el sistema muestra "Cambio: $15.78" en verde, completa pago exitosamente
3. **Pago en efectivo monto insuficiente**: Usuario ingresa $30.00 para orden de $34.22, ve mensaje "Monto insuficiente" en rojo, el botón "Completar pago" está deshabilitado
4. **Cambio calculado en tiempo real**: Usuario escribe "$5" (total es $34.22), ve "Monto insuficiente", sigue escribiendo hasta "$50", el cambio actualiza en tiempo real a "$15.78"
5. **Pago con tarjeta**: Usuario selecciona "Tarjeta", ve mensaje "Procesa el pago en tu terminal y confirma", checkbox "Confirmo que el pago fue autorizado", marca checkbox, hace clic en "Completar pago"
6. **Tarjeta sin confirmar**: Usuario selecciona "Tarjeta", no marca checkbox, el botón "Completar pago" permanece deshabilitado
7. **Cancelar pago**: Usuario abre modal de pago, ingresa datos, hace clic en "Cancelar", el modal se cierra, los productos permanecen en el carrito
8. **Modal de confirmación con detalles**: Usuario completa pago de $34.22 en efectivo con $50, ve modal "¡Venta completada! Orden #012", Total: $34.22, Método: Efectivo, Cambio: $15.78
9. **Nueva venta desde confirmación**: Usuario ve modal de confirmación, hace clic en "Nueva venta", el modal se cierra, el carrito está vacío listo para siguiente orden
10. **Error al procesar pago**: Usuario intenta completar pago pero hay error de red, aparece toast "Error al procesar el pago", el modal permanece abierto con los datos, usuario reintenta exitosamente
11. **Carrito vacío no permite procesar**: Usuario no tiene productos en carrito, el botón "Procesar pago" está deshabilitado y opaco
12. **Spinner durante procesamiento**: Usuario hace clic en "Completar pago", el botón muestra spinner y texto "Procesando...", campos quedan deshabilitados, después de 1-2 segundos muestra confirmación
13. **Orden cerrada automáticamente**: Usuario completa pago, el sistema crea orden con número secuencial y estado "Cerrada" automáticamente
14. **Atajo Enter en modal**: Usuario ingresa monto en efectivo suficiente, presiona Enter, el pago se procesa automáticamente (igual que hacer clic en botón)
15. **Atajo Escape cancela**: Usuario abre modal de pago, presiona tecla Escape, el modal se cierra sin procesar

---