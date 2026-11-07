## HU-030: Agregar Notas a la Orden desde POS

### Descripción
Como usuario (Owner o Cajero), quiero agregar notas a la orden desde el POS para registrar instrucciones especiales del cliente antes de procesar el pago.

### Criterios de Aceptación

**Campo de Notas en POS:**
- Ubicado en el área del carrito, debajo de la lista de productos
- Antes del resumen de totales
- Label: "Notas" o "Instrucciones especiales"
- Textarea de 2-3 líneas
- Placeholder: "Ej: Sin cebolla, para llevar, etc. (opcional)"
- Contador de caracteres: "0/500"

**Edición de Notas:**
- El campo es editable en cualquier momento mientras se construye la orden
- Máximo 500 caracteres
- Al alcanzar el límite, no permitir más escritura
- Si se excede en pegado, truncar a 500 caracteres

**Notas en Modal de Pago:**
- Al abrir modal de pago, mostrar las notas si existen
- Sección "Notas:" con el contenido de las notas
- Las notas son solo lectura en el modal (no editables)
- Si no hay notas, no mostrar la sección

**Notas en Orden Creada:**
- Al completar el pago, las notas se guardan en la orden
- En el detalle de la orden, las notas son visibles
- Las notas se pueden editar después desde el detalle de la orden (solo si no está cerrada)

**Persistencia de Notas:**
- Las notas permanecen en el carrito mientras se agregan/quitan productos
- Las notas NO se limpian automáticamente al completar venta
- Al iniciar nueva venta, limpiar también el campo de notas

**Formato de Notas:**
- Mantener saltos de línea si el usuario los ingresa
- Trimear espacios al inicio y final
- No permitir solo espacios en blanco

**Campo Opcional:**
- Las notas son completamente opcionales
- Se puede procesar pago sin notas
- No mostrar error o validación si está vacío

### Escenarios

1. **Agregar notas al construir orden**: Usuario agrega 3 productos, escribe en notas "Sin cebolla en la hamburguesa", abre modal de pago, ve las notas en la sección correspondiente
2. **Orden sin notas**: Usuario construye orden sin escribir notas, procesa pago exitosamente, la orden creada aparece sin notas
3. **Editar notas antes de pagar**: Usuario escribe "Sin tomate", agrega más productos, edita notas a "Sin tomate ni cebolla", procesa pago, la orden guarda la versión final
4. **Contador de caracteres**: Usuario escribe en notas, ve contador actualizar "47/500 caracteres", continúa escribiendo hasta "255/500"
5. **Límite de caracteres**: Usuario escribe 500 caracteres, intenta escribir más, el campo no permite más escritura
6. **Pegar texto largo**: Usuario copia texto de 800 caracteres, lo pega en notas, el sistema trunca automáticamente a 500 caracteres
7. **Notas con saltos de línea**: Usuario escribe notas en 3 líneas usando Enter, las notas se guardan respetando los saltos de línea
8. **Notas en orden cerrada**: Usuario completa pago con notas "Para llevar", abre detalle de orden #015, ve las notas guardadas correctamente
9. **Limpiar notas al iniciar nueva venta**: Usuario completa orden con notas, hace clic en "Nueva venta", el carrito queda vacío y el campo de notas también está vacío
10. **Notas permanecen al modificar carrito**: Usuario escribe notas, agrega productos, elimina productos, cambia cantidades, las notas permanecen intactas durante todo el proceso

---