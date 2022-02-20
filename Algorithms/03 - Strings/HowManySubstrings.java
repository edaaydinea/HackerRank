import java.io.ByteArrayInputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.util.*;

public class How_Many_Substrings {
    public int lenbuf = 0, ptrbuf = 0;
    InputStream is;
    PrintWriter out;
    String INPUT = "";
    private byte[] inbuf = new byte[1024];

    public static long sumFenwick(long[] ft, int i) {
        long sum = 0;
        for (i++; i > 0; i -= i & -i) sum += ft[i];
        return sum;
    }

    public static void addFenwick(long[] ft, int i, long v) {
        if (v == 0) return;
        int n = ft.length;
        for (i++; i < n; i += i & -i) ft[i] += v;
    }

    public static int firstGEFenwick(long[] ft, long v) {
        int i = 0, n = ft.length;
        for (int b = Integer.highestOneBit(n); b != 0; b >>= 1) {
            if ((i | b) < n && ft[i | b] < v) {
                i |= b;
                v -= ft[i];
            }
        }
        return i;
    }

    public static long[] restoreFenwick(long[] ft) {
        int n = ft.length - 1;
        long[] ret = new long[n];
        for (int i = 0; i < n; i++) ret[i] = sumFenwick(ft, i);
        for (int i = n - 1; i >= 1; i--) ret[i] -= ret[i - 1];
        return ret;
    }

    public static int findGFenwick(long[] ft, long v) {
        int i = 0;
        int n = ft.length;
        for (int b = Integer.highestOneBit(n); b != 0 && i < n; b >>= 1) {
            if (i + b < n) {
                int t = i + b;
                if (v >= ft[t]) {
                    i = t;
                    v -= ft[t];
                }
            }
        }
        return v != 0 ? -(i + 1) : i - 1;
    }

    public static long[] buildFenwick(long[] a) {
        int n = a.length;
        long[] ft = new long[n + 1];
        System.arraycopy(a, 0, ft, 1, n);
        for (int k = 2, h = 1; k <= n; k *= 2, h *= 2) {
            for (int i = k; i <= n; i += k) {
                ft[i] += ft[i - h];
            }
        }
        return ft;
    }

    public static void addRangeFenwick(long[] ft0, long[] ft1, int i, long v) {
        addFenwick(ft1, i + 1, -v);
        addFenwick(ft1, 0, v);
        addFenwick(ft0, i + 1, v * (i + 1));
    }

    public static void addRangeFenwick(long[] ft0, long[] ft1, int a, int b, long v) {
        if (a <= b) {
            addFenwick(ft1, b + 1, -v);
            addFenwick(ft0, b + 1, v * (b + 1));
            addFenwick(ft1, a, v);
            addFenwick(ft0, a, -v * a);
        }
    }

    public static long sumRangeFenwick(long[] ft0, long[] ft1, int i) {
        return sumFenwick(ft1, i) * (i + 1) + sumFenwick(ft0, i);
    }

    public static long[] restoreRangeFenwick(long[] ft0, long[] ft1) {
        int n = ft0.length - 1;
        long[] ret = new long[n];
        for (int i = 0; i < n; i++) ret[i] = sumRangeFenwick(ft0, ft1, i);
        for (int i = n - 1; i >= 1; i--) ret[i] -= ret[i - 1];
        return ret;
    }

    public static int lca2(int a, int b, int[][] spar, int[] depth) {
        if (depth[a] < depth[b]) {
            b = ancestor(b, depth[b] - depth[a], spar);
        } else if (depth[a] > depth[b]) {
            a = ancestor(a, depth[a] - depth[b], spar);
        }

        if (a == b)
            return a;
        int sa = a, sb = b;
        for (int low = 0, high = depth[a], t = Integer.highestOneBit(high), k = Integer
                .numberOfTrailingZeros(t); t > 0; t >>>= 1, k--) {
            if ((low ^ high) >= t) {
                if (spar[k][sa] != spar[k][sb]) {
                    low |= t;
                    sa = spar[k][sa];
                    sb = spar[k][sb];
                } else {
                    high = low | t - 1;
                }
            }
        }
        return spar[0][sa];
    }

