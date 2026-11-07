# Historias de Usuario - Configuración Básica
## MVP SaaS Administración de Restaurantes

---

## HU-037: Ver Configuración del Restaurante

### Descripción
Como usuario Owner, quiero ver la configuración actual de mi restaurante para conocer los datos registrados y verificar que la información esté correcta.

### Criterios de Aceptación

**Estructura de la Página:**
- La página muestra un título "Configuración del Restaurante" en la parte superior
- Incluye breadcrumb: Dashboard > Configuración
- Botón "Editar" en la esquina superior derecha
- El contenido está organizado en una card o sección principal
- Si no hay configuración guardada (primera vez), mostrar formulario de configuración inicial

**Información Mostrada:**
- Los datos se muestran en formato de lectura (no editables directamente)
- Organización clara con labels y valores:
  - **Nombre del restaurante**: [Valor actual]
  - **Dirección**: [Valor actual]
  - **Moneda**: [Símbolo y código, ej: "$ - USD (Dólar estadounidense)"]
  - **Impuesto**: [Porcentaje, ej: "18%"]

**Formato Visual:**
- Cada campo tiene su label claramente identificado
- Los valores están destacados (negrita o tamaño mayor)
- Espaciado adecuado entre campos para legibilidad
- Diseño limpio tipo "ficha informativa"

**Botón Editar:**
- Al hacer clic, cambiar la vista a modo edición
- Los campos se convierten en inputs editables
- El botón "Editar" cambia a botones "Cancelar" y "Guardar cambios"

**Estado Inicial (Primera Configuración):**
- Si el restaurante no tiene configuración guardada (registro nuevo):
  - Mostrar mensaje: "Configura los datos básicos de tu restaurante"
  - Mostrar formulario directamente en modo edición
  - Botón "Guardar configuración" (en lugar de "Guardar cambios")

**Valores por Defecto (Primera Configuración):**
- Nombre: Vacío (debe completarse)
- Dirección: Vacío (opcional)
- Moneda: "USD - Dólar estadounidense" (predeterminado)
- Impuesto: "0%" (predeterminado)

**Estados de Carga:**
- Al cargar la página, mostrar skeleton loader con estructura de campos
- La carga debe completarse en menos de 2 segundos

**Manejo de Errores:**
- Si hay error al cargar configuración, mostrar: "Error al cargar configuración" con botón "Reintentar"

**Responsive Design:**
- En desktop: Card centrada con ancho máximo (600-700px)
- En tablet/mobile: Card ocupa todo el ancho con padding adecuado

**Permisos:**
- Esta página solo es accesible para usuarios con rol Owner
- Si un Cajero intenta acceder, ver página 403 "No tienes permisos para acceder a esta sección"

### Escenarios

1. **Ver configuración existente**: Owner accede a `/settings`, ve configuración actual: "Restaurante El Sabor", "Calle Principal 123", "$ - USD", "18%"
2. **Primera vez sin configuración**: Owner recién registrado accede a `/settings`, ve mensaje "Configura los datos básicos de tu restaurante" y formulario en modo edición
3. **Click en Editar**: Owner hace clic en "Editar", la vista cambia a modo edición, todos los campos se vuelven editables, aparecen botones "Cancelar" y "Guardar cambios"
4. **Formato de moneda legible**: Owner ve moneda como "$ - USD (Dólar estadounidense)" en lugar de solo código
5. **Impuesto formateado**: Owner ve impuesto como "18%" (con símbolo de porcentaje)
6. **Campo dirección vacío**: Owner configuró solo nombre y moneda, la dirección muestra "-" o "Sin dirección configurada"
7. **Error al cargar**: Hay error de red al cargar configuración, Owner ve mensaje "Error al cargar configuración" con botón "Reintentar", hace clic y los datos cargan
8. **Vista en mobile**: Owner accede desde teléfono, ve card de configuración ocupando todo el ancho con campos apilados verticalmente
9. **Cajero intenta acceder**: Usuario Cajero intenta navegar a `/settings`, ve página 403 "No tienes permisos para acceder a esta sección"

---

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

## HU-039: Impacto de la Configuración en el Sistema

### Descripción
Como usuario Owner, necesito que los cambios en la configuración se apliquen correctamente en todas las partes del sistema donde se utilizan estos valores.

### Criterios de Aceptación

**Uso del Nombre del Restaurante:**
- Se muestra en:
  - Header/navbar de la aplicación (opcional)
  - Tickets de venta impresos
  - Facturas (si aplica)
  - Emails automáticos (si aplica)
  - Footer de exportaciones (opcional)
