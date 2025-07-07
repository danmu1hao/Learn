class AnimalInfo {
    constructor(name, species, age, lifespan) {
        this.name = name;
        this.species = species;
        this.age = age;
        this.lifespan = lifespan;
    }
}

class Animal {
    constructor(info) {
        this.info = info;
    }
    move() {}
    shout() {}
}

class Bird extends Animal {
    move() { console.log(this.info.name + 'は飛びます。'); }
    shout() { console.log(this.info.name + 'はピヨピヨと鳴きます。'); }
}

class Fish extends Animal {
    move() { console.log(this.info.name + 'は泳ぎます。'); }
    shout() { console.log(this.info.name + 'はブクブクと鳴きます。'); }
}

class Rabbit extends Animal {
    move() { console.log(this.info.name + 'は走ります。'); }
    shout() { console.log(this.info.name + 'はピョンピョンと鳴きます。'); }
}

const birdInfo = new AnimalInfo('スズメ', '鳥', 1, 3);
const fishInfo = new AnimalInfo('金魚', '魚', 2, 5);
const rabbitInfo = new AnimalInfo('うさぎ', '哺乳類', 3, 8);

const bird = new Bird(birdInfo);
const fish = new Fish(fishInfo);
const rabbit = new Rabbit(rabbitInfo);

bird.move(); bird.shout();
fish.move(); fish.shout();
rabbit.move(); rabbit.shout(); 