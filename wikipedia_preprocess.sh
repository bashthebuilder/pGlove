bzip2 -d enwiki-20150805-pages-articles-multistream.xml.bz2
python2.7 ../wikipedia_extractor enwiki-20150805-pages-articles-multistream.xml --threads 30 -o wiki_documents
awk 'NR>1{print $1}' RS=[ FS=] enwiki-20150702-pages-articles-multistream.xml > anchors.txt #extract text between double braces
sed -i '/http:\/\//d' anchors.txt #remove http
sed -i '/^$/d' anchors.txt #remove extra lines
sed -i '/https:\/\//d' anchors.txt
sed -i '/Category:\/\//d' anchors.txt
sed -i '/File:\/\//d' anchors.txt
mongoimport --db db --collection wikidata --type json --file wikidata-20150817-all.json --jsonArray
mongod --dbpath db/ --cpu -v
find . -type f -name "wiki*" | xargs cat | grep -w "</doc>" | wc -l #find number of wikipedia artciles
cd yourdirectory
perl -e 'for(<*>){((stat)[9]<(unlink))}' #fast delete files