- Actualización: Inmediata al guardar

**Uso de la Dirección:**
- Se muestra en:
  - Tickets de venta impresos (si está configurada)
  - Facturas (si aplica)
  - Información de contacto (si aplica)
- Si no hay dirección configurada, no mostrar en tickets
- Actualización: Inmediata al guardar

**Uso de la Moneda:**
- Se aplica en:
  - Todos los precios de productos (menú)
  - Totales en POS
  - Totales en órdenes
  - Totales en historial de ventas
  - Reportes y exportaciones
  - Dashboard (KPIs)
- El símbolo de moneda ($, €, S/) se muestra antes o después del número según convención
- Actualización: Inmediata al guardar (refrescar vistas abiertas)

**Uso del Impuesto:**
- Se aplica en:
  - Cálculo de totales en POS (nuevas ventas)
  - Cálculo de totales en órdenes nuevas
  - Resumen de ventas (nuevas)
- NO se aplica retroactivamente a:
  - Ventas anteriores (mantienen su impuesto original)
  - Órdenes cerradas (mantienen su impuesto original)
- Actualización: Inmediata al guardar, afecta solo transacciones nuevas

**Validación de Consistencia:**
- Al cambiar moneda, validar que todos los precios siguen siendo válidos
- Al cambiar impuesto, recalcular totales en carrito del POS (si hay uno activo)
- Mostrar advertencias apropiadas si hay impacto

**Notificación de Cambios:**
- Si hay usuarios con sesión activa cuando se cambia la configuración:
  - Notificar con mensaje: "La configuración del sistema ha sido actualizada"
  - Sugerir refrescar la página si es necesario
  - Actualizar automáticamente valores visibles (ideal)

**Preservación de Datos Históricos:**
- Las ventas anteriores mantienen:
  - El porcentaje de impuesto con el que fueron calculadas
  - La moneda original (aunque cambie la configuración)
- Esto evita discrepancias en reportes históricos

**Valores de Configuración en Base de Datos:**
- Almacenar como registro único por restaurante
- Incluir timestamps (created_at, updated_at)
- Registrar usuario que realizó el último cambio (audit)

**Configuración Inicial Obligatoria:**
- Al crear una cuenta nueva, solicitar configuración básica
- No permitir usar el sistema sin configurar al menos:
  - Nombre del restaurante
  - Moneda
  - Impuesto (puede ser 0%)
- La dirección es opcional

### Escenarios

1. **Cambio de nombre refleja en tickets**: Owner cambia nombre a "El Sabor Restaurant", realiza venta, imprime ticket, el ticket muestra el nuevo nombre
2. **Cambio de moneda actualiza POS**: Owner cambia de "$" a "S/", accede al POS, todos los precios ahora muestran "S/" en lugar de "$"
3. **Cambio de moneda actualiza historial**: Owner cambia moneda, accede a historial de ventas, todas las ventas nuevas muestran "S/", pero ventas anteriores mantienen "$" (datos históricos)
4. **Cambio de impuesto afecta nueva venta**: Owner cambia impuesto de 18% a 16%, crea nueva orden en POS con $100 subtotal, el impuesto calculado es $16 (no $18)
5. **Cambio de impuesto NO afecta ventas anteriores**: Owner cambia impuesto, consulta venta de ayer, la venta mantiene el 18% original con el que fue registrada
6. **Dirección en ticket**: Owner configura dirección "Calle Principal 123", imprime ticket de venta, el ticket incluye la dirección debajo del nombre
7. **Ticket sin dirección**: Owner no ha configurado dirección, imprime ticket, el ticket muestra solo nombre del restaurante sin dirección
8. **Actualización en dashboard**: Owner cambia moneda a "€", accede al dashboard, los KPIs de ventas muestran "€1,250.00" en lugar de "$1,250.00"
9. **Recálculo en carrito activo**: Owner tiene carrito con productos en POS, cambia impuesto de 18% a 20%, el total en el carrito se recalcula automáticamente con el nuevo 20%
10. **Notificación a otros usuarios**: Owner cambia configuración mientras Cajero tiene sesión abierta en POS, Cajero ve notificación "La configuración del sistema ha sido actualizada", refresca y ve nuevos valores
11. **Primera configuración obligatoria**: Owner recién registrado intenta acceder al POS, es redirigido a `/settings` con mensaje "Por favor, configura tu restaurante antes de continuar"
12. **Audit de cambios**: Owner cambia impuesto, el sistema registra internamente: usuario "Owner", fecha/hora del cambio, valor anterior y nuevo valor

