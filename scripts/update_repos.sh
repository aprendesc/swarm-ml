source C:/Users/AlejandroPrendesCabo/Desktop/Proyectos/eigenlib/.venv/Scripts/activate.bat

sleep 0.2
cd C:/Users/AlejandroPrendesCabo/Desktop/Proyectos/eigenlib
git add .
git commit -m "cluster submit"
git push
sleep 0.2
databricks repos update --repo-id 40158810694901 --branch main

cd C:/Users/AlejandroPrendesCabo/Desktop/Proyectos/swarm-ml
git add .
git commit -m "cluster submit"
git push
sleep 0.2
cd C:/Users/AlejandroPrendesCabo/Desktop/Proyectos/swarm-ml
databricks repos update --repo-id 935976220025428 --branch main
sleep 0.2