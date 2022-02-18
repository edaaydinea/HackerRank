import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class PseudoIsomorphicSubstrings {

    public static void main(final String[] args) {
        final Scanner in = new Scanner(System.in);
        final String line = in.next();
        final char[] charsLine = line.toCharArray();
        final int[] indexesMinusprevOccurenceIndexes = new int[line.length()];
        final Map<Character, Integer> prev = new HashMap<>();
        for (int i = 0; i < line.length(); i++) {
            if (prev.containsKey(charsLine[i])) {
                indexesMinusprevOccurenceIndexes[i] = i - prev.get(charsLine[i]);
            }
            prev.put(charsLine[i], i);
        }
        new ST(indexesMinusprevOccurenceIndexes);
    }

    public static class ST {

        private final int[] values;
        private final Node root;
        private ActivePoint activePoint;
        private int remainder;
        private long totalLeavesCount;
        private long leavesSum;
        public ST(final int[] values) {
            this.values = values;
            this.root = new Node(0);
            this.activePoint = new ActivePoint(this.root, null, 0);
            this.remainder = 0;
            this.totalLeavesCount = 0;
            this.leavesSum = 0;
            build();
        }

        private void build() {
            for (int i = 0; i < this.values.length; i++) {
                add(i);
            }
        }

        private void add(final int index) {
            this.remainder++;
            boolean valueFoundInTheTree = false;
            Node previouslyAddedNodeOrAddedEdgeNode = null;
            while (!valueFoundInTheTree && this.remainder > 0) {
                final int suffixStartIndex = index - this.remainder + 1;
                final int valueToCheckExistanceInTree = this.activePoint.getSuffixValue(suffixStartIndex, this.values, index);
                if (this.activePoint.pointsToActiveNode()) {
                    if (this.activePoint.activeNodeHasEdgeStartingWith(valueToCheckExistanceInTree)) {
                        activeNodeHasEdgeStartingWithValue(valueToCheckExistanceInTree,
                                previouslyAddedNodeOrAddedEdgeNode);
                        valueFoundInTheTree = true;
                    } else {
                        if (this.activePoint.activeNodeIs(this.root)) {
                            rootNodeHasNotEdgeStartingWithValue(suffixStartIndex, index, valueToCheckExistanceInTree);
                        } else {
                            previouslyAddedNodeOrAddedEdgeNode = internalNodeHasNotEdgeStartingWithValue(
                                    suffixStartIndex,
                                    index,
                                    valueToCheckExistanceInTree,
                                    previouslyAddedNodeOrAddedEdgeNode);
                        }
                    }
                } else {
                    if (this.activePoint.pointsToOnActiveEdge(this.values, valueToCheckExistanceInTree)) {
                        activeEdgeHasValue();
                        valueFoundInTheTree = true;
                    } else {
                        if (this.activePoint.activeNodeIs(this.root)) {
                            previouslyAddedNodeOrAddedEdgeNode = edgeFromRootNodeHasNotValue(suffixStartIndex,
                                    index,
                                    valueToCheckExistanceInTree,
                                    previouslyAddedNodeOrAddedEdgeNode);
                        } else {
                            previouslyAddedNodeOrAddedEdgeNode = edgeFromInternalNodeHasNotValue(suffixStartIndex,
                                    index,
                                    valueToCheckExistanceInTree,
                                    previouslyAddedNodeOrAddedEdgeNode);
                        }
                    }
                }
            }
            this.leavesSum += this.totalLeavesCount;
            System.out.println(this.leavesSum);
        }

        private void activeNodeHasEdgeStartingWithValue(final int value,
                                                        final Node previouslyAddedNodeOrAddedEdgeNode) {
            this.activePoint.setSlinkToActiveNode(previouslyAddedNodeOrAddedEdgeNode);
            this.activePoint = this.activePoint.moveToEdgeStartingWithAndByOne(value);
            if (this.activePoint.pointsToTheEndOfActiveEdge()) {
                this.activePoint = this.activePoint.moveToNextNodeOfActiveEdge();
            }
        }

        private void rootNodeHasNotEdgeStartingWithValue(final int suffixStartIndex, final int index, final int value) {
            this.activePoint.addEdgeToActiveNode(value, new Edge(suffixStartIndex, index, this.values.length, null));
            this.totalLeavesCount++;
            this.activePoint = this.activePoint.moveTo(this.root);
            this.remainder--;
            assert this.remainder == 0;
        }

        private Node internalNodeHasNotEdgeStartingWithValue(final int suffixStartIndex,
                                                             final int index,
                                                             final int value,
                                                             Node previouslyAddedNodeOrAddedEdgeNode) {
            this.activePoint.addEdgeToActiveNode(value, new Edge(suffixStartIndex, index, this.values.length, null));
            this.totalLeavesCount++;
            previouslyAddedNodeOrAddedEdgeNode = this.activePoint.setSlinkToActiveNode(
                    previouslyAddedNodeOrAddedEdgeNode);
            if (this.activePoint.activeNodeHasSlink()) {
                this.activePoint = this.activePoint.moveToSlink(this.values, suffixStartIndex + 1, index);
            } else {
                this.activePoint = this.activePoint.moveTo(this.root, this.remainder - 2);
            }
            this.activePoint = walkDown(suffixStartIndex + 1);
            this.remainder--;
            return previouslyAddedNodeOrAddedEdgeNode;
        }

        private void activeEdgeHasValue() {
            this.activePoint = this.activePoint.moveByOneValue();
            if (this.activePoint.pointsToTheEndOfActiveEdge()) {
                this.activePoint = this.activePoint.moveToNextNodeOfActiveEdge();
            }
        }

        private Node edgeFromRootNodeHasNotValue(final int suffixStartIndex,
                                                 final int index,
                                                 final int value,
                                                 Node previouslyAddedNodeOrAddedEdgeNode) {
            final Node newNode = this.activePoint.splitActiveEdge(this.values,
                    suffixStartIndex,
                    index,
                    value);
            this.totalLeavesCount++;
            previouslyAddedNodeOrAddedEdgeNode = this.activePoint.setSlinkTo(previouslyAddedNodeOrAddedEdgeNode,
                    newNode);
            this.activePoint = this.activePoint.moveTo(this.root, this.remainder - 2);
            this.activePoint = walkDown(suffixStartIndex + 1);
            this.remainder--;
            return previouslyAddedNodeOrAddedEdgeNode;
        }

        private Node edgeFromInternalNodeHasNotValue(final int suffixStartIndex,
                                                     final int index,
                                                     final int value,
                                                     Node previouslyAddedNodeOrAddedEdgeNode) {
            final Node newNode = this.activePoint.splitActiveEdge(this.values,
                    suffixStartIndex,
                    index,
                    value);
            this.totalLeavesCount++;
            previouslyAddedNodeOrAddedEdgeNode = this.activePoint.setSlinkTo(previouslyAddedNodeOrAddedEdgeNode,
                    newNode);
            if (this.activePoint.activeNodeHasSlink()) {
                this.activePoint = this.activePoint.moveToSlink(this.values, suffixStartIndex + 1, index);
            } else {
                this.activePoint = this.activePoint.moveTo(this.root, this.remainder - 2);
            }
            this.activePoint = walkDown(suffixStartIndex + 1);
            this.remainder--;
            return previouslyAddedNodeOrAddedEdgeNode;
        }

        private ActivePoint walkDown(final int suffixStartIndex) {
            while (!this.activePoint.pointsToActiveNode()
                    && (this.activePoint.pointsToTheEndOfActiveEdge() || this.activePoint.pointsAfterTheEndOfActiveEdge())) {
                if (this.activePoint.pointsAfterTheEndOfActiveEdge()) {
                    this.activePoint = this.activePoint.moveToNextNodeOfActiveEdge(this.values, suffixStartIndex);
                } else {
                    this.activePoint = this.activePoint.moveToNextNodeOfActiveEdge();
                }
            }
            return this.activePoint;
        }

        public static class Node {
            private final int valuesFromRootCount;
            private final Map<Integer, Edge> edges;
            private Node slink;

            public Node(final int valuesFromRootCount) {
                this.valuesFromRootCount = valuesFromRootCount;
                this.edges = new HashMap<>();
            }

            public int getValuesFromRootCount() {
                return this.valuesFromRootCount;
            }

            public Map<Integer, Edge> getEdges() {
                return this.edges;
            }

            public Node getSlink() {
                return this.slink;
            }

            public void setSlink(final Node slink) {
                this.slink = slink;
            }
        }

        public static class Edge {
            private final int suffixStartIndex;
            private final int from;
            private final int to;
            private final Node next;

            public Edge(final int suffixStartIndex, final int from, final int to, final Node next) {
                this.suffixStartIndex = suffixStartIndex;
                this.from = from;
                this.to = to;
                this.next = next;
            }

            public int getSuffixStartIndex() {
                return this.suffixStartIndex;
            }

            public int getFrom() {
                return this.from;
            }

            public int getTo() {
                return this.to;
            }

            public Node getNext() {
                return this.next;
            }

            public int getLength() {
                return this.to - this.from;
            }
        }

        public static class ActivePoint {
            private final Node activeNode;
            private final Integer activeEdgeFirstValue;
            private final int activeLength;

            public ActivePoint(final Node activeNode,
                               final Integer activeEdgeFirstValue,
                               final int activeLength) {
                this.activeNode = activeNode;
                this.activeEdgeFirstValue = activeEdgeFirstValue;
                this.activeLength = activeLength;
            }

            private Edge getActiveEdge() {
                return this.activeNode.getEdges().get(this.activeEdgeFirstValue);
            }

            private int getActiveValue(final int[] values) {
                final int valueOnEdgeIndex = getActiveEdge().getFrom() + this.activeLength;
                return getSuffixValue(getActiveEdge().getSuffixStartIndex(), values, valueOnEdgeIndex);
            }

            public int getSuffixValue(final int suffixStartIndex, final int[] values, final int valueIndex) {
                return suffixStartIndex <= valueIndex - values[valueIndex] ? values[valueIndex] : 0;
            }

            public boolean pointsToActiveNode() {
                return this.activeLength == 0;
            }

            public boolean activeNodeIs(final Node node) {
                return this.activeNode == node;
            }

            public boolean activeNodeHasEdgeStartingWith(final int value) {
                return this.activeNode.getEdges().containsKey(value);
            }

            public boolean activeNodeHasSlink() {
                return this.activeNode.getSlink() != null;
            }

            public boolean pointsToOnActiveEdge(final int[] values, final int value) {
                return getActiveValue(values) == value;
            }

            public boolean pointsToTheEndOfActiveEdge() {
                return this.getActiveEdge().getLength() == this.activeLength;
            }

            public boolean pointsAfterTheEndOfActiveEdge() {
                return this.getActiveEdge().getLength() < this.activeLength;
            }

            public ActivePoint moveToEdgeStartingWithAndByOne(final int value) {
                return new ActivePoint(this.activeNode, value, 1);
            }

            public ActivePoint moveToNextNodeOfActiveEdge() {
                return new ActivePoint(this.getActiveEdge().getNext(), null, 0);
            }

            public ActivePoint moveToSlink(final int[] values,
                                           final int suffixStartIndex,
                                           final int index) {
                final int slinkIndex = suffixStartIndex + this.activeNode.getSlink().getValuesFromRootCount();
                final int slinkValue = getSuffixValue(suffixStartIndex, values, slinkIndex);
                final int slinkActiveLength = index - slinkIndex;
                return new ActivePoint(this.activeNode.getSlink(),
                        slinkValue,
                        slinkActiveLength);
            }

            public ActivePoint moveTo(final Node node) {
                return new ActivePoint(node, null, 0);
            }

            public ActivePoint moveTo(final Node node, final int activeLength) {
                return new ActivePoint(node, 0, activeLength);
            }

            public ActivePoint moveByOneValue() {
                return new ActivePoint(this.activeNode,
                        this.activeEdgeFirstValue,
                        this.activeLength + 1);
            }

            public ActivePoint moveToNextNodeOfActiveEdge(final int[] values,
                                                          final int suffixStartIndex) {
                final int valueAtTheEndOfEdgeIndex = suffixStartIndex + this.activeNode.getValuesFromRootCount() + this.getActiveEdge()
                        .getLength();
                final int valueAtTheEndOfEdge = getSuffixValue(suffixStartIndex, values, valueAtTheEndOfEdgeIndex);
                return new ActivePoint(this.getActiveEdge().getNext(),
                        valueAtTheEndOfEdge,
                        this.activeLength - this.getActiveEdge().getLength());
            }

            public void addEdgeToActiveNode(final int value, final Edge edge) {
                this.activeNode.getEdges().put(value, edge);
            }

            public Node splitActiveEdge(final int[] values,
                                        final int suffixStartIndex,
                                        final int index,
                                        final int value) {
                final Node newNode = new Node(this.activeNode.getValuesFromRootCount()
                        + this.activeLength);
                final Edge activeEdgeToSplit = this.getActiveEdge();
                final Edge splittedEdge = new Edge(activeEdgeToSplit.getSuffixStartIndex(), activeEdgeToSplit.getFrom(),
                        activeEdgeToSplit.getFrom() + this.activeLength,
                        newNode);
                newNode.getEdges().put(getActiveValue(values),
                        new Edge(activeEdgeToSplit.getSuffixStartIndex(),
                                activeEdgeToSplit.getFrom() + this.activeLength,
                                activeEdgeToSplit.getTo(),
                                activeEdgeToSplit.getNext()));
                newNode.getEdges().put(value, new Edge(suffixStartIndex, index, values.length, null));
                this.activeNode.getEdges().put(this.activeEdgeFirstValue, splittedEdge);
                return newNode;
            }

            public Node setSlinkTo(final Node previouslyAddedNodeOrAddedEdgeNode,
                                   final Node node) {
                if (previouslyAddedNodeOrAddedEdgeNode != null) {
                    previouslyAddedNodeOrAddedEdgeNode.setSlink(node);
                }
                return node;
            }

            public Node setSlinkToActiveNode(final Node previouslyAddedNodeOrAddedEdgeNode) {
                return setSlinkTo(previouslyAddedNodeOrAddedEdgeNode, this.activeNode);
            }
        }
    }
}
