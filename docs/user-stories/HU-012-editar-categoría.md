## HU-012: Editar Categoría

### Descripción
Como usuario Owner, quiero editar el nombre de una categoría existente para corregir errores o actualizar la nomenclatura del menú.

### Criterios de Aceptación

**Trigger del Modal:**
- Al hacer clic en botón "Editar" (ícono de lápiz) de una categoría en la lista, abrir modal de edición
- El modal carga automáticamente con los datos actuales de la categoría

**Estructura del Modal:**
- Título: "Editar categoría"
- Campos del formulario:
  - Nombre de la categoría (requerido, input de texto precargado con valor actual)
- Botones:
  - "Cancelar" (secundario, izquierda)
  - "Guardar cambios" (primario, derecha)
- Botón X en esquina superior derecha para cerrar

**Campo Nombre Precargado:**
- El campo muestra el nombre actual de la categoría
- El texto está seleccionado automáticamente para facilitar el reemplazo
- Las validaciones son las mismas que en creación:
  - Requerido
  - Mínimo 2 caracteres, máximo 50 caracteres
  - No puede ser igual a otra categoría existente (excepto la actual)

**Validaciones:**
- Si el campo queda vacío, mostrar error: "El nombre es requerido"
- Si el nombre tiene menos de 2 caracteres, mostrar error: "El nombre debe tener al menos 2 caracteres"
- Si el nombre excede 50 caracteres, mostrar error: "El nombre no puede exceder 50 caracteres"
- Si el nombre ya existe en otra categoría (case-insensitive), mostrar error: "Ya existe una categoría con este nombre"
- Si el nombre es idéntico al actual, permitir guardar (sin cambios)

**Detección de Cambios:**
- El botón "Guardar cambios" está habilitado solo si el nombre es diferente al original Y es válido
- Si el nombre no ha cambiado, el botón permanece deshabilitado (no hay nada que guardar)

**Comportamiento del Botón Guardar:**
- Al hacer clic, mostrar spinner en el botón y cambiar texto a "Guardando..."
- Mientras está en estado de carga, deshabilitar el botón

**Edición Exitosa:**
- Si la edición es exitosa, cerrar el modal automáticamente
- Actualizar la fila correspondiente en la lista con el nuevo nombre
- Mantener el orden alfabético de la lista
- Mostrar toast de éxito: "Categoría actualizada exitosamente"

**Manejo de Errores:**
- Si hay error de red o servidor, mostrar toast: "No se pudo actualizar la categoría. Por favor, intenta de nuevo"
- El modal permanece abierto para permitir reintentos
- Mantener el valor editado en el campo

**Cierre del Modal:**
- Al hacer clic en "Cancelar", cerrar modal sin guardar
- Al hacer clic en X, cerrar modal sin guardar
- Al hacer clic fuera del modal (overlay), cerrar sin guardar
- Al presionar tecla ESC, cerrar sin guardar
- Si hay cambios sin guardar y se intenta cerrar, mostrar confirmación: "¿Deseas salir sin guardar los cambios?"

**Preservación de Datos:**
- Al editar el nombre, se mantienen:
  - El estado de la categoría (Activa/Inactiva)
  - Los productos asociados a la categoría
  - El ID único de la categoría

### Escenarios

1. **Editar nombre exitosamente**: Owner hace clic en "Editar" de categoría "Bebidads" (error tipográfico), el modal se abre con "Bebidads" seleccionado, Owner escribe "Bebidas", hace clic en "Guardar cambios", ve spinner, el modal se cierra, aparece toast "Categoría actualizada exitosamente", la lista muestra "Bebidas"
2. **Campo precargado con texto seleccionado**: Owner hace clic en "Editar" de "Postres", el modal se abre con "Postres" ya seleccionado, Owner puede empezar a escribir inmediatamente para reemplazar
3. **Botón deshabilitado sin cambios**: Owner abre edición de "Entradas", no modifica nada, el botón "Guardar cambios" permanece deshabilitado
4. **Validar nombre duplicado**: Existen "Bebidas" y "Postres", Owner edita "Postres" e intenta cambiarlo a "Bebidas", ve error "Ya existe una categoría con este nombre"
5. **Campo vacío al editar**: Owner abre edición, borra todo el texto, intenta guardar, ve error "El nombre es requerido"
6. **Mantener orden alfabético**: Existen "Bebidas", "Entradas", "Postres", Owner edita "Postres" a "Sopas", al guardar la lista se reordena: "Bebidas", "Entradas", "Sopas"
7. **Preservar estado al editar**: Categoría "Bebidas" está Inactiva, Owner edita nombre a "Drinks", al guardar la categoría "Drinks" sigue Inactiva
8. **Preservar productos asociados**: Categoría "Postres" tiene 8 productos, Owner cambia nombre a "Desserts", después del cambio "Desserts" sigue teniendo 8 productos
9. **Cerrar sin guardar con confirmación**: Owner cambia "Entradas" a "Starters", intenta cerrar con X, ve confirmación "¿Deseas salir sin guardar los cambios?", hace clic en "Salir", el modal se cierra sin guardar, la categoría sigue siendo "Entradas"
10. **Mantener cambios en confirmación**: Owner cambia nombre, ve confirmación de cerrar, hace clic en "Cancelar" en la confirmación, el modal permanece abierto con el texto editado
11. **Error al guardar**: Owner edita "Bebidas" a "Drinks", hace clic en "Guardar", hay error de red, aparece toast "No se pudo actualizar la categoría", el modal permanece abierto con "Drinks" en el campo
12. **Editar con Enter**: Owner edita nombre a "Platos Principales", presiona Enter, los cambios se guardan exitosamente (igual que hacer clic en botón)

---