## HU-011: Crear Categoría

### Descripción
Como usuario Owner, quiero crear nuevas categorías para organizar los productos del menú de manera lógica y facilitar la navegación en el punto de venta.

### Criterios de Aceptación

**Trigger del Modal:**
- Al hacer clic en "Nueva categoría" desde la lista de categorías, abrir modal de creación
- Al hacer clic en "Crear primera categoría" desde estado vacío, abrir modal de creación

**Estructura del Modal:**
- Título: "Nueva categoría"
- Campos del formulario:
  - Nombre de la categoría (requerido, input de texto)
- Botones:
  - "Cancelar" (secundario, izquierda)
  - "Crear categoría" (primario, derecha)
- Botón X en esquina superior derecha para cerrar

**Campo Nombre:**
- Label: "Nombre de la categoría"
- Placeholder: "Ej: Bebidas, Platos principales, Postres"
- Requerido (marcado con asterisco *)
- Mínimo 2 caracteres, máximo 50 caracteres
- Permite letras, números, espacios, y algunos caracteres especiales (guion, paréntesis)

**Validaciones:**
- Si el campo está vacío al intentar crear, mostrar error: "El nombre es requerido"
- Si el nombre tiene menos de 2 caracteres, mostrar error: "El nombre debe tener al menos 2 caracteres"
- Si el nombre tiene más de 50 caracteres, mostrar error: "El nombre no puede exceder 50 caracteres"
- Si el nombre ya existe (case-insensitive), mostrar error: "Ya existe una categoría con este nombre"
- Los mensajes de error aparecen debajo del campo en color rojo

**Estado Inicial de la Categoría:**
- Al crear, la categoría se crea automáticamente con estado "Activa"
- No hay opción de elegir el estado inicial (siempre Activa por defecto)

**Comportamiento del Botón Crear:**
- El botón "Crear categoría" está habilitado solo si el campo tiene contenido válido
- Al hacer clic, mostrar spinner en el botón y cambiar texto a "Creando..."
- Mientras está en estado de carga, deshabilitar el botón

**Creación Exitosa:**
- Si la creación es exitosa, cerrar el modal automáticamente
- Actualizar la lista de categorías mostrando la nueva categoría
- Mostrar toast de éxito: "Categoría creada exitosamente"
- La nueva categoría aparece en la lista ordenada alfabéticamente

**Manejo de Errores:**
- Si hay error de red o servidor, mostrar toast: "No se pudo crear la categoría. Por favor, intenta de nuevo"
- El modal permanece abierto para permitir reintentos
- Mantener el valor ingresado en el campo

**Cierre del Modal:**
- Al hacer clic en "Cancelar", cerrar modal sin guardar
- Al hacer clic en X, cerrar modal sin guardar
- Al hacer clic fuera del modal (overlay), cerrar sin guardar
- Al presionar tecla ESC, cerrar sin guardar
- Si hay texto ingresado y se intenta cerrar, mostrar confirmación: "¿Deseas salir sin guardar?"

**Focus y UX:**
- Al abrir el modal, el cursor debe estar automáticamente en el campo "Nombre"
- Al presionar Enter en el campo, intentar crear la categoría (equivalente a clic en botón)

### Escenarios

1. **Crear categoría exitosamente**: Owner abre modal, ingresa "Bebidas", hace clic en "Crear categoría", ve spinner por 1 segundo, el modal se cierra, aparece toast "Categoría creada exitosamente", la lista muestra la nueva categoría "Bebidas" con estado Activa
2. **Campo vacío al intentar crear**: Owner abre modal, deja campo vacío, hace clic en "Crear categoría", ve mensaje de error "El nombre es requerido" debajo del campo
3. **Nombre muy corto**: Owner ingresa "A" (1 carácter), intenta crear, ve error "El nombre debe tener al menos 2 caracteres"
4. **Nombre muy largo**: Owner ingresa texto de 60 caracteres, intenta crear, ve error "El nombre no puede exceder 50 caracteres"
5. **Nombre duplicado**: Ya existe categoría "Bebidas", Owner intenta crear otra "bebidas" (minúsculas), ve error "Ya existe una categoría con este nombre"
6. **Cerrar modal con Cancelar**: Owner ingresa "Postres", hace clic en "Cancelar", el modal se cierra sin guardar, la categoría no se crea
7. **Cerrar modal con X**: Owner ingresa texto, hace clic en X, el modal se cierra sin guardar
8. **Cerrar modal con ESC**: Owner ingresa texto, presiona tecla ESC, el modal se cierra sin guardar
9. **Cerrar modal con click fuera**: Owner ingresa texto, hace clic en el overlay oscuro fuera del modal, el modal se cierra sin guardar
10. **Confirmación al cerrar con datos**: Owner ingresa "Entradas", intenta cerrar con X, ve confirmación "¿Deseas salir sin guardar?", hace clic en "Salir" para confirmar, el modal se cierra sin guardar
11. **Focus automático en campo**: Owner hace clic en "Nueva categoría", el modal se abre con el cursor automáticamente en el campo "Nombre", puede empezar a escribir de inmediato
12. **Crear con Enter**: Owner ingresa "Ensaladas", presiona tecla Enter, la categoría se crea exitosamente (igual que hacer clic en botón)
13. **Error al crear**: Owner ingresa "Sopas", hace clic en "Crear", hay error de red, aparece toast "No se pudo crear la categoría. Por favor, intenta de nuevo", el modal permanece abierto con "Sopas" en el campo
14. **Nueva categoría aparece ordenada**: Existen categorías "Bebidas" y "Postres", Owner crea "Entradas", al cerrar el modal la lista muestra: "Bebidas", "Entradas", "Postres" (orden alfabético)

---