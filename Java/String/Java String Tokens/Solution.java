import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String s = scan.nextLine();
        scan.close();

        s = s.trim();
        if (s.length() == 0) {
            System.out.println(0);
        } else {
            String[] strings = s.split("[!,?._'@ ]+");
            System.out.println(strings.length);
            for(int i = 0; i < strings.length; i++){
                System.out.println(strings[i]);
            }
        }
    }
}

