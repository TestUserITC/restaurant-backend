## HU-005: Roles de Usuario (Owner vs Cajero)

### Descripción
Como sistema, necesito diferenciar entre roles de usuario (Owner y Cajero) para mostrar u ocultar funcionalidades según los permisos de cada rol.

### Criterios de Aceptación

**Rol de Owner:**
- Tiene acceso completo a todas las funcionalidades del sistema
- Puede acceder a:
  - Dashboard (con todos los KPIs)
  - Gestión de menú (categorías y productos)
  - POS (punto de venta)
  - Órdenes
  - Historial de ventas
  - Configuración del restaurante
- El menú lateral/navegación muestra todas las opciones disponibles

**Rol de Cajero:**
- Tiene acceso limitado solo a funcionalidades operativas
- Puede acceder a:
  - Dashboard (solo vista de órdenes abiertas y básicos)
  - POS (punto de venta)
  - Órdenes (ver y cambiar estados)
- NO puede acceder a:
  - Gestión de menú
  - Historial de ventas
  - Configuración
- El menú lateral/navegación solo muestra las opciones permitidas (Dashboard, POS, Órdenes)

**Asignación de Rol:**
- El primer usuario que registra el restaurante (usuario que crea la cuenta) recibe automáticamente rol "Owner"
- Solo el Owner puede invitar/crear nuevos usuarios con rol "Cajero" (esto está fuera del MVP pero el sistema debe estar preparado)

**Protección de Rutas por Rol:**
- Si un Cajero intenta acceder manualmente a una URL protegida (ej: `/menu`, `/sales`, `/settings`), mostrar página de error 403 con mensaje: "No tienes permisos para acceder a esta sección"
- Incluir botón "Volver al inicio" que redirige a `/dashboard`

**Visual de Rol:**
- En el menú lateral, mostrar el nombre del usuario y su rol debajo (ej: "Juan Pérez - Owner" o "María López - Cajero")
- El rol se muestra siempre visible para que el usuario sepa con qué permisos está operando

**Dashboard según Rol:**
- Owner ve dashboard completo con todos los KPIs (ventas del día, órdenes abiertas, ticket promedio, productos más vendidos)
- Cajero ve dashboard simplificado con solo órdenes abiertas y pendientes de preparar
- El título del dashboard es el mismo ("Dashboard"), pero el contenido varía según rol

**Navegación según Rol:**
- El menú lateral renderiza dinámicamente según el rol:
  - Owner: Dashboard, Menú, POS, Órdenes, Ventas, Configuración
  - Cajero: Dashboard, POS, Órdenes

### Escenarios

1. **Owner accede a todas las secciones**: Usuario con rol Owner navega a cada sección del menú, puede acceder sin problemas a Menú, Ventas y Configuración
2. **Cajero accede a secciones permitidas**: Usuario con rol Cajero navega a Dashboard, POS y Órdenes, puede acceder sin problemas
3. **Cajero intenta acceder a Menú**: Usuario con rol Cajero intenta navegar manualmente a `/menu`, ve página de error 403 "No tienes permisos para acceder a esta sección" con botón "Volver al inicio"
4. **Cajero intenta acceder a Ventas**: Usuario con rol Cajero intenta navegar a `/sales`, ve página 403 con mensaje de permiso denegado
5. **Cajero intenta acceder a Configuración**: Usuario con rol Cajero intenta navegar a `/settings`, ve página 403 con mensaje de permiso denegado
6. **Dashboard de Owner**: Usuario Owner accede a dashboard, ve todos los KPIs: ventas del día ($1,250.00), órdenes abiertas (5), ticket promedio ($25.00), y top 5 productos más vendidos
7. **Dashboard de Cajero**: Usuario Cajero accede a dashboard, ve solo órdenes abiertas y pendientes, NO ve KPIs de ventas ni productos más vendidos
8. **Visualización de rol en menú**: Usuario Owner ve en menú lateral "Juan Pérez - Owner", usuario Cajero ve "María López - Cajero"
9. **Registro crea Owner automáticamente**: Nuevo usuario completa registro de restaurante, al acceder por primera vez a dashboard, su rol es "Owner" y ve todas las opciones en menú lateral
10. **Menú lateral dinámico para Owner**: Usuario Owner ve en menú lateral 6 opciones: Dashboard, Menú, POS, Órdenes, Ventas, Configuración
11. **Menú lateral dinámico para Cajero**: Usuario Cajero ve en menú lateral solo 3 opciones: Dashboard, POS, Órdenes
12. **Click en Volver al inicio desde 403**: Usuario Cajero ve página 403, hace clic en "Volver al inicio", es redirigido a `/dashboard`

---

## Resumen de Rutas

| Ruta | Descripción | Roles Permitidos | Redirección |
|------|-------------|------------------|-------------|
| `/login` | Pantalla de inicio de sesión | Sin autenticar | Si autenticado → `/dashboard` |
| `/register` | Registro de restaurante | Sin autenticar | Si autenticado → `/dashboard` |
| `/recuperar-password` | Recuperación de contraseña | Sin autenticar | Si autenticado → `/dashboard` |
| `/restablecer-password` | Establecer nueva contraseña | Sin autenticar (con token) | - |
| `/dashboard` | Panel principal | Owner, Cajero | Si no autenticado → `/login` |
| `/menu` | Gestión de menú | Solo Owner | Si no autenticado → `/login`<br>Si Cajero → Error 403 |
| `/pos` | Punto de venta | Owner, Cajero | Si no autenticado → `/login` |
| `/orders` | Gestión de órdenes | Owner, Cajero | Si no autenticado → `/login` |
| `/sales` | Historial de ventas | Solo Owner | Si no autenticado → `/login`<br>Si Cajero → Error 403 |
| `/settings` | Configuración | Solo Owner | Si no autenticado → `/login`<br>Si Cajero → Error 403 |

---

## Notas Técnicas

**Almacenamiento de Sesión:**
- Se recomienda usar localStorage o sessionStorage para el token (según requerimientos de seguridad)
- El token debe incluir información del rol para evitar requests adicionales
- Implementar refresh token si la sesión debe extenderse automáticamente

**Validación de Token:**
- Validar el token en cada request al API
- Manejar respuestas 401 (no autenticado) y 403 (sin permisos) apropiadamente
- Implementar un interceptor global para requests HTTP

**Estados de Carga:**
- Mostrar skeleton loaders en lugar de spinners donde sea posible para mejor UX
- Los loaders de validación de token no deben exceder 1 segundo en condiciones normales

**Seguridad:**
- Nunca exponer contraseñas en logs o estados del cliente
- Los tokens deben tener expiración definida
- Implementar HTTPS en producción
- Rate limiting en endpoints de login y registro