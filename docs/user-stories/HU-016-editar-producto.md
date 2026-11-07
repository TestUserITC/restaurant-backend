## HU-016: Editar Producto

### Descripción
Como usuario Owner, quiero editar los productos existentes para actualizar precios, cambiar información, o corregir errores en el menú.

### Criterios de Aceptación

**Trigger del Modal:**
- Al hacer clic en botón "Editar" de un producto en la lista, abrir modal de edición
- El modal carga automáticamente con todos los datos actuales del producto

**Estructura del Modal:**
- Título: "Editar producto"
- Mismos campos que creación, pero precargados:
  - Imagen actual (si existe)
  - Nombre del producto
  - Categoría seleccionada
  - Precio
  - Descripción
- Botones:
  - "Cancelar" (secundario, izquierda)
  - "Guardar cambios" (primario, derecha)
- Botón X en esquina superior derecha para cerrar

**Campos Precargados:**
- Imagen: Muestra imagen actual o placeholder si no tiene
- Nombre: Precargado con valor actual, texto seleccionado
- Categoría: Dropdown con categoría actual seleccionada
- Precio: Precargado con precio actual formateado
- Descripción: Precargada con descripción actual (o vacía si no tiene)

**Validaciones:**
- Las mismas validaciones que en creación
- Si el nombre se cambia a uno que ya existe en otro producto, mostrar error: "Ya existe un producto con este nombre"
- Permitir guardar si el nombre es igual al actual (sin cambios)

**Cambio de Imagen:**
- Mostrar imagen actual con botón "Cambiar imagen"
- Al hacer clic, abrir selector de archivo
- Preview de la nueva imagen seleccionada
- Opción "Eliminar imagen" para quitar la imagen actual (producto quedará sin imagen)

**Detección de Cambios:**
- El botón "Guardar cambios" está habilitado solo si hay cambios Y los datos son válidos
- Si no hay cambios, el botón permanece deshabilitado

**Comportamiento del Botón Guardar:**
- Al hacer clic, validar todos los campos
- Mostrar spinner en el botón y cambiar texto a "Guardando..."
- Deshabilitar botón mientras se procesa

**Edición Exitosa:**
- Si la edición es exitosa, cerrar el modal automáticamente
- Actualizar la fila correspondiente en la lista con los nuevos datos
- Mantener el orden y filtros aplicados
- Mostrar toast de éxito: "Producto actualizado exitosamente"

**Cambio de Categoría:**
- Permitir cambiar el producto de categoría
- Si hay filtro activo por la categoría anterior, el producto desaparece de la vista
- El producto ahora pertenece a la nueva categoría

**Manejo de Errores:**
- Si hay error, mostrar toast: "No se pudo actualizar el producto. Por favor, intenta de nuevo"
- El modal permanece abierto con los datos editados

**Cierre del Modal:**
- Al hacer clic en "Cancelar", cerrar modal sin guardar
- Al hacer clic en X, cerrar modal sin guardar
- Al hacer clic fuera del modal (overlay), cerrar sin guardar
- Al presionar ESC, cerrar sin guardar
- Si hay cambios sin guardar, mostrar confirmación: "¿Deseas salir sin guardar los cambios?"

**Preservación de Datos:**
- Al editar, se mantiene:
  - El estado del producto (Disponible/No disponible)
  - El ID único del producto
  - Las ventas históricas asociadas

### Escenarios

1. **Editar precio exitosamente**: Owner hace clic en "Editar" de "Hamburguesa", el modal se abre con datos actuales, Owner cambia precio de "$10.00" a "$12.50", hace clic en "Guardar", ve toast "Producto actualizado exitosamente", la lista muestra nuevo precio
2. **Editar múltiples campos**: Owner edita "Pizza", cambia nombre a "Pizza Grande", precio a "$15.00", y descripción, guarda exitosamente, todos los cambios se reflejan en la lista
3. **Cambiar categoría**: Owner edita producto de categoría "Entradas" y lo cambia a "Platos Fuertes", guarda, el producto ahora aparece con badge "Platos Fuertes"
4. **Cambiar imagen**: Owner edita producto, hace clic en "Cambiar imagen", selecciona nueva foto, guarda, el producto muestra la nueva imagen en la lista
5. **Eliminar imagen**: Owner edita producto que tiene imagen, hace clic en "Eliminar imagen", guarda, el producto ahora muestra placeholder
6. **Sin cambios, botón deshabilitado**: Owner abre edición, no modifica nada, el botón "Guardar cambios" permanece deshabilitado
7. **Validar nombre duplicado**: Owner edita "Tacos" e intenta cambiarlo a "Burritos" (que ya existe), ve error "Ya existe un producto con este nombre"
8. **Producto desaparece con filtro**: Filtro activo en "Bebidas", Owner edita producto "Coca Cola" y lo cambia a categoría "Otros", al guardar el producto desaparece de la vista (porque ya no es Bebida)
9. **Preservar estado al editar**: Producto está "No disponible", Owner edita nombre y precio, después de guardar el producto sigue "No disponible"
10. **Cerrar sin guardar con confirmación**: Owner cambia precio de "$10" a "$15", intenta cerrar con X, ve confirmación, hace clic en "Salir", el modal se cierra sin guardar, el precio sigue siendo "$10"
11. **Error al guardar**: Owner edita producto, hay error de red, aparece toast "No se pudo actualizar el producto", el modal permanece abierto con los cambios
12. **Editar descripción vacía**: Producto no tenía descripción, Owner agrega descripción "Deliciosa pizza artesanal", guarda exitosamente

---