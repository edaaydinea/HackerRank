import java.util.*;

class Solution {
    public static void main(String []argh){
        Scanner in = new Scanner(System.in);
        int t=in.nextInt();
        for(int i=0;i<t;i++) {
            int a = in.nextInt();
            int b = in.nextInt();
            int n = in.nextInt();
            int result = a;
            for (int j = 0; j < n; j++) {
                result += (int) (Math.pow(2, j) * b);
                System.out.print(result + " ");
            }
            System.out.print("\n");
        }
        in.close();
    }
}