# Historias de Usuario - Punto de Venta (POS)
## MVP SaaS Administración de Restaurantes

---

## HU-024: Interfaz Principal del POS

### Descripción
Como usuario (Owner o Cajero), quiero una interfaz de punto de venta clara y eficiente para tomar pedidos rápidamente y sin errores durante el servicio a clientes.

### Criterios de Aceptación

**Layout Principal:**
- La interfaz está dividida en 2 secciones principales:
  - Izquierda (60-65%): Catálogo de productos
  - Derecha (35-40%): Carrito de compra y resumen
- Diseño optimizado para tablet (landscape) y desktop
- Sin distracciones: interfaz limpia enfocada en velocidad

**Sección Izquierda: Catálogo de Productos**
- Título "Productos" en la parte superior
- Filtros por categoría en tabs o pills horizontales:
  - "Todas" (muestra todos los productos)
  - Cada categoría activa del sistema
- Barra de búsqueda rápida con placeholder "Buscar producto..."
- Grid de productos con cards:
  - Imagen del producto (o placeholder si no tiene)
  - Nombre del producto
  - Precio
  - Badge "No disponible" si el producto no está disponible
- Cards clickeables para agregar al carrito
- Scroll vertical si hay muchos productos

**Sección Derecha: Carrito y Resumen**
- Título "Orden actual" en la parte superior
- Lista de productos agregados mostrando:
  - Nombre del producto
  - Precio unitario
  - Controles de cantidad (-, cantidad, +)
  - Subtotal (precio × cantidad)
  - Botón eliminar (X o ícono de basura)
- Si el carrito está vacío, mostrar mensaje: "No hay productos agregados"
- Resumen de totales al final:
  - Subtotal
  - Impuesto (% y monto)
  - Total (destacado, grande)
- Botón principal "Procesar pago" (grande, color primario)
- Botón secundario "Limpiar carrito"

**Filtro por Categoría:**
- Al hacer clic en una categoría, mostrar solo productos de esa categoría
- La categoría activa se destaca visualmente
- "Todas" muestra todos los productos disponibles

**Búsqueda de Productos:**
- Búsqueda en tiempo real mientras se escribe (debounce de 300ms)
- Busca en nombre del producto
- Muestra solo productos que coincidan con la búsqueda
- Botón X para limpiar búsqueda

**Estado de Productos No Disponibles:**
- Productos marcados como "No disponible" se muestran con opacidad reducida
- Badge "No disponible" sobre la card
- No son clickeables (no se pueden agregar al carrito)
- Tooltip al hacer hover: "Este producto no está disponible actualmente"

**Productos de Categorías Inactivas:**
- No mostrar productos de categorías inactivas
- Solo mostrar productos de categorías activas

**Responsive Design:**
- Desktop (>1024px): Layout de 2 columnas (60/40)
- Tablet landscape (768px-1024px): Layout de 2 columnas ajustado
- Tablet portrait/Mobile (<768px): Carrito en modal que se abre con botón flotante "Ver carrito (X items)"

**Estados de Carga:**
- Al cargar el POS, mostrar skeleton loaders en grid de productos
- Al cargar categorías, mostrar skeleton en filtros
- La carga debe completarse en menos de 2 segundos

**Manejo de Errores:**
- Si hay error al cargar productos, mostrar: "Error al cargar productos" con botón "Reintentar"
- Si no hay productos disponibles, mostrar: "No hay productos disponibles para vender"

**Permisos:**
- Tanto Owner como Cajero tienen acceso completo al POS

### Escenarios

1. **POS con productos cargados**: Usuario accede a `/pos`, ve grid con 15 productos organizados por categorías, carrito vacío a la derecha con mensaje "No hay productos agregados"
2. **Filtrar por categoría Bebidas**: Usuario hace clic en tab "Bebidas", el grid muestra solo 8 productos de esa categoría
3. **Volver a ver todas las categorías**: Usuario hace clic en "Todas", el grid vuelve a mostrar todos los productos disponibles
4. **Buscar producto**: Usuario escribe "ham" en búsqueda, el grid muestra solo "Hamburguesa Clásica" y "Hamburguesa con Queso"
5. **Limpiar búsqueda**: Usuario hace clic en X del campo de búsqueda, el grid vuelve a mostrar todos los productos
6. **Producto no disponible**: Producto "Coca Cola" está marcado como no disponible, aparece con opacidad reducida y badge "No disponible", no se puede hacer clic
7. **Hover en producto no disponible**: Usuario hace hover sobre producto no disponible, ve tooltip "Este producto no está disponible actualmente"
8. **Carrito vacío**: Usuario ve mensaje "No hay productos agregados" en sección derecha, el botón "Procesar pago" está deshabilitado
9. **Vista en tablet landscape**: Usuario accede desde iPad en horizontal, ve layout de 2 columnas optimizado para pantalla
10. **Vista en mobile**: Usuario accede desde teléfono, ve grid de productos en pantalla completa, botón flotante "Ver carrito (0 items)" en parte inferior
11. **Error al cargar productos**: Hay error de red, usuario ve mensaje "Error al cargar productos" con botón "Reintentar", hace clic y los productos cargan correctamente
12. **Sin productos disponibles**: Todos los productos están marcados como no disponibles o eliminados, usuario ve mensaje "No hay productos disponibles para vender"
13. **Categorías inactivas ocultas**: Categoría "Promociones" está inactiva, no aparece en los filtros del POS y sus productos no se muestran

