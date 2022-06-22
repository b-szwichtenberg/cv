#pragma once

#include <stdbool.h>

int load_map(char fpath[], const size_t width, const size_t height, char map[][width]);
void print_map(const size_t width, const size_t height, char map[][width], const size_t direction);
void print_map_line(char line[], const size_t width, const size_t direction);
char get_directed_sign(const size_t direction);