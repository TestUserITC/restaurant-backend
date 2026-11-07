## HU-039: Impacto de la Configuración en el Sistema

### Descripción
Como usuario Owner, necesito que los cambios en la configuración se apliquen correctamente en todas las partes del sistema donde se utilizan estos valores.

### Criterios de Aceptación

**Uso del Nombre del Restaurante:**
- Se muestra en:
  - Header/navbar de la aplicación (opcional)
  - Tickets de venta impresos
  - Facturas (si aplica)
  - Emails automáticos (si aplica)
  - Footer de exportaciones (opcional)
- Actualización: Inmediata al guardar

**Uso de la Dirección:**
- Se muestra en:
  - Tickets de venta impresos (si está configurada)
  - Facturas (si aplica)
  - Información de contacto (si aplica)
- Si no hay dirección configurada, no mostrar en tickets
- Actualización: Inmediata al guardar

**Uso de la Moneda:**
- Se aplica en:
  - Todos los precios de productos (menú)
  - Totales en POS
  - Totales en órdenes
  - Totales en historial de ventas
  - Reportes y exportaciones
  - Dashboard (KPIs)
- El símbolo de moneda ($, €, S/) se muestra antes o después del número según convención
- Actualización: Inmediata al guardar (refrescar vistas abiertas)

**Uso del Impuesto:**
- Se aplica en:
  - Cálculo de totales en POS (nuevas ventas)
  - Cálculo de totales en órdenes nuevas
  - Resumen de ventas (nuevas)
- NO se aplica retroactivamente a:
  - Ventas anteriores (mantienen su impuesto original)
  - Órdenes cerradas (mantienen su impuesto original)
- Actualización: Inmediata al guardar, afecta solo transacciones nuevas

**Validación de Consistencia:**
- Al cambiar moneda, validar que todos los precios siguen siendo válidos
- Al cambiar impuesto, recalcular totales en carrito del POS (si hay uno activo)
- Mostrar advertencias apropiadas si hay impacto

**Notificación de Cambios:**
- Si hay usuarios con sesión activa cuando se cambia la configuración:
  - Notificar con mensaje: "La configuración del sistema ha sido actualizada"
  - Sugerir refrescar la página si es necesario
  - Actualizar automáticamente valores visibles (ideal)

**Preservación de Datos Históricos:**
- Las ventas anteriores mantienen:
  - El porcentaje de impuesto con el que fueron calculadas
  - La moneda original (aunque cambie la configuración)
- Esto evita discrepancias en reportes históricos

**Valores de Configuración en Base de Datos:**
- Almacenar como registro único por restaurante
- Incluir timestamps (created_at, updated_at)
- Registrar usuario que realizó el último cambio (audit)

**Configuración Inicial Obligatoria:**
- Al crear una cuenta nueva, solicitar configuración básica
- No permitir usar el sistema sin configurar al menos:
  - Nombre del restaurante
  - Moneda
  - Impuesto (puede ser 0%)
- La dirección es opcional

### Escenarios

1. **Cambio de nombre refleja en tickets**: Owner cambia nombre a "El Sabor Restaurant", realiza venta, imprime ticket, el ticket muestra el nuevo nombre
2. **Cambio de moneda actualiza POS**: Owner cambia de "$" a "S/", accede al POS, todos los precios ahora muestran "S/" en lugar de "$"
3. **Cambio de moneda actualiza historial**: Owner cambia moneda, accede a historial de ventas, todas las ventas nuevas muestran "S/", pero ventas anteriores mantienen "$" (datos históricos)
4. **Cambio de impuesto afecta nueva venta**: Owner cambia impuesto de 18% a 16%, crea nueva orden en POS con $100 subtotal, el impuesto calculado es $16 (no $18)
5. **Cambio de impuesto NO afecta ventas anteriores**: Owner cambia impuesto, consulta venta de ayer, la venta mantiene el 18% original con el que fue registrada
6. **Dirección en ticket**: Owner configura dirección "Calle Principal 123", imprime ticket de venta, el ticket incluye la dirección debajo del nombre
7. **Ticket sin dirección**: Owner no ha configurado dirección, imprime ticket, el ticket muestra solo nombre del restaurante sin dirección
8. **Actualización en dashboard**: Owner cambia moneda a "€", accede al dashboard, los KPIs de ventas muestran "€1,250.00" en lugar de "$1,250.00"
9. **Recálculo en carrito activo**: Owner tiene carrito con productos en POS, cambia impuesto de 18% a 20%, el total en el carrito se recalcula automáticamente con el nuevo 20%
10. **Notificación a otros usuarios**: Owner cambia configuración mientras Cajero tiene sesión abierta en POS, Cajero ve notificación "La configuración del sistema ha sido actualizada", refresca y ve nuevos valores
11. **Primera configuración obligatoria**: Owner recién registrado intenta acceder al POS, es redirigido a `/settings` con mensaje "Por favor, configura tu restaurante antes de continuar"
12. **Audit de cambios**: Owner cambia impuesto, el sistema registra internamente: usuario "Owner", fecha/hora del cambio, valor anterior y nuevo valor

---