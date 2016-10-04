#!/bin/bash

# Makes programs, downloads sample data, trains a GloVe model, and then evaluates it.
# One optional argument can specify the language used for eval script: matlab, octave or [default] python

make
if [ ! -e text8 ]; then
  if hash wget 2>/dev/null; then
    wget http://mattmahoney.net/dc/text8.zip
  else
    curl -O http://mattmahoney.net/dc/text8.zip
  fi
  unzip text8.zip
  rm text8.zip
fi

#CORPUS=/home/msjameel/acl_2016/glove_model/standard/GloVe-1.2/wikipedia_entities_hyphenated.txt
CORPUS=text8
VOCAB_FILE=vocab.txt
COOCCURRENCE_FILE=cooccurrence.bin
COOCCURRENCE_FILE_DISCRETE=cooccurrence_discrete.bin
COOCCURRENCE_SHUF_FILE=cooccurrence.shuf.bin
BUILDDIR=build
SAVE_FILE=vectors
VERBOSE=2
MEMORY=4.0
VOCAB_MIN_COUNT=10
VECTOR_SIZE=100
MAX_ITER=5
WINDOW_SIZE=10
BINARY=2
NUM_THREADS=1
X_MAX=10

$BUILDDIR/vocab_count -min-count $VOCAB_MIN_COUNT -verbose $VERBOSE < $CORPUS > $VOCAB_FILE
if [[ $? -eq 0 ]]
  then
  $BUILDDIR/cooccur -memory $MEMORY -vocab-file $VOCAB_FILE -verbose $VERBOSE -window-size $WINDOW_SIZE < $CORPUS > $COOCCURRENCE_FILE
if [[ $? -eq 0 ]]
  then
  #$BUILDDIR/cooccur_discrete -memory $MEMORY -vocab-file $VOCAB_FILE -verbose $VERBOSE -window-size $WINDOW_SIZE < $CORPUS > $COOCCURRENCE_FILE_DISCRETE
    if [[ $? -eq 0 ]]
    then
    #$BUILDDIR/bin_to_txt $COOCCURRENCE_FILE
    #mkdir temp_files
    #mv bin_to_txt.txt temp_files/
    #cd temp_files
    #awk '{ print > $1 ".tmp" }' bin_to_txt.txt
    #cd ..
  if [[ $? -eq 0 ]]
  then
    #$BUILDDIR/zero_counts
  if [[ $? -eq 0 ]]
  then
    #cd temp_files
    #find . -maxdepth 1 -type f -name '*.tmp' -print0 | sort -z | xargs -0 cat -- >> bin_to_txt.txt
    #mv bin_to_txt.txt ../
    #cd ..
if [[ $? -eq 0 ]]
  then
    #$BUILDDIR/text_to_binary bin_to_txt.txt
  if [[ $? -eq 0 ]]
  then
    $BUILDDIR/shuffle -memory $MEMORY -verbose $VERBOSE < $COOCCURRENCE_FILE > $COOCCURRENCE_SHUF_FILE
    if [[ $? -eq 0 ]]
    then
       $BUILDDIR/glove -save-file $SAVE_FILE -threads $NUM_THREADS -input-file $COOCCURRENCE_SHUF_FILE -x-max $X_MAX -iter $MAX_ITER -vector-size $VECTOR_SIZE -binary $BINARY -vocab-file $VOCAB_FILE -verbose $VERBOSE
       if [[ $? -eq 0 ]]
       then
           if [ "$1" = 'matlab' ]; then
               matlab -nodisplay -nodesktop -nojvm -nosplash < ./eval/matlab/read_and_evaluate.m 1>&2 
           elif [ "$1" = 'octave' ]; then
               octave < ./eval/octave/read_and_evaluate_octave.m 1>&2 
           else
               python eval/python/evaluate.py > google_result_100.txt
               python eval/msr_eval/evaluate.py --vectors_file  $SAVE_FILE.txt > msr_result_100.txt
               python /home/msjameel/acl_2016/evaluation/manal_code/all_wordsim.py $SAVE_FILE.txt /home/msjameel/acl_2016/evaluation/manal_code/data/word-sim > similarity_result_100.txt
           fi
       fi
    fi
  fi
fi
fi
fi
fi
fi
fi
#rm -rf temp_files
#unlink bin_to_txt.txt
