@echo off
title Ta Te Ti - TATETI
cd /d "%~dp0"
echo Ruta: %CD%
if not exist "main.py" echo ERROR: main.py no encontrado & pause & exit /b 1
echo OK: main.py listo.
"C:\Users\torre\AppData\Local\Programs\Python\Python310\python.exe" main.py
pause
