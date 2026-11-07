# Historias de Usuario - Dashboard Básico
## MVP SaaS Administración de Restaurantes

---

## HU-006: Dashboard para Usuario Owner

### Descripción
Como usuario con rol Owner, quiero ver un dashboard completo con los KPIs principales de mi restaurante para tener una visión general del estado del negocio y tomar decisiones informadas.

### Criterios de Aceptación

**Estructura y Contenido del Dashboard:**
- El dashboard muestra un título "Dashboard" en la parte superior
- El contenido está organizado en una grilla responsive con 4 cards de KPIs principales:
  - Ventas del día
  - Órdenes abiertas
  - Ticket promedio
  - Productos más vendidos (top 5)
- Cada card tiene un diseño consistente con título, valor principal, y contexto adicional

**Card: Ventas del Día**
- Título: "Ventas del día"
- Valor principal: Monto total de ventas del día actual en formato moneda con 2 decimales (ej: "$1,250.00")
- Icono representativo de dinero/ventas
- Texto secundario: Fecha actual (ej: "26 de enero, 2026")
- Si no hay ventas en el día, mostrar "$0.00"

**Card: Órdenes Abiertas**
- Título: "Órdenes abiertas"
- Valor principal: Número total de órdenes con estados "Pendiente", "Preparación" o "Lista" (ej: "5")
- Icono representativo de orden/documento
- Texto secundario: Desglose por estado (ej: "3 en preparación, 2 listas")
- Si no hay órdenes abiertas, mostrar "0" con texto "Sin órdenes abiertas"
- El card es clickeable y redirige a `/orders`

**Card: Ticket Promedio**
- Título: "Ticket promedio"
- Valor principal: Promedio del valor de las órdenes completadas del día en formato moneda (ej: "$25.00")
- Icono representativo de ticket/recibo
- Texto secundario: Número de ventas consideradas (ej: "Basado en 50 ventas")
- Si no hay ventas en el día, mostrar "$0.00" con texto "Sin ventas hoy"
- Cálculo: Total de ventas del día ÷ Número de órdenes cerradas del día

