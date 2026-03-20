# Guía de despliegue en AWS

## Objetivo
Desplegar la API Flask con:
- GitHub como repositorio fuente
- AWS CodePipeline como orquestador
- AWS CodeBuild para build y pruebas
- AWS Elastic Beanstalk para hosting

## Arquitectura propuesta
1. Subes cambios a GitHub
2. CodePipeline detecta el commit
3. CodeBuild instala dependencias, entrena el modelo y corre pruebas usando `buildspec.yml`
4. CodePipeline manda el artefacto a Elastic Beanstalk
5. Elastic Beanstalk actualiza la aplicación automáticamente

## Paso 1. Subir el proyecto a GitHub
1. Crear un repositorio nuevo
2. Subir todo el contenido del proyecto
3. Confirmar que `buildspec.yml`, `Procfile`, `requirements.txt` y `app/app.py` estén en el repo

## Paso 2. Crear aplicación en Elastic Beanstalk
1. Entrar a AWS Elastic Beanstalk
2. Crear una nueva aplicación
3. Elegir plataforma Python
4. Crear un environment web server
5. Anotar el nombre de la aplicación y del environment

AWS indica que Elastic Beanstalk para Python corre aplicaciones WSGI y usa Gunicorn por defecto, además de permitir configuración mediante `Procfile`. citeturn836773search2turn836773search0

## Paso 3. Crear proyecto en CodeBuild
1. Entrar a AWS CodeBuild
2. Crear proyecto nuevo
3. Como fuente usar CodePipeline
4. Como ambiente usar Ubuntu administrado por AWS y Python 3.11
5. Activar privilegios estándar
6. Dejar que CodeBuild lea `buildspec.yml`

AWS documenta que CodeBuild usa el archivo `buildspec.yml` como especificación de compilación. citeturn836773search3turn836773search7

## Paso 4. Crear pipeline en CodePipeline
1. Entrar a AWS CodePipeline
2. Crear pipeline nuevo
3. Agregar etapa Source con GitHub via GitHub App
4. Seleccionar tu repositorio y rama
5. Agregar etapa Build con el proyecto de CodeBuild
6. Agregar etapa Deploy con Elastic Beanstalk
7. Seleccionar la aplicación y environment creados antes

AWS indica que toda pipeline requiere por lo menos una etapa Source y otra de Build o Deploy. También permite usar conexión con GitHub mediante GitHub App y desplegar directamente a Elastic Beanstalk. citeturn836773search9turn480934search1turn480934search9

## Paso 5. Verificar despliegue
1. Hacer un commit en GitHub
2. Confirmar que se ejecute CodePipeline
3. Revisar CodeBuild logs
4. Entrar a la URL pública de Elastic Beanstalk
5. Probar:
   - GET /health
   - POST /predict

## Qué mostrar en el video
- repositorio en GitHub
- archivo `buildspec.yml`
- pipeline ejecutándose en CodePipeline
- logs exitosos de CodeBuild
- aplicación corriendo en Elastic Beanstalk
- prueba real del endpoint `/predict`

## Errores comunes
- no entrenar el modelo antes del deploy
- olvidar incluir `Procfile`
- no tener permisos del rol de servicio
- pipeline sin stage de despliegue
- nombre incorrecto del entrypoint en Gunicorn
