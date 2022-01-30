import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT.
        Your class should be named Solution. */

        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();

        LinkedList<Integer> list = new LinkedList<>();
        for(int i = 0; i < n; i++){
            int value = scanner.nextInt();
            list.add(value);
        }

        int queries = scanner.nextInt();
        for (int i = 0; i < queries; i++){
            String operation = scanner.next();
            if (operation.equals("Insert")){
                int index = scanner.nextInt();
                int value = scanner.nextInt();
                list.add(index, value);
            }
            else if (operation.equals("Delete")) {
                int index = scanner.nextInt();
                list.remove(index);
            }
        }
        for(Integer num : list){
            System.out.print(num + " ");
        }
    }
}