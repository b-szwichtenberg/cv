#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

#include "map.h"
#include "utils.h"

#define MAX_FPATH_SIZE 256
#define MAX_MAP_SPOTS 2

void exit_on_error(int r);
void exit_on_error_(int r, int e);
int move_left(const size_t width, const size_t height, char map[][width], Position *p, Position spots[]);
int move_up(const size_t width, const size_t height, char map[][width], Position *p, Position spots[]);
int move_right(const size_t width, const size_t height, char map[][width], Position *p, Position spots[]);
int move_down(const size_t width, const size_t height, char map[][width], Position *p, Position spots[]);
void quit();
void print_inf();
bool is_any_move_available(const size_t width, const size_t height, char map[][width]);
bool is_container_set(const size_t row, const size_t col, Position spots[]);
void bring_back_spot_if_any(const size_t width, char map[][width], Position spots[]);

int main() {
    puts("Witaj w grze SOKOBAN");
    puts("Wybierz poziom ...");
    size_t option = 0;
    do {
        puts("1 - łatwy");
        puts("2 - średni");
        puts("0 - opuść grę");
        exit_on_error_(scanf("%ld", &option), 1);
    } while (option > 2);
    if (option == 0) {
        exit(EXIT_SUCCESS);
    }
    print_inf();

    char f_path[MAX_FPATH_SIZE];
    exit_on_error(obtain_full_fpath(f_path, option, MAX_FPATH_SIZE));

    size_t width = 0;
    size_t height = 0;
    exit_on_error(set_width_and_height(f_path, &width, &height));

    char map[height][width];
    exit_on_error(load_map(f_path, width, height, map));

    Position player_pos = {0, 0};
    exit_on_error(set_player_coord(width, height, map, &player_pos));

    Position spots[MAX_MAP_SPOTS];
    size_t x = 0;
    for (x; x < MAX_MAP_SPOTS; ++x) {
        spots[x].row = 0;
        spots[x].col = 0;
    }
    exit_on_error(set_places_coord(width, height, map, spots));

    size_t containers_to_set = 0;
    exit_on_error(count_containers(width, height, map, &containers_to_set));

    puts("Gra została rozpoczęta");

    size_t set_containers = 0;
    size_t direction = 0;
    print_map(width, height, map, direction);
    while (true) {
        char c;
        exit_on_error_(scanf(" %c", &c), 1);
        int r = system("tput clear");

        switch (c) {
            case 'a':
                set_containers += move_left(width, height, map, &player_pos, spots);
                direction = 3;
                break;
            case 'A':
                set_containers += move_left(width, height, map, &player_pos, spots);
                direction = 3;
                break;
            case 'w':
                set_containers += move_up(width, height, map, &player_pos, spots);
                direction = 0;
                break;
            case 'W':
                set_containers += move_up(width, height, map, &player_pos, spots);
                direction = 0;
                break;
            case 'd':
                set_containers += move_right(width, height, map, &player_pos, spots);
                direction = 1;
                break;
            case 'D':
                set_containers += move_right(width, height, map, &player_pos, spots);
                direction = 1;
                break;
            case 's':
                set_containers += move_down(width, height, map, &player_pos, spots);
                direction = 2;
                break;
            case 'S':
                set_containers += move_down(width, height, map, &player_pos, spots);
                direction = 2;
                break;
            case 'q':
                quit();
                break;
            case 'Q':
                quit();
                break;
            case 'i':
                print_inf();
                break;
            case 'I':
                print_inf();
                break;
            default:
                puts("Nie wiem co masz na myśli...");
                break;
        }

        bring_back_spot_if_any(width, map, spots);

        if (set_containers == containers_to_set) {
            int r_ = system("tput clear");
            puts("Udało Ci się! Ukończyłeś poziom!");
            print_map(width, height, map, direction);
            break;
        }

        print_map(width, height, map, direction);

        if (!is_any_move_available(width, height, map)) {
            puts("Nie ma już możliwości ukończenia mapy!");
            break;
        }
    }

    quit();
}

void exit_on_error(int r) {
    exit_on_error_(r, 0);
}

void exit_on_error_(int r, int e) {
    if (r != e) {
        exit(EXIT_FAILURE);
    }
}

int move_left(const size_t width, const size_t height, char map[][width], Position *p, Position spots[]) {
    if (map[p->row][p->col - 1] == ' ') {
        map[p->row][p->col - 1] = 'A';
        map[p->row][p->col] = ' ';
        p->col -= 1;
    }
    else if (map[p->row][p->col - 1] == 'X') {
        map[p->row][p->col - 1] = 'A';
        map[p->row][p->col] = ' ';
        p->col -= 1;
    }
    else if (map[p->row][p->col - 1] == '#') {
        puts("Nie można zrealizować tego ruchu.");
    }
    else if (map[p->row][p->col - 1] == 'O') {
        if (is_container_set(p->row, p->col - 1, spots)) {
            puts("Nie można przesunąć tego kontenera - jest już ustawiony.");
        }
        else if (map[p->row][p->col - 2] == ' ') {
            map[p->row][p->col - 2] = 'O';
            map[p->row][p->col - 1] = 'A';
            map[p->row][p->col] = ' ';
            p->col -= 1;
        }
        else if (map[p->row][p->col - 2] == '#' || map[p->row][p->col - 2] == 'O') {
            puts("Nie można przesunąć kontenera - stoi przed przeszkodą.");
        }
        else if (map[p->row][p->col - 2] == 'X') {
            map[p->row][p->col - 2] = 'O';
            map[p->row][p->col - 1] = 'A';
            map[p->row][p->col] = ' ';
            p->col -= 1;
            return 1;
        }
    }

    return 0;
}

