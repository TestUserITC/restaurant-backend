## HU-038: Editar Configuración del Restaurante

### Descripción
Como usuario Owner, quiero editar la configuración de mi restaurante para actualizar datos cuando sea necesario (cambio de dirección, ajuste de impuesto, etc.).

### Criterios de Aceptación

**Modo Edición:**
- Al hacer clic en "Editar", los campos de solo lectura se convierten en inputs editables
- Botón "Editar" desaparece, aparecen:
  - "Cancelar" (secundario, izquierda)
  - "Guardar cambios" (primario, derecha)
- El formulario mantiene el mismo layout pero con campos interactivos

**Campo: Nombre del Restaurante**
- Label: "Nombre del restaurante *" (asterisco indica requerido)
- Input de texto
- Valor precargado con el nombre actual
- Placeholder: "Ej: Restaurante El Sabor"
- Mínimo 2 caracteres, máximo 100 caracteres
- Requerido

**Validaciones de Nombre:**
- Si está vacío, mostrar error: "El nombre es requerido"
- Si tiene menos de 2 caracteres, mostrar error: "El nombre debe tener al menos 2 caracteres"
- Si excede 100 caracteres, mostrar error: "El nombre no puede exceder 100 caracteres"

**Campo: Dirección**
- Label: "Dirección"
- Input de texto (o textarea de 2 líneas)
- Valor precargado con la dirección actual (o vacío si no hay)
- Placeholder: "Ej: Calle Principal 123, Lima, Perú"
- Máximo 200 caracteres
- Opcional

**Validaciones de Dirección:**
- Si excede 200 caracteres, mostrar error: "La dirección no puede exceder 200 caracteres"
- Permitir dejarlo vacío

**Campo: Moneda**
- Label: "Moneda *" (requerido)
- Dropdown/Select con lista de monedas comunes
- Valor precargado con la moneda actual
- Opciones incluyen:
  - USD - Dólar estadounidense ($)
  - EUR - Euro (€)
  - PEN - Sol peruano (S/)
  - MXN - Peso mexicano ($)
  - COP - Peso colombiano ($)
  - CLP - Peso chileno ($)
  - ARS - Peso argentino ($)
  - (Agregar otras según necesidad)
- Mostrar formato: "USD - Dólar estadounidense ($)"
- Requerido

**Campo: Impuesto**
- Label: "Impuesto (%) *" (requerido)
- Input numérico
- Valor precargado con el impuesto actual
- Placeholder: "Ej: 18"
- Acepta decimales (1 dígito, ej: 18.5)
- Rango: 0 a 100
- Requerido

**Validaciones de Impuesto:**
- Si está vacío, mostrar error: "El impuesto es requerido"
- Si es menor a 0, ajustar automáticamente a 0
- Si es mayor a 100, mostrar error: "El impuesto no puede exceder 100%"
- Permitir 0% (sin impuesto)
- Permitir decimales con 1 dígito (ej: 18.5, 16.7)

**Formato Visual de Impuesto:**
- Mostrar símbolo "%" automáticamente
- Si el usuario escribe "18", mostrar "18%" en el campo
- Al editar, seleccionar solo el número (sin el %)

**Detección de Cambios:**
- El botón "Guardar cambios" está habilitado solo si hay cambios en algún campo
- Si no hay cambios, el botón está deshabilitado
- Mostrar indicador visual de campos modificados (opcional)

**Comportamiento del Botón Guardar:**
- Al hacer clic, validar todos los campos
- Si hay errores, mostrar mensajes debajo de cada campo con error
- Si todo es válido, mostrar spinner en el botón y cambiar texto a "Guardando..."
- Deshabilitar ambos botones mientras se procesa

**Guardado Exitoso:**
- Si el guardado es exitoso:
  - Volver a modo lectura automáticamente
  - Mostrar los nuevos valores guardados
  - Mostrar toast: "Configuración actualizada exitosamente"
  - Los cambios se aplican inmediatamente en todo el sistema

