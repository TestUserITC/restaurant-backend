# Historias de Usuario - Gestión de Menú (Core)
## MVP SaaS Administración de Restaurantes

---

## HU-010: Ver Lista de Categorías

### Descripción
Como usuario Owner, quiero ver todas las categorías del menú del restaurante para tener una visión organizada de cómo está estructurado mi menú y poder gestionar las categorías fácilmente.

### Criterios de Aceptación

**Estructura de la Página:**
- La página muestra un título "Categorías" en la parte superior
- Incluye un botón primario "Nueva categoría" en la esquina superior derecha
- El contenido principal muestra una tabla con las categorías existentes
- Si no hay categorías, mostrar estado vacío con mensaje "No hay categorías creadas" y botón "Crear primera categoría"

**Tabla de Categorías:**
- Columnas visibles:
  - Nombre (texto, ordenable)
  - Productos (número de productos en la categoría)
  - Estado (badge: Activa/Inactiva)
  - Acciones (botones de editar y toggle estado)
- Las filas se pueden ordenar por nombre (A-Z o Z-A) haciendo clic en el encabezado de columna
- Cada fila muestra:
  - Nombre de la categoría con icono representativo si existe
  - Número de productos asociados (ej: "12 productos")
  - Badge de estado: "Activa" (verde) o "Inactiva" (gris)
  - Botón "Editar" (ícono de lápiz)
  - Toggle switch para activar/desactivar

**Ordenamiento por Defecto:**
- Las categorías se muestran ordenadas alfabéticamente (A-Z) por defecto
- Al cargar la página, el encabezado "Nombre" muestra un indicador de orden ascendente

**Acciones Rápidas:**
- Al hacer clic en el toggle de estado, la categoría cambia inmediatamente entre Activa/Inactiva
- Al cambiar estado, mostrar toast de confirmación: "Categoría actualizada correctamente"
- Al hacer clic en "Editar", abrir modal de edición de categoría
- Al hacer clic en el botón "Nueva categoría", abrir modal de creación

**Estados de Categoría:**
- Activa: La categoría y sus productos están disponibles para selección en el POS
- Inactiva: La categoría y sus productos NO están disponibles en el POS pero se mantienen en el sistema

**Conteo de Productos:**
- Si la categoría tiene 0 productos, mostrar "Sin productos"
- Si tiene 1 producto, mostrar "1 producto"
- Si tiene más de 1, mostrar "X productos"
- El conteo incluye todos los productos (disponibles y no disponibles)

**Estados de Carga:**
- Al cargar la página, mostrar skeleton loader con estructura de tabla
- Al cambiar estado de categoría, mostrar spinner en el toggle mientras se procesa
- La carga inicial debe completarse en menos de 2 segundos

**Manejo de Errores:**
- Si hay error al cargar categorías, mostrar mensaje: "Error al cargar categorías" con botón "Reintentar"
- Si hay error al cambiar estado, mostrar toast de error: "No se pudo actualizar la categoría. Intenta de nuevo"
- El toggle vuelve a su estado anterior si falla la actualización

**Responsive Design:**
- En desktop (>1024px): Mostrar tabla completa con todas las columnas
- En tablet (768px-1024px): Tabla con scroll horizontal si es necesario
- En mobile (<768px): Convertir tabla en cards, cada card muestra nombre, conteo productos, estado y botones de acción

**Permisos:**
- Esta página solo es accesible para usuarios con rol Owner
- Si un Cajero intenta acceder, ver página 403

### Escenarios

1. **Ver lista con categorías existentes**: Owner accede a `/menu/categorias`, ve tabla con 5 categorías ordenadas alfabéticamente con sus nombres, conteo de productos, estados y botones de acción
2. **Estado vacío sin categorías**: Owner accede a página por primera vez, ve mensaje "No hay categorías creadas" con botón "Crear primera categoría"
3. **Cambiar estado de categoría a Inactiva**: Owner hace clic en toggle de categoría "Bebidas" (actualmente Activa), el toggle muestra spinner, la categoría cambia a Inactiva, badge cambia a gris, aparece toast "Categoría actualizada correctamente"
4. **Cambiar estado de categoría a Activa**: Owner hace clic en toggle de categoría "Postres" (actualmente Inactiva), la categoría cambia a Activa, badge cambia a verde
5. **Ordenar por nombre descendente**: Owner hace clic en encabezado "Nombre", la tabla se reordena de Z-A, el indicador cambia a orden descendente
6. **Ordenar por nombre ascendente nuevamente**: Owner hace clic nuevamente en "Nombre", la tabla vuelve al orden A-Z
7. **Ver categoría sin productos**: Categoría "Promociones" muestra "Sin productos" en columna de productos
8. **Ver categoría con múltiples productos**: Categoría "Platos Fuertes" muestra "23 productos"
9. **Click en Nueva categoría**: Owner hace clic en botón "Nueva categoría", se abre modal de creación de categoría
10. **Click en Editar**: Owner hace clic en botón "Editar" de categoría "Entradas", se abre modal de edición con los datos de esa categoría
11. **Error al cargar categorías**: Hay error de red al cargar la página, Owner ve mensaje "Error al cargar categorías" con botón "Reintentar", hace clic y los datos cargan correctamente
12. **Error al cambiar estado**: Owner intenta cambiar estado de categoría pero hay error de red, toggle vuelve a posición original, aparece toast "No se pudo actualizar la categoría. Intenta de nuevo"
13. **Vista en mobile**: Owner accede desde teléfono, ve categorías como cards apiladas verticalmente, cada card muestra nombre, estado, conteo y botones
14. **Cajero intenta acceder**: Usuario con rol Cajero intenta navegar a `/menu/categorias`, ve página 403 con mensaje "No tienes permisos para acceder a esta sección"

