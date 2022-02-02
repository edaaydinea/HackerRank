import java.io.*;
import java.util.*;
import java.security.MessageDigest;
import java.util.Scanner;

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner scanner = new Scanner(System.in);
        String str = scanner.next();
        scanner.close();
        try {
            MessageDigest md = MessageDigest.getInstance("MD5");
            md.update(str.getBytes());
            byte[] digest = md.digest();
            for (byte b : digest)
            {
                System.out.printf("%02x",b);
            }
        }
        catch (Exception ex)
        {
            throw new RuntimeException(ex);
        }
    }
}