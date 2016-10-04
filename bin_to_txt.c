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

typedef struct cooccur_rec {
    int word1;
    int word2;
    double val;
} CREC;

int main(int argc, char ** argv) {
    fprintf(stderr, "RUNNING BIN-TO-TXT\n");
    char *input_file = NULL;
    input_file = (char *) malloc(MAX_STRING_LENGTH * sizeof ( char));
    if (input_file == NULL) {
        fprintf(stderr, "malloc() memory allocation error\n");
        exit(1);
    }
    strcat(input_file, argv [ 1 ]);
    FILE *fin;
    fin = fopen(input_file, "rb");
    if (fin == NULL) {
        fprintf(stderr, "Cooccurrence file open error in bin_to_txt\n");
        exit(1);
    }

    FILE *output_file = NULL;
    output_file = fopen("bin_to_txt.txt", "w");
    if (output_file == NULL) {
        fprintf(stderr, "File write error in bin_to_txt.txt\n");
        exit(1);
    }

    CREC cr;
    while (!feof(fin)) {
        fread(&cr, sizeof ( CREC), 1, fin);
        fprintf(output_file, "%d %d %lf\n", cr.word1, cr.word2, cr.val);
    }

    fprintf(stderr, "DONE GENERATING TEXT\n");

    fclose(fin);
    fclose(output_file);
    return ( EXIT_SUCCESS);
}