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