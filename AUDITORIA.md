# Informe de entrega · 27 de octubre de 2026

## Resultado

Nuevo diseño integral de Credisnet, con 26 HTML y navegación de las 24 páginas internas conservada. HTML estático para continuidad con el alojamiento existente y mínima dependencia. No se publicó ni modificó el sitio actual.

## Verificación ejecutada

- `validate_site.py`: 26 HTML, 24 páginas internas, 25 URLs de sitemap, canonical y referencias locales válidas.
- `check_quality.py`: un H1 por página, IDs únicos, fragmentos locales, imágenes con alt y dimensiones, JSON-LD válido y copia GitHub Pages no indexable.
- `node --check docs/js/site.js`: sintaxis válida.
- `test_interactions.cjs`: apertura del menú, Escape y retorno del foco, búsqueda sin tildes, estado vacío, restauración de tarjetas y destinos del selector permitidos. Ejecutado con DOM simulado; no sustituye pruebas en navegador.
- Inspección de las imágenes originales para verificar que corresponden al contenido.

## Matriz de evaluación

No se asignan puntuaciones numéricas ni una nota global: no existen mediciones suficientes.

| Dimensión | Objetivo | Estado | Evidencia y pendiente / próxima mejora |
|---|---|---|---|
| Diseño y marca | Lenguaje visual coherente | Revisado parcialmente | Nueva paleta, tipografía, componentes e imágenes; validar composición en navegador. |
| UX y arquitectura | Encontrar línea y consultar | Revisado parcialmente | 19 líneas, selector, buscador y flujo a WhatsApp; prueba de usuario pendiente. |
| Código | Modular y reproducible | Verificado | Generador Python sin dependencias; CSS y JS separados. |
| Funcionalidad | Navegación sin enlaces rotos | Revisado parcialmente | Enlaces locales y lógica JS comprobados; WhatsApp real no enviado. |
| SEO | Rutas, metadata y rastreo consistentes | Verificado en código | 25 URLs, canonical, metadata y sitemap. Indexación real no comprobada. |
| AEO / contenido | Respuestas claras sin promesas | Revisado parcialmente | FAQ y contenido semántico; no garantiza citas en buscadores o IA. |
| Accesibilidad | Base WCAG 2.2 AA | Revisado parcialmente | Labels, skip link, foco, idioma, detalles nativos y movimiento reducido. Falta revisión con lector de pantalla y contraste automatizado. |
| Responsive | Móvil, tablet, escritorio | Revisado parcialmente | Breakpoints y layouts implementados; no hubo prueba visual en dispositivos. |
| Rendimiento | Poco JS y recursos locales | Revisado parcialmente | Sin librerías, CDNs ni fuentes externas. No se ejecutaron Lighthouse ni Web Vitals. |
| Seguridad | Minimizar superficie | Revisado parcialmente | Sin backend ni secretos; WhatsApp con noopener; revisar headers en hosting. |
| Privacidad | Minimizar datos | Revisado parcialmente | Sin cookies, analítica ni captura de datos; WhatsApp externo. Política ajustada a esta implementación. |
| Contenido legal | Exactitud aplicable al negocio | Pendiente de comprobar | Términos del original retenidos, incluyendo referencias normativas. Revisión jurídica y datos de responsable pendientes. |
| Credibilidad | No inventar prueba social | Verificado en contenido nuevo | Sin testimonios, cifras de clientes ni promesas de aprobación/tiempo. |
| Conversión | Consulta contextual | Revisado parcialmente | CTA por línea y selector; impacto comercial no medido. |
| Compatibilidad | Navegadores modernos | Pendiente de comprobar | No hubo Safari/Firefox/Chrome real. |
| Mantenimiento | Edición centralizada | Verificado | Generador y documentación de despliegue. |
| Analítica | Medir sin asumir permisos | No aplicable en esta entrega | No se incorporó un proveedor. Proponer eventos de consulta sólo tras definir privacidad y medición. |
| Backend, pagos y cuentas | No requeridos | No aplicable | El modelo del proyecto es consulta por WhatsApp. |

## Limitaciones reales

La infraestructura de vista previa devolvió “sites-previewd mailbox is unavailable”. Se confirmó el mismo fallo con `sites-preview status`. No se pudo realizar QA visual en navegador, capturas, medición Lighthouse ni Core Web Vitals. No se afirma 10/10, cumplimiento legal o certificación de accesibilidad.

La selección de imágenes y contenido se basa en los archivos suministrados; no se verificaron derechos, acuerdos con entidades ni condición de agente autorizado. Confirmar ambos números de WhatsApp antes de publicar.

Los `_headers` y `_redirects` heredados sólo funcionan en hostings que los soporten; GitHub Pages no aplica esos archivos. Las rutas antiguas y cabeceras deben probarse en el alojamiento definitivo. El workflow sigue siendo de **prueba no indexable**, como en el original.

Las páginas de líneas conservan nombres y rutas, pero sustituyen cifras y condiciones no verificadas por orientación y consulta específica. Para publicar ofertas concretas, incorporar la propuesta vigente de la entidad, sus requisitos y sus costos.

## Fuente financiera

Se consultó BCRA, “Préstamos personales: qué tener en cuenta antes de decidir”, el 27/10/2026: https://www.bcra.gob.ar/prestamos-personales-comparar-costos-y-condiciones/

Se usa para explicar la comparación de costos; no se usa para validar Credisnet ni sus operatorias.

## Próximo paso

Probar este repositorio en una URL separada, revisar todos los tamaños y contactos, validar los textos legales y recién entonces decidir el reemplazo. No hay defectos críticos conocidos en las comprobaciones ejecutadas; falta la validación visual y operativa indicada.
