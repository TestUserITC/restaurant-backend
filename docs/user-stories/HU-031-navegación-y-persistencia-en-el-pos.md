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