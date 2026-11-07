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