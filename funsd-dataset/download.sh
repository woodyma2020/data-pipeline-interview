wget https://guillaumejaume.github.io/FUNSD/dataset.zip
unzip dataset.zip 
mv dataset/testing_data/images images
rsync dataset/training_data/images images
mv images/images images
rm -rf dataset.zip __MACOSX
rm -rf dataset