---

## HU-040: Validaciones y Restricciones de Configuración

### Descripción
Como sistema, necesito validar la configuración del restaurante para prevenir errores y mantener la integridad de los datos en todas las operaciones.

### Criterios de Aceptación

**Validación de Nombre:**
- Frontend: Validar longitud (2-100 caracteres) antes de enviar
- Backend: Validar nuevamente longitud y que no sea solo espacios
- Trimear espacios al inicio y final
- No permitir solo espacios en blanco
- Caracteres permitidos: letras, números, espacios, guiones, paréntesis, apóstrofes

**Validación de Dirección:**
- Frontend: Validar longitud máxima (200 caracteres)
- Backend: Validar longitud máxima
- Permitir vacío (opcional)
- Trimear espacios al inicio y final
- Permitir saltos de línea (para direcciones de múltiples líneas)

**Validación de Moneda:**
- Frontend: Validar que se seleccione una opción del dropdown
- Backend: Validar que el código de moneda sea válido
- Solo permitir monedas de la lista predefinida
- No permitir valores custom o inventados
- Requerido (no puede estar vacío)

**Validación de Impuesto:**
- Frontend: Validar que sea número entre 0 y 100
- Backend: Validar rango 0-100 y formato numérico
- Permitir decimales con 1 dígito (ej: 18.5)
- No permitir valores negativos
- Redondear a 1 decimal si se ingresan más decimales
- Requerido (no puede estar vacío)

**Restricciones de Cambio de Moneda:**
- Advertir al usuario sobre el impacto antes de guardar
- Requerir confirmación explícita
- Sugerir revisar precios de productos después del cambio
- Registrar el cambio en logs de auditoría

**Restricciones de Cambio de Impuesto:**
- Informar que solo afecta nuevas ventas
- No requiere confirmación adicional (cambio menos crítico)
- Registrar el cambio en logs de auditoría

**Prevención de Configuración Incompleta:**
- No permitir dejar campos requeridos vacíos
- Deshabilitar botón "Guardar" si hay errores de validación
- Mostrar mensajes de error claros y específicos

**Validación en Backend (Crítico):**
- Nunca confiar solo en validaciones de frontend
- Validar todos los campos antes de guardar
- Retornar errores específicos si hay problemas
- Usar códigos de error estándar (400 Bad Request)

**Manejo de Valores por Defecto:**
- Si es primera configuración y el usuario no completa un campo opcional, usar valor por defecto:
  - Dirección: null o vacío
- Campos requeridos no tienen valor por defecto (usuario debe ingresarlos)

**Sanitización de Inputs:**
- Eliminar HTML/scripts si el usuario intenta inyectarlos
- Escapar caracteres especiales para prevenir XSS
- Validar que no haya código malicioso

**Consistencia de Datos:**
- Asegurar que solo haya un registro de configuración por restaurante
- Usar transacciones para garantizar atomicidad de cambios
- Prevenir condiciones de carrera si múltiples usuarios editan simultáneamente

**Mensajes de Error Específicos:**
- "El nombre es requerido"
- "El nombre debe tener entre 2 y 100 caracteres"
- "La dirección no puede exceder 200 caracteres"
- "Debes seleccionar una moneda"
- "El impuesto debe estar entre 0 y 100"
- "El impuesto debe ser un número válido"

### Escenarios

1. **Validación de nombre muy corto**: Owner intenta guardar nombre "A" (1 carácter), ve error "El nombre debe tener al menos 2 caracteres"
2. **Validación de nombre muy largo**: Owner ingresa 120 caracteres, ve error "El nombre no puede exceder 100 caracteres"
3. **Nombre solo con espacios**: Owner intenta guardar "   " (solo espacios), ve error "El nombre es requerido"
4. **Dirección excede límite**: Owner escribe 250 caracteres en dirección, ve error "La dirección no puede exceder 200 caracteres"
5. **Impuesto negativo**: Owner intenta ingresar "-5", el sistema ajusta automáticamente a "0" o muestra error
6. **Impuesto mayor a 100**: Owner ingresa "150", ve error "El impuesto no puede exceder 100%"
7. **Impuesto con decimales**: Owner ingresa "18.567", el sistema redondea a "18.6" (1 decimal)
8. **Moneda sin seleccionar**: Owner deja dropdown de moneda vacío, intenta guardar, ve error "Debes seleccionar una moneda"
9. **Confirmación de cambio de moneda**: Owner cambia moneda, ve modal de advertencia sobre impacto, debe confirmar explícitamente para guardar
10. **Validación backend rechaza datos**: Owner manipula request y envía datos inválidos, el backend rechaza con error 400 y mensaje específico
11. **Sanitización de HTML**: Owner intenta ingresar `<script>alert('hack')</script>` en nombre, el sistema sanitiza o rechaza el input
12. **Edición simultánea**: Owner A y Owner B intentan editar configuración simultáneamente, el segundo en guardar recibe error "La configuración fue actualizada por otro usuario. Por favor, recarga y vuelve a intentar"
13. **Impuesto de 0%**: Owner configura impuesto en "0", guarda exitosamente, las ventas nuevas se calculan sin impuesto (subtotal = total)
14. **Trimming de espacios**: Owner ingresa "  El Sabor  " (con espacios), el sistema guarda "El Sabor" (sin espacios al inicio/final)