    protected static int ancestor(int a, int m, int[][] spar) {
        for (int i = 0; m > 0 && a != -1; m >>>= 1, i++) {
            if ((m & 1) == 1)
                a = spar[i][a];
        }
        return a;
    }

    public static int[][] logstepParents(int[] par) {
        int n = par.length;
        int m = Integer.numberOfTrailingZeros(Integer.highestOneBit(n - 1)) + 1;
        int[][] pars = new int[m][n];
        pars[0] = par;
        for (int j = 1; j < m; j++) {
            for (int i = 0; i < n; i++) {
                pars[j][i] = pars[j - 1][i] == -1 ? -1 : pars[j - 1][pars[j - 1][i]];
            }
        }
        return pars;
    }

    public static int[][] parents3(int[][] g, int root) {
        int n = g.length;
        int[] par = new int[n];
        Arrays.fill(par, -1);

        int[] depth = new int[n];
        depth[0] = 0;

        int[] q = new int[n];
        q[0] = root;
        for (int p = 0, r = 1; p < r; p++) {
            int cur = q[p];
            for (int nex : g[cur]) {
                if (par[cur] != nex) {
                    q[r++] = nex;
                    par[nex] = cur;
                    depth[nex] = depth[cur] + 1;
                }
            }
        }
        return new int[][]{par, q, depth};
    }

    static int[][] packU(int n, int[] from, int[] to) {
        int[][] g = new int[n][];
        int[] p = new int[n];
        for (int f : from)
            p[f]++;
        for (int t : to)
            p[t]++;
        for (int i = 0; i < n; i++)
            g[i] = new int[p[i]];
        for (int i = 0; i < from.length; i++) {
            g[from[i]][--p[from[i]]] = to[i];
            g[to[i]][--p[to[i]]] = from[i];
        }
        return g;
    }

    public static void main(String[] args) throws Exception {
        new How_Many_Substrings().run();
    }

    private static void tr(Object... o) {
        System.out.println(Arrays.deepToString(o));
    }

