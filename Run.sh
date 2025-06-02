cd ~/SALOME-9.14.0-native-UB24.04-SRC/

./salome -t ~/Downloads/artem/Mesh.py

cd ~/Downloads/artem
ideasUnvToFoam Mesh.unv
sed -i '33s/patch/empty/;39s/patch/wall/' constant/polyMesh/boundary

icoFoam
paraFoam

echo run