---

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

## HU-014: Ver Lista de Productos

### Descripción
Como usuario Owner, quiero ver todos los productos del menú organizados por categoría para tener control completo sobre los items que ofrezco y poder gestionarlos fácilmente.

### Criterios de Aceptación

**Estructura de la Página:**
- La página muestra un título "Productos" en la parte superior
- Incluye un botón primario "Nuevo producto" en la esquina superior derecha
- Incluye un filtro dropdown "Todas las categorías" para filtrar por categoría específica
- El contenido principal muestra una tabla con los productos existentes
- Si no hay productos, mostrar estado vacío con mensaje "No hay productos creados" y botón "Crear primer producto"

**Filtro por Categoría:**
- Dropdown con opciones:
  - "Todas las categorías" (opción por defecto)
  - Lista de todas las categorías existentes
- Al seleccionar una categoría, la tabla muestra solo productos de esa categoría
- Al seleccionar "Todas las categorías", mostrar todos los productos

**Tabla de Productos:**
- Columnas visibles:
  - Imagen (thumbnail pequeño, 60x60px)
  - Nombre (texto, ordenable)
  - Categoría (badge con nombre de categoría)
  - Precio (formato moneda, ordenable)
  - Estado (badge: Disponible/No disponible)
  - Acciones (botones de editar y toggle estado)
- Las filas se pueden ordenar por nombre (A-Z o Z-A) o por precio (menor a mayor, mayor a menor)
- Cada fila muestra toda la información del producto de forma clara

**Imagen del Producto:**
- Si el producto tiene imagen, mostrar thumbnail de 60x60px con bordes redondeados
- Si no tiene imagen, mostrar placeholder con ícono de imagen
- La imagen es clickeable y abre preview en tamaño completo (modal lightbox)

**Badge de Categoría:**
- Muestra el nombre de la categoría en un badge con color distintivo
- Si el filtro está activo en una categoría, los badges de esa categoría se destacan visualmente

**Formato de Precio:**
- Usar símbolo de moneda configurado en el sistema (ej: "$", "€", "S/")
- Formato con separador de miles y 2 decimales (ej: "$1,250.00")

**Estados del Producto:**
- Disponible (badge verde): El producto está activo y disponible para venta en el POS
- No disponible (badge gris): El producto existe pero no está disponible para venta

**Acciones Rápidas:**
- Toggle switch para cambiar estado Disponible/No disponible
- Al cambiar estado, mostrar toast: "Producto actualizado correctamente"
- Botón "Editar" (ícono de lápiz) abre modal de edición
- Botón "Eliminar" (ícono de basura) abre modal de confirmación

**Ordenamiento por Defecto:**
- Los productos se muestran ordenados alfabéticamente (A-Z) por nombre
- Al cargar la página, el encabezado "Nombre" muestra indicador de orden ascendente

**Paginación:**
- Si hay más de 20 productos, implementar paginación
- Mostrar selector de "Elementos por página": 10, 20, 50
- Mostrar información: "Mostrando 1-20 de 45 productos"
- Botones: Anterior, 1, 2, 3, Siguiente

**Búsqueda Rápida:**
- Campo de búsqueda con placeholder "Buscar producto..."
- Búsqueda en tiempo real mientras se escribe (debounce de 300ms)
- Busca en nombre y categoría del producto
- Limpiar búsqueda con botón X dentro del campo

**Estados de Carga:**
- Al cargar la página, mostrar skeleton loader con estructura de tabla
- Al filtrar o buscar, mostrar indicador de carga
- Al cambiar estado de producto, mostrar spinner en el toggle

