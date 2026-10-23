# HIGHFLY UNIFIED — Playtest S23

**Distribución WebGL de pruebas:** [Abrir HIGHFLY UNIFIED](https://drakentzy07.github.io/HIGHFLY-UNIFIED-PLAYTEST/)

Este repositorio **no contiene una segunda versión del motor**. GitHub Actions construye
un commit **fijado** y auditado de `drakentzy07/cobalt-hollow-lab` desde la rama Recovery,
y publica su WebGL como una Pages independiente para probar en Samsung S23 Ultra horizontal.

## Compilación fijada
- Origen: `drakentzy07/cobalt-hollow-lab`
- Commit: `87f4fb52389d1aab5223f2663460aa7eb8ab5e97`
- Mundo / recursos congelados: `levy-street/world-of-claudecraft@9b57e49c9676d75962700f828cc00a50a9a988b5`
- Patrón: una sola app con World LV1 y LAB de prueba; el laboratorio no cambia la partida.
- Habilidades: se compran al Veterano con cobre, sin bloqueo por nivel para Hunter Universal.
- Guardados: IndexedDB + localStorage exclusivos para esta URL; no leen datos de Draken
  ni de la antigua candidata en el mismo dominio GitHub Pages.

## Actualización
Actualizar exclusivamente el SHA fijado en `.github/workflows/pages.yml` después
de las pruebas, o iniciar `Actions → HIGHFLY UNIFIED → Run workflow` para reconstruir
el mismo commit. **No copiar assets, saves ni codigo a producción**.

El enlace es público y el guardado WORLD aquí sigue siendo de prueba. No compartir
datos sensibles ni asumir que el navegador está conectado a servidores multijugador.
