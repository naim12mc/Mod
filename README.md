# NAIMSAURIA — El Despertar de los Cinco Titanes

**Fabric para Minecraft Java 26.2 · Entrega 0.1.0-alpha · PROYECTO FUENTE, NO JAR VERIFICADO**

Este ZIP **no es un mod instalable aún**. Contiene el código fuente del primer prototipo de NAIMSAUR PRIME y un documento de diseño de los otros cuatro jefes. El entorno de generación solo dispone de Java 21, no dispone de Gradle y no puede acceder a los repositorios de dependencias, por lo que **no se ha podido compilar ni arrancar Minecraft 26.2**. No debe considerarse una versión terminada o probada dentro del juego.

## Qué contiene realmente

- Proyecto Gradle preparado para Minecraft Java **26.2**, Fabric Loader **0.20.1**, Fabric API **0.155.2+26.2**, GeckoLib Fabric **5.5.5** y Java **25**.
- Registro de **una entidad** `naimsauria:naimsaur_prime`, con 520 puntos de salud definidos, objetivos de ataque, barra de jefe, introducción por partículas y rugidos vanilla.
- Lógica de **cuatro fases** (75/50/25 % de salud), selección de ataques, avisos previos y daños calculados en el servidor.
- Cinco ataques previstos en el prototipo: mordisco, terremoto, aliento energético, meteorito visual y apocalipsis circular (con zona segura en el centro).
- Objeto `naimsauria:sello_primordial` que intenta invocar al jefe al usarlo sobre un bloque; receta de fabricación y objeto de recompensa `naimsauria:nucleo_saurio_omega`.
- **Modelo 3D original procedural de 17 huesos**, una textura pixel-art 256×256 y **8 animaciones** GeckoLib: idle, walk, roar, bite, stomp, beam, transform, death. La animación `death` está creada como recurso, **no conectada aún** al ciclo de muerte del juego.
- Archivo editable aproximado `.bbmodel` para Blockbench (requiere verificar UV y escala).
- Documento de progresión y diseño de los **otros cuatro jefes**, todavía **sin implementar**.
- Test de lógica Java `CombatDirectorTest` (ejecutable sin Minecraft), superado con Java 21.

## Lo que NO está implementado

- **No están implementadas** las otras cuatro entidades, sus arenas, templos, estructuras, reliquias ni progresión.
- No hay cámara cinematográfica personalizada, vibración real del cliente, eclipse real ni iluminación dinámica. La introducción actual usa partículas y sonidos básicos.
- No hay efectos de audio originales integrados, solo eventos de sonido existentes de Minecraft.
- No hay integración con Twitch, TikTok o Streamer.bot.
- No se han validado los recursos, el renderizado ni el rendimiento dentro del cliente de Minecraft.
- El código adaptador a Fabric/GeckoLib necesita una primera compilación real, y posiblemente pequeños ajustes de APIs antes de poder ejecutar el juego.

## Cómo compilar en Windows (requiere Internet)

1. Instala **JDK 25** (no Java 21), versión compatible con Minecraft 26.2.
2. Instala **Gradle 9.5.1** o genera un wrapper con una instalación de Gradle compatible. Comprueba `java -version` y `gradle --version`.
3. Abre una terminal en la carpeta del proyecto.
4. Ejecuta `gradle build --stacktrace`.
5. Si compila correctamente, el `.jar` de salida aparecerá en `build/libs/`.
6. Instala Minecraft Java **26.2** con Fabric Loader para esa versión y coloca en `mods` el `.jar` construido, la versión compatible de **Fabric API** y **GeckoLib**.
7. Prueba primero en un **mundo nuevo de pruebas**, nunca directamente en un mundo Hardcore importante.

**Si aparece un error de compilación**, pega el primer bloque de `error:` y el `Caused by:` completo en la conversación para reparar el proyecto. No hay garantía de que compile en el primer intento.

## Cómo probar cuando compile

```
/give @p naimsauria:sello_primordial
/give @p naimsauria:nucleo_saurio_omega
/summon naimsauria:naimsaur_prime ~ ~ ~
```

**Recomendación:** usa el sello en una zona amplia, lejos de tu base. El combate está pensado para prueba de dificultad, no está equilibrado aún para supervivencia pública.

## Tests offline

Con JDK 21+:

```bash
javac -d test-classes src/main/java/net/naimsauria/titanes/combat/CombatDirector.java src/test/java/net/naimsauria/titanes/combat/CombatDirectorTest.java
java -cp test-classes net.naimsauria.titanes.combat.CombatDirectorTest
```

Este test solo verifica reglas de fases y selección de ataques; **no verifica** API, Gradle, funcionamiento de entidades o cliente.

## Próxima iteración

1. Compilar y resolver errores de integración de 26.2.
2. Probar el modelo en Blockbench y cliente, corregir escala/UV y aliento desde el anclaje de mandíbula.
3. Integrar animación de derrota, mejores rugidos y pantalla de introducción.
4. Implementar cámara de aproximación y sacudidas opcionales, con reducción de efectos.
5. Construir las otras cuatro entidades, modelos, estructuras y progresión de reliquias.

## Fuentes técnicas usadas

- https://fabricmc.net/2026/06/15/262.html
- https://docs.fabricmc.net/develop/entities/first-entity
- https://docs.fabricmc.net/develop/items/first-item
- https://wiki.geckolib.com/docs/geckolib5/entities/the-entity-class/
- https://wiki.geckolib.com/docs/geckolib5/entities/the-entity-renderer/
- https://wiki.geckolib.com/docs/geckolib5/setup/fabric/quick-reference/

Assets artísticos procedurales de este proyecto creados desde cero para este prototipo.
