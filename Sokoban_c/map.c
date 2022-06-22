#define _GNU_SOURCE
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "map.h"
#include "utils.h"

#define MAP_SIZE 2

int load_map(char fpath[], const size_t width, const size_t height, char map[][width]) {
    FILE *fp;
    fp = fopen(fpath, "r");
    if (fp == NULL) {
        printf("Can't open the file[%s].\n", fpath);
        return -1;
    }

    char *line = (char*) malloc(sizeof(char)); // zapomnialem zalokowac odpowiednia ilosc elementow
    size_t len = width + 1;  
    int r = getline(&line, &len, fp);  // getline from GNU libc
    // first line dropped

    int ret_code = 0;
    size_t i = 0;
    for (i; i < height; ++i) {
        r = getline(&line, &len, fp);
        if (r != width + 1) {
            printf("Wrong width of line, r=%d instead of %ld.\n", r, width + 1);
            ret_code = -1;
            break;
        }
        memcpy(map[i], line, width * sizeof(char));
    }

    free(line);
    fclose(fp);

    return ret_code;
}

void print_map(const size_t width, const size_t height, char map[][width], const size_t direction) {
    // direction could be value from range(0, 3)
    size_t i = 0;
    for (i; i < height; ++i) {
        print_map_line(map[i], width, direction);
    }
}

void print_map_line(char line[], const size_t width, const size_t direction) {
    char new_line[width * MAP_SIZE];
    size_t i = 0;
    for (i; i < width; ++i) {
        char c = line[i];
        if (c == 'A') {  // A represent player
            c = get_directed_sign(direction);
        }
        size_t j = 0;
        for (j; j < MAP_SIZE; ++j) {
            new_line[i * MAP_SIZE + j] = c;
        }
    }

    size_t k = 0;
    for (k; k < MAP_SIZE; ++k) {
        size_t l = 0;
        for (l; l < width * MAP_SIZE; ++l) {
            if (new_line[l] == 'O') {
                green();
                putchar(new_line[l]);
                reset();
            }
            else if (new_line[l] == 'X') {
                red();
                putchar(new_line[l]);
                reset();
            }
            else if (new_line[l] == '^' || new_line[l] == '>' || new_line[l] == 'v' || new_line[l] == '<') {
                blue();
                putchar(new_line[l]);
                reset();
            }
            else {
                putchar(new_line[l]);
            }
        }
        puts("");
    }
}

char get_directed_sign(const size_t direction) {
    switch (direction) {
        case 0:  // UP
            return '^';
        case 1:  // RIGHT
            return '>';
        case 2:  // DOWN
            return 'v';
        case 3: // LEFT
            return '<';
        default:  // UP
            return '^';
    }
}
