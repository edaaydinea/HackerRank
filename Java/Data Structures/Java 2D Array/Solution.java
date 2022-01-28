import java.util.Scanner;

public class Solution {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        int arr[][] = new int[6][6];

        for(int row=0; row < 6; row++){
            for(int column=0; column <6; column++){
                arr[row][column] = scanner.nextInt();
            }
        }
        scanner.close();

        int max= Integer.MIN_VALUE;

        for (int row=0; row<4;row++){
            for (int column=0; column<4; column++){
                int sum = arr[row+0][column+0] + arr[row+0][column+1] + arr[row+0][column+2]
                                               + arr[row+1][column+1] +
                          arr[row+2][column+0] + arr[row+2][column+1] + arr[row+2][column+2];
                max = Math.max(max,sum);
            }
        }
        System.out.println(max);
    }
}