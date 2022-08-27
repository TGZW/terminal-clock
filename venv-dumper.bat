pip-chill --no-chill > requirements.txt
pip freeze > requirementscomp.txt
pip uninstall -r requirementscomp.txt
echo deleting requirementscomp.txt
del "requirementscomp.txt" /q
echo done