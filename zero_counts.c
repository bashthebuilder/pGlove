/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include </home/msjameel/gsl-2.1/gsl/gsl_randist.h>

#define _FILE_OFFSET_BITS 64
#define MAX_STRING_LENGTH 1000

int main(int argc, char ** argv) {
    fprintf(stderr, "RUNNING ZERO COUNTS\n");
    int file_counter = 0;
    int number_of_lines = 0;
    int vocab_size = 0;
    int i = 0;
    int word1 = 0;
    int word2 = 0;
    int *word1_array = NULL;
    int *word2_array = NULL;
    int *missing_contexts = NULL; //finding zero contexts.
    int *chosen_contexts = NULL;
    int number_of_elements = 0;

    double val = 0.0;

    FILE *fid = NULL;
    fid = fopen("vocab.txt", "r");
    if (fid == NULL) {
        fprintf(stderr, "Unable to open vocab file vocab.txt\n");
        return 1;
    }
    while ((i = getc(fid)) != EOF) {
        if (i == '\n') {
            vocab_size++; // Count number of entries in vocab_file
        }
    }
    fclose(fid);

    char *file_name = NULL;
    file_name = (char *) malloc(MAX_STRING_LENGTH * sizeof ( char));
    if (file_name == NULL) {
        fprintf(stderr, "malloc() memory allocation error in file_name\n");
        exit(1);
    }
    memset(file_name, 0, MAX_STRING_LENGTH);
    word1_array = (int *) malloc(vocab_size * sizeof (int));
    if (word1_array == NULL) {
        fprintf(stderr, "malloc() memory allocation error in word1\n");
        exit(1);
    }
    word2_array = (int *) malloc(vocab_size * sizeof (int));
    if (word2_array == NULL) {
        fprintf(stderr, "malloc() memory allocation error in word2\n");
        exit(1);
    }
    memset(word2_array, 0, vocab_size);
    missing_contexts = (int *) malloc(vocab_size * sizeof (int));
    if (missing_contexts == NULL) {
        fprintf(stderr, "malloc() memory allocation error in missing_contexts\n");
        exit(1);
    }
    chosen_contexts = (int*) malloc(vocab_size * sizeof (int));
    if (chosen_contexts == NULL) {
        fprintf(stderr, "malloc() memory allocation error in chosen_contexts\n");
        exit(1);
    }

    const gsl_rng_type * T;
    gsl_rng * r;
    gsl_rng_env_setup();
    T = gsl_rng_default;
    r = gsl_rng_alloc(T);

    FILE *context_file = NULL;
    memset(word1_array, 0, vocab_size);
    memset(word2_array, 0, vocab_size);
    memset(missing_contexts, 0, vocab_size);
    memset(chosen_contexts, 0, vocab_size);

    for (file_counter = 1; file_counter <= vocab_size; file_counter++) {
        sprintf(file_name, "temp_files/%d", file_counter);
        strcat(file_name, ".tmp");
        context_file = fopen(file_name, "r");
        if (context_file == NULL) {
            fprintf(stderr, "Context file open error\n");
            exit(1);
        }
        while (!feof(context_file)) {
            fscanf(context_file, "%d %d %lf\n", &word1, &word2, &val);
            word1_array[word1] = 1;
            word2_array[word2] = 1;
            number_of_lines++;
        }//read the entire file now.
        fclose(context_file);
        context_file = fopen(file_name, "a");
        if (context_file == NULL) {
            fprintf(stderr, "Context file open error\n");
            exit(1);
        }
        for (i = 1; i <= vocab_size; i++) {
            if (word2_array[i] == 0) {
                missing_contexts[number_of_elements] = i;
                number_of_elements++;
            }
        }
        if ( number_of_lines > number_of_elements)
        {
            number_of_lines = number_of_elements;
        }
        gsl_ran_shuffle(r, missing_contexts, number_of_lines, sizeof (int));
        gsl_ran_choose(r, chosen_contexts, 3, missing_contexts, number_of_elements, sizeof (int));
        for (i = 0; i < number_of_lines; i++) {
            fprintf(context_file, "%d %d %lf\n", word1, chosen_contexts[i], 0.0);
        }
        memset(word1_array, 0, vocab_size);
        memset(word2_array, 0, vocab_size);
        memset(missing_contexts, 0, vocab_size);
        memset(chosen_contexts, 0, vocab_size);
        number_of_lines = 0;
        number_of_elements = 0;
        fclose(context_file);
        memset(file_name, 0, MAX_STRING_LENGTH);
    }

    fprintf(stderr,"ZERO COUNTING DONE\n");
    free(file_name);
    free(word1_array);
    free(word2_array);
    free(missing_contexts);
    free(chosen_contexts);
    gsl_rng_free(r);
    return ( EXIT_SUCCESS);
}
