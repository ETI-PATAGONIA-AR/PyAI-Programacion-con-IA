@echo off
REM ============================================================== 
REM PyAI_v1\run_PyAI_v1.bat - ETI Patagonia - prof.martintorres@educ.ar
REM ==============================================================

REM --------------------------------------------------------------
REM 1️⃣ Cambiar al directorio del script
REM --------------------------------------------------------------
cd /d %~dp0

REM --------------------------------------------------------------
REM 2️⃣ Actualizar pip a la última versión
REM --------------------------------------------------------------
echo Comprobando actualización de pip...
python -m pip install --upgrade pip

REM --------------------------------------------------------------
REM 3️⃣ Función para instalar paquetes solo si no están presentes
REM --------------------------------------------------------------
echo Instalando dependencias necesarias...
python - <<END
import subprocess
import pkg_resources

packages = {
    "PyQt5": "5.15.11",
    "requests": "2.32.5",
    "Pygments": "2.19.2",
    "pyttsx3": None
}

for pkg, ver in packages.items():
    try:
        pkg_resources.get_distribution(pkg)
        print(f"{pkg} ya instalado")
    except pkg_resources.DistributionNotFound:
        if ver:
            print(f"Instalando {pkg}=={ver}...")
            subprocess.check_call(["pip", "install", f"{pkg}=={ver}"])
        else:
            print(f"Instalando {pkg}...")
            subprocess.check_call(["pip", "install", pkg])
END

REM --------------------------------------------------------------
REM 4️⃣ Ejecutar el programa principal
REM --------------------------------------------------------------
echo Iniciando PyAI v1...
python main.py

pause

