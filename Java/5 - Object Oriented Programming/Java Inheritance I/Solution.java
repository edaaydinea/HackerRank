import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

class Animal{
    void walk()
    {
        System.out.println("I am walking");
    }
}
class Bird extends Animal implements asd
{
    void fly()
    {
        System.out.println("I am flying");
    }

    @Override
    public void sing() {
        System.out.println("I am singing");
    }
}

interface  asd{
    void sing();
}

public class Solution{

    public static void main(String args[]){

        Bird bird = new Bird();
        bird.walk();
        bird.fly();
        bird.sing();

    }
}