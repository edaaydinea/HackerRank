import java.util.Locale;
import java.util.Scanner;

public class Solution {

    static boolean isAnagram(String a, String b) {
        // Complete the function
        a = a.toUpperCase();
        b = b.toUpperCase();
        boolean anagram = false;
        StringBuilder b1 = new StringBuilder(b);

        if(a.length() == b.length()) {
            for (int i = 0; i < a.length(); i++){
                for (int j = 0; j < b1.length(); j++){
                    if(a.charAt(i) == b1.charAt(j)){
                        b1.deleteCharAt(j);
                        if (i==a.length()-1 && b1.length()==0){
                            anagram = true;
                            break;
                        }
                        break;
                    }
                }
            }
        }
        return anagram;
    }

    public static void main(String[] args) {

        Scanner scan = new Scanner(System.in);
        String a = scan.next();
        String b = scan.next();
        scan.close();
        boolean ret = isAnagram(a, b);
        System.out.println( (ret) ? "Anagrams" : "Not Anagrams" );
    }
}
