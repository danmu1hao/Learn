class AnimalInfo {
    String name;
    String species;
    int age;
    int lifespan;
    AnimalInfo(String name, String species, int age, int lifespan) {
        this.name = name;
        this.species = species;
        this.age = age;
        this.lifespan = lifespan;
    }
}

interface IShout {
    void shout();
}

abstract class Animal implements IShout {
    AnimalInfo info;
    Animal(AnimalInfo info) {
        this.info = info;
    }
    abstract void move();
}

class Bird extends Animal {
    Bird(AnimalInfo info) { super(info); }
    void move() { System.out.println(info.name + "は飛びます。"); }
    public void shout() { System.out.println(info.name + "はピヨピヨと鳴きます。"); }
}

class Fish extends Animal {
    Fish(AnimalInfo info) { super(info); }
    void move() { System.out.println(info.name + "は泳ぎます。"); }
    public void shout() { System.out.println(info.name + "はブクブクと鳴きます。"); }
}

class Rabbit extends Animal {
    Rabbit(AnimalInfo info) { super(info); }
    void move() { System.out.println(info.name + "は走ります。"); }
    public void shout() { System.out.println(info.name + "はピョンピョンと鳴きます。"); }
}

public class Class_java {
    public static void main(String[] args) {
        AnimalInfo birdInfo = new AnimalInfo("スズメ", "鳥", 1, 3);
        AnimalInfo fishInfo = new AnimalInfo("金魚", "魚", 2, 5);
        AnimalInfo rabbitInfo = new AnimalInfo("うさぎ", "哺乳類", 3, 8);

        Animal bird = new Bird(birdInfo);
        Animal fish = new Fish(fishInfo);
        Animal rabbit = new Rabbit(rabbitInfo);

        bird.move(); bird.shout();
        fish.move(); fish.shout();
        rabbit.move(); rabbit.shout();
    }
} 