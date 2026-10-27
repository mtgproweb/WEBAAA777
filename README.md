# Credisnet · Rediseño visual V2

Esta entrega reemplaza la propuesta anterior. Parte del repositorio original suministrado, no del primer rediseño.

## Alcance

**El contenido aprobado se conserva.** Se mantienen los textos, montos, cuotas, requisitos, testimonios, condiciones, contactos, URLs, imágenes, metadata y datos estructurados de las 26 páginas originales.

Cambian la presentación y distribución visual:

- Azul de marca, blanco y verde para las consultas.
- Portada con título comercial original e imagen de familia junto al mensaje.
- Las ocho tarjetas de préstamos originales se muestran como catálogo de dos filas en escritorio, con montos y cuotas visibles. En móvil tienen desplazamiento manual y flechas.
- Secciones claras para organismos, requisitos, proceso, testimonios y preguntas.
- Encabezados azules y contenido de lectura sobre blanco en las páginas internas.
- Se conserva Credis, el asistente original, y sus respuestas.

No se tocaron el sitio activo ni el repositorio remoto.

## Probar en tu computadora

Desde esta carpeta, con Python 3:

```sh
python -m http.server 8000 --directory docs
```

Abrí http://localhost:8000. Ctrl+C detiene el servidor.

## Subir a un repositorio de prueba

1. Descomprimí el ZIP.
2. Creá un repositorio nuevo en GitHub.
3. Subí **el contenido** de `credisnet-rediseno-v2`, incluyendo la carpeta `.github`, en la raíz. No subas el ZIP como único archivo.
4. En Settings → Pages elegí GitHub Actions.
5. El workflow heredado valida y publica una copia no indexable de prueba. Si no arranca, ejecutalo desde Actions.
6. Revisá la URL que entregue GitHub antes de reemplazar tu sitio.

`docs/` conserva la configuración para el dominio actual. `_site/` es la copia no indexable que genera el workflow. No es una vista privada.

## Qué editar

- `docs/css/rediseno.css`: nueva dirección visual y responsive.
- `docs/css/style.css` y `docs/css/pages.css`: componentes originales adaptados a superficies claras.
- `docs/js/main.js`: catálogo sin desplazamiento automático; resto de interacciones originales.
- `docs/js/rediseno.js`: ajustes de menú móvil y teclado.
- `docs/index.html`: reubicación del bloque de familia y carga del nuevo estilo.
- Las demás páginas sólo incorporan los archivos de presentación; el contenido original permanece.

No utilizar el generador de la primera propuesta: no forma parte de este repositorio.

## Comprobaciones

```sh
python scripts/validate_site.py
python scripts/verify_content.py
node --check docs/js/main.js
node --check docs/js/rediseno.js
```

La segunda comprobación compara cada página con firmas de contenido del ZIP original. Permite cambiar el orden de bloques; detecta cambios de textos, enlaces, imágenes, metadatos o datos estructurados.

## Límite de verificación

Se comprobaron la conservación del contenido, enlaces locales y sintaxis JavaScript. La vista previa del entorno no estuvo disponible, por lo que no se afirma haber revisado visualmente el resultado en navegador ni medido Lighthouse. Revisar escritorio y móvil en la URL de prueba antes de reemplazar el sitio actual.