---

## Resumen de Configuración Básica

**Campos de Configuración:**
- ✅ Nombre del restaurante (requerido, 2-100 caracteres)
- ✅ Dirección (opcional, máx. 200 caracteres)
- ✅ Moneda (requerido, selección de lista)
- ✅ Impuesto (requerido, 0-100%, permite decimales)

**Monedas Soportadas (Ejemplos):**
- USD - Dólar estadounidense ($)
- EUR - Euro (€)
- PEN - Sol peruano (S/)
- MXN - Peso mexicano ($)
- COP - Peso colombiano ($)
- CLP - Peso chileno ($)
- ARS - Peso argentino ($)

**Aplicación de Configuración:**
- Nombre: Tickets, facturas, header
- Dirección: Tickets, facturas
- Moneda: Todos los precios y totales del sistema
- Impuesto: Cálculo de totales en nuevas ventas

**Restricciones:**
- Solo Owner puede acceder y editar
- Primera configuración obligatoria antes de usar el sistema
- Cambios de moneda requieren confirmación
- Cambios NO afectan datos históricos

---

## Navegación en Configuración

**URLs:**
- `/settings` → Configuración del restaurante

**Breadcrumb:**
- `/settings`: Dashboard > Configuración

**Acceso:**
- Desde menú lateral: "Configuración" o "Ajustes"
- Desde perfil de usuario: Opción "Configuración"
- Primera vez: Redirección automática al crear cuenta

---

## Notas Técnicas

**Almacenamiento:**
- Tabla: `restaurant_settings` o `restaurants`
- Campos:
  - `id` (PK)
  - `restaurant_id` (FK, unique)
  - `name` (string, required)
  - `address` (text, nullable)
  - `currency_code` (string, required)
  - `tax_rate` (decimal, required)
  - `created_at` (timestamp)
  - `updated_at` (timestamp)
  - `updated_by_user_id` (FK, audit)

**Formato de Moneda:**
- Almacenar código ISO (USD, EUR, PEN)
- Tener mapeo a símbolo ($, €, S/)
- Considerar posición del símbolo (antes/después del número)
- Para USD, MXN, COP, CLP, ARS: Símbolo $ antes del número
- Para EUR: Símbolo € después del número
- Para PEN: Símbolo S/ antes del número

**Impuesto:**
- Almacenar como decimal (0.18 para 18%)
- Mostrar como porcentaje en UI (18%)
- Cálculo: subtotal × tax_rate
- Redondear resultado a 2 decimales

**Caché:**
- Cachear configuración en memoria (alta frecuencia de acceso)
- TTL: 5 minutos o invalidar al actualizar
- Evitar queries repetitivas a DB

**Validaciones:**
- Frontend: Validación inmediata en cada campo
- Backend: Validación completa antes de guardar
- Usar librería de validación (ej: Joi, Zod, Yup)

**Auditoría:**
- Registrar quién y cuándo cambió cada campo
- Tabla de historial de cambios (opcional pero recomendado)
- Útil para debugging y compliance

**Migración/Import:**
- Permitir configuración vía seed/setup inicial
- Útil para testing y demos
- Considerar import desde archivo (futuro)

**Timezone:**
- Agregar timezone como campo futuro (no MVP)
- Por ahora usar timezone del servidor o hardcoded
- Importante para cálculos de "día actual"

**Internacionalización:**
- Preparar estructura para múltiples idiomas (futuro)
- Por ahora solo español
- Nombres de monedas en español

**Seguridad:**
- Solo Owner puede modificar
- Validar permisos en cada request
- Proteger endpoints de configuración
- Registrar cambios para auditoría
