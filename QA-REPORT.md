# Informe de calidad — Credisnet, nueva versión V2

**Estado:** Prototipo estático funcional con pruebas parciales. **No listo aún para publicar en el dominio de producción** sin las verificaciones pendientes.

**Alcance de la revisión:** HTML, CSS, JavaScript, contenido generado, enlaces, SEO estático, responsive y comportamiento en Chromium usando render aislado. No se revisó íntegramente el código original ni el sitio con pruebas Lighthouse de servidor. Fecha de preparación: 27/10/2026.

## Resultados verificables

| Criterio | Estado | Evidencia / resultado | Pendiente |
|---|---|---|---|
| Arquitectura de páginas | Verificado | 25 rutas indexables + 404 | Revisión de equivalencia exacta con inventario original |
| Enlaces internos | Verificado | 703 enlaces internos evaluados; 0 rotos | Navegación HTTP real en hosting |
| SEO técnico estático | Verificado | Canónicas, títulos, descriptions, sitemap con 25 URLs, robots | Search Console y revisión de indexabilidad del staging |
| Datos estructurados | Verificado sintaxis | 70 bloques JSON-LD analizados sin error | Validación de elegibilidad enriquecida con herramientas externas |
| Responsive | Revisado parcialmente | Chromium 1440, 768, 390, 320 px, sin overflow detectado | Dispositivos físicos, contraste completo y navegadores adicionales |
| Menú móvil / FAQ | Verificado aislado | Expandir/cerrar menú y FAQ; Escape probado | Flujos externos en hosting real |
| Selector de sector | Revisado parcialmente | 18 rutas configuradas; HTML y JS revisados, destinos locales comprobados | Redirección end-to-end por HTTP real |
| JavaScript | Verificado sintaxis | `node --check` pasó; sin page errors en escenas ensayadas | Pruebas de regresión más amplias |
| Seguridad estática | Revisado parcialmente | Headers CSP, frame protection, referrer y permissions declarados | Cabeceras de red entregadas por Cloudflare, escaneo OWASP |
| Privacidad | Revisado parcialmente | No hay formularios de DNI, cuentas, trackers o cookies añadidos | Texto legal final, rol del responsable y medios de contacto |
| Contenido financiero | Revisado parcialmente | No se inventan tasas, reseñas ni garantías de crédito | Verificar convenios, normas, entidades, disponibilidad y cualquier oferta real |
| Accesibilidad | Revisado parcialmente | Landmarks, H1, etiquetas, teclado menú, focus visible, reduced motion | Auditoría WCAG 2.2 AA manual + automática con herramienta externa |
| Rendimiento | Pendiente de comprobar | Diseño sin librerías JS ni fuentes externas; sin métricas inventadas | Lighthouse y Core Web Vitals reales |
| Conversión comercial | Pendiente de comprobar | CTA WhatsApp, navegación por sector | Confirmar número y medir leads sin vulnerar privacidad |
| Pruebas legales | Pendiente de comprobar | Bases de términos y política | Firma/revisión por abogado responsable |
| Integración y despliegue | Pendiente de comprobar | Directorio `docs` compatible con static Pages | Staging, redirects históricos, DNS, HTTP, OG y publicación |

No se asigna una nota global 10/10 ni puntuaciones de Lighthouse porque no hay mediciones apropiadas.

## Riesgos de mayor severidad

**Alto — Número comercial contradictorio.** Contactos del sitio anterior: CTA `541122845514`; cabecera `541169707265`. El nuevo generador usa provisionalmente el primero; validar con el titular de la marca.

**Alto — Política y términos sin aprobación legal.** Los borradores incluyen avisos explícitos. No sustituir los textos vigentes hasta revisar la normativa aplicable y los datos de identificación de la empresa.

**Medio — Redirecciones.** Se comprobaron en el README original, pero el contenido histórico exacto no estuvo disponible. Copiarlo antes de migrar.

**Medio — Veracidad de líneas y reglamentación.** Confirmar qué organismos, prestatarios, condiciones y marcos legales están operativos; actualizar por escrito las páginas de cada sector.

**Medio — Pruebas de hosting.** Los ensayos visuales y de interacción se realizaron sobre HTML aislado porque el navegador local tiene acceso de red bloqueado. El routing real, CSP, SEO de producción y rendimiento deben medirse una vez publicado en un entorno de pruebas.

## Criterios para pasar a producción

- Teléfono confirmado y prueba de apertura de WhatsApp desde desktop y móvil.
- Legal y privacidad autorizados, con identificaciones/contactos completos.
- Revisadas todas las páginas para evitar afirmaciones no verificadas.
- Redirecciones migradas, 404 confirmada, canonical apuntando a dominio definitivo en producción.
- Validación funcional por HTTP, accesibilidad manual, Lighthouse y medidas de seguridad básicas.

**Conclusión:** Entrega de código lista para revisión y staging; no se declara 10/10 ni validación para producción.
