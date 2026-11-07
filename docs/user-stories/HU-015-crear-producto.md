## HU-015: Crear Producto

### Descripción
Como usuario Owner, quiero crear nuevos productos para ampliar el menú del restaurante y poder ofrecerlos a los clientes en el punto de venta.

### Criterios de Aceptación

**Trigger del Modal:**
- Al hacer clic en "Nuevo producto" desde la lista de productos, abrir modal de creación
- Al hacer clic en "Crear primer producto" desde estado vacío, abrir modal de creación

**Estructura del Modal:**
- Título: "Nuevo producto"
- El modal es más grande que el de categorías (width: 600px en desktop)
- Campos del formulario organizados verticalmente:
  - Imagen del producto (opcional)
  - Nombre del producto (requerido)
  - Categoría (requerido, dropdown)
  - Precio (requerido)
  - Descripción (opcional, textarea)
- Botones:
  - "Cancelar" (secundario, izquierda)
  - "Crear producto" (primario, derecha)
- Botón X en esquina superior derecha para cerrar

**Campo Imagen (opcional):**
- Área de carga de imagen con texto: "Arrastra una imagen o haz clic para seleccionar"
- Preview de la imagen seleccionada (máximo 200x200px)
- Botón "Cambiar imagen" si ya hay una seleccionada
- Formatos aceptados: JPG, PNG, WebP
- Tamaño máximo: 5MB
- Si se excede el tamaño, mostrar error: "La imagen no puede superar 5MB"
- Si el formato no es válido, mostrar error: "Solo se aceptan imágenes JPG, PNG o WebP"

**Campo Nombre (requerido):**
- Label: "Nombre del producto *"
- Placeholder: "Ej: Hamburguesa Clásica, Coca Cola 500ml"
- Mínimo 2 caracteres, máximo 100 caracteres
- Error si vacío: "El nombre es requerido"
- Error si < 2 caracteres: "El nombre debe tener al menos 2 caracteres"

**Campo Categoría (requerido):**
- Label: "Categoría *"
- Dropdown con lista de categorías activas del sistema
- Placeholder: "Selecciona una categoría"
- Si no hay categorías creadas, mostrar mensaje: "Primero debes crear una categoría" con botón "Crear categoría"
- Error si no se selecciona: "La categoría es requerida"

**Campo Precio (requerido):**
- Label: "Precio *"
- Input numérico con símbolo de moneda (ej: "$")
- Placeholder: "0.00"
- Acepta decimales (2 dígitos después del punto)
- Mínimo: 0.01 (debe ser mayor a 0)
- Máximo: 999999.99
- Error si vacío o 0: "El precio es requerido y debe ser mayor a 0"
- Error si excede máximo: "El precio no puede superar $999,999.99"
- Formatear automáticamente mientras escribe (ej: "1250" → "1,250.00")

**Campo Descripción (opcional):**
- Label: "Descripción"
- Textarea de 3-4 líneas
- Placeholder: "Descripción del producto (opcional)"
- Máximo 500 caracteres
- Mostrar contador: "0/500 caracteres"
- Error si excede: "La descripción no puede superar 500 caracteres"

**Estado Inicial del Producto:**
- Al crear, el producto se crea automáticamente con estado "Disponible"
- No hay opción de elegir el estado inicial

**Validación de Campos Requeridos:**
- El botón "Crear producto" está deshabilitado hasta que todos los campos requeridos sean válidos
- Visual: campos requeridos marcados con asterisco (*)

**Comportamiento del Botón Crear:**
- Al hacer clic, validar todos los campos
- Si hay errores, mostrar mensajes debajo de cada campo con error
- Si todo es válido, mostrar spinner en el botón y cambiar texto a "Creando..."
- Deshabilitar el botón mientras se procesa

**Creación Exitosa:**
- Si la creación es exitosa, cerrar el modal automáticamente
- Agregar el nuevo producto a la lista
- Si había filtro activo por categoría, mantener el filtro y mostrar el producto si corresponde
- Mostrar toast de éxito: "Producto creado exitosamente"

**Manejo de Errores:**
- Si hay error de red o servidor, mostrar toast: "No se pudo crear el producto. Por favor, intenta de nuevo"
- El modal permanece abierto con los datos ingresados
- Si el nombre del producto ya existe, mostrar error: "Ya existe un producto con este nombre"