**Card: Productos Más Vendidos (Top 5)**
- Título: "Productos más vendidos"
- Contenido: Lista de los 5 productos más vendidos del día
- Cada producto muestra:
  - Posición (#1, #2, #3, #4, #5)
  - Nombre del producto (truncado si es muy largo, máximo 30 caracteres)
  - Cantidad vendida (ej: "25 vendidos")
- Si hay menos de 5 productos con ventas, mostrar solo los que tienen ventas
- Si no hay ventas del día, mostrar mensaje "Sin ventas registradas hoy"
- Los productos se ordenan por cantidad vendida (descendente)

**Estados de Carga:**
- Al cargar el dashboard, mostrar skeleton loaders en cada card mientras se obtienen los datos
- Los skeleton loaders deben tener el mismo tamaño y forma que los cards con datos
- La carga debe completarse en menos de 2 segundos en condiciones normales

**Actualización de Datos:**
- Los KPIs se calculan en tiempo real basados en el día actual (desde 00:00 hasta 23:59)
- Al cambiar de día (pasada la medianoche), los KPIs se reinician automáticamente
- Incluir botón de actualizar (icono de refresh) en la esquina superior derecha del dashboard
- Al hacer clic en actualizar, mostrar animación de loading y recargar todos los KPIs

**Manejo de Errores:**
- Si hay error al cargar algún KPI, mostrar mensaje de error en el card correspondiente: "Error al cargar datos"
- Incluir botón "Reintentar" en el card con error
- El error en un card no debe impedir que se muestren los demás

**Responsive Design:**
- En desktop (>1024px): Mostrar cards en grilla de 2x2 (Ventas y Órdenes arriba, Ticket y Productos abajo)
- En tablet (768px-1024px): Mostrar cards en grilla de 2x2 con menor espaciado
- En mobile (<768px): Mostrar cards apilados verticalmente, uno debajo del otro

**Navegación:**
- El dashboard es la página principal después de login (`/dashboard`)
- Al hacer clic en el card "Órdenes abiertas", redirigir a `/orders`
- Los demás cards no son clickeables

### Escenarios

1. **Dashboard con datos completos**: Owner accede al dashboard, ve Ventas del día "$1,250.00", Órdenes abiertas "5 (3 en preparación, 2 listas)", Ticket promedio "$25.00 (Basado en 50 ventas)", y Top 5 productos con sus cantidades
2. **Dashboard sin ventas del día**: Owner accede al dashboard a primera hora del día, ve Ventas "$0.00", Órdenes "0", Ticket "$0.00 - Sin ventas hoy", y "Sin ventas registradas hoy" en productos
3. **Dashboard con menos de 5 productos vendidos**: Solo 3 productos se han vendido en el día, el card muestra solo esos 3 productos con sus posiciones #1, #2, #3
4. **Click en Órdenes abiertas**: Owner hace clic en card "Órdenes abiertas", es redirigido a `/orders`
5. **Actualización manual de datos**: Owner hace clic en botón de refresh, ve animación de loading en todos los cards por 1 segundo, los datos se actualizan con valores nuevos
6. **Error al cargar ventas**: Hay error de red al obtener ventas del día, el card de ventas muestra "Error al cargar datos" con botón "Reintentar", los demás cards se cargan normalmente
7. **Reintentar después de error**: Owner ve error en card de ventas, hace clic en "Reintentar", el card muestra loading, se cargan correctamente los datos de ventas
8. **Carga inicial con skeleton**: Owner accede al dashboard, ve skeleton loaders en los 4 cards por 0.5 segundos, después se muestran los datos reales
9. **Dashboard en mobile**: Owner accede desde teléfono, ve los 4 cards apilados verticalmente, puede scrollear para ver todos
10. **Dashboard en tablet**: Owner accede desde tablet, ve los cards en grilla 2x2 con buen uso del espacio disponible
11. **Cambio de día automático**: Owner tiene dashboard abierto a las 23:59, a las 00:00 los KPIs se reinician automáticamente a 0 sin necesidad de refresh
12. **Ticket promedio con pocas ventas**: Solo hay 2 ventas en el día ($20 y $30), el ticket promedio muestra "$25.00 (Basado en 2 ventas)"

---

## HU-007: Dashboard para Usuario Cajero

### Descripción
Como usuario con rol Cajero, quiero ver un dashboard simplificado centrado en órdenes para enfocarme en las operaciones diarias sin distracciones de KPIs financieros.

### Criterios de Aceptación

**Estructura y Contenido del Dashboard:**
- El dashboard muestra un título "Dashboard" en la parte superior
- El contenido está enfocado únicamente en órdenes operativas
- Muestra 2 secciones principales:
  - Órdenes abiertas (resumen en card)
  - Lista de órdenes pendientes de atención

**Card: Órdenes Abiertas**
- Título: "Órdenes abiertas"
- Valor principal: Número total de órdenes con estados "Pendiente", "Preparación" o "Lista"
- Desglose visual por estado:
  - Badge con número de órdenes "Pendiente" (color naranja/amarillo)
  - Badge con número de órdenes "Preparación" (color azul)
  - Badge con número de órdenes "Lista" (color verde)
- Si no hay órdenes abiertas, mostrar "Sin órdenes abiertas" con icono de checkmark
- El card es clickeable y redirige a `/orders`

**Sección: Órdenes Pendientes de Atención**
- Título: "Órdenes pendientes"
- Muestra lista de las últimas 10 órdenes con estados "Pendiente" o "Preparación" (excluye "Lista" y "Cerrada")
- Cada orden en la lista muestra:
  - Número de orden (ej: "#001")
  - Estado actual con badge de color (Pendiente/Preparación)
  - Hora de creación (ej: "10:30 AM")
  - Total de la orden (ej: "$45.00")
  - Botón rápido "Ver detalle"
- Las órdenes se ordenan por hora de creación (más reciente primero)
- Si no hay órdenes pendientes, mostrar mensaje "¡Excelente! No hay órdenes pendientes" con icono de celebración

**Interacciones:**
- Al hacer clic en el card "Órdenes abiertas", redirigir a `/orders`
- Al hacer clic en "Ver detalle" de una orden, redirigir a `/orders/[id]` (detalle de la orden)
- Al hacer clic en cualquier parte de una fila de orden (no solo el botón), también redirigir al detalle

**Estados de Carga:**
- Al cargar el dashboard, mostrar skeleton loader en el card de órdenes abiertas
- En la sección de órdenes pendientes, mostrar skeleton loaders de filas (3-4 filas)
- La carga debe completarse en menos de 2 segundos

**Actualización en Tiempo Real:**
- El dashboard se actualiza automáticamente cada 30 segundos para reflejar nuevas órdenes
- Al crear una nueva orden desde el POS, el dashboard debe actualizarse automáticamente (WebSocket o polling)
- Incluir botón de actualizar manual en la esquina superior derecha
- Mostrar indicador visual discreto cuando se actualiza automáticamente (pequeño ícono pulsante)

**Manejo de Errores:**
- Si hay error al cargar las órdenes, mostrar mensaje: "Error al cargar órdenes" con botón "Reintentar"
- El botón "Reintentar" recarga los datos sin refrescar toda la página

**Responsive Design:**
- En desktop (>1024px): Card de órdenes abiertas ocupa 1/3 del ancho, lista de órdenes pendientes ocupa 2/3
- En tablet (768px-1024px): Card arriba, lista debajo
- En mobile (<768px): Card y lista apilados verticalmente, lista muestra 5 órdenes con scroll

**Elementos NO Visibles para Cajero:**
- No mostrar KPI de ventas del día
- No mostrar ticket promedio
- No mostrar productos más vendidos
- Enfoque 100% operativo en órdenes

### Escenarios

1. **Dashboard con órdenes activas**: Cajero accede al dashboard, ve "Órdenes abiertas: 8" con badges "3 Pendiente, 4 Preparación, 1 Lista", y lista con las 8 órdenes más recientes
2. **Dashboard sin órdenes pendientes**: Cajero accede al dashboard, ve "Órdenes abiertas: 0" con mensaje "Sin órdenes abiertas", y sección de pendientes muestra "¡Excelente! No hay órdenes pendientes"
3. **Click en card de órdenes**: Cajero hace clic en el card "Órdenes abiertas", es redirigido a `/orders`
4. **Click en Ver detalle**: Cajero hace clic en "Ver detalle" de orden #005, es redirigido a `/orders/005` con el detalle completo
5. **Click en fila de orden**: Cajero hace clic en cualquier parte de la fila de orden #003, es redirigido al detalle de esa orden
6. **Actualización automática**: Cajero tiene dashboard abierto, después de 30 segundos aparecen automáticamente 2 nuevas órdenes en la lista sin necesidad de refresh
7. **Actualización manual**: Cajero hace clic en botón de refresh, ve loading por 1 segundo, la lista se actualiza con datos nuevos
8. **Nueva orden desde POS**: Otro usuario crea orden desde POS, el dashboard del cajero se actualiza en tiempo real mostrando la nueva orden
9. **Más de 10 órdenes pendientes**: Hay 15 órdenes pendientes, el dashboard muestra solo las 10 más recientes con mensaje "Mostrando últimas 10 órdenes. Ver todas en Órdenes"
10. **Error al cargar órdenes**: Hay error de red, el dashboard muestra "Error al cargar órdenes" con botón "Reintentar", cajero hace clic y los datos se cargan correctamente
11. **Dashboard en mobile**: Cajero accede desde teléfono, ve card arriba y lista de 5 órdenes debajo con scroll para ver más
12. **Badges de estado**: Dashboard muestra 2 pendientes (badge naranja), 5 en preparación (badge azul), 1 lista (badge verde)
13. **Indicador de actualización automática**: Mientras el cajero observa, cada 30 segundos aparece un pequeño icono pulsante indicando actualización, los datos se refrescan silenciosamente

---

## HU-008: Cálculo y Actualización de KPIs

### Descripción
Como sistema, necesito calcular y actualizar los KPIs del dashboard de manera precisa y eficiente para mostrar información confiable a los usuarios.

### Criterios de Aceptación

**Cálculo de Ventas del Día:**
- Sumar el total de todas las órdenes con estado "Cerrada" del día actual (desde 00:00:00 hasta 23:59:59)
- El cálculo se realiza en el backend basado en la zona horaria del restaurante
- Incluir solo órdenes completadas (pagadas)
- Excluir órdenes canceladas o anuladas
- El valor se actualiza en tiempo real cuando se cierra una nueva orden

**Cálculo de Órdenes Abiertas:**
- Contar todas las órdenes con estados: "Pendiente", "Preparación" o "Lista"
- Excluir órdenes con estado "Cerrada"
- El conteo se actualiza en tiempo real cuando cambia el estado de una orden
- Desglosar por estado para mostrar la distribución

**Cálculo de Ticket Promedio:**
- Fórmula: Total de ventas del día ÷ Número de órdenes cerradas del día
- Si no hay órdenes cerradas, el ticket promedio es $0.00
- Redondear a 2 decimales
- Se recalcula cada vez que se cierra una nueva orden
- El número de ventas consideradas debe coincidir exactamente con las órdenes cerradas del día

**Cálculo de Productos Más Vendidos:**
- Contar la cantidad vendida de cada producto en órdenes cerradas del día actual
- Ordenar por cantidad vendida de mayor a menor
- Tomar los primeros 5 productos
- Si un producto tiene múltiples ocurrencias en diferentes órdenes, sumar todas las cantidades
- Si hay productos con la misma cantidad vendida, ordenar alfabéticamente como criterio secundario
- Si no hay ventas del día, retornar array vacío

**Periodo de Cálculo (Día Actual):**
- "Día actual" se define desde las 00:00:00 hasta las 23:59:59 según la zona horaria del restaurante
- Al cambiar de día (después de medianoche), todos los KPIs se reinician automáticamente
- La zona horaria se configura en los datos del restaurante (configuración)

**Actualización en Tiempo Real:**
- Cuando se crea una orden nueva: actualizar "Órdenes abiertas"
- Cuando se cambia estado de orden: actualizar "Órdenes abiertas"
- Cuando se cierra una orden: actualizar "Ventas del día", "Ticket promedio", "Productos más vendidos", y "Órdenes abiertas"
- Las actualizaciones deben reflejarse en todos los dashboards abiertos (Owner y Cajero)

**Optimización de Performance:**
- Los KPIs se calculan en el backend, no en el frontend
- Usar caché con TTL de 30 segundos para evitar cálculos repetitivos
- Al crear/actualizar/cerrar orden, invalidar caché para forzar recálculo
- El frontend hace polling cada 30 segundos para obtener datos actualizados

**Validación de Datos:**
- Validar que las órdenes incluidas en cálculos pertenezcan al restaurante/sucursal correcta
- Validar que las fechas de las órdenes correspondan al día actual
- Validar que los totales de órdenes sean valores numéricos válidos (no negativos)

**Manejo de Casos Especiales:**
- Si el total de una orden es $0.00, no incluir en cálculo de ticket promedio
- Si un producto fue eliminado del menú pero tiene ventas del día, incluir en top 5 con su nombre original
- Si hay menos de 5 productos con ventas, retornar solo los que tienen ventas

### Escenarios

1. **Primera venta del día**: Son las 8:00 AM, no hay ventas previas, se cierra orden de $50.00, los KPIs muestran: Ventas "$50.00", Órdenes abiertas "-1", Ticket "$50.00 (Basado en 1 venta)", Productos según lo vendido en esa orden
2. **Múltiples ventas consecutivas**: Se cierran 3 órdenes ($20, $30, $40), Ventas muestra "$90.00", Ticket muestra "$30.00 (Basado en 3 ventas)"
3. **Cambio de día a medianoche**: Son las 23:59, hay ventas de $1,000, a las 00:00 los KPIs se reinician automáticamente a $0.00
4. **Actualización de órdenes abiertas**: Hay 5 órdenes abiertas, 1 cambia de Pendiente a Preparación, el conteo sigue siendo 5 pero el desglose cambia
5. **Cierre de orden actualiza múltiples KPIs**: Se cierra orden de $25 con 2 productos (Hamburguesa x1, Refresco x1), se actualizan: Ventas (+$25), Ticket (recalculado), Órdenes abiertas (-1), Productos más vendidos (Hamburguesa +1, Refresco +1)
6. **Producto vendido múltiples veces**: Se venden 3 órdenes con Hamburguesa (2 en orden 1, 3 en orden 2, 1 en orden 3), el top muestra Hamburguesa con 6 vendidos
7. **Empate en cantidad vendida**: Pizza y Tacos tienen 5 vendidos cada uno, se ordenan alfabéticamente (Pizza primero, luego Tacos)
8. **Menos de 5 productos con ventas**: Solo se vendieron 2 productos diferentes en el día, el top muestra solo esos 2
9. **Orden con total $0.00**: Se cierra orden de $0.00 (promoción), no se incluye en cálculo de ticket promedio pero sí en conteo de órdenes
10. **Producto eliminado con ventas**: Se eliminó "Pizza Especial" del menú pero hoy tuvo ventas, aparece en top 5 con nombre "Pizza Especial"
11. **Actualización en tiempo real en múltiples dashboards**: Owner y 2 Cajeros tienen dashboard abierto, se cierra una orden, los 3 dashboards se actualizan simultáneamente
12. **Polling cada 30 segundos**: Dashboard cargado sin actividad, cada 30 segundos hace request silencioso al backend para obtener KPIs actualizados
13. **Caché invalidado al cerrar orden**: Dashboard hace request, recibe datos cacheados, se cierra orden (invalida caché), siguiente request obtiene datos frescos recalculados

---

## HU-009: Navegación y Acceso al Dashboard

### Descripción
Como usuario autenticado (Owner o Cajero), quiero acceder fácilmente al dashboard desde cualquier parte de la aplicación para tener siempre disponible la visión general del estado del restaurante.

### Criterios de Aceptación

**Acceso Directo al Dashboard:**
- El dashboard es la página de aterrizaje después de login exitoso
- La URL del dashboard es `/dashboard`
- El dashboard está disponible tanto para Owner como para Cajero

**Navegación desde el Menú Lateral:**
- El menú lateral/navegación principal incluye un ítem "Dashboard" con icono de home/panel
- El ítem "Dashboard" está siempre visible para ambos roles
- Cuando el usuario está en el dashboard, el ítem "Dashboard" en el menú aparece con estado activo (destacado visualmente)
- Al hacer clic en "Dashboard" desde cualquier página, redirigir a `/dashboard`

**Navegación desde el Header:**
- El header/navbar incluye el nombre de la aplicación o logo que funciona como link
- Al hacer clic en el logo/nombre, redirigir a `/dashboard` desde cualquier página

**Breadcrumb:**
- El dashboard NO muestra breadcrumb ya que es la página principal
- Otras páginas sí muestran breadcrumb con "Dashboard" como primer nivel clickeable

**Estado Activo en Navegación:**
- Cuando el usuario está en `/dashboard`, el ítem "Dashboard" en el menú lateral muestra:
  - Background de color distintivo (ej: azul claro, gris claro)
  - Borde izquierdo de color primario
  - Texto en color primario o negrita
  - Icono en color primario
- Los demás ítems del menú aparecen en estado normal

**Responsive - Menú Móvil:**
- En mobile (<768px), el menú lateral se colapsa en un menú hamburguesa
- Al abrir el menú hamburguesa, "Dashboard" aparece como primer ítem
- Al seleccionar "Dashboard", el menú se cierra y redirige a `/dashboard`

**Redirección por Defecto:**
- Si el usuario accede a la raíz del dominio (`/`) estando autenticado, redirigir a `/dashboard`
- Si el usuario accede a una URL inválida estando autenticado, mostrar página 404 con botón "Ir al Dashboard"

**Persistencia de Navegación:**
- Al navegar a otra sección y volver al dashboard, el estado del dashboard se recarga (datos frescos)
- No se guarda scroll position del dashboard al navegar

### Escenarios

1. **Login exitoso redirige a dashboard**: Usuario ingresa credenciales correctas, hace clic en "Iniciar Sesión", es redirigido automáticamente a `/dashboard`
2. **Click en Dashboard desde menú**: Usuario está en `/menu`, hace clic en "Dashboard" en menú lateral, es redirigido a `/dashboard`
3. **Click en logo desde otra página**: Usuario está en `/orders`, hace clic en logo en header, es redirigido a `/dashboard`
4. **Dashboard con estado activo**: Usuario está en `/dashboard`, ve el ítem "Dashboard" en menú lateral destacado con background de color y borde izquierdo
5. **Navegación a otra sección**: Usuario en dashboard hace clic en "Órdenes" en menú, el ítem "Dashboard" pierde el estado activo, "Órdenes" se activa
6. **Breadcrumb en otra página**: Usuario está en `/orders`, ve breadcrumb "Dashboard > Órdenes", hace clic en "Dashboard" del breadcrumb, es redirigido a `/dashboard`
7. **Acceso a raíz estando autenticado**: Usuario autenticado navega manualmente a `/`, es redirigido automáticamente a `/dashboard`
8. **Página 404 con botón al dashboard**: Usuario autenticado intenta acceder a `/pagina-inexistente`, ve página 404 con mensaje y botón "Ir al Dashboard", hace clic y es redirigido a `/dashboard`
9. **Menú hamburguesa en mobile**: Usuario en mobile hace clic en ícono hamburguesa, se abre menú lateral, "Dashboard" aparece como primer ítem, hace clic en "Dashboard", el menú se cierra y navega a dashboard
10. **Volver al dashboard recarga datos**: Usuario en dashboard ve "Ventas: $100", navega a `/pos`, cierra orden de $50, vuelve al dashboard, ve "Ventas: $150" (datos actualizados)
11. **Dashboard sin breadcrumb**: Usuario está en `/dashboard`, no ve breadcrumb en la página (es la página principal)
12. **Múltiples navegaciones al dashboard**: Usuario navega Dashboard → Menú → Dashboard → POS → Dashboard, cada vez que llega al dashboard los datos se recargan automáticamente

---

## Resumen de Componentes del Dashboard

### Para Owner:
- ✅ Card: Ventas del día
- ✅ Card: Órdenes abiertas (clickeable → `/orders`)
- ✅ Card: Ticket promedio
- ✅ Card: Productos más vendidos (top 5)
- ✅ Botón de actualizar manual
- ✅ Skeleton loaders durante carga
- ✅ Manejo de errores por card

### Para Cajero:
- ✅ Card: Órdenes abiertas (clickeable → `/orders`)
- ✅ Sección: Lista de órdenes pendientes (últimas 10)
- ✅ Actualización automática cada 30 segundos
- ✅ Botón de actualizar manual
- ✅ Skeleton loaders durante carga
- ✅ Manejo de errores

### Cálculos Backend:
- ✅ Total ventas del día (desde 00:00 a 23:59)
- ✅ Conteo órdenes abiertas por estado
- ✅ Ticket promedio (ventas ÷ órdenes cerradas)
- ✅ Top 5 productos más vendidos del día
- ✅ Caché con TTL 30s e invalidación al actualizar orden
- ✅ Polling frontend cada 30s

### Navegación:
- ✅ Dashboard como landing page post-login
- ✅ Acceso desde menú lateral (siempre visible)
- ✅ Acceso desde logo/nombre app en header
- ✅ Estado activo en menú cuando está en dashboard
- ✅ Responsive con menú hamburguesa en mobile

---

## Notas Técnicas

**Actualización en Tiempo Real:**
- Implementar WebSocket para notificaciones de cambios en órdenes (ideal)
- Alternativa: Polling cada 30 segundos (más simple para MVP)
- Invalidación de caché al crear/actualizar/cerrar órdenes

**Performance:**
- Cálculos de KPIs en backend con SQL optimizado
- Usar índices en campos de fecha y estado de órdenes
- Caché de 30s para reducir carga en DB
- Paginación en lista de órdenes pendientes (aunque MVP muestra solo 10)

**Formato de Moneda:**
- Usar la moneda configurada en `/settings` del restaurante
- Formato con separador de miles y 2 decimales
- Símbolo de moneda según configuración (ej: "$", "€", "S/")

**Zona Horaria:**
- Usar la zona horaria configurada en `/settings`
- Todos los cálculos de "día actual" respetan esta zona horaria
- Mostrar fechas/horas en formato local del restaurante

**Skeleton Loaders:**
- Usar skeleton loaders en lugar de spinners para mejor UX
- Mantener estructura visual similar a los datos reales
- Duración de 0.5-1 segundo antes de mostrar datos
