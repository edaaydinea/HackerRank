import java.io.*;
import java.nio.charset.StandardCharsets;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.util.*;

public class Solution {

    public static void main(String[] args) throws NoSuchAlgorithmException {
        /* Enter your code here. Read input from STDIN.
        Print output to STDOUT. Your class should be named Solution. */

        Scanner scanner = new Scanner(System.in);
        MessageDigest messageDigest = MessageDigest.getInstance("SHA-256");
        messageDigest.reset();
        messageDigest.update(scanner.nextLine().getBytes(StandardCharsets.UTF_8));
        for (byte i : messageDigest.digest())
        {
            System.out.printf("%02x",i);
        }
        System.out.println();
    }
}