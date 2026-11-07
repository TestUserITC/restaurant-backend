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