import java.io.InputStream;
import java.util.LinkedList;
import java.util.List;
import java.util.Scanner;

public class SimilarStrings {

    private final int CHAR_COUNT = 10;
    int[] charIndexA = new int[CHAR_COUNT];
    int[] charIndexB = new int[CHAR_COUNT];
    int[] charIndex = new int[CHAR_COUNT];

    public static void main(String[] args) {
        new SimilarStrings().solve(System.in);
    }

    private Node build(String s) {
        Node root = new Node();

        for (int i = 0; i < s.length(); i++) {

            Node current = root;

            int charCount = 0;
            int[] charIndex = new int[CHAR_COUNT];
            for (int j = 0; j < CHAR_COUNT; j++) {
                charIndex[j] = -1;
            }

            for (int j = i; j < s.length(); j++) {
                int c = s.charAt(j) - 'a';
                int index = charIndex[c];

                if (index == -1) {
                    charIndex[c] = index = charCount++;
                }


                Node next = current.children[index];
                if (next == null) {
                    next = current.children[index] = new Node();
                }

                current = next;
                current.count++;
                if (j - i >= 50) {
                    if (current.startPositions == null) {
                        current.startPositions = new LinkedList<Integer>();
                    }
                    current.startPositions.add(i);
                    break;
                }
            }
        }

        return root;
    }

    private boolean isEqual(String str, int offsetA, int offsetB, int length) {
        int charCount = 0;

        for (int j = 0; j < CHAR_COUNT; j++) {
            charIndexA[j] = -1;
            charIndexB[j] = -1;
        }

        for (int i = 0; i < length; i++) {
            int ca = str.charAt(offsetA + i) - 'a';
            int cb = str.charAt(offsetB + i) - 'a';

            int indexA = charIndexA[ca];
            int indexB = charIndexB[cb];

            if (indexA != indexB) {
                return false;
            }

            if (indexA == -1) {
                charIndexA[ca] = charCount;
                charIndexB[cb] = charCount;
                charCount++;
            }
        }

        return true;
    }

    private int query(Node current, String str, int offset, int length) {

        int charCount = 0;
        for (int j = 0; j < CHAR_COUNT; j++) {
            charIndex[j] = -1;
        }

        for (int j = 0; j < length; j++) {
            int c = str.charAt(offset + j) - 'a';
            int index = charIndex[c];

            if (index == -1) {
                charIndex[c] = index = charCount++;
            }

            Node next = current.children[index];
            if (next == null) {

                if (current.startPositions != null) {
                    int cnt = 0;
                    for (int os : current.startPositions) {
                        int oe = os + length;
                        if (oe <= str.length() && isEqual(str, os, offset, length)) {
                            cnt++;
                        }
                    }
                    return cnt;
                }
                return 0;
            }

            current = next;
        }
        return current.count;
    }

    public void solve(InputStream stream) {
        Scanner s = new Scanner(stream);
        int n = s.nextInt();
        int q = s.nextInt();
        String str = s.next();
        Node tree = build(str);

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < q; i++) {
            int si = s.nextInt() - 1;
            int sj = s.nextInt() - 1;
            int result = query(tree, str, si, sj - si + 1);
            sb.append(result);
            sb.append('\n');
        }
        System.out.println(sb);
    }
}


class Node {
    int count;
    Node[] children;
    List<Integer> startPositions;

    Node() {
        children = new Node[10];
    }
}