#include <iostream>
#include <string>
using namespace std;

struct AnimalInfo {
    string name;
    string species;
    int age;
    int lifespan;
};

class IShout {
public:
    virtual void Shout() = 0;
};

class Animal : public IShout {
public:
    AnimalInfo info;
    Animal(const AnimalInfo& i) : info(i) {}
    virtual void Move() = 0;
};

class Bird : public Animal {
public:
    Bird(const AnimalInfo& i) : Animal(i) {}
    void Move() override { cout << info.name << "は飛びます。" << endl; }
    void Shout() override { cout << info.name << "はピヨピヨと鳴きます。" << endl; }
};

class Fish : public Animal {
public:
    Fish(const AnimalInfo& i) : Animal(i) {}
    void Move() override { cout << info.name << "は泳ぎます。" << endl; }
    void Shout() override { cout << info.name << "はブクブクと鳴きます。" << endl; }
};

class Rabbit : public Animal {
public:
    Rabbit(const AnimalInfo& i) : Animal(i) {}
    void Move() override { cout << info.name << "は走ります。" << endl; }
    void Shout() override { cout << info.name << "はピョンピョンと鳴きます。" << endl; }
};

int main() {
    AnimalInfo birdInfo = {"スズメ", "鳥", 1, 3};
    AnimalInfo fishInfo = {"金魚", "魚", 2, 5};
    AnimalInfo rabbitInfo = {"うさぎ", "哺乳類", 3, 8};

    Bird bird(birdInfo);
    Fish fish(fishInfo);
    Rabbit rabbit(rabbitInfo);

    bird.Move(); bird.Shout();
    fish.Move(); fish.Shout();
    rabbit.Move(); rabbit.Shout();
    return 0;
} 