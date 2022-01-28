import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN.
        Print output to STDOUT. Your class should be named Solution. */
        Scanner in = new Scanner(System.in);
        int N = in.nextInt();
        int M = in.nextInt();
        BitSet[] bitSets = new BitSet[] {new BitSet(N), new BitSet(N)};
        for (int i = 0; i <M; i++){
            String q = in.next();
            int left = in.nextInt() - 1;
            int right = in.nextInt() - 1;
            if (q.equals("AND"))
                bitSets[left].and(bitSets[right]);
            if (q.equals("OR"))
                bitSets[left].or(bitSets[right]);
            if (q.equals("XOR"))
                bitSets[left].xor(bitSets[right]);
            if (q.equals("FLIP"))
                bitSets[left].flip(N - right - 1);
            if (q.equals("SET"))
                bitSets[left].set(N - right - 1);
            System.out.println(bitSets[0].cardinality() + " "+ bitSets[1].cardinality());
        }
    }
}