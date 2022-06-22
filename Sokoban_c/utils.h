#pragma once

struct Position_ {
    size_t row;
    size_t col;
} typedef Position;

int obtain_full_fpath(char fpath[], const size_t option, const size_t max_size);
int set_width_and_height(char fpath[], size_t *width, size_t *height);
int set_player_coord(const size_t width, const size_t height, char map[][width], Position *p);
int set_places_coord(const size_t width, const size_t height, char map[][width], Position ps[]);
int count_containers(const size_t width, const size_t height, char map[][width], size_t *c);
void red();
void green();
void blue();
void reset();