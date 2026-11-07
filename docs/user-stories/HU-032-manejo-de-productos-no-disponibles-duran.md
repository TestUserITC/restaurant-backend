## HU-032: Manejo de Productos No Disponibles Durante Venta

### Descripción
Como usuario (Owner o Cajero), quiero que el sistema me alerte si un producto se vuelve no disponible mientras estoy construyendo una orden para evitar errores en el proceso de venta.

### Criterios de Aceptación

**Detección de Cambio de Estado:**
- Si un producto en el carrito cambia a "No disponible" (por acción de otro usuario), el sistema debe detectarlo
- La detección ocurre:
  - Al abrir el modal de pago
  - Durante la validación antes de procesar pago
  - Opcionalmente, en tiempo real con WebSocket/polling

**Alerta de Producto No Disponible:**
- Si se detecta producto no disponible en el carrito, mostrar modal de alerta
- Título: "Producto no disponible"
- Mensaje: "El siguiente producto ya no está disponible: [Nombre del producto]"
- Si son múltiples productos: "Los siguientes productos ya no están disponibles: [Lista]"
- Botones:
  - "Eliminar del carrito" (primario)
  - No permitir continuar con el pago hasta eliminar productos no disponibles

**Marcado Visual en Carrito:**
- Los productos no disponibles se muestran con:
  - Opacidad reducida
  - Texto tachado
  - Badge "No disponible" en rojo
  - Ícono de alerta
- El subtotal incluye una nota: "Este producto no está disponible"

**Botón Procesar Pago Deshabilitado:**
- Si hay productos no disponibles en el carrito, deshabilitar botón "Procesar pago"
- Tooltip al hacer hover: "Elimina los productos no disponibles para continuar"

**Eliminación Automática (Opcional):**
- Ofrecer botón "Eliminar productos no disponibles" en la alerta
- Al hacer clic, eliminar automáticamente todos los productos no disponibles
- Actualizar totales y permitir continuar con los productos restantes

**Validación al Procesar Pago:**
- Antes de crear la orden, validar en backend que todos los productos están disponibles
- Si alguno no está disponible, rechazar el pago y mostrar error
- Esta es una validación final de seguridad

**Actualización en Tiempo Real (Ideal):**
- Con WebSocket o polling corto, detectar cambios en disponibilidad de productos
- Actualizar visualmente el carrito si un producto se vuelve no disponible
- Mostrar notificación: "[Producto] ya no está disponible"

### Escenarios

1. **Producto se vuelve no disponible durante construcción**: Usuario tiene 3 productos en carrito, otro usuario marca "Coca Cola" como no disponible, usuario ve el producto en carrito con opacidad reducida y badge "No disponible"
2. **Alerta al abrir modal de pago**: Usuario construye orden con "Pizza", intenta procesar pago, al abrir modal ve alerta "Producto no disponible: Pizza", hace clic en "Eliminar del carrito", el producto se quita, puede continuar con los demás
3. **Múltiples productos no disponibles**: Usuario tiene 5 productos, 2 se vuelven no disponibles, ve alerta "Los siguientes productos ya no están disponibles: Pizza, Tacos", elimina ambos, continúa con los otros 3
4. **Botón pago deshabilitado**: Usuario tiene producto no disponible en carrito, el botón "Procesar pago" está deshabilitado, hace hover y ve tooltip "Elimina los productos no disponibles para continuar"
5. **Eliminar productos no disponibles**: Usuario ve alerta con 2 productos no disponibles, hace clic en "Eliminar productos no disponibles", ambos se quitan automáticamente del carrito, los totales se actualizan
6. **Validación final en backend**: Usuario intenta procesar pago, durante la validación backend detecta que un producto se volvió no disponible, rechaza el pago, usuario ve error y debe eliminar el producto
7. **Actualización en tiempo real**: Usuario tiene carrito con "Hamburguesa", otro usuario la marca no disponible, inmediatamente en el POS del primer usuario aparece la hamburguesa con badge "No disponible" y notificación
8. **Carrito solo con productos no disponibles**: Usuario tiene 2 productos, ambos se vuelven no disponibles, el carrito muestra ambos tachados, botón "Procesar pago" deshabilitado, usuario debe limpiar carrito

---

## Resumen del Flujo del POS

**Flujo Completo de Venta:**
```
1. Acceder a POS (/pos)
2. Agregar productos al carrito
3. Ajustar cantidades según necesidad
4. Agregar notas (opcional)
5. Hacer clic en "Procesar pago"
6. Seleccionar método de pago (Efectivo/Tarjeta)
7. Completar campos según método
8. Hacer clic en "Completar pago"
9. Ver confirmación de venta exitosa
10. Hacer clic en "Nueva venta"
11. Carrito limpio, listo para siguiente orden
```

**Métodos de Pago:**
- **Efectivo**: Requiere monto recibido, calcula cambio automáticamente
- **Tarjeta**: Requiere confirmación de pago autorizado (checkbox)

**Acciones Principales:**
- Agregar producto (click en card)
- Cambiar cantidad (+, -, edición directa)
- Eliminar producto (botón X)
- Limpiar carrito (con confirmación)
- Procesar pago (modal con validaciones)
- Nueva venta (limpiar todo)

---

## Navegación en POS

**URLs:**
- `/pos` → Interfaz del punto de venta

**Acceso al POS:**
- Desde menú lateral: "POS"
- Desde dashboard: Botón rápido "Crear orden"
- Desde órdenes: Botón "Nueva orden"

**Breadcrumb:**
- `/pos`: Dashboard > Punto de Venta

---

## Notas Técnicas

**Persistencia del Carrito:**
- Usar localStorage para persistir entre sesiones
- Estructura de datos: array de productos con { id, nombre, precio, cantidad }
- Incluir notas y timestamp
- Limpiar al completar venta
- Implementar expiración de 24 horas

**Cálculos de Precio:**
- Usar aritmética precisa para dinero (evitar problemas de punto flotante)
- Redondear a 2 decimales
- Validar consistencia entre frontend y backend

**Performance:**
- Lazy loading de imágenes de productos
- Virtualización de lista de productos si hay muchos
- Debounce en búsqueda (300ms)
- Optimizar recálculo de totales

**Validaciones:**
- Frontend: Validar antes de abrir modal de pago
- Backend: Validar disponibilidad de productos antes de crear orden
- Backend: Validar que precios no hayan cambiado
- Backend: Crear orden con estado "Cerrada" directamente

**Estados de Orden desde POS:**
- Las órdenes creadas desde POS se crean con estado "Cerrada" automáticamente
- No pasan por Pendiente/Preparación/Lista (flujo directo de pago)
- Canal: "Mostrador" (fijo)

**Accesibilidad:**
- Botones grandes para tablet/touch
- Controles de cantidad fáciles de tocar
- Alto contraste en elementos importantes
- Atajos de teclado para acciones frecuentes

**Optimización para Tablet:**
- Layout optimizado para tablet en landscape (1024x768)
- Botones con tamaño mínimo de 44x44px
- Espaciado adecuado entre elementos clickeables
- Scroll suave en lista de productos

**Seguridad:**
- Validar precios en backend (no confiar en frontend)
- Verificar disponibilidad de productos en tiempo real
- Validar que el total calculado coincida con servidor
- Logging de todas las transacciones