int move_up(const size_t width, const size_t height, char map[][width], Position *p, Position spots[]) {
    if (map[p->row - 1][p->col] == ' ') {
        map[p->row - 1][p->col] = 'A';
        map[p->row][p->col] = ' ';
        p->row -= 1;
    }
    else if (map[p->row - 1][p->col] == 'X') {
        map[p->row - 1][p->col] = 'A';
        map[p->row][p->col] = ' ';
        p->row -= 1;
    }
    else if (map[p->row - 1][p->col] == '#') {
        puts("Nie można zrealizować tego ruchu.");
    }
    else if (map[p->row - 1][p->col] == 'O') {
        if (is_container_set(p->row - 1, p->col, spots)) {
            puts("Nie można przesunąć tego kontenera - jest już ustawiony.");
        }
        else if (map[p->row - 2][p->col] == ' ') {
            map[p->row - 2][p->col] = 'O';
            map[p->row - 1][p->col] = 'A';
            map[p->row][p->col] = ' ';
            p->row -= 1;
        }
        else if (map[p->row - 2][p->col] == '#' || map[p->row - 2][p->col] == 'O') {
            puts("Nie można przesunąć kontenera - stoi przed przeszkodą.");
        }
        else if (map[p->row - 2][p->col] == 'X') {
            map[p->row - 2][p->col] = 'O';
            map[p->row - 1][p->col] = 'A';
            map[p->row][p->col] = ' ';
            p->row -= 1;
            return 1;
        }
    }

    return 0;
}

int move_right(const size_t width, const size_t height, char map[][width], Position *p, Position spots[]) {
    if (map[p->row][p->col + 1] == ' ') {
        map[p->row][p->col + 1] = 'A';
        map[p->row][p->col] = ' ';
        p->col += 1;
    }
    else if (map[p->row][p->col + 1] == 'X') {
        map[p->row][p->col + 1] = 'A';
        map[p->row][p->col] = ' ';
        p->col += 1;
    }
    else if (map[p->row][p->col + 1] == '#') {
        puts("Nie można zrealizować tego ruchu.");
    }
    else if (map[p->row][p->col + 1] == 'O') {
        if (is_container_set(p->row, p->col + 1, spots)) {
            puts("Nie można przesunąć tego kontenera - jest już ustawiony.");
        }
        else if (map[p->row][p->col + 2] == ' ') {
            map[p->row][p->col + 2] = 'O';
            map[p->row][p->col + 1] = 'A';
            map[p->row][p->col] = ' ';
            p->col += 1;
        }
        else if (map[p->row][p->col + 2] == '#' || map[p->row][p->col + 2] == 'O') {
            puts("Nie można przesunąć kontenera - stoi przed przeszkodą.");
        }
        else if (map[p->row][p->col + 2] == 'X') {
            map[p->row][p->col + 2] = 'O';
            map[p->row][p->col + 1] = 'A';
            map[p->row][p->col] = ' ';
            p->col += 1;
            return 1;
        }
    }

    return 0;
}

int move_down(const size_t width, const size_t height, char map[][width], Position *p, Position spots[]) {
    if (map[p->row + 1][p->col] == ' ') {
        map[p->row + 1][p->col] = 'A';
        map[p->row][p->col] = ' ';
        p->row += 1;
    }
    else if (map[p->row + 1][p->col] == 'X') {
        map[p->row + 1][p->col] = 'A';
        map[p->row][p->col] = ' ';
        p->row += 1;
    }
    else if (map[p->row + 1][p->col] == '#') {
        puts("Nie można zrealizować tego ruchu.");
    }
    else if (map[p->row + 1][p->col] == 'O') {
        if (is_container_set(p->row + 1, p->col, spots)) {
            puts("Nie można przesunąć tego kontenera - jest już ustawiony.");
        }
        else if (map[p->row + 2][p->col] == ' ') {
            map[p->row + 2][p->col] = 'O';
            map[p->row + 1][p->col] = 'A';
            map[p->row][p->col] = ' ';
            p->row += 1;
        }
        else if (map[p->row + 2][p->col] == '#' || map[p->row + 2][p->col] == 'O') {
            puts("Nie można przesunąć kontenera - stoi przed przeszkodą.");
        }
        else if (map[p->row + 2][p->col] == 'X') {
            map[p->row + 2][p->col] = 'O';
            map[p->row + 1][p->col] = 'A';
            map[p->row][p->col] = ' ';
            p->row += 1;
            return 1;
        }
    }

    return 0;
}

void quit() {
    puts("Opuszczam grę.");
    exit(EXIT_SUCCESS);
}

void print_inf() {
    puts("Wciśnięcie w dowolnym momencie `q` spowoduje wyjście z gry");
    puts("Wciśnięcie w dowolnym momencie `i` wypisze informację o sterowaniu");
    puts("Sterowanie odbywa się za pomocą:");
    puts("`w` - ruch w górę");
    puts("`d` - ruch w prawo");
    puts("`s` - ruch w dół");
    puts("`a` - ruch w lewo");
}

bool is_any_move_available(const size_t width, const size_t height, char map[][width]) {
    return true;
}

bool is_container_set(const size_t row, const size_t col, Position spots[]) {
    size_t i = 0;
    for (i; i < MAX_MAP_SPOTS; ++i) {
        if (spots[i].row == row && spots[i].col == col) {
            return true;
        }
    }
    return false;
}

void bring_back_spot_if_any(const size_t width, char map[][width], Position spots[]) {
    size_t i = 0;
    for (i; i < MAX_MAP_SPOTS; ++i) {
        if (map[spots[i].row][spots[i].col] == ' ') { // in case actor was standing on that field
            map[spots[i].row][spots[i].col] = 'X';
        }
    }
}