awk 'NR>1{print $1}' RS=[ FS=] enwiki-20150805-pages-articles-multistream.xml > anchors.txt #this will get the anchors, but more preprocessing is needed.
sed -i '/http:\/\//d' anchors.txt #remove http
sed -i '/https:\/\//d' anchors.txt
sed -i '/Category:\/\//d' anchors.txt
sed -i '/File:\/\//d' anchors.txt
sed -i '/User talk/d' anchors.txt
sed -i '/WP:/d' anchors.txt
sed -i '/wikt:/d' anchors.txt
sed -i '/p\. /d' anchors.txt
sed -i '/:nost:/d' anchors.txt
sed -i '/User:/d' anchors.txt
sed -i 's/\&amp/\&/g' anchors.txt #replace &amp to &
sed -i '/s:/d' anchors.txt
awk '{$2=$2}1' anchors.txt > tmp #remove extra spaces
mv tmp ./anchors.txt
sed -i '/^$/d' anchors.txt #remove extra lines
