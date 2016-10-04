/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define _FILE_OFFSET_BITS 64
#define MAX_STRING_LENGTH 1000
#define TUNED_REGULARIZER 5000

typedef struct cooccur_rec {
    int word1;
    int word2;
    double val;
} CREC;

int main(int argc, char ** argv) {
    fprintf(stderr, "ADDING DIRICHLET COUNTS\n");
    char *input_file = NULL;//this will be the unshuffled co-occurrence file
    input_file = (char *) malloc(MAX_STRING_LENGTH * sizeof ( char));
    if (input_file == NULL) {
        fprintf(stderr, "malloc() memory allocation error\n");
        exit(1);
    }
    strcat(input_file, argv [ 1 ]);
    
    char *vocab_file = NULL;
    vocab_file = malloc(sizeof(char) * MAX_STRING_LENGTH);
    if ( vocab_file == NULL )
    {
        fprintf (stderr,"malloc() memory allocation error in vocab_file\n");
        exit(1);
    }
    strcat(vocab_file,argv[2]);

    double *dirichlet_alpha = NULL;
    unsigned int vocab_size = 0;
    FILE *fid;
    unsigned int i = 0;
    unsigned int b = 0;

    fid = fopen(vocab_file, "r");
    if (fid == NULL) {
        fprintf(stderr, "Unable to open vocab file %s.\n", vocab_file);
        exit(1);
    }
    while ((i = getc(fid)) != EOF)
        if (i == '\n')
            vocab_size++; // Count number of entries in vocab_file
    fclose(fid);

    char * word = NULL;
    word = (char *) malloc(MAX_STRING_LENGTH * sizeof (char));
    if (word == NULL) {
        fprintf(stderr, "malloc() memory allocation error in word\n");
        exit(1);
    }
    
    double total_sum_cooccurrences = 0.0; //this will carry the total sum of all co-occurrences
    double val = 0.0;
    
    for (b = 0; b < vocab_size; b++) {
        fscanf(fid, "%s %lf\n", word, &val);
        total_sum_cooccurrences += val;
    }
    rewind(fid);
    
    dirichlet_alpha = (double *) malloc(vocab_size * sizeof ( double));
    if (dirichlet_alpha == NULL) {
        fprintf(stderr, "malloc() memory allocation error in dirichlet_alpha\n");
        exit(1);
    }
    memset(dirichlet_alpha, 0, vocab_size);
    
    for (b = 0; b < vocab_size; b++) {
        fscanf(fid, "%s %lf\n", word, &val);
        dirichlet_alpha[b] = (val / total_sum_cooccurrences) * TUNED_REGULARIZER;
    }
    fclose(fid);
    free(word);
    free(vocab_file);
    free(input_file);

    FILE *fin;
    fin = fopen(input_file, "rb");
    if (fin == NULL) {
        fprintf(stderr, "Cooccurrence file open error in bin_to_txt\n");
        exit(1);
    }

    FILE *output_file = NULL;
    output_file = fopen("dirichlet_added.bin", "wb");
    if (output_file == NULL) {
        fprintf(stderr, "File write error in dirichlet_added.bin\n");
        exit(1);
    }

    CREC cr;
    while (!feof(fin)) {
        fread(&cr, sizeof ( CREC), 1, fin);        
        fwrite(&cr.word1, sizeof (int), 1, output_file);
        fwrite(&cr.word2, sizeof (int), 1, output_file);
        fwrite(&(dirichlet_alpha[cr.word2-1]+cr.val), sizeof (double), 1, output_file);
    }

    fprintf(stderr, "DONE GENERATING FILE\n");

    fclose(fin);
    fclose(output_file);
    return ( EXIT_SUCCESS);
}