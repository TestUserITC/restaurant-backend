## HU-020: Cambiar Estado de Orden

### Descripción
Como usuario (Owner o Cajero), quiero cambiar el estado de las órdenes para reflejar el progreso en la preparación y entrega de los pedidos.

### Criterios de Aceptación

**Flujo de Estados:**
- El ciclo de estados es lineal: Pendiente → Preparación → Lista → Cerrada
- No se puede saltar estados (ej: de Pendiente a Lista)
- No se puede retroceder estados (ej: de Preparación a Pendiente)
- Una vez Cerrada, la orden no puede cambiar de estado

**Cambio de Estado desde Lista de Órdenes:**
- En cada fila de la tabla, incluir dropdown o botones rápidos para cambiar estado
- Mostrar solo la siguiente acción disponible según estado actual:
  - Pendiente: Botón "Iniciar preparación"
  - Preparación: Botón "Marcar como lista"
  - Lista: Botón "Cerrar orden"
  - Cerrada: No mostrar botones

**Cambio de Estado desde Detalle:**
- En la página de detalle, mostrar botón grande destacado para el siguiente estado
- El botón debe ser visualmente prominente y fácil de identificar

**Modal de Confirmación:**
- Al hacer clic en cualquier botón de cambio de estado, abrir modal de confirmación
- Título: "¿Cambiar estado de orden?"
- Mensaje según acción:
  - "¿Iniciar preparación de orden #XXX?"
  - "¿Marcar orden #XXX como lista?"
  - "¿Cerrar orden #XXX?"
- Botones:
  - "Cancelar" (secundario)
  - "Confirmar" (primario)

**Comportamiento del Cambio:**
- Al confirmar, mostrar spinner en el botón
- Si el cambio es exitoso:
  - Actualizar el badge de estado inmediatamente
  - Mostrar toast de confirmación: "Orden actualizada exitosamente"
  - Si está en lista de órdenes, actualizar la fila
  - Si está en detalle, actualizar toda la vista
  - Actualizar contadores en los tabs de filtros

**Manejo de Errores:**
- Si hay error al cambiar estado, mostrar toast: "No se pudo actualizar la orden. Por favor, intenta de nuevo"
- El estado permanece en el valor anterior
- El modal permanece abierto para permitir reintentos

**Validación de Estado Actual:**
- Antes de cambiar, validar en backend que la orden está en el estado esperado
- Esto previene conflictos si múltiples usuarios cambian la misma orden simultáneamente
- Si el estado ya cambió, mostrar error: "Esta orden ya fue actualizada por otro usuario"

**Timestamp de Cambios:**
- Registrar fecha y hora de cada cambio de estado
- Registrar usuario que realizó el cambio (Owner o Cajero)
- Esta información se usa para el historial de estados

**Cambios Masivos (en Lista):**
- Permitir seleccionar múltiples órdenes con checkbox
- Botón "Cambiar estado" habilitado solo si todas las órdenes seleccionadas están en el mismo estado
- Al hacer clic, abrir modal: "¿Cambiar estado de X órdenes?"
- Aplicar cambio a todas las órdenes seleccionadas simultáneamente

**Indicadores Visuales:**
- Al cambiar estado en la lista, animar la transición del badge de color
- Si la orden se mueve a otro filtro (ej: de Pendiente a Preparación), removerla de la vista con animación de salida

**Atajos de Teclado (Opcional):**
- En detalle de orden, permitir atajos:
  - "P" para Iniciar preparación
  - "L" para Marcar como lista
  - "C" para Cerrar orden
- Mostrar hints de atajos en los botones

### Escenarios

1. **Cambiar de Pendiente a Preparación desde lista**: Usuario hace clic en "Iniciar preparación" de orden #005, ve modal de confirmación, hace clic en "Confirmar", el badge cambia de naranja a azul, aparece toast "Orden actualizada exitosamente"
2. **Cambiar de Preparación a Lista desde detalle**: Usuario en detalle de orden #003 hace clic en botón "Marcar como lista", confirma en modal, el badge cambia a verde, toast confirma cambio
3. **Cambiar de Lista a Cerrada**: Usuario hace clic en "Cerrar orden", confirma, el badge cambia a gris, la orden se marca como completada
4. **Cancelar cambio de estado**: Usuario hace clic en "Iniciar preparación", ve modal, hace clic en "Cancelar", el modal se cierra sin cambios, el estado permanece en Pendiente
5. **Error al cambiar estado**: Usuario intenta cambiar estado pero hay error de red, aparece toast "No se pudo actualizar la orden", el estado permanece sin cambios
6. **Conflicto de estado**: Usuario A intenta cambiar orden #005 a Preparación, pero usuario B ya la cambió, usuario A ve error "Esta orden ya fue actualizada por otro usuario"
7. **Orden desaparece de vista filtrada**: Vista filtrada en "Pendiente" muestra 5 órdenes, usuario cambia una a Preparación, la orden desaparece de la vista con animación
8. **Actualización de contadores**: Tab "Pendiente" muestra "5", usuario cambia una orden a Preparación, el contador de "Pendiente" cambia a "4" y "Preparación" aumenta de "2" a "3"
9. **Cambio masivo de 3 órdenes**: Usuario selecciona 3 órdenes en estado Pendiente con checkboxes, hace clic en "Cambiar estado", selecciona "Preparación", confirma, las 3 órdenes cambian simultáneamente
10. **Intento de cambio masivo con estados mixtos**: Usuario selecciona 2 órdenes Pendientes y 1 en Preparación, el botón "Cambiar estado" permanece deshabilitado o muestra error
11. **Animación de transición**: Al cambiar estado, el badge anima el cambio de color suavemente de naranja a azul
12. **Historial actualizado**: Después de cambiar a Preparación, el historial en detalle muestra nueva entrada "En preparación - 11:45 AM - Cajero: María"
13. **Orden Cerrada sin botones**: Usuario abre detalle de orden Cerrada, no ve ningún botón de cambio de estado
14. **Atajo de teclado**: Usuario en detalle de orden Pendiente presiona "P", se abre modal de confirmación para iniciar preparación

---