    void solve() {
        int n = ni(), Q = ni();
        char[] s = ns(n);
        int[][] qs = new int[Q][];
        for (int z = 0; z < Q; z++) {
            qs[z] = new int[]{ni(), ni(), z};
        }
        Arrays.sort(qs, new Comparator<int[]>() {
            public int compare(int[] a, int[] b) {
                return a[1] - b[1];
            }
        });

        SuffixAutomatonOfBit sa = SuffixAutomatonOfBit.build(s);
        sa.sortTopologically();
        SuffixAutomatonOfBit.Node[] nodes = sa.nodes;
        int[] from = new int[nodes.length - 1];
        int[] to = new int[nodes.length - 1];
        int p = 0;
        for (SuffixAutomatonOfBit.Node node : nodes) {
            if (node.id >= 1) {
                from[p] = node.link.id;
                to[p] = node.id;
                p++;
            }
        }
        assert p == nodes.length - 1;
        int[][] g = packU(nodes.length, from, to);
        int[][] pars = parents3(g, 0);
        int[] par = pars[0], ord = pars[1], dep = pars[2];
        HeavyLightDecomposition hld = new HeavyLightDecomposition(g, par, ord, dep);
        int m = hld.cluspath.length;
        SegmentTreeOverwrite[] sts = new SegmentTreeOverwrite[m];
        for (int i = 0; i < m; i++) {
            sts[i] = new SegmentTreeOverwrite(hld.cluspath[i].length);
        }

        int[] base = new int[n];
        int qp = 0;
        int np = 0;
        long[] ft0 = new long[n + 3];
        long[] ft1 = new long[n + 3];
        long[] ans = new long[Q];
        for (int i = 0; i < n; i++) {
            while (!(nodes[np].len == i + 1 && nodes[np].original == null)) np++;
            base[i] = np;
//            tr("base", base[i]);

            // 5 3 1 0
            // 5 3 1 0
            // 8 6 3 1 0 ?
            // aaba

            // delete
            int cur = 0;
            int ppos = 0;
            while (true) {
                int last = sts[hld.clus[cur]].get(hld.clusiind[cur]);
                if (last == -1) break;
                int lca = hld.lca(base[last], base[i]);
                // delete from lca to cur
                //            nodes[cur].len, nodes[lca].len;
                int inf = last - nodes[lca].len + 1;
                int sup = last - ppos + 1;
//                tr("del", last, ppos, nodes[lca].len, inf, sup);
                // _/
                addFenwick(ft0, 0, -(sup - inf));
                addFenwick(ft0, sup + 1, +(sup - inf));
                addFenwick(ft0, inf + 1, -(inf + 1));
                addFenwick(ft0, sup + 1, +inf + 1);
                addFenwick(ft1, inf + 1, 1);
                addFenwick(ft1, sup + 1, -1);
//                tr(i, restoreRangeFenwick(ft0, ft1));
                ppos = nodes[lca].len;
                assert dep[base[i]] - dep[lca] - 1 >= 0;
                cur = hld.ancestor(base[i], dep[base[i]] - dep[lca] - 1);
            }
            // x
            //b a
            //   a

            // paint
            int cx = hld.clus[base[i]]; // cluster
            int ind = hld.clusiind[base[i]]; // pos in cluster
            while (true) {
                sts[cx].update(0, ind + 1, i);
                int con = par[hld.cluspath[cx][0]];
                if (con == -1) break;
                ind = hld.clusiind[con];
                cx = hld.clus[con];
            }

//            tr(i, restoreRangeFenwick(ft0, ft1));
            addFenwick(ft0, 0, i + 1 + 1);
            addFenwick(ft0, i + 1 + 1, -(i + 1 + 1));
            addFenwick(ft1, 0, -1);
            addFenwick(ft1, i + 1 + 1, 1);
//            tr(i, restoreRangeFenwick(ft0, ft1));

            while (qp < Q && qs[qp][1] <= i) {
//                tr(qs[qp]);
                ans[qs[qp][2]] = sumRangeFenwick(ft0, ft1, qs[qp][0]);
                qp++;
            }
        }
        for (long an : ans) {
            out.println(an);
        }
    }

    void run() throws Exception {
        is = INPUT.isEmpty() ? System.in : new ByteArrayInputStream(INPUT.getBytes());
        out = new PrintWriter(System.out);

        long s = System.currentTimeMillis();
        solve();
        out.flush();
        if (!INPUT.isEmpty()) tr(System.currentTimeMillis() - s + "ms");
    }

    private int readByte() {
        if (lenbuf == -1) throw new InputMismatchException();
        if (ptrbuf >= lenbuf) {
            ptrbuf = 0;
            try {
                lenbuf = is.read(inbuf);
            } catch (IOException e) {
                throw new InputMismatchException();
            }
            if (lenbuf <= 0) return -1;
        }
        return inbuf[ptrbuf++];
    }

    private boolean isSpaceChar(int c) {
        return !(c >= 33 && c <= 126);
    }

    private int skip() {
        int b;
        while ((b = readByte()) != -1 && isSpaceChar(b)) ;
        return b;
    }

    private double nd() {
        return Double.parseDouble(ns());
    }

    private char nc() {
        return (char) skip();
    }

    private String ns() {
        int b = skip();
        StringBuilder sb = new StringBuilder();
        while (!(isSpaceChar(b))) { // when nextLine, (isSpaceChar(b) && b != ' ')
            sb.appendCodePoint(b);
            b = readByte();
        }
        return sb.toString();
    }

    private char[] ns(int n) {
        char[] buf = new char[n];
        int b = skip(), p = 0;
        while (p < n && !(isSpaceChar(b))) {
            buf[p++] = (char) b;
            b = readByte();
        }
        return n == p ? buf : Arrays.copyOf(buf, p);
    }

    private char[][] nm(int n, int m) {
        char[][] map = new char[n][];
        for (int i = 0; i < n; i++) map[i] = ns(m);
        return map;
    }

