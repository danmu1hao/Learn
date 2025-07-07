using System;

public struct AnimalInfo
{
    public string Name;
    public string Species;
    public int Age;
    public int LifeSpan;
}

public interface IShout
{
    void Shout();
}

public abstract class Animal : IShout
{
    public AnimalInfo Info;

    public Animal(AnimalInfo info)
    {
        Info = info;
    }

    public abstract void Move();
    public abstract void Shout();
}

public class Bird : Animal
{
    public Bird(AnimalInfo info) : base(info) { }
    public override void Move()
    {
        Console.WriteLine($"{Info.Name}は飛びます。");
    }
    public override void Shout()
    {
        Console.WriteLine($"{Info.Name}はピヨピヨと鳴きます。");
    }
}

public class Fish : Animal
{
    public Fish(AnimalInfo info) : base(info) { }
    public override void Move()
    {
        Console.WriteLine($"{Info.Name}は泳ぎます。");
    }
    public override void Shout()
    {
        Console.WriteLine($"{Info.Name}はブクブクと鳴きます。");
    }
}

public class Rabbit : Animal
{
    public Rabbit(AnimalInfo info) : base(info) { }
    public override void Move()
    {
        Console.WriteLine($"{Info.Name}は走ります。");
    }
    public override void Shout()
    {
        Console.WriteLine($"{Info.Name}はピョンピョンと鳴きます。");
    }
}

class Program
{
    static void Main()
    {
        AnimalInfo birdInfo = new AnimalInfo { Name = "スズメ", Species = "鳥", Age = 1, LifeSpan = 3 };
        AnimalInfo fishInfo = new AnimalInfo { Name = "金魚", Species = "魚", Age = 2, LifeSpan = 5 };
        AnimalInfo rabbitInfo = new AnimalInfo { Name = "うさぎ", Species = "哺乳類", Age = 3, LifeSpan = 8 };

        Animal bird = new Bird(birdInfo);
        Animal fish = new Fish(fishInfo);
        Animal rabbit = new Rabbit(rabbitInfo);

        bird.Move(); bird.Shout();
        fish.Move(); fish.Shout();
        rabbit.Move(); rabbit.Shout();
    }
}
