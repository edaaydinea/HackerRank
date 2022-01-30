import java.awt.event.WindowFocusListener;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN.
        Print output to STDOUT. Your class should be named Solution. */

        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();

        ArrayList<ArrayList<Integer>> lists = new ArrayList();
        for(int row = 0; row < n; row++){
            int d = scanner.nextInt();
            ArrayList<Integer> list = new ArrayList();
            for (int column=0; column<d; column++){
                list.add(scanner.nextInt());
            }
            lists.add(list);
        }

        int queries = scanner.nextInt();
        for (int i =0; i <queries; i++){
            int x = scanner.nextInt();
            int y = scanner.nextInt();
            ArrayList<Integer> list = lists.get(x-1);
            if (y<=list.size()){
                System.out.println(list.get(y-1));
            }
            else {
                System.out.println("ERROR!");
            }
        }
    }
}