    private int[] na(int n) {
        int[] a = new int[n];
        for (int i = 0; i < n; i++) a[i] = ni();
        return a;
    }

    private int ni() {
        int num = 0, b;
        boolean minus = false;
        while ((b = readByte()) != -1 && !((b >= '0' && b <= '9') || b == '-')) ;
        if (b == '-') {
            minus = true;
            b = readByte();
        }

        while (true) {
            if (b >= '0' && b <= '9') {
                num = num * 10 + (b - '0');
            } else {
                return minus ? -num : num;
            }
            b = readByte();
        }
    }

    private long nl() {
        long num = 0;
        int b;
        boolean minus = false;
        while ((b = readByte()) != -1 && !((b >= '0' && b <= '9') || b == '-')) ;
        if (b == '-') {
            minus = true;
            b = readByte();
        }

        while (true) {
            if (b >= '0' && b <= '9') {
                num = num * 10 + (b - '0');
            } else {
                return minus ? -num : num;
            }
            b = readByte();
        }
    }

    public static class SegmentTreeOverwrite {
        public int M, H, N;
        public int[] cover;
        public int I = Integer.MAX_VALUE;

        public SegmentTreeOverwrite(int len) {
            N = len;
            M = Integer.highestOneBit(Math.max(N - 1, 1)) << 2;
            H = M >>> 1;
            cover = new int[M];
            Arrays.fill(cover, I);
            for (int i = 0; i < N; i++) {
                cover[H + i] = -1;
            }
            for (int i = H - 1; i >= 1; i--) {
                propagate(i);
            }
        }

        private void propagate(int i) {
        }

        public void update(int l, int r, int v) {
            update(l, r, v, 0, H, 1);
        }

        private void update(int l, int r, int v, int cl, int cr, int cur) {
            if (l <= cl && cr <= r) {
                cover[cur] = v;
                propagate(cur);
            } else {
                int mid = cl + cr >>> 1;
                if (cover[cur] != I) { // back-propagate
                    cover[2 * cur] = cover[2 * cur + 1] = cover[cur];
                    cover[cur] = I;
                    propagate(2 * cur);
                    propagate(2 * cur + 1);
                }
                if (cl < r && l < mid) {
                    update(l, r, v, cl, mid, 2 * cur);
                }
                if (mid < r && l < cr) {
                    update(l, r, v, mid, cr, 2 * cur + 1);
                }
                propagate(cur);
            }
        }

        public int get(int x) {
            int val = I;
            for (int i = H + x; i >= 1; i >>>= 1) {
                if (cover[i] != I) val = cover[i];
            }
            return val;
        }
    }

    public static class HeavyLightDecomposition {
        public int[] clus;
        public int[][] cluspath;
        public int[] clusiind;
        public int[] par, dep;

        public HeavyLightDecomposition(int[][] g, int[] par, int[] ord, int[] dep) {
            init(g, par, ord, dep);
        }

        public static int[] decomposeToHeavyLight(int[][] g, int[] par, int[] ord) {
            int n = g.length;
            int[] size = new int[n];
            Arrays.fill(size, 1);
            for (int i = n - 1; i > 0; i--) size[par[ord[i]]] += size[ord[i]];

            int[] clus = new int[n];
            Arrays.fill(clus, -1);
            int p = 0;
            for (int i = 0; i < n; i++) {
                int u = ord[i];
                if (clus[u] == -1) clus[u] = p++;
                // centroid path (not heavy path)
                int argmax = -1;
                for (int v : g[u]) {
                    if (par[u] != v && (argmax == -1 || size[v] > size[argmax])) argmax = v;
                }
                if (argmax != -1) clus[argmax] = clus[u];
            }
            return clus;
        }

        public static int[][] clusPaths(int[] clus, int[] ord) {
            int n = clus.length;
            int[] rp = new int[n];
            int sup = 0;
            for (int i = 0; i < n; i++) {
                rp[clus[i]]++;
                sup = Math.max(sup, clus[i]);
            }
            sup++;

            int[][] row = new int[sup][];
            for (int i = 0; i < sup; i++) row[i] = new int[rp[i]];

            for (int i = n - 1; i >= 0; i--) {
                row[clus[ord[i]]][--rp[clus[ord[i]]]] = ord[i];
            }
            return row;
        }

