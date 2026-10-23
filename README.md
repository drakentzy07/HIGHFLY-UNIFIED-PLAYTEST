# HIGHFLY UNIFIED — Playtest S23

**Distribución WebGL de pruebas:** [Abrir HIGHFLY UNIFIED](https://drakentzy07.github.io/HIGHFLY-UNIFIED-PLAYTEST/)

Este repositorio **no contiene una segunda versión del motor**. GitHub Actions construye
un commit **fijado** y auditado de `drakentzy07/cobalt-hollow-lab` desde la rama Recovery,
y publica su WebGL como una Pages independiente para probar en Samsung S23 Ultra horizontal.

## Compilación fijada
- Origen: `drakentzy07/cobalt-hollow-lab`
- Commit: `a7f52967e3dd2daa0ff4d37a438dab7c77fc133b`
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

## Combat Fluidity 1.0 (23 Oct 2026)

Actualización: combo físico 1–4 más fluido y con una única pulsación anticipada, animaciones menos pesadas, corrección de entrada LTR Samsung y uso de segunda espada de una mano en ranura offhand. Misma app, mismo mapa y mismos guardados de prueba. **No se modifican las partidas originales de Draken.**