---

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

## HU-028: Cálculo Automático de Totales

### Descripción
Como usuario (Owner o Cajero), quiero que el sistema calcule automáticamente los totales de la orden incluyendo impuestos para tener el monto exacto a cobrar sin hacer cálculos manuales.

### Criterios de Aceptación

**Componentes del Cálculo:**
- Subtotal: Suma de (precio unitario × cantidad) de todos los productos
- Impuesto: Subtotal × (porcentaje de impuesto configurado)
- Total: Subtotal + Impuesto

**Porcentaje de Impuesto:**
- Usar el porcentaje configurado en `/settings` del restaurante
- Si no está configurado, usar 0% por defecto
- El porcentaje se aplica sobre el subtotal

**Visualización en Carrito:**
- Mostrar resumen de totales al final del carrito:
  - "Subtotal: $XX.XX"
  - "IVA (18%): $XX.XX" (mostrar porcentaje y monto)
  - "Total: $XX.XX" (destacado, más grande o en negrita)

**Formato de Moneda:**
- Usar el símbolo de moneda configurado en settings (ej: "$", "€", "S/")
- Formato con separador de miles y 2 decimales obligatorios
- Ejemplos: "$1,250.50", "€45.00", "S/123.75"

**Actualización Automática:**
- Los totales se recalculan inmediatamente cuando:
  - Se agrega un producto
  - Se cambia cantidad de un producto
  - Se elimina un producto
  - Se limpia el carrito
- No requiere botón "Calcular" ni acción manual

**Precisión de Cálculos:**
- Usar aritmética de punto flotante adecuada para dinero
- Redondear impuesto y total a 2 decimales
- Asegurar que la suma sea exacta (subtotal + impuesto = total)

**Carrito Vacío:**
- Si no hay productos, mostrar:
  - "Subtotal: $0.00"
  - "IVA (18%): $0.00"
  - "Total: $0.00"

**Ejemplo de Cálculo:**
- Producto 1: Hamburguesa × 2 = $20.00
- Producto 2: Coca Cola × 3 = $9.00
- Subtotal: $29.00
- IVA (18%): $5.22
- Total: $34.22

**Validación de Consistencia:**
- El total mostrado en el carrito debe coincidir exactamente con el total en el modal de pago
- El total guardado en la orden debe ser idéntico al calculado en el POS

### Escenarios

1. **Cálculo con un producto**: Usuario agrega Hamburguesa ($10), el carrito muestra Subtotal: $10.00, IVA (18%): $1.80, Total: $11.80
2. **Cálculo con múltiples productos**: Usuario agrega Hamburguesa × 2 ($20) y Coca Cola × 3 ($9), Subtotal: $29.00, IVA: $5.22, Total: $34.22
3. **Actualización al cambiar cantidad**: Usuario tiene Hamburguesa × 1 (Total: $11.80), incrementa a × 3, inmediatamente el Total actualiza a $35.40 (sin delay)
4. **Actualización al eliminar producto**: Usuario tiene 3 productos (Total: $50), elimina uno de $10, el Total actualiza automáticamente considerando nuevo subtotal e impuesto
5. **Carrito vacío muestra ceros**: Usuario limpia carrito, el resumen muestra Subtotal: $0.00, IVA: $0.00, Total: $0.00
6. **Impuesto 0% configurado**: Restaurante tiene impuesto configurado en 0%, usuario agrega productos por $25, el resumen muestra Subtotal: $25.00, IVA (0%): $0.00, Total: $25.00
7. **Formato con separador de miles**: Usuario construye orden de $1,250.75, el Total se muestra como "$1,250.75" con separador de miles
8. **Precisión en decimales**: Usuario tiene orden donde el 18% da un resultado con muchos decimales (ej: $10.7777...), el sistema redondea correctamente a $10.78
9. **Consistencia con modal de pago**: Usuario ve Total: $34.22 en carrito, abre modal de pago, el total mostrado es exactamente $34.22
10. **Cálculo con 10 productos**: Usuario agrega 10 productos diferentes con varias cantidades, el sistema calcula correctamente la suma de todos los subtotales, aplica impuesto y muestra total preciso