        public static int[] clusIInd(int[][] clusPath, int n) {
            int[] iind = new int[n];
            for (int[] path : clusPath) {
                for (int i = 0; i < path.length; i++) {
                    iind[path[i]] = i;
                }
            }
            return iind;
        }

        public void init(int[][] g, int[] par, int[] ord, int[] dep) {
            clus = decomposeToHeavyLight(g, par, ord);
            cluspath = clusPaths(clus, ord);
            clusiind = clusIInd(cluspath, g.length);
            this.par = par;
            this.dep = dep;
        }

        public int lca(int x, int y) {
            int rx = cluspath[clus[x]][0];
            int ry = cluspath[clus[y]][0];
            while (clus[x] != clus[y]) {
                if (dep[rx] > dep[ry]) {
                    x = par[rx];
                    rx = cluspath[clus[x]][0];
                } else {
                    y = par[ry];
                    ry = cluspath[clus[y]][0];
                }
            }
            return clusiind[x] > clusiind[y] ? y : x;
        }

        public int ancestor(int x, int v) {
            while (x != -1) {
                if (v <= clusiind[x]) return cluspath[clus[x]][clusiind[x] - v];
                v -= clusiind[x] + 1;
                x = par[cluspath[clus[x]][0]];
            }
            return x;
        }
    }

    public static class SuffixAutomatonOfBit {
        public Node t0;
        public int len;
        public Node[] nodes;
        public int gen;
        private boolean sortedTopologically = false;
        private boolean lexsorted = false;

        private SuffixAutomatonOfBit(int n) {
            gen = 0;
            nodes = new Node[2 * n];
            this.t0 = makeNode(0, null);
        }

        public static SuffixAutomatonOfBit build(char[] str) {
            int n = str.length;
            SuffixAutomatonOfBit sa = new SuffixAutomatonOfBit(n);
            sa.len = str.length;

            Node last = sa.t0;
            for (char c : str) {
                last = sa.extend(last, c);
            }

            return sa;
        }

        private Node makeNode(int len, Node original) {
            Node node = new Node();
            node.id = gen;
            node.original = original;
            node.len = len;
            nodes[gen++] = node;
            return node;
        }

        public Node extend(Node last, char c) {
            Node cur = makeNode(last.len + 1, null);
            Node p;
            for (p = last; p != null && !p.containsKeyNext(c); p = p.link) {
                p.putNext(c, cur);
            }
            if (p == null) {
                cur.link = t0;
            } else {
                Node q = p.getNext(c); // not null
                if (p.len + 1 == q.len) {
                    cur.link = q;
                } else {
                    Node clone = makeNode(p.len + 1, q);
                    clone.next = Arrays.copyOf(q.next, q.next.length);
                    clone.hit = q.hit;
                    clone.np = q.np;
                    clone.link = q.link;
                    for (; p != null && q.equals(p.getNext(c)); p = p.link) {
                        p.putNext(c, clone);
                    }
                    q.link = cur.link = clone;
                }
            }
            return cur;
        }

        public SuffixAutomatonOfBit lexSort() {
            for (int i = 0; i < gen; i++) {
                Node node = nodes[i];
                Arrays.sort(node.next, 0, node.np, new Comparator<Node>() {
                    public int compare(Node a, Node b) {
                        return a.key - b.key;
                    }
                });
            }
            lexsorted = true;
            return this;
        }

        public SuffixAutomatonOfBit sortTopologically() {
            int[] indeg = new int[gen];
            for (int i = 0; i < gen; i++) {
                for (int j = 0; j < nodes[i].np; j++) {
                    indeg[nodes[i].next[j].id]++;
                }
            }
            Node[] sorted = new Node[gen];
            sorted[0] = t0;
            int p = 1;
            for (int i = 0; i < gen; i++) {
                Node cur = sorted[i];
                for (int j = 0; j < cur.np; j++) {
                    if (--indeg[cur.next[j].id] == 0) {
                        sorted[p++] = cur.next[j];
                    }
                }
            }

            for (int i = 0; i < gen; i++) sorted[i].id = i;
            nodes = sorted;
            sortedTopologically = true;
            return this;
        }

