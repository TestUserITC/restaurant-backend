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