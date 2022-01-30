import java.util.*;
class Solution{

    public static void main(String []argh)
    {
        Scanner sc = new Scanner(System.in);

        while (sc.hasNext()) {
            String input=sc.next();
            //Complete the code
            while (input.length() != (input = input.replaceAll("\\(\\)|\\[\\]|\\{\\}","")).length());
                System.out.println(input.isEmpty());
        }

    }
}