        public String toString() {
            StringBuilder sb = new StringBuilder();
            for (Node n : nodes) {
                if (n != null) {
                    sb.append(String.format("{id:%d, len:%d, link:%d, cloned:%b, ",
                            n.id,
                            n.len,
                            n.link != null ? n.link.id : null,
                            n.original.id));
                    sb.append("next:{");
                    for (int i = 0; i < n.np; i++) {
                        sb.append(n.next[i].key + ":" + n.next[i].id + ",");
                    }
                    sb.append("}");
                    sb.append("}");
                    sb.append("\n");
                }
            }
            return sb.toString();
        }

        // visualizer

        public String toGraphviz(boolean next, boolean suffixLink) {
            StringBuilder sb = new StringBuilder("http://chart.apis.google.com/chart?cht=gv:dot&chl=");
            sb.append("digraph{");
            for (Node n : nodes) {
                if (n != null) {
                    if (suffixLink && n.link != null) {
                        sb.append(n.id)
                                .append("->")
                                .append(n.link.id)
                                .append("[style=dashed],");
                    }

                    if (next && n.next != null) {
                        for (int i = 0; i < n.np; i++) {
                            sb.append(n.id)
                                    .append("->")
                                    .append(n.next[i].id)
                                    .append("[label=")
                                    .append(n.next[i].key)
                                    .append("],");
                        }
                    }
                }
            }
            sb.append("}");
            return sb.toString();
        }

        public String label(Node n) {
            if (n.original != null) {
                return n.id + "C";
            } else {
                return n.id + "";
            }
        }

        public String toDot(boolean next, boolean suffixLink) {
            StringBuilder sb = new StringBuilder("digraph{\n");
            sb.append("graph[rankdir=LR];\n");
            sb.append("node[shape=circle];\n");
            for (Node n : nodes) {
                if (n != null) {
                    if (suffixLink && n.link != null) {
                        sb.append("\"" + label(n) + "\"")
                                .append("->")
                                .append("\"" + label(n.link) + "\"")
                                .append("[style=dashed];\n");
                    }

                    if (next && n.next != null) {
                        for (int i = 0; i < n.np; i++) {
                            sb.append("\"" + label(n) + "\"")
                                    .append("->")
                                    .append("\"" + label(n.next[i]) + "\"")
                                    .append("[label=\"")
                                    .append(n.next[i].key)
                                    .append("\"];\n");
                        }
                    }
                }
            }
            sb.append("}\n");
            return sb.toString();
        }

        public static class Node {
            public int id;
            public int len;
            public char key;
            public Node link;
            public Node original;
            public int np = 0;
            public int hit = 0;
            private Node[] next = new Node[3];

            public void putNext(char c, Node to) {
                to.key = c;
                if (hit << ~(c - 'a') < 0) {
                    for (int i = 0; i < np; i++) {
                        if (next[i].key == c) {
                            next[i] = to;
                            return;
                        }
                    }
                }
                hit |= 1 << c - 'a';
                if (np == next.length) {
                    next = Arrays.copyOf(next, np * 2);
                }
                next[np++] = to;
            }

            public boolean containsKeyNext(char c) {
                return hit << ~(c - 'a') < 0;
//                for(int i = 0;i < np;i++){
//                    if(next[i].key == c)return true;
//                }
//                return false;
            }

            public Node getNext(char c) {
                if (hit << ~(c - 'a') < 0) {
                    for (int i = 0; i < np; i++) {
                        if (next[i].key == c) return next[i];
                    }
                }
                return null;
            }

            public List<String> suffixes(char[] s) {
                List<String> list = new ArrayList<String>();
                if (id == 0) return list;
                int first = original != null ? original.len : len;
                for (int i = link.len + 1; i <= len; i++) {
                    list.add(new String(s, first - i, i));
                }
                return list;
            }
        }
    }
}