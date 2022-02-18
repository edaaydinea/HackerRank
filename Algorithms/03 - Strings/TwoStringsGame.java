import java.io.*;
import java.util.Arrays;
import java.util.StringTokenizer;

public class TwoStringsGame {

    static final int maximum_n = 300000;
    static final long limit = 1000000000000000000L;

    static boolean[] was = new boolean[30];
    static long[] srt;

    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        StringTokenizer stringTokenizer = new StringTokenizer(bufferedReader.readLine());
        int n = Integer.parseInt(stringTokenizer.nextToken());
        int m = Integer.parseInt(stringTokenizer.nextToken());
        long k = Long.parseLong(stringTokenizer.nextToken());

        srt = new long[maximum_n * 2 + 3];

        Sfa sfa1 = new Sfa(n);

        char[] a = bufferedReader.readLine().toCharArray();
        for (int i = 0; i < n; i++) {
            sfa1.push(a[i] - 'a');
        }

        Sfa sfa2 = new Sfa(n);

        char[] b = bufferedReader.readLine().toCharArray();
        for (int i = 0; i < m; i++) {
            sfa2.push(b[i] - 'a');
        }

        sfa1.grundyPreCalculation();
        for (int i = 1; i <= (Math.min(sfa2.nodes, 29)); i++) {
            was[i] = false;
        }

        sfa2.grundyPreCalculation();
        sfa2.subStrPreCalculation();

        for (int i = 1; i <= sfa1.nodes; i++) {
            srt[i] = ((long) sfa1.length[i] << 32L) | i;
        }
        Arrays.sort(srt, 1, sfa1.nodes + 1);
        for (int i = 1; i <= sfa1.nodes; i++) {
            int kk = (int) (srt[sfa1.nodes - i + 1] & 0xffffffffL);
            sfa1.dp[kk] = sfa2.dp[1] - sfa2.grundySum[sfa1.grundy[kk]];
            for (int j = 0; j < 26; j++) {
                if (sfa1.next[j][kk] > 0) {
                    sfa1.dp[kk] += sfa1.dp[sfa1.next[j][kk]];
                    if (sfa1.dp[kk] > limit) {
                        sfa1.dp[kk] = limit;
                    }
                }
            }
        }

        if (k > sfa1.dp[1]) {
            bufferedWriter.write("no solution");
            bufferedWriter.newLine();

            bufferedWriter.close();
            bufferedReader.close();
            return;
        }
        int cur = 1;
        while (k > 0) {
            if (k <= sfa2.dp[1] - sfa2.grundySum[sfa1.grundy[cur]]) {
                break;
            } else {
                k -= sfa2.dp[1] - sfa2.grundySum[sfa1.grundy[cur]];
            }
            for (int j = 0; j < 26; j++)
                if (k > sfa1.dp[sfa1.next[j][cur]])
                    k -= sfa1.dp[sfa1.next[j][cur]];
                else {
                    bufferedWriter.write('a' + j);
                    cur = sfa1.next[j][cur];
                    break;
                }
        }
        bufferedWriter.newLine();

        int badValue = sfa1.grundy[cur];
        sfa2.dpReCalculation(badValue);
        cur = 1;
        while (k > 0) {
            if (sfa2.grundy[cur] != badValue) {
                --k;
                if (k == 0) {
                    break;
                }
            }
            for (int j = 0; j < 26; j++) {
                if (k > sfa2.dp[sfa2.next[j][cur]]) {
                    k -= sfa2.dp[sfa2.next[j][cur]];
                } else {
                    bufferedWriter.write('a' + j);
                    cur = sfa2.next[j][cur];
                    break;
                }
            }
        }

        bufferedWriter.newLine();

        bufferedWriter.close();
        bufferedReader.close();
    }

    static class Sfa {

        long[] dp;
        long[] grundySum;
        long[] ways;

        int[][] next;
        int[] length;
        int[] lnk;
        int[] grundy;

        int nodes, last;

        Sfa(int n) {
            dp = new long[maximum_n * 2 + 3];
            grundySum = new long[30];
            ways = new long[maximum_n * 2 + 3];

            next = new int[26][maximum_n * 2 + 3];
            length = new int[maximum_n * 2 + 3];
            lnk = new int[maximum_n * 2 + 3];
            grundy = new int[maximum_n * 2 + 3];

            nodes = last = 1;
            length[1] = lnk[1] = 0;
        }

        void push(int c) {
            int cur = ++nodes, p;
            length[cur] = length[last] + 1;
            for (p = last; (p > 0) && (next[c][p] == 0); p = lnk[p]) {
                next[c][p] = cur;
            }
            if (p == 0) {
                lnk[cur] = 1;
            } else {
                int q = next[c][p];
                if (length[p] + 1 == length[q]) {
                    lnk[cur] = q;
                } else {
                    int clone = ++nodes;
                    length[clone] = length[p] + 1;
                    for (int j = 0; j < 26; j++) {
                        next[j][clone] = next[j][q];
                    }
                    lnk[clone] = lnk[q];
                    for (; (p > 0) && next[c][p] == q; p = lnk[p]) {
                        next[c][p] = clone;
                    }
                    lnk[q] = lnk[cur] = clone;
                }
            }
            last = cur;
        }

        void grundyPreCalculation() {
            for (int i = 1; i <= nodes; i++) {
                srt[i] = ((long) length[i] << 32L) | i;
            }
            Arrays.sort(srt, 1, nodes + 1);
            for (int i = 1; i <= nodes; i++) {
                int k = (int) (srt[nodes - i + 1] & 0xffffffffL);
                dp[k] = 1;
                Arrays.fill(was, false);
                for (int j = 0; j < 26; j++) {
                    if (next[j][k] > 0) {
                        was[grundy[next[j][k]]] = true;
                    }
                }
                for (int j = 0; j < 30; j++) {
                    if (!was[j]) {
                        grundy[k] = j;
                        break;
                    }
                }
            }
        }

        void subStrPreCalculation() {
            for (int i = 1; i <= nodes; i++) {
                srt[i] = ((long) length[i] << 32L) | i;
            }
            Arrays.sort(srt, 1, nodes + 1);
            for (int i = 1; i <= nodes; i++) {
                int k = (int) (srt[nodes - i + 1] & 0xffffffffL);
                dp[k] = 1;
                for (int j = 0; j < 26; j++) {
                    if (next[j][k] > 0) {
                        dp[k] += dp[next[j][k]];
                    }
                }
            }
            ways[1] = 1;
            for (int i = 1; i <= nodes; i++) {
                int k = (int) (srt[i] & 0xffffffffL);
                for (int j = 0; j < 26; j++) {
                    if (next[j][k] > 0) {
                        ways[next[j][k]] += ways[k];
                    }
                }
            }
            for (int i = 1; i <= nodes; i++) {
                grundySum[grundy[i]] += ways[i];
            }
        }

        void dpReCalculation(int badValue) {
            for (int i = 1; i <= nodes; i++) {
                srt[i] = ((long) length[i] << 32L) | i;
            }
            Arrays.sort(srt, 1, nodes + 1);
            for (int i = 1; i <= nodes; i++) {
                int k = (int) (srt[nodes - i + 1] & 0xffffffffL);
                dp[k] = grundy[k] != badValue ? 1 : 0;
                for (int j = 0; j < 26; j++) {
                    if (next[j][k] > 0) {
                        dp[k] += dp[next[j][k]];
                    }
                }
            }
        }
    }
}