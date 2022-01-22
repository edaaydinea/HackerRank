import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */

        Scanner input = new Scanner(System.in);
        int b = input.nextInt();
        int h = input.nextInt();
        boolean flag = b > 0 && h > 0;

        if (!flag)
        {
            System.out.println("java.lang.Exception: Breadth and height must be positive");
        }
        else
        {
            System.out.println(b*h);
        }
    }
}