/*
Java Stdin and Stdout I

Scanner scanner = new Scanner(System.in);
String myString = scanner.next();
int myInt = scanner.nextInt();
scanner.close();

System.out.println("myString is: " + myString);
System.out.println("myInt is: " + myInt);

Author: Eda AYDIN
 */

import java.util.*;

public class Solution {

    public static void main(String[] args) {
        try (Scanner scan = new Scanner(System.in)) {
            int a = scan.nextInt();
            int b = scan.nextInt();
            int c = scan.nextInt();

            System.out.println(a);
            System.out.println(b);
            System.out.println(c);
        }
    }
}