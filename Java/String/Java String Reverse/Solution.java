import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {

        Scanner sc=new Scanner(System.in);
        String A=sc.next();
        /* Enter your code here. Print output to STDOUT. */

        StringBuilder reverseA = new StringBuilder();
        reverseA.append(A);
        reverseA.reverse();

        System.out.println(A.contentEquals(reverseA)?"Yes":"No");
    }
}



