# Historias de Usuario - Órdenes (Core)
## MVP SaaS Administración de Restaurantes

---

## HU-018: Ver Lista de Órdenes en Tiempo Real

### Descripción
Como usuario (Owner o Cajero), quiero ver todas las órdenes del restaurante en tiempo real para monitorear el flujo de trabajo y gestionar los pedidos activos eficientemente.

### Criterios de Aceptación

**Estructura de la Página:**
- La página muestra un título "Órdenes" en la parte superior
- Incluye un botón primario "Nueva orden" en la esquina superior derecha
- Incluye filtros rápidos por estado en la parte superior (tabs o pills)
- El contenido principal muestra una tabla/lista de órdenes
- Si no hay órdenes, mostrar estado vacío con mensaje "No hay órdenes registradas" y botón "Crear primera orden"

**Filtros por Estado:**
- Tabs/pills horizontales:
  - "Todas" (por defecto, muestra todas las órdenes)
  - "Pendiente" (badge con número de órdenes pendientes)
  - "Preparación" (badge con número en preparación)
  - "Lista" (badge con número listas)
  - "Cerrada" (órdenes completadas)
- Al hacer clic en un filtro, la lista se actualiza mostrando solo órdenes de ese estado
- El filtro activo se destaca visualmente

**Tabla/Lista de Órdenes:**
- Columnas visibles:
  - Número de orden (ej: #001, #002)
  - Estado (badge con color distintivo)
  - Hora (hora de creación, formato 12h: "10:30 AM")
  - Items (número de productos, ej: "3 items")
  - Total (formato moneda)
  - Notas (ícono si tiene notas)
  - Acciones (botón ver detalle)
- Cada fila es clickeable para abrir el detalle
- Las órdenes se ordenan por hora de creación (más reciente primero)

**Badges de Estado:**
- Pendiente: Color naranja/amarillo
- Preparación: Color azul
- Lista: Color verde
- Cerrada: Color gris

**Actualización en Tiempo Real:**
- Las órdenes se actualizan automáticamente cada 10-15 segundos
- Cuando hay un cambio (nueva orden, cambio de estado), mostrar actualización suave sin recargar toda la página
- Indicador visual discreto cuando se actualiza (pequeño ícono pulsante o texto "Actualizado hace X segundos")

**Botón de Actualización Manual:**
- Incluir botón de refresh en la parte superior
- Al hacer clic, actualizar inmediatamente la lista de órdenes
- Mostrar animación de loading durante la actualización

**Detalle Rápido en Fila:**
- Cada fila muestra información resumida
- Número de items: "3 items"
- Total: "$45.50"
- Si tiene notas, mostrar ícono de nota con tooltip del contenido al hacer hover

**Estados de Carga:**
- Al cargar la página por primera vez, mostrar skeleton loader con estructura de tabla
- La carga inicial debe completarse en menos de 2 segundos

**Manejo de Errores:**
- Si hay error al cargar órdenes, mostrar mensaje: "Error al cargar órdenes" con botón "Reintentar"
- Si falla la actualización automática, seguir mostrando datos anteriores y permitir actualización manual

**Paginación:**
- Si hay más de 50 órdenes, implementar paginación
- Mostrar selector de "Elementos por página": 25, 50, 100
- Mostrar información: "Mostrando 1-25 de 100 órdenes"
- Por defecto, mostrar últimas 50 órdenes

**Filtro por Fecha:**
- Dropdown para filtrar por fecha:
  - "Hoy" (por defecto)
  - "Ayer"
  - "Últimos 7 días"
  - "Este mes"
  - "Personalizado" (abre selector de rango de fechas)
- Al cambiar fecha, actualizar la lista de órdenes

**Búsqueda Rápida:**
- Campo de búsqueda con placeholder "Buscar orden..."
- Búsqueda por número de orden (ej: "001", "#001")
- Búsqueda en tiempo real mientras se escribe (debounce de 300ms)
- Limpiar búsqueda con botón X dentro del campo

**Responsive Design:**
- En desktop (>1024px): Tabla completa con todas las columnas
- En tablet (768px-1024px): Tabla con scroll horizontal
- En mobile (<768px): Convertir en cards verticales, cada card muestra número, estado, hora, total y botón ver detalle

**Permisos:**
- Esta página es accesible tanto para Owner como para Cajero
- Ambos roles ven la misma información

### Escenarios

1. **Ver lista con órdenes activas**: Usuario accede a `/orders`, ve tabla con 12 órdenes mostrando número, estado, hora, items, total y botones de acción
2. **Estado vacío sin órdenes**: Usuario accede por primera vez en el día, ve mensaje "No hay órdenes registradas" con botón "Crear primera orden"
3. **Filtrar por Pendiente**: Usuario hace clic en tab "Pendiente", la lista muestra solo 5 órdenes con estado Pendiente
4. **Filtrar por Preparación**: Usuario hace clic en tab "Preparación", ve 3 órdenes en preparación
5. **Volver a ver Todas**: Usuario hace clic en tab "Todas", la lista vuelve a mostrar todas las órdenes
6. **Actualización automática**: Usuario tiene lista abierta, después de 15 segundos aparece una nueva orden automáticamente sin refresh manual
7. **Actualización manual**: Usuario hace clic en botón de refresh, ve animación de loading por 1 segundo, la lista se actualiza con datos frescos
8. **Buscar orden por número**: Usuario escribe "005" en búsqueda, la lista muestra solo la orden #005
9. **Limpiar búsqueda**: Usuario hace clic en X del campo de búsqueda, la búsqueda se limpia, vuelve a mostrar todas las órdenes
10. **Filtrar por fecha - Hoy**: Usuario selecciona "Hoy" en filtro de fecha, ve solo órdenes del día actual
11. **Filtrar por fecha - Últimos 7 días**: Usuario selecciona "Últimos 7 días", ve órdenes de la última semana
12. **Click en fila abre detalle**: Usuario hace clic en cualquier parte de la fila de orden #008, es redirigido a página de detalle `/orders/008`
13. **Ver tooltip de notas**: Orden #003 tiene notas, usuario hace hover sobre ícono de nota, ve tooltip con el contenido de la nota
14. **Paginación con muchas órdenes**: Hay 150 órdenes, la tabla muestra primeras 25 con paginación, usuario hace clic en página 2, ve órdenes 26-50
15. **Error al cargar**: Hay error de red, usuario ve mensaje "Error al cargar órdenes" con botón "Reintentar", hace clic y los datos cargan correctamente
16. **Vista en mobile**: Usuario accede desde teléfono, ve órdenes como cards verticales con información resumida
17. **Badge de estado con conteo**: Tab "Pendiente" muestra badge "5" indicando hay 5 órdenes pendientes
18. **Indicador de actualización**: En esquina superior aparece texto "Actualizado hace 10 segundos" que se actualiza continuamente
19. **Click en Nueva orden**: Usuario hace clic en "Nueva orden", es redirigido al POS `/pos`

---

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

## HU-020: Cambiar Estado de Orden

### Descripción
Como usuario (Owner o Cajero), quiero cambiar el estado de las órdenes para reflejar el progreso en la preparación y entrega de los pedidos.

### Criterios de Aceptación

**Flujo de Estados:**
- El ciclo de estados es lineal: Pendiente → Preparación → Lista → Cerrada
- No se puede saltar estados (ej: de Pendiente a Lista)
- No se puede retroceder estados (ej: de Preparación a Pendiente)
- Una vez Cerrada, la orden no puede cambiar de estado

**Cambio de Estado desde Lista de Órdenes:**
- En cada fila de la tabla, incluir dropdown o botones rápidos para cambiar estado
- Mostrar solo la siguiente acción disponible según estado actual:
  - Pendiente: Botón "Iniciar preparación"
  - Preparación: Botón "Marcar como lista"
  - Lista: Botón "Cerrar orden"
  - Cerrada: No mostrar botones

**Cambio de Estado desde Detalle:**
- En la página de detalle, mostrar botón grande destacado para el siguiente estado
- El botón debe ser visualmente prominente y fácil de identificar

**Modal de Confirmación:**
- Al hacer clic en cualquier botón de cambio de estado, abrir modal de confirmación
- Título: "¿Cambiar estado de orden?"
- Mensaje según acción:
  - "¿Iniciar preparación de orden #XXX?"
  - "¿Marcar orden #XXX como lista?"
  - "¿Cerrar orden #XXX?"
- Botones:
  - "Cancelar" (secundario)
  - "Confirmar" (primario)

**Comportamiento del Cambio:**
- Al confirmar, mostrar spinner en el botón
- Si el cambio es exitoso:
  - Actualizar el badge de estado inmediatamente
  - Mostrar toast de confirmación: "Orden actualizada exitosamente"
  - Si está en lista de órdenes, actualizar la fila
  - Si está en detalle, actualizar toda la vista
  - Actualizar contadores en los tabs de filtros

**Manejo de Errores:**
- Si hay error al cambiar estado, mostrar toast: "No se pudo actualizar la orden. Por favor, intenta de nuevo"
- El estado permanece en el valor anterior
- El modal permanece abierto para permitir reintentos

**Validación de Estado Actual:**
- Antes de cambiar, validar en backend que la orden está en el estado esperado
- Esto previene conflictos si múltiples usuarios cambian la misma orden simultáneamente
- Si el estado ya cambió, mostrar error: "Esta orden ya fue actualizada por otro usuario"

**Timestamp de Cambios:**
- Registrar fecha y hora de cada cambio de estado
- Registrar usuario que realizó el cambio (Owner o Cajero)
- Esta información se usa para el historial de estados

**Cambios Masivos (en Lista):**
- Permitir seleccionar múltiples órdenes con checkbox
- Botón "Cambiar estado" habilitado solo si todas las órdenes seleccionadas están en el mismo estado
- Al hacer clic, abrir modal: "¿Cambiar estado de X órdenes?"
- Aplicar cambio a todas las órdenes seleccionadas simultáneamente

**Indicadores Visuales:**
- Al cambiar estado en la lista, animar la transición del badge de color
- Si la orden se mueve a otro filtro (ej: de Pendiente a Preparación), removerla de la vista con animación de salida

**Atajos de Teclado (Opcional):**
- En detalle de orden, permitir atajos:
  - "P" para Iniciar preparación
  - "L" para Marcar como lista
  - "C" para Cerrar orden
- Mostrar hints de atajos en los botones

### Escenarios

1. **Cambiar de Pendiente a Preparación desde lista**: Usuario hace clic en "Iniciar preparación" de orden #005, ve modal de confirmación, hace clic en "Confirmar", el badge cambia de naranja a azul, aparece toast "Orden actualizada exitosamente"
2. **Cambiar de Preparación a Lista desde detalle**: Usuario en detalle de orden #003 hace clic en botón "Marcar como lista", confirma en modal, el badge cambia a verde, toast confirma cambio
3. **Cambiar de Lista a Cerrada**: Usuario hace clic en "Cerrar orden", confirma, el badge cambia a gris, la orden se marca como completada
4. **Cancelar cambio de estado**: Usuario hace clic en "Iniciar preparación", ve modal, hace clic en "Cancelar", el modal se cierra sin cambios, el estado permanece en Pendiente
5. **Error al cambiar estado**: Usuario intenta cambiar estado pero hay error de red, aparece toast "No se pudo actualizar la orden", el estado permanece sin cambios
6. **Conflicto de estado**: Usuario A intenta cambiar orden #005 a Preparación, pero usuario B ya la cambió, usuario A ve error "Esta orden ya fue actualizada por otro usuario"
7. **Orden desaparece de vista filtrada**: Vista filtrada en "Pendiente" muestra 5 órdenes, usuario cambia una a Preparación, la orden desaparece de la vista con animación
8. **Actualización de contadores**: Tab "Pendiente" muestra "5", usuario cambia una orden a Preparación, el contador de "Pendiente" cambia a "4" y "Preparación" aumenta de "2" a "3"
9. **Cambio masivo de 3 órdenes**: Usuario selecciona 3 órdenes en estado Pendiente con checkboxes, hace clic en "Cambiar estado", selecciona "Preparación", confirma, las 3 órdenes cambian simultáneamente
10. **Intento de cambio masivo con estados mixtos**: Usuario selecciona 2 órdenes Pendientes y 1 en Preparación, el botón "Cambiar estado" permanece deshabilitado o muestra error
11. **Animación de transición**: Al cambiar estado, el badge anima el cambio de color suavemente de naranja a azul
12. **Historial actualizado**: Después de cambiar a Preparación, el historial en detalle muestra nueva entrada "En preparación - 11:45 AM - Cajero: María"
13. **Orden Cerrada sin botones**: Usuario abre detalle de orden Cerrada, no ve ningún botón de cambio de estado
14. **Atajo de teclado**: Usuario en detalle de orden Pendiente presiona "P", se abre modal de confirmación para iniciar preparación

---

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

## HU-022: Agregar y Editar Notas en Orden

### Descripción
Como usuario (Owner o Cajero), quiero agregar o editar notas en una orden para comunicar instrucciones especiales o información relevante sobre el pedido.

### Criterios de Aceptación

**Agregar Notas al Crear Orden:**
- Durante la creación de orden (en POS o mini-POS), incluir campo opcional "Notas"
- Placeholder: "Instrucciones especiales (opcional)"
- Textarea de 2-3 líneas
- Máximo 500 caracteres
- Contador de caracteres: "0/500"
- Las notas se guardan al crear la orden

**Editar Notas en Detalle de Orden:**
- En la página de detalle, mostrar sección "Notas"
- Si hay notas, mostrarlas en un área de texto editable
- Si no hay notas, mostrar botón "Agregar notas"
- Solo permitir editar notas si la orden NO está Cerrada

**Botón Agregar Notas:**
- Al hacer clic, convertir el área en textarea editable
- Placeholder: "Escribe notas sobre esta orden..."
- Botones: "Cancelar" (secundario) y "Guardar" (primario)

**Edición de Notas Existentes:**
- Al hacer clic en área de notas, convertir en textarea editable
- Mostrar botones: "Cancelar" y "Guardar cambios"
- Permitir modificar o borrar todo el contenido

**Validaciones:**
- Máximo 500 caracteres
- Si se excede, mostrar error: "Las notas no pueden superar 500 caracteres"
- Permitir guardar notas vacías (equivalente a eliminar notas)

**Guardar Notas:**
- Al hacer clic en "Guardar", mostrar spinner en el botón
- Si es exitoso:
  - Mostrar toast: "Notas actualizadas correctamente"
  - Volver a mostrar las notas en modo lectura
- Si hay error:
  - Mostrar toast: "No se pudieron guardar las notas. Intenta de nuevo"
  - Mantener textarea editable con el contenido

**Cancelar Edición:**
- Al hacer clic en "Cancelar", descartar cambios
- Volver a mostrar las notas en modo lectura (o mensaje "Sin notas" si no había)

**Restricción en Órdenes Cerradas:**
- Si la orden está Cerrada, mostrar notas en modo solo lectura
- No mostrar botón de edición
- Mostrar mensaje: "Las órdenes cerradas no pueden ser editadas"

**Indicador de Notas en Lista:**
- En la tabla de órdenes, mostrar ícono de nota si la orden tiene notas
- Al hacer hover sobre el ícono, mostrar tooltip con las primeras 100 caracteres de las notas
- Click en el ícono abre el detalle de la orden

**Formato de Notas:**
- Mantener saltos de línea si el usuario los ingresa
- Trimear espacios al inicio y final
- No permitir solo espacios en blanco

### Escenarios

1. **Agregar notas al crear orden**: Usuario crea nueva orden en POS, escribe en campo "Notas": "Sin cebolla, extra queso", crea la orden, al ver detalle las notas aparecen guardadas
2. **Crear orden sin notas**: Usuario crea orden sin escribir notas, la orden se crea exitosamente, en detalle aparece botón "Agregar notas"
3. **Agregar notas después de crear**: Usuario abre detalle de orden sin notas, hace clic en "Agregar notas", escribe "Cliente preguntó por tiempo de espera", hace clic en "Guardar", aparece toast "Notas actualizadas correctamente", las notas se muestran en modo lectura
4. **Editar notas existentes**: Usuario abre orden con notas "Sin cebolla", hace clic en área de notas, edita a "Sin cebolla, sin tomate", hace clic en "Guardar cambios", las notas se actualizan
5. **Cancelar edición de notas**: Usuario empieza a editar notas, hace cambios, hace clic en "Cancelar", las notas vuelven al contenido original sin guardar cambios
6. **Eliminar notas**: Usuario edita notas, borra todo el contenido, hace clic en "Guardar", las notas se eliminan, aparece botón "Agregar notas"
7. **Validación de máximo caracteres**: Usuario intenta escribir 550 caracteres en notas, al llegar a 500 se detiene la escritura o ve error "Las notas no pueden superar 500 caracteres"
8. **Contador de caracteres**: Usuario escribe notas, ve contador actualizar "45/500 caracteres"
9. **Notas en orden Cerrada**: Usuario abre detalle de orden Cerrada que tiene notas, las notas se muestran en modo solo lectura sin opción de editar
10. **Intento de editar orden Cerrada**: Usuario intenta hacer clic en notas de orden Cerrada, no pasa nada o ve mensaje "Las órdenes cerradas no pueden ser editadas"
11. **Ícono de notas en lista**: Orden #005 tiene notas, en la tabla aparece ícono de nota, usuario hace hover, ve tooltip con primeras líneas de las notas
12. **Click en ícono de notas**: Usuario hace clic en ícono de nota en la lista, es redirigido al detalle de la orden
13. **Error al guardar notas**: Usuario edita notas, hace clic en "Guardar", hay error de red, aparece toast "No se pudieron guardar las notas", el textarea permanece editable con el contenido
14. **Notas con saltos de línea**: Usuario escribe notas en múltiples líneas con Enter, guarda, al ver las notas se respetan los saltos de línea

---

## HU-023: Consultar Historial de Órdenes

### Descripción
Como usuario Owner, quiero consultar el historial completo de órdenes para revisar pedidos anteriores, analizar ventas o recuperar información de órdenes específicas.

### Criterios de Aceptación

**Acceso al Historial:**
- Desde la página de órdenes, el filtro de fecha permite seleccionar periodos anteriores
- Por defecto, la vista muestra "Hoy"
- Owner puede cambiar a "Ayer", "Últimos 7 días", "Este mes", o rango personalizado

**Filtro de Fecha Personalizado:**
- Al seleccionar "Personalizado", abrir date picker de rango
- Permite seleccionar fecha inicial y fecha final
- Botón "Aplicar" para ejecutar la búsqueda
- Botón "Limpiar" para volver a la vista de hoy

**Órdenes Históricas:**
- Mostrar todas las órdenes del periodo seleccionado
- Incluir órdenes en todos los estados (Pendiente, Preparación, Lista, Cerrada)
- Ordenar por fecha/hora de creación (más reciente primero)

**Información Visible:**
- Las mismas columnas que la vista principal
- Todas las órdenes históricas muestran su estado final
- Click en una orden abre su detalle completo

**Búsqueda en Historial:**
- El campo de búsqueda funciona también en historial
- Permite buscar por número de orden en cualquier fecha
- Buscar orden específica sin importar el rango de fecha activo

**Exportación de Historial (Opcional):**
- Botón "Exportar" para descargar historial en CSV
- El CSV incluye: número orden, fecha, hora, estado, items, total, notas
- El nombre del archivo incluye el rango de fechas (ej: "ordenes_2026-01-20_2026-01-26.csv")

**Paginación en Historial:**
- Si hay muchas órdenes, implementar paginación
- Mostrar selector de elementos por página: 25, 50, 100
- Información de paginación: "Mostrando 1-25 de 200 órdenes"

**Estados de Carga:**
- Al cambiar rango de fecha, mostrar loading mientras se cargan órdenes
- Skeleton loaders durante la carga

**Manejo de Errores:**
- Si hay error al cargar historial, mostrar: "Error al cargar historial de órdenes" con botón "Reintentar"
- Si el rango de fechas es inválido (fecha final antes de inicial), mostrar error: "Rango de fechas inválido"

**Estadísticas Rápidas del Periodo:**
- Mostrar resumen del periodo seleccionado:
  - Total de órdenes
  - Total de ventas
  - Ticket promedio
- Este resumen aparece en la parte superior de la lista

**Permisos:**
- Solo Owner puede acceder a historial completo
- Cajero solo puede ver órdenes del día actual

### Escenarios

1. **Ver órdenes de ayer**: Owner selecciona "Ayer" en filtro de fecha, ve todas las órdenes del día anterior con sus estados finales
2. **Ver últimos 7 días**: Owner selecciona "Últimos 7 días", ve todas las órdenes de la última semana, hay 150 órdenes con paginación
3. **Rango personalizado**: Owner selecciona "Personalizado", elige del 1 al 15 de enero, hace clic en "Aplicar", ve todas las órdenes de ese periodo
4. **Búsqueda en historial**: Owner está viendo historial de último mes, busca "025", encuentra orden #025 del 15 de enero
5. **Click en orden histórica**: Owner hace clic en orden #018 de hace 3 días, ve detalle completo con todos los productos y estado final "Cerrada"
6. **Estadísticas del periodo**: Owner selecciona "Últimos 7 días", ve en parte superior: "150 órdenes, $3,250.00 total ventas, $21.67 ticket promedio"
7. **Exportar historial**: Owner selecciona "Este mes", hace clic en "Exportar", descarga archivo "ordenes_2026-01-01_2026-01-26.csv" con todas las órdenes del mes
8. **Volver a vista de hoy**: Owner está viendo historial, hace clic en "Hoy" en filtro de fecha, vuelve a ver solo órdenes del día actual
9. **Rango inválido**: Owner selecciona fecha final antes de fecha inicial, ve error "Rango de fechas inválido", no se ejecuta la búsqueda
10. **Paginación en historial grande**: Owner selecciona "Este mes" con 500 órdenes, ve primeras 25 con paginación, navega a página 5 para ver órdenes 101-125
11. **Error al cargar historial**: Owner selecciona periodo, hay error de red, ve mensaje "Error al cargar historial de órdenes" con botón "Reintentar"
12. **Cajero intenta ver historial**: Usuario Cajero intenta cambiar a "Ayer", el sistema no permite o muestra mensaje "Solo puedes ver órdenes de hoy"

---

## Resumen de Estados de Órdenes

**Estados Disponibles:**
1. **Pendiente** - Orden creada, esperando preparación (Color: Naranja/Amarillo)
2. **Preparación** - Orden en proceso de preparación (Color: Azul)
3. **Lista** - Orden lista para entregar (Color: Verde)
4. **Cerrada** - Orden completada y entregada (Color: Gris)

**Flujo de Estados:**
```
Pendiente → Preparación → Lista → Cerrada
```

**Restricciones:**
- No se puede saltar estados
- No se puede retroceder estados
- Cerrada es estado final (no cambia)

---

## Navegación en Módulo de Órdenes

**URLs:**
- `/orders` → Lista de órdenes
- `/orders/[id]` → Detalle de orden específica

**Breadcrumbs:**
- `/orders`: Dashboard > Órdenes
- `/orders/[id]`: Dashboard > Órdenes > Orden #XXX

**Acciones desde Órdenes:**
- "Nueva orden" → Redirige a `/pos`
- Click en fila → Redirige a `/orders/[id]`
- "Volver a órdenes" → Redirige a `/orders`

---

## Notas Técnicas

**Actualización en Tiempo Real:**
- Implementar WebSocket o polling (cada 10-15 segundos)
- Actualizar lista cuando hay cambios en órdenes
- Notificar cambios si usuario tiene detalle abierto
- Optimizar para no hacer requests innecesarios

**Numeración de Órdenes:**
- Generar número secuencial automático
- Formato: #001, #002, #003...
- Considerar reinicio diario o secuencia continua
- Asegurar unicidad con índice en base de datos

**Cálculo de Totales:**
- Subtotal: Suma de (precio × cantidad) de todos los productos
- Impuesto: Subtotal × (% impuesto configurado)
- Total: Subtotal + Impuesto
- Almacenar totales calculados en la orden (no recalcular cada vez)

**Performance:**
- Índices en: estado, fecha_creacion, numero_orden
- Paginación para listas grandes
- Caché de órdenes activas (Pendiente, Preparación, Lista)
- Lazy loading de órdenes históricas

**Timestamps:**
- created_at: Fecha/hora de creación
- updated_at: Última actualización
- Timestamp por cada cambio de estado (opcional)
- Zona horaria del restaurante

**Soft Delete:**
- No implementar eliminación de órdenes
- Todas las órdenes se mantienen en el sistema
- Estado "Cerrada" es el estado final

**Permisos:**
- Owner: Acceso completo (crear, ver, editar, historial)
- Cajero: Crear, ver y cambiar estados (solo órdenes del día)
- Validar permisos en frontend y backend

**Canal:**
- Para MVP: Solo "Mostrador" (fijo)
- Preparar estructura para futuros canales (Delivery, Para llevar, etc.)
