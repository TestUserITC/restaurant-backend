## HU-022: Agregar y Editar Notas en Orden

### Descripción
Como usuario (Owner o Cajero), quiero agregar o editar notas en una orden para comunicar instrucciones especiales o información relevante sobre el pedido.

### Criterios de Aceptación

**Agregar Notas al Crear Orden:**
- Durante la creación de orden (en POS o mini-POS), incluir campo opcional "Notas"
- Placeholder: "Instrucciones especiales (opcional)"
- Textarea de 2-3 líneas
- Máximo 500 caracteres
- Contador de caracteres: "0/500"
- Las notas se guardan al crear la orden

**Editar Notas en Detalle de Orden:**
- En la página de detalle, mostrar sección "Notas"
- Si hay notas, mostrarlas en un área de texto editable
- Si no hay notas, mostrar botón "Agregar notas"
- Solo permitir editar notas si la orden NO está Cerrada

**Botón Agregar Notas:**
- Al hacer clic, convertir el área en textarea editable
- Placeholder: "Escribe notas sobre esta orden..."
- Botones: "Cancelar" (secundario) y "Guardar" (primario)

**Edición de Notas Existentes:**
- Al hacer clic en área de notas, convertir en textarea editable
- Mostrar botones: "Cancelar" y "Guardar cambios"
- Permitir modificar o borrar todo el contenido

**Validaciones:**
- Máximo 500 caracteres
- Si se excede, mostrar error: "Las notas no pueden superar 500 caracteres"
- Permitir guardar notas vacías (equivalente a eliminar notas)

**Guardar Notas:**
- Al hacer clic en "Guardar", mostrar spinner en el botón
- Si es exitoso:
  - Mostrar toast: "Notas actualizadas correctamente"
  - Volver a mostrar las notas en modo lectura
- Si hay error:
  - Mostrar toast: "No se pudieron guardar las notas. Intenta de nuevo"
  - Mantener textarea editable con el contenido

**Cancelar Edición:**
- Al hacer clic en "Cancelar", descartar cambios
- Volver a mostrar las notas en modo lectura (o mensaje "Sin notas" si no había)

**Restricción en Órdenes Cerradas:**
- Si la orden está Cerrada, mostrar notas en modo solo lectura
- No mostrar botón de edición
- Mostrar mensaje: "Las órdenes cerradas no pueden ser editadas"

**Indicador de Notas en Lista:**
- En la tabla de órdenes, mostrar ícono de nota si la orden tiene notas
- Al hacer hover sobre el ícono, mostrar tooltip con las primeras 100 caracteres de las notas
- Click en el ícono abre el detalle de la orden

**Formato de Notas:**
- Mantener saltos de línea si el usuario los ingresa
- Trimear espacios al inicio y final
- No permitir solo espacios en blanco

### Escenarios

1. **Agregar notas al crear orden**: Usuario crea nueva orden en POS, escribe en campo "Notas": "Sin cebolla, extra queso", crea la orden, al ver detalle las notas aparecen guardadas
2. **Crear orden sin notas**: Usuario crea orden sin escribir notas, la orden se crea exitosamente, en detalle aparece botón "Agregar notas"
3. **Agregar notas después de crear**: Usuario abre detalle de orden sin notas, hace clic en "Agregar notas", escribe "Cliente preguntó por tiempo de espera", hace clic en "Guardar", aparece toast "Notas actualizadas correctamente", las notas se muestran en modo lectura
4. **Editar notas existentes**: Usuario abre orden con notas "Sin cebolla", hace clic en área de notas, edita a "Sin cebolla, sin tomate", hace clic en "Guardar cambios", las notas se actualizan
5. **Cancelar edición de notas**: Usuario empieza a editar notas, hace cambios, hace clic en "Cancelar", las notas vuelven al contenido original sin guardar cambios
6. **Eliminar notas**: Usuario edita notas, borra todo el contenido, hace clic en "Guardar", las notas se eliminan, aparece botón "Agregar notas"
7. **Validación de máximo caracteres**: Usuario intenta escribir 550 caracteres en notas, al llegar a 500 se detiene la escritura o ve error "Las notas no pueden superar 500 caracteres"
8. **Contador de caracteres**: Usuario escribe notas, ve contador actualizar "45/500 caracteres"
9. **Notas en orden Cerrada**: Usuario abre detalle de orden Cerrada que tiene notas, las notas se muestran en modo solo lectura sin opción de editar
10. **Intento de editar orden Cerrada**: Usuario intenta hacer clic en notas de orden Cerrada, no pasa nada o ve mensaje "Las órdenes cerradas no pueden ser editadas"
11. **Ícono de notas en lista**: Orden #005 tiene notas, en la tabla aparece ícono de nota, usuario hace hover, ve tooltip con primeras líneas de las notas
12. **Click en ícono de notas**: Usuario hace clic en ícono de nota en la lista, es redirigido al detalle de la orden
13. **Error al guardar notas**: Usuario edita notas, hace clic en "Guardar", hay error de red, aparece toast "No se pudieron guardar las notas", el textarea permanece editable con el contenido
14. **Notas con saltos de línea**: Usuario escribe notas en múltiples líneas con Enter, guarda, al ver las notas se respetan los saltos de línea

---