**Manejo de Errores:**
- Si hay error al cargar productos, mostrar mensaje: "Error al cargar productos" con botón "Reintentar"
- Si hay error al cambiar estado, mostrar toast: "No se pudo actualizar el producto. Intenta de nuevo"

**Responsive Design:**
- En desktop (>1024px): Tabla completa con todas las columnas
- En tablet (768px-1024px): Tabla con scroll horizontal
- En mobile (<768px): Convertir en cards, cada card muestra imagen, nombre, categoría, precio, estado y botones

**Permisos:**
- Esta página solo es accesible para usuarios con rol Owner
- Si un Cajero intenta acceder, ver página 403

### Escenarios

1. **Ver lista con productos existentes**: Owner accede a `/menu/productos`, ve tabla con 15 productos mostrando imagen, nombre, categoría, precio, estado y botones de acción
2. **Estado vacío sin productos**: Owner accede por primera vez, ve mensaje "No hay productos creados" con botón "Crear primer producto"
3. **Filtrar por categoría específica**: Owner selecciona "Bebidas" en el dropdown, la tabla muestra solo los 8 productos de categoría Bebidas
4. **Volver a ver todas las categorías**: Owner selecciona "Todas las categorías", la tabla vuelve a mostrar todos los productos
5. **Cambiar estado a No disponible**: Owner hace clic en toggle de producto "Coca Cola" (actualmente Disponible), el producto cambia a No disponible, badge cambia a gris
6. **Ordenar por precio ascendente**: Owner hace clic en encabezado "Precio", la tabla se reordena de menor a mayor precio
7. **Ordenar por precio descendente**: Owner hace clic nuevamente en "Precio", la tabla se reordena de mayor a menor precio
8. **Buscar producto**: Owner escribe "ham" en búsqueda, la tabla muestra solo "Hamburguesa Clásica" y "Hamburguesa con Queso"
9. **Limpiar búsqueda**: Owner hace clic en X del campo de búsqueda, la búsqueda se limpia, la tabla vuelve a mostrar todos los productos
10. **Ver imagen en grande**: Owner hace clic en thumbnail de producto, se abre modal lightbox mostrando imagen en tamaño completo
11. **Producto sin imagen**: Producto "Agua" no tiene imagen, muestra placeholder con ícono de imagen
12. **Paginación con muchos productos**: Hay 45 productos, la tabla muestra primeros 20 con paginación "1-20 de 45 productos", Owner hace clic en página 2, ve productos 21-40
13. **Cambiar elementos por página**: Owner cambia selector a "50 elementos por página", la tabla muestra todos los 45 productos sin paginación
14. **Click en Nuevo producto**: Owner hace clic en "Nuevo producto", se abre modal de creación de producto
15. **Click en Editar**: Owner hace clic en "Editar" de producto "Pizza Margarita", se abre modal de edición con los datos de ese producto
16. **Error al cargar productos**: Hay error de red, Owner ve mensaje "Error al cargar productos" con botón "Reintentar"
17. **Vista en mobile**: Owner accede desde teléfono, ve productos como cards apiladas, cada card muestra imagen, nombre, precio, categoría, estado y botones
18. **Badge de categoría destacado con filtro**: Owner filtra por "Postres", los badges "Postres" en la tabla se destacan con color más intenso
19. **Cajero intenta acceder**: Usuario Cajero intenta navegar a `/menu/productos`, ve página 403 "No tienes permisos para acceder a esta sección"

---

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

## HU-017: Eliminar Producto

### Descripción
Como usuario Owner, quiero eliminar productos del menú que ya no ofrezco para mantener el catálogo actualizado y limpio.

### Criterios de Aceptación

**Trigger de Eliminación:**
- En la tabla de productos, columna "Acciones" incluye botón "Eliminar" (ícono de basura)
- El botón está siempre habilitado (no hay restricción por ventas históricas)
- Al hacer clic, abrir modal de confirmación

**Modal de Confirmación:**
- Título: "¿Eliminar producto?"
- Mensaje: "¿Estás seguro de que deseas eliminar '[Nombre del producto]'? Este producto ya no estará disponible en el menú."
- Submensaje: "Nota: Las ventas históricas de este producto se mantendrán."
- El nombre del producto se muestra en negrita
- Botones:
  - "Cancelar" (secundario, izquierda)
  - "Eliminar" (destructivo/rojo, derecha)

**Comportamiento de Eliminación:**
- Al hacer clic en "Eliminar", mostrar spinner en el botón y cambiar texto a "Eliminando..."
- Deshabilitar ambos botones durante el proceso
- Si la eliminación es exitosa:
  - Cerrar el modal automáticamente
  - Remover el producto de la lista con animación de salida
  - Mostrar toast de éxito: "Producto eliminado exitosamente"

