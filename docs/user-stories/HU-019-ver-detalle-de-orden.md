## HU-019: Ver Detalle de Orden

### Descripción
Como usuario (Owner o Cajero), quiero ver el detalle completo de una orden para conocer todos los productos, el estado actual, y poder gestionar la orden.

### Criterios de Aceptación

**Estructura de la Página:**
- La página muestra un título "Orden #XXX" en la parte superior
- Incluye breadcrumb: Dashboard > Órdenes > Orden #XXX
- Botón "Volver a órdenes" en la esquina superior izquierda
- El contenido está dividido en secciones claramente definidas

**Sección: Información de la Orden**
- Card con información general:
  - Número de orden (grande y destacado)
  - Estado actual con badge de color
  - Fecha y hora de creación (formato: "26 de enero, 2026 - 10:30 AM")
  - Canal: "Mostrador" (fijo para MVP)
  - Tiempo transcurrido (ej: "Hace 15 minutos", "Hace 2 horas")

**Sección: Control de Estado**
- Botones de acción según estado actual:
  - Si está "Pendiente": Botón "Iniciar preparación" (cambia a Preparación)
  - Si está "Preparación": Botón "Marcar como lista" (cambia a Lista)
  - Si está "Lista": Botón "Cerrar orden" (cambia a Cerrada)
  - Si está "Cerrada": No mostrar botones de cambio de estado
- Los botones son grandes y destacados para fácil acceso
- Al hacer clic, mostrar modal de confirmación

**Sección: Productos de la Orden**
- Lista de productos con:
  - Nombre del producto
  - Cantidad (ej: "x2")
  - Precio unitario
  - Subtotal (cantidad × precio unitario)
- Al final, mostrar resumen:
  - Subtotal de productos
  - Impuesto (% configurado, ej: "IVA 18%: $5.40")
  - Total final (grande y destacado)

**Formato de Precios:**
- Usar moneda configurada en el sistema
- Formato con separador de miles y 2 decimales (ej: "$45.50")
- Total final en negrita o tamaño mayor

**Sección: Notas de la Orden**
- Mostrar notas si existen
- Si no hay notas, mostrar mensaje: "Sin notas adicionales"
- Las notas aparecen en un área de texto con borde distintivo

**Botón de Impresión:**
- Incluir botón "Imprimir" en la parte superior
- Al hacer clic, abrir vista de impresión optimizada
- La vista de impresión incluye: número de orden, fecha/hora, productos, total, notas

**Estados de Carga:**
- Al cargar la página, mostrar skeleton loaders en cada sección
- La carga debe completarse en menos de 2 segundos

**Manejo de Errores:**
- Si la orden no existe, mostrar página 404: "Orden no encontrada" con botón "Volver a órdenes"
- Si hay error al cargar, mostrar mensaje: "Error al cargar orden" con botón "Reintentar"

**Actualización en Tiempo Real:**
- Si otro usuario cambia el estado de la orden, actualizar automáticamente la vista
- Mostrar notificación: "Esta orden fue actualizada" con botón "Recargar"
- Al recargar, mostrar el nuevo estado

**Historial de Estados (Opcional pero Recomendado):**
- Timeline mostrando cambios de estado:
  - "Creada - 10:30 AM"
  - "En preparación - 10:35 AM"
  - "Lista - 10:50 AM"
  - "Cerrada - 11:00 AM"
- Mostrar usuario que realizó cada cambio (si aplica)

**Responsive Design:**
- En desktop: Layout de 2 columnas (información + control de estado a la izquierda, productos a la derecha)
- En tablet/mobile: Layout vertical apilado (información arriba, productos abajo)

**Permisos:**
- Tanto Owner como Cajero pueden ver detalle de órdenes
- Ambos pueden cambiar estados de órdenes

### Escenarios

1. **Ver detalle de orden Pendiente**: Usuario hace clic en orden #005 con estado Pendiente, ve página de detalle con toda la información, productos listados, total, y botón "Iniciar preparación"
2. **Ver detalle de orden en Preparación**: Usuario abre orden #003 que está en Preparación, ve información completa y botón "Marcar como lista"
3. **Ver detalle de orden Lista**: Usuario abre orden #008 que está Lista, ve detalle y botón "Cerrar orden"
4. **Ver detalle de orden Cerrada**: Usuario abre orden #001 que está Cerrada, ve toda la información pero sin botones de cambio de estado
5. **Orden con notas**: Usuario ve detalle de orden que tiene nota "Sin cebolla", la nota aparece en sección destacada
6. **Orden sin notas**: Usuario ve detalle de orden sin notas, la sección muestra "Sin notas adicionales"
7. **Click en Iniciar preparación**: Usuario en detalle de orden Pendiente hace clic en "Iniciar preparación", ve modal de confirmación "¿Cambiar estado a Preparación?", confirma, el badge cambia a "Preparación", aparece toast "Orden actualizada"
8. **Click en Marcar como lista**: Usuario en orden en Preparación hace clic en "Marcar como lista", confirma en modal, el estado cambia a "Lista"
9. **Click en Cerrar orden**: Usuario en orden Lista hace clic en "Cerrar orden", confirma, la orden cambia a "Cerrada", los botones de acción desaparecen
10. **Cálculo de total**: Orden tiene 2 Hamburguesas ($10 c/u) y 1 Refresco ($3), el subtotal muestra $23.00, impuesto 18% muestra $4.14, total final muestra $27.14
11. **Click en Volver a órdenes**: Usuario hace clic en "Volver a órdenes", es redirigido a `/orders`
12. **Click en Imprimir**: Usuario hace clic en "Imprimir", se abre vista de impresión con formato limpio mostrando todos los detalles de la orden
13. **Orden no existe**: Usuario intenta acceder a `/orders/999` (no existe), ve página 404 "Orden no encontrada" con botón "Volver a órdenes"
14. **Error al cargar**: Hay error de red al cargar orden, usuario ve mensaje "Error al cargar orden" con botón "Reintentar", hace clic y los datos cargan
15. **Actualización por otro usuario**: Usuario A tiene orden #005 abierta, usuario B cambia su estado, usuario A ve notificación "Esta orden fue actualizada" con botón "Recargar", recarga y ve el nuevo estado
16. **Vista en mobile**: Usuario accede desde teléfono, ve información apilada verticalmente, botones de acción grandes y fáciles de tocar
17. **Historial de estados**: Usuario ve timeline con "Creada - 10:30 AM", "En preparación - 10:35 AM", "Lista - 10:50 AM"
18. **Tiempo transcurrido actualizado**: Al cargar orden creada hace 5 minutos, muestra "Hace 5 minutos", después de 10 minutos muestra "Hace 15 minutos"

---