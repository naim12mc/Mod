# Intentar compilar el mod usando GitHub Actions

La compilación local **no se ha podido realizar** por falta de Java 25, Gradle y conectividad a los repositorios de Fabric. El proyecto **no está verificado** y puede contener errores de compilación.

1. Crea un repositorio privado nuevo en GitHub.
2. Descomprime este ZIP y sube **el contenido de la carpeta raíz** al repositorio (deben verse `build.gradle`, `gradle.properties`, `settings.gradle`, `src/` y `.github/`).
3. Ve a **Actions → Compilar NAIMSAURIA para Minecraft 26.2 → Run workflow**.
4. Si aparece el estado verde, descarga el artefacto **NAIMSAURIA-Fabric-26.2-JAR**; en su interior estará el `.jar` de salida. El código no está probado en Minecraft.
5. Si aparece rojo, revisa el registro del paso **Compilar el mod**: copia el primer error de compilación para poder corregir el código. No intentes instalar el `.jar` hasta que termine correctamente.

El flujo utiliza Java 25 y Gradle 9.5.1; GitHub descargará las dependencias necesarias durante la compilación. No garantiza que el código fuente actual compile sin correcciones.