**Preservación de Datos Históricos:**
- La eliminación es "soft delete" (desactivación)
- Las ventas históricas que incluyen este producto se mantienen intactas
- En reportes históricos, el producto sigue apareciendo con su nombre original
- El producto simplemente deja de estar disponible para nuevas ventas

**Manejo de Errores:**
- Si hay error al eliminar, mostrar toast: "No se pudo eliminar el producto. Por favor, intenta de nuevo"
- El modal permanece abierto para permitir reintentos

**Impacto en Categoría:**
- Al eliminar un producto, el conteo de productos de su categoría se actualiza automáticamente
- Si era el último producto de la categoría, la categoría ahora muestra "Sin productos" y puede ser eliminada

**Estado Vacío Después de Eliminar:**
- Si después de eliminar no quedan más productos, mostrar estado vacío: "No hay productos creados" con botón "Crear primer producto"

**Cierre del Modal:**
- Al hacer clic en "Cancelar", cerrar modal sin eliminar
- Al hacer clic en X, cerrar modal sin eliminar
- Al hacer clic fuera del modal (overlay), cerrar sin eliminar
- Al presionar ESC, cerrar sin eliminar

### Escenarios

1. **Eliminar producto exitosamente**: Owner hace clic en "Eliminar" de producto "Tacos", ve modal de confirmación con nombre "Tacos" en negrita, hace clic en "Eliminar", ve spinner, el modal se cierra, la fila desaparece con animación, aparece toast "Producto eliminado exitosamente"
2. **Cancelar eliminación**: Owner hace clic en "Eliminar", ve modal, hace clic en "Cancelar", el modal se cierra sin eliminar, el producto permanece en la lista
3. **Cerrar modal con X**: Owner abre modal de eliminación, hace clic en X, el modal se cierra sin eliminar
4. **Mantener ventas históricas**: Owner elimina producto "Pizza" que tiene 50 ventas del mes pasado, el producto se elimina pero las ventas del mes pasado siguen mostrando "Pizza" correctamente
5. **Actualizar conteo de categoría**: Categoría "Bebidas" tiene 5 productos, Owner elimina "Coca Cola", el conteo de "Bebidas" ahora muestra "4 productos"
6. **Último producto de categoría**: Categoría "Promociones" tiene solo 1 producto, Owner lo elimina, la categoría ahora muestra "Sin productos" y su botón "Eliminar" se habilita
7. **Estado vacío después de eliminar todo**: Owner tiene 3 productos, los elimina todos, ve estado vacío "No hay productos creados" con botón "Crear primer producto"
8. **Error al eliminar**: Owner intenta eliminar producto, hay error de red, aparece toast "No se pudo eliminar el producto", el modal permanece abierto
9. **Eliminar con filtro activo**: Filtro activo en "Bebidas" que tiene 5 productos, Owner elimina uno, la lista ahora muestra 4 productos de Bebidas
10. **Cerrar con ESC**: Owner abre modal de confirmación, presiona tecla ESC, el modal se cierra sin eliminar

---

## Resumen de Navegación en Gestión de Menú

**Estructura de URLs:**
- `/menu` → Redirige a `/menu/categorias` (página principal)
- `/menu/categorias` → Lista de categorías
- `/menu/productos` → Lista de productos

**Navegación en Menú Lateral:**
- Ítem "Menú" con sub-ítems:
  - Categorías
  - Productos
- Al hacer clic en "Menú", expandir sub-menú
- Marcar como activo el sub-ítem de la página actual

**Breadcrumb:**
- `/menu/categorias`: Dashboard > Menú > Categorías
- `/menu/productos`: Dashboard > Menú > Productos

---

## Notas Técnicas

**Imágenes:**
- Almacenar en storage/CDN
- Generar thumbnails automáticamente (60x60, 200x200)
- Optimizar al subir (comprimir, convertir a WebP si es posible)
- Lazy loading de imágenes en la lista

**Validación de Nombres:**
- Validar unicidad case-insensitive
- Trimear espacios al inicio y final
- No permitir solo espacios

**Performance:**
- Cargar productos con paginación o virtual scrolling si hay muchos
- Caché de lista de categorías (usada en múltiples lugares)
- Optimizar queries con índices en nombre, categoría, estado

**Soft Delete:**
- Productos eliminados no se borran físicamente
- Campo deleted_at para marcar como eliminado
- Queries excluyen productos eliminados por defecto
- Mantener integridad referencial con órdenes históricas

**Estados de Producto:**
- Disponible: Activo y visible en POS
- No disponible: Existe pero no se puede vender (temporalmente agotado)
- Eliminado (soft delete): No aparece en ningún lado excepto historial

**Formatos de Moneda:**
- Usar la moneda configurada en settings
- Todos los precios en formato consistente
- Validar que precio > 0