---

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

## HU-031: Navegación y Persistencia en el POS

### Descripción
Como usuario (Owner o Cajero), quiero que el POS mantenga mi progreso si navego accidentalmente a otra página y que sea fácil volver a empezar una nueva venta.

### Criterios de Aceptación

**Persistencia del Carrito:**
- El contenido del carrito se guarda en localStorage/sessionStorage
- Si el usuario navega a otra página y vuelve, el carrito mantiene los productos
- La persistencia incluye:
  - Productos agregados
  - Cantidades
  - Notas
- La persistencia NO incluye el estado del modal de pago

**Advertencia al Navegar:**
- Si el carrito tiene productos y el usuario intenta navegar a otra página, mostrar modal de confirmación
- Título: "¿Salir del punto de venta?"
- Mensaje: "Tienes una orden en progreso. Si sales, los productos se mantendrán para cuando vuelvas."
- Botones:
  - "Cancelar" (permanece en POS)
  - "Salir" (navega a la página solicitada)
- Esta advertencia NO aparece si el carrito está vacío

**Restauración al Volver:**
- Al volver a `/pos`, restaurar automáticamente:
  - Todos los productos con sus cantidades
  - Las notas ingresadas
  - Los totales calculados
- Mostrar notificación temporal: "Orden en progreso restaurada"

**Limpiar Carrito:**
- Botón "Limpiar carrito" elimina todos los productos y notas
- También limpia la persistencia en localStorage
- Mostrar confirmación antes de limpiar (modal)

**Nueva Venta:**
- Después de completar un pago, el carrito se limpia automáticamente
- La persistencia se limpia
- El POS queda listo para nueva orden

**Timeout de Persistencia (Opcional):**
- Si el carrito persiste por más de 24 horas sin actividad, limpiarlo automáticamente
- Al volver después de 24h, mostrar mensaje: "La orden anterior expiró. Puedes comenzar una nueva venta."

**Botón Nueva Venta:**
- Incluir botón "Nueva venta" o "Limpiar" visible en la parte superior del POS
- Color secundario o neutral
- Al hacer clic, si hay productos, mostrar confirmación

**Acceso Directo desde Otras Páginas:**
- Desde el dashboard, botón rápido "Crear orden" que redirige al POS
- Desde órdenes, botón "Nueva orden" que redirige al POS
- Si hay carrito persistido, restaurarlo automáticamente

### Escenarios

1. **Navegación accidental con carrito**: Usuario tiene 5 productos en carrito, hace clic en "Órdenes" en el menú, ve modal "¿Salir del punto de venta?" con mensaje, hace clic en "Cancelar", permanece en POS
2. **Salir con orden en progreso**: Usuario confirma salir del POS, navega a Dashboard, vuelve al POS, el carrito se restaura automáticamente con los 5 productos originales
3. **Navegación con carrito vacío**: Usuario no tiene productos en carrito, navega a otra página, no aparece advertencia, navega libremente
4. **Notificación de restauración**: Usuario vuelve a POS después de 5 minutos, ve notificación temporal "Orden en progreso restaurada" durante 3 segundos
5. **Notas también se restauran**: Usuario tenía productos y notas "Sin cebolla", salió y volvió, tanto productos como notas están intactos
6. **Limpiar carrito con confirmación**: Usuario hace clic en "Limpiar carrito", ve modal de confirmación, hace clic en "Limpiar", todos los productos y notas se eliminan
7. **Nueva venta limpia todo**: Usuario completa pago exitosamente, hace clic en "Nueva venta", el carrito está completamente vacío, no hay persistencia anterior
8. **Persistencia entre sesiones**: Usuario cierra pestaña del navegador con carrito lleno, abre nueva pestaña y va al POS, el carrito se restaura (si usa localStorage)
9. **Expiración después de 24h**: Usuario deja carrito con productos, vuelve después de 2 días, ve mensaje "La orden anterior expiró", el carrito está vacío
10. **Botón Nueva Venta desde header**: Usuario tiene orden en progreso, hace clic en "Nueva venta" en header, ve confirmación, confirma, el carrito se limpia
11. **Acceso desde Dashboard**: Usuario en Dashboard hace clic en "Crear orden", es redirigido a POS, si había carrito persistido se restaura con notificación

---

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