**Aplicación de Cambios:**
- Cambio de nombre: Se refleja en header, facturas, tickets
- Cambio de dirección: Se refleja en tickets (si se usa)
- Cambio de moneda: Se aplica a todos los precios, totales, reportes
- Cambio de impuesto: Se aplica a todas las nuevas ventas (no afecta ventas anteriores)

**Manejo de Errores:**
- Si hay error al guardar, mostrar toast: "No se pudo guardar la configuración. Por favor, intenta de nuevo"
- El formulario permanece en modo edición con los datos ingresados

**Botón Cancelar:**
- Al hacer clic en "Cancelar", descartar todos los cambios
- Volver a modo lectura mostrando los valores originales
- Si hay cambios sin guardar, mostrar confirmación: "¿Descartar cambios?"

**Modal de Confirmación al Cancelar:**
- Título: "¿Descartar cambios?"
- Mensaje: "Los cambios que realizaste no se guardarán."
- Botones:
  - "Continuar editando" (volver al formulario)
  - "Descartar" (cerrar y perder cambios)

**Advertencia de Cambio de Moneda:**
- Si el usuario cambia la moneda, mostrar advertencia (modal o mensaje destacado)
- Mensaje: "⚠️ Cambiar la moneda afectará todos los precios y totales del sistema. Asegúrate de actualizar los precios de tus productos después de este cambio."
- Botones:
  - "Cancelar"
  - "Confirmar cambio"

**Advertencia de Cambio de Impuesto:**
- Si el usuario cambia el impuesto, mostrar mensaje informativo
- Mensaje: "ℹ️ El nuevo porcentaje de impuesto se aplicará a partir de la próxima venta. Las ventas anteriores mantienen el impuesto con el que fueron registradas."
- Botón: "Entendido"

### Escenarios

1. **Editar nombre exitosamente**: Owner hace clic en "Editar", cambia nombre de "Restaurante El Sabor" a "El Sabor Restaurant", hace clic en "Guardar cambios", ve toast "Configuración actualizada exitosamente", el nombre se actualiza en modo lectura
2. **Validar nombre vacío**: Owner borra el nombre completamente, intenta guardar, ve error "El nombre es requerido" debajo del campo
3. **Editar dirección**: Owner actualiza dirección de "Calle Principal 123" a "Av. Libertadores 456, Lima", guarda exitosamente
4. **Dejar dirección vacía**: Owner borra la dirección, guarda, la configuración se guarda sin dirección (campo opcional)
5. **Cambiar moneda**: Owner cambia de "USD" a "PEN - Sol peruano (S/)", ve advertencia sobre impacto en precios, confirma, guarda exitosamente, todos los precios ahora muestran "S/" en lugar de "$"
6. **Cambiar impuesto**: Owner cambia impuesto de "18%" a "16%", ve mensaje informativo sobre aplicación a próximas ventas, confirma, guarda, el nuevo impuesto se aplica en POS inmediatamente
7. **Impuesto con decimal**: Owner ingresa "18.5", el sistema acepta y muestra "18.5%" correctamente
8. **Impuesto mayor a 100**: Owner intenta ingresar "120", ve error "El impuesto no puede exceder 100%"
9. **Sin cambios, botón deshabilitado**: Owner hace clic en "Editar", no modifica nada, el botón "Guardar cambios" permanece deshabilitado
10. **Cancelar con cambios**: Owner modifica nombre y dirección, hace clic en "Cancelar", ve modal "¿Descartar cambios?", hace clic en "Descartar", vuelve a modo lectura con valores originales
11. **Continuar editando**: Owner hace cambios, intenta cancelar, ve confirmación, hace clic en "Continuar editando", permanece en modo edición con sus cambios intactos
12. **Error al guardar**: Owner modifica configuración, hay error de red al guardar, ve toast "No se pudo guardar la configuración", el formulario permanece en modo edición
13. **Formato automático de impuesto**: Owner escribe "18" en campo de impuesto, el campo muestra automáticamente "18%"
14. **Primera configuración**: Owner nuevo completa todos los campos por primera vez, hace clic en "Guardar configuración", la configuración se guarda exitosamente

---