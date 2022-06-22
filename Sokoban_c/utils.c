#include <stdlib.h>
#include <stdio.h>
#include <string.h>

#include "utils.h"

int obtain_full_fpath(char fpath[], const size_t option, const size_t max_size) {
    // option should be either 1 or 2
    char *proj_path = getenv("SOKOBAN_PATH");
    if (proj_path == NULL) {
        puts("Can't find project path.\n");
        return -1;
    }
    int r = snprintf(fpath, max_size, "%s/data/map0%ld.txt", proj_path, option);
    if (r < 0 || r > max_size) {
        printf("Too long path (%d chars) or encoding problem occurs.\n", r);
        return -1;
    }

    return 0;
}

int set_width_and_height(char fpath[], size_t *width, size_t *height) {
    FILE *fp;
    fp = fopen(fpath, "r");
    if (fp == NULL) {
        printf("Can't open the file[%s].\n", fpath);
        return -1;
    }

    char *line = NULL;
    size_t def_len = 0;
    int ret_code = 0;
    int r = getline(&line, &def_len, fp);  // getline from GNU libc
    if (r == 4) {  // line would be for example "2,3\n"
        // we know that width and height are from range(1, 9)
        *width = line[0] - '0';
        *height = line[2] - '0';
    }
    else {
        printf("Can't read map size, r=%d instead of 4.\n", r);
        ret_code = -1;
    }

    fclose(fp);
    free(line); // allocated in getline
    return ret_code;
}

int set_player_coord(const size_t width, const size_t height, char map[][width], Position *p) {
    size_t i = 0;
    for (i; i < height; ++i) {
        size_t j = 0;
        for (j; j < width; ++j) {
            if (map[i][j] == 'A') {
                p->row = i;
                p->col = j;
                // break;
            }
        }
    }

    if (p->row == 0 || p->col == 0) {
        puts("Can't find player on map.");
        return -1;
    }

    return 0;
}

int set_places_coord(const size_t width, const size_t height, char map[][width], Position ps[]) {
    size_t ps_counter = 0;
    size_t i = 0;
    for (i; i < height; ++i) {
        size_t j = 0;
        for (j; j < width; ++j) {
            if (map[i][j] == 'X') {
                ps[ps_counter].row = i;
                ps[ps_counter].col = j;
                ++ps_counter;
            }
        }
    }

    if (ps_counter == 0) {
        puts("Can't find all free container spots on map.");
        return -1;
    }

    return 0;
}

int count_containers(const size_t width, const size_t height, char map[][width], size_t *c) {
    size_t i = 0;
    for (i; i < height; ++i) {
        size_t j = 0;
        for (j; j < width; ++j) {
            if (map[i][j] == 'O') {
                *c = *c + 1;
            }
        }
    }

    if (*c == 0) {
        puts("Can't find containers on map.");
        return -1;
    }

    return 0;
}

void red() {
    printf("\x1B[31m");
}

void green() {
    printf("\x1B[32m");
}

void blue() {
    printf("\x1B[34m");
}

void reset() {
    printf("\x1B[0m");
}