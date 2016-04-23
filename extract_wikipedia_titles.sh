cd /home/msjameel/ijcai_2016/wikipedia/wiki_documents
for f in *; do
    if [[ -d $f ]]; then
        cd $f
        mv ../titles.txt .
        for d in *;
        do
	  awk -v FS="(\" title\=\"|\"\>)" '{print $2}' >> titles.txt
        done
        mv titles.txt ../
        cd ..
    fi
done