**Carga de Imagen:**
- Mientras se sube la imagen, mostrar indicador de carga sobre el preview
- Si hay error al subir, mostrar: "Error al cargar la imagen. Intenta con otra"

**Cierre del Modal:**
- Al hacer clic en "Cancelar", cerrar modal sin guardar
- Al hacer clic en X, cerrar modal sin guardar
- Al hacer clic fuera del modal (overlay), cerrar sin guardar
- Al presionar ESC, cerrar sin guardar
- Si hay datos ingresados y se intenta cerrar, mostrar confirmación: "¿Deseas salir sin guardar?"

**Creación Rápida de Categoría:**
- Si no hay categorías y Owner hace clic en "Crear categoría" desde el mensaje, abrir modal de creación de categoría
- Al crear la categoría, volver automáticamente al modal de producto con la nueva categoría seleccionada

### Escenarios

1. **Crear producto completo exitosamente**: Owner abre modal, carga imagen de hamburguesa, ingresa nombre "Hamburguesa Clásica", selecciona categoría "Platos Fuertes", ingresa precio "12.50", escribe descripción "Carne, lechuga, tomate, queso", hace clic en "Crear producto", ve spinner, el modal se cierra, aparece toast "Producto creado exitosamente", el producto aparece en la lista con estado Disponible
2. **Crear producto sin imagen**: Owner completa todos los campos excepto imagen, crea el producto exitosamente, el producto aparece con placeholder de imagen
3. **Crear producto sin descripción**: Owner completa campos requeridos, deja descripción vacía, crea exitosamente
4. **Validar campos requeridos vacíos**: Owner hace clic en "Crear producto" sin llenar nada, ve errores en Nombre, Categoría y Precio
5. **Validar precio mínimo**: Owner ingresa precio "0", intenta crear, ve error "El precio es requerido y debe ser mayor a 0"
6. **Validar precio máximo**: Owner ingresa "1000000" (un millón), ve error "El precio no puede superar $999,999.99"
7. **Formatear precio automáticamente**: Owner ingresa "1250", el campo muestra automáticamente "$1,250.00"
8. **Contador de caracteres en descripción**: Owner escribe en descripción, ve contador actualizar "45/500 caracteres"
9. **Descripción excede límite**: Owner escribe 550 caracteres, ve error "La descripción no puede superar 500 caracteres"
10. **Imagen excede tamaño máximo**: Owner intenta cargar imagen de 8MB, ve error "La imagen no puede superar 5MB"
11. **Formato de imagen inválido**: Owner intenta cargar archivo .gif, ve error "Solo se aceptan imágenes JPG, PNG o WebP"
12. **Sin categorías creadas**: Owner abre modal de producto, ve mensaje "Primero debes crear una categoría" con botón "Crear categoría"
13. **Crear categoría desde producto**: Owner hace clic en "Crear categoría", se abre modal de categoría, crea "Bebidas", el modal de categoría se cierra, vuelve a modal de producto con "Bebidas" seleccionada automáticamente
14. **Nombre duplicado**: Ya existe "Coca Cola", Owner intenta crear otro "Coca Cola", ve error "Ya existe un producto con este nombre"
15. **Cerrar con datos sin guardar**: Owner completa varios campos, intenta cerrar con X, ve confirmación "¿Deseas salir sin guardar?", hace clic en "Salir", el modal se cierra
16. **Producto aparece en lista filtrada**: Filtro activo en "Bebidas", Owner crea producto en categoría "Bebidas", al cerrar modal el producto aparece inmediatamente en la lista
17. **Producto no aparece con filtro diferente**: Filtro activo en "Bebidas", Owner crea producto en categoría "Postres", al cerrar modal el producto NO aparece (porque el filtro sigue activo en Bebidas)
18. **Preview de imagen**: Owner arrastra imagen, ve preview de 200x200px, hace clic en "Cambiar imagen", selecciona otra, el preview se actualiza
19. **Error al crear**: Owner completa todos los campos, hace clic en "Crear", hay error de red, aparece toast "No se pudo crear el producto", el modal permanece abierto con los datos

---