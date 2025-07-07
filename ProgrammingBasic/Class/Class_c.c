#include <stdio.h>

// 動物の基本情報を表す構造体
typedef struct {
    char name[20];
    char species[20];
    int age;
    int lifespan;
} AnimalInfo;

// 動物を表す構造体（関数ポインタで多態性を模倣）
typedef struct Animal {
    AnimalInfo info;
    void (*move)(struct Animal*);
    void (*shout)(struct Animal*);
} Animal;

void bird_move(Animal* self) {
    printf("%sは飛びます。\n", self->info.name);
}
void bird_shout(Animal* self) {
    printf("%sはピヨピヨと鳴きます。\n", self->info.name);
}

int main() {
    AnimalInfo birdInfo = {"スズメ", "鳥", 1, 3};
    Animal bird;
    bird.info = birdInfo;
    bird.move = bird_move;
    bird.shout = bird_shout;

    bird.move(&bird);
    bird.shout(&bird);
    return 0;
} 