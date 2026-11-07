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