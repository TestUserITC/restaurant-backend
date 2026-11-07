## HU-013: Eliminar Categoría

### Descripción
Como usuario Owner, quiero eliminar categorías que ya no necesito para mantener el menú organizado y limpio, con la seguridad de que no puedo eliminar categorías que tienen productos asociados.

### Criterios de Aceptación

**Trigger de Eliminación:**
- En la tabla de categorías, agregar columna de "Acciones" con botón "Eliminar" (ícono de basura)
- El botón "Eliminar" solo está visible y habilitado si la categoría tiene 0 productos
- Si la categoría tiene productos asociados, el botón aparece deshabilitado con tooltip explicativo

**Tooltip para Botón Deshabilitado:**
- Al hacer hover sobre el botón "Eliminar" deshabilitado, mostrar tooltip: "No se puede eliminar. Esta categoría tiene X productos asociados"
- El tooltip indica claramente por qué no se puede eliminar

**Modal de Confirmación:**
- Al hacer clic en "Eliminar" (en categoría sin productos), abrir modal de confirmación
- Título del modal: "¿Eliminar categoría?"
- Mensaje: "¿Estás seguro de que deseas eliminar la categoría '[Nombre]'? Esta acción no se puede deshacer."
- El nombre de la categoría se muestra en negrita o color distintivo
- Botones:
  - "Cancelar" (secundario, izquierda)
  - "Eliminar" (destructivo/rojo, derecha)

**Comportamiento de Eliminación:**
- Al hacer clic en "Eliminar" en el modal, mostrar spinner en el botón y cambiar texto a "Eliminando..."
- Deshabilitar ambos botones durante el proceso
- Si la eliminación es exitosa:
  - Cerrar el modal automáticamente
  - Remover la categoría de la lista con animación de salida
  - Mostrar toast de éxito: "Categoría eliminada exitosamente"

**Manejo de Errores:**
- Si hay error al eliminar, mostrar toast: "No se pudo eliminar la categoría. Por favor, intenta de nuevo"
- El modal permanece abierto para permitir reintentos
- Si la categoría tiene productos (validación de backend), mostrar error específico: "No se puede eliminar esta categoría porque tiene productos asociados"

**Validación de Backend:**
- Aunque el frontend deshabilita el botón, el backend debe validar nuevamente que la categoría no tenga productos
- Esto previene condiciones de carrera (ej: se agrega producto mientras se intenta eliminar)

**Estado Vacío Después de Eliminar:**
- Si después de eliminar una categoría no quedan más categorías, mostrar estado vacío: "No hay categorías creadas" con botón "Crear primera categoría"

**Cierre del Modal de Confirmación:**
- Al hacer clic en "Cancelar", cerrar modal sin eliminar
- Al hacer clic en X, cerrar modal sin eliminar
- Al hacer clic fuera del modal (overlay), cerrar sin eliminar
- Al presionar ESC, cerrar sin eliminar
- No mostrar confirmación adicional al cerrar (el modal ya ES la confirmación)

### Escenarios

1. **Eliminar categoría sin productos exitosamente**: Owner tiene categoría "Promociones" con 0 productos, hace clic en botón "Eliminar", ve modal de confirmación "¿Eliminar categoría 'Promociones'?", hace clic en "Eliminar", ve spinner, el modal se cierra, la fila desaparece con animación, aparece toast "Categoría eliminada exitosamente"
2. **Botón deshabilitado con productos**: Categoría "Bebidas" tiene 12 productos, el botón "Eliminar" aparece deshabilitado y con opacidad reducida
3. **Tooltip en botón deshabilitado**: Owner hace hover sobre botón "Eliminar" deshabilitado de categoría con 8 productos, ve tooltip "No se puede eliminar. Esta categoría tiene 8 productos asociados"
4. **Cancelar eliminación**: Owner hace clic en "Eliminar", ve modal de confirmación, hace clic en "Cancelar", el modal se cierra, la categoría permanece en la lista
5. **Cerrar modal de confirmación con X**: Owner abre modal de eliminación, hace clic en X, el modal se cierra sin eliminar
6. **Estado vacío después de eliminar última categoría**: Owner tiene solo 1 categoría sin productos, la elimina exitosamente, ve estado vacío "No hay categorías creadas" con botón "Crear primera categoría"
7. **Error al eliminar**: Owner intenta eliminar categoría, hay error de red, aparece toast "No se pudo eliminar la categoría. Por favor, intenta de nuevo", el modal permanece abierto
8. **Validación backend con productos**: Owner intenta eliminar categoría que entre tanto recibió productos, el backend rechaza la operación, aparece toast "No se puede eliminar esta categoría porque tiene productos asociados"
9. **Eliminar múltiples categorías**: Owner elimina 3 categorías vacías una tras otra, cada eliminación muestra confirmación individual, toast de éxito, y la lista se actualiza correctamente
10. **Categoría con 1 producto no se puede eliminar**: Categoría tiene exactamente 1 producto, botón "Eliminar" está deshabilitado, tooltip dice "No se puede eliminar. Esta categoría tiene 1 producto asociado"
11. **Cerrar con ESC**: Owner abre modal de confirmación de eliminación, presiona tecla ESC, el modal se cierra sin eliminar

---