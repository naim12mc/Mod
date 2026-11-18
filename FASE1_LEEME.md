# NAIMSAURIA: Reyes del Jurásico — FASE 1

**Es un parche de estructura para el repositorio fuente existente `naim12mc/Mod`, no un proyecto autónomo.**
**No borres los archivos `.java` ni los modelos ya presentes en ese repositorio.**

## Aplicación

1. Descarga el ZIP, extráelo en una carpeta temporal.
2. Copia su contenido sobre la **raíz del repositorio fuente** existente, aceptando la sustitución de los archivos coincidentes.
3. Conserva las carpetas `src/main/java/.../entity`, `registry`, `combat`, `item`, `client` y los recursos existentes.
4. Sube los cambios a GitHub. El flujo `.github/workflows/compilar.yml` compilará automáticamente en `main`.
5. Descarga el único JAR publicado en el artefacto de GitHub Actions si la ejecución termina en verde.

Para compilar en local: JDK 25, Gradle 9.5.1 y conexión de red a los repositorios Maven.
Ejecuta: `python3 fix_naimsauria_26_2.py && gradle testClasses && gradle clean build -x test`.

## Estructura

- `build.gradle`, `settings.gradle`, `gradle.properties`: compilación Fabric 26.2, Gradle y GeckoLib.
- `src/main/resources/fabric.mod.json`: identificador histórico `naimsauria`, nuevo nombre visible.
- `src/main/java/net/naimsauria/titanes/NaimsauriaMod.java`: entrypoint común preexistente **no sobrescrito**.
- `src/main/java/net/naimsauria/titanes/client/NaimsauriaClient.java`: entrypoint gráfico preexistente **no sobrescrito**.
- `entity/`, `registry/`, `combat/`, `item/`: código de NAIMSAUR PRIME **conservado**.
- `boss/`, `network/`, `client/hud/`, `client/cinematic/`: reservadas para fases 2 y 3.
- `config/`, `world/`, `loot/`: reservadas para fase 6.
- `assets/naimsauria/sounds`: aquí irán `.ogg`, uno por sonido, y `sounds.json` en `assets/naimsauria/`.
- `assets/naimsauria/textures/gui`: futuras barras de vida PNG.
- `assets/naimsauria/textures/particle`: futuras partículas PNG.

## Mixins

La fase 1 no requiere un mixin. No se ha declarado un `mixins` en el manifiesto.
Solo se añadirá un mixin donde la API oficial de Fabric no cubra una operación necesaria.

## Estado verificado

El repositorio original compiló correctamente en GitHub Actions #6 con Java 25, Gradle 9.5.1 y el script de corrección.
Esta entrega modifica metadatos y workflow; **su compilación posterior y su funcionamiento en el cliente todavía deben verificarse**.
No hay cinco jefes implementados, barras personalizadas, efectos de cámara o nuevas arenas en esta fase.

## Prueba de juego

1. Guarda una copia de tu mundo y usa un mundo creativo de pruebas.
2. Instala Fabric 26.2, Fabric API compatible, GeckoLib Fabric 5.5.5 y el nuevo JAR.
3. Verifica que Minecraft inicia y muestra `NAIMSAURIA: Reyes del Jurásico` en la lista de mods.
4. Intenta `/give @s naimsauria:sello_primordial` y prueba el prototipo en una zona abierta.
5. Guarda `latest.log` si hay errores de carga o renderizado.

El `-sources.jar` no se instala en Minecraft.
