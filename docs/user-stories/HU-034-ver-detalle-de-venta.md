## HU-034: Ver Detalle de Venta

### Descripción
Como usuario Owner, quiero ver el detalle completo de una venta específica para conocer todos los productos vendidos, el método de pago y otra información relevante de la transacción.

### Criterios de Aceptación

**Estructura de la Página:**
- La página muestra un título "Detalle de Venta - Orden #XXX" en la parte superior
- Incluye breadcrumb: Dashboard > Historial de Ventas > Orden #XXX
- Botón "Volver al historial" en la esquina superior izquierda
- Botón "Imprimir ticket" en la esquina superior derecha
- El contenido está dividido en secciones claramente definidas

**Sección: Información General**
- Card con información de la venta:
  - Número de orden (grande y destacado)
  - Estado: "Cerrada" (con badge gris)
  - Fecha y hora completa (formato: "26 de enero, 2026 - 10:30 AM")
  - Canal: "Mostrador" (fijo para MVP)
  - Método de pago (badge con color según tipo)
  - Información adicional según método de pago:
    - Efectivo: Monto recibido y cambio entregado
    - Tarjeta: Solo indicador de pago autorizado

**Ejemplo Información Efectivo:**
- "Método de pago: Efectivo"
- "Monto recibido: $50.00"
- "Cambio entregado: $15.78"

**Sección: Productos Vendidos**
- Lista detallada de productos con:
  - Nombre del producto
  - Cantidad (ej: "x2")
  - Precio unitario
  - Subtotal (cantidad × precio unitario)
- Si un producto fue eliminado del menú, mostrar su nombre original
- Los productos aparecen en el mismo orden que fueron agregados

**Sección: Resumen de Totales**
- Al final de la lista de productos:
  - Subtotal de productos
  - Impuesto (% y monto)
  - Total final (destacado, grande, en negrita)

**Formato de Moneda:**
- Usar moneda configurada en el sistema
- Formato con separador de miles y 2 decimales
- Consistente en toda la página

**Sección: Notas**
- Si la venta tiene notas, mostrarlas en un área destacada
- Título: "Notas"
- Contenido de las notas con formato (respetando saltos de línea)
- Si no hay notas, mostrar: "Sin notas adicionales"

**Botón Imprimir Ticket:**
- Al hacer clic, abrir vista de impresión optimizada
- La vista incluye:
  - Nombre del restaurante
  - Número de orden
  - Fecha y hora
  - Lista de productos con cantidades y precios
  - Totales
  - Método de pago
  - Notas (si existen)
  - Mensaje de agradecimiento (opcional)

**Vista de Impresión:**
- Formato optimizado para impresora de tickets (58mm o 80mm)
- Texto alineado correctamente
- Sin elementos de navegación
- Sin colores (blanco y negro)
- Fuente legible

**Navegación:**
- Al hacer clic en "Volver al historial", redirigir a `/sales`
- Mantener el filtro de fecha activo antes de abrir el detalle

**Estados de Carga:**
- Al cargar la página, mostrar skeleton loaders en cada sección
- La carga debe completarse en menos de 2 segundos

**Manejo de Errores:**
- Si la venta no existe, mostrar página 404: "Venta no encontrada" con botón "Volver al historial"
- Si hay error al cargar, mostrar: "Error al cargar detalle de venta" con botón "Reintentar"

**Información Inmutable:**
- Toda la información mostrada es de solo lectura
- No hay opciones de edición (la venta está cerrada y completada)
- Los datos son un registro histórico permanente

**Responsive Design:**
- En desktop: Layout organizado en cards y secciones claras
- En tablet/mobile: Secciones apiladas verticalmente con buen espaciado

**Permisos:**
- Solo Owner puede ver detalle de ventas
- Si Cajero intenta acceder, ver página 403

### Escenarios

1. **Ver detalle de venta completa**: Owner hace clic en orden #012 desde lista, ve página de detalle con toda la información: fecha/hora, método de pago "Efectivo", 5 productos, totales, y notas
2. **Venta con pago en efectivo**: Owner ve detalle de orden #008, método "Efectivo", muestra "Monto recibido: $50.00" y "Cambio entregado: $15.78"
3. **Venta con pago en tarjeta**: Owner ve detalle de orden #015, método "Tarjeta", muestra "Pago autorizado" sin detalles de cambio
4. **Venta sin notas**: Owner ve detalle de venta que no tiene notas, la sección "Notas" muestra "Sin notas adicionales"
5. **Venta con notas**: Owner ve detalle con notas "Sin cebolla, para llevar", las notas aparecen en área destacada respetando el formato
6. **Producto eliminado del menú**: Owner ve venta de hace 1 mes que incluye "Pizza Especial" (producto ya eliminado), el nombre aparece correctamente en la lista
7. **Cálculo de totales**: Venta tiene 2 Hamburguesas ($10 c/u = $20) y 1 Refresco ($3), detalle muestra Subtotal: $23.00, IVA 18%: $4.14, Total: $27.14
8. **Click en Volver al historial**: Owner hace clic en "Volver al historial", es redirigido a `/sales` manteniendo el filtro de fecha activo
9. **Click en Imprimir ticket**: Owner hace clic en "Imprimir", se abre vista de impresión optimizada con todos los detalles en formato de ticket
10. **Vista de impresión**: La vista muestra nombre del restaurante "Restaurante El Sabor", orden #012, fecha, productos con cantidades, totales, método de pago, y "¡Gracias por su compra!"
11. **Venta no encontrada**: Owner intenta acceder a `/sales/999` (no existe), ve página 404 "Venta no encontrada" con botón "Volver al historial"
12. **Error al cargar**: Hay error de red al cargar detalle, Owner ve mensaje "Error al cargar detalle de venta" con botón "Reintentar"
13. **Vista en mobile**: Owner accede desde teléfono, ve información apilada verticalmente con buen espaciado y legibilidad
14. **Producto con cantidad alta**: Venta incluye "Coca Cola x 12", el detalle muestra correctamente cantidad, precio unitario $3.00, subtotal $36.00
15. **Cajero intenta acceder**: Usuario Cajero intenta navegar a `/sales/001`, ve página 403 "No tienes permisos para acceder a esta sección"

---