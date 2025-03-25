@echo off

echo Creazione virtual environment "venv_lezione_01"...
python -m venv venv_lezione_01
echo Fatto! La cartella "venv_lezione_01" è stata creata.
pause

echo Attivazione virtual environment "venv_lezione_01"...
call venv_lezione_01\Scripts\activate
