import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution{
    public static void main(String[] args){

        Scanner in = new Scanner(System.in);
        int testCases = Integer.parseInt(in.nextLine());
        Pattern pattern = Pattern.compile("<([^>]+)>([^<]+)</\\1>");
        while(testCases>0){
            String line = in.nextLine();

            //Write your code here
            Matcher matcher = pattern.matcher(line);
            int matches = 0;
            while(matcher.find()){
                matches ++;
                System.out.println(matcher.group(2));
            }
            if(matches == 0){
                System.out.println("None");
            }

            testCases--;
        }
    }
}



