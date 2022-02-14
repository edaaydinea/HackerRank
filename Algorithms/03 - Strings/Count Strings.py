#!/bin/python3

import math
import os
import random
import re
import sys
from enum import Enum
from collections import namedtuple

#
# Complete the 'countStrings' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING r
#  2. INTEGER l
#

Edge = namedtuple("Edge", "dest char")


class Alphabet(Enum):
    a = "a"
    b = "b"
    e = None


def empty_edge(dest):
    return Edge(dest, Alphabet.e)


class CountStrings:
    def __init__(self, regex_string):
        RegexGraphNFA.node_count = 0
        self.regex_string = regex_string
        nfa_graph = self.translate_regex()
        translate_graph = TranslateGraph(nfa_graph)
        self.dfa_graph = translate_graph.translate()

    def calculate(self, string_length):
        return self.dfa_graph.count_paths(string_length)

    def translate_regex(self, index=0):
        result_set = ResultSet()
        while index < len(self.regex_string):
            if self.regex_string[index] == '(':
                out_list, index = self.translate_regex(index + 1)
                result_set.insert(out_list)
            elif self.regex_string[index] == ')':
                result = result_set.calculate_result()
                return result, index
            elif self.regex_string[index] == '|':
                result_set.set_or()
            else:
                result_set.insert(self.regex_string[index])
            index += 1
        return result_set.calculate_result()


class ResultSet:
    def __init__(self):
        self.r1 = None
        self.r2 = None
        self.has_or = False

    def set_or(self):
        self.has_or = True

    def calculate_result(self):
        repeat = True if self.r2 == '*' else False
        if self.r2 is None:
            pass
        elif repeat:
            self.calculate_repeat()
        elif self.has_or:
            self.calculate_or()
        else:
            self.calculate_and()
        return self.r1

    def calculate_repeat(self):
        self.r1.graph_repeat()

    def calculate_or(self):
        self.r1.graph_or(self.r2)

    def calculate_and(self):
        self.r1.graph_add(self.r2)

    def insert(self, value):
        if value != '*' and isinstance(value, str):
            value = RegexGraphNFA.get_char_graph(Alphabet[value])
        if self.r1 is None:
            self.r1 = value
        else:
            self.r2 = value


class RegexGraphNFA:
    node_count = 0

    def __init__(self):
        self.edges = None
        self.head = None
        self.tail = None

    @staticmethod
    def get_char_graph(value):
        my_graph = RegexGraphNFA()
        my_graph.insert_char(value)
        return my_graph

    @classmethod
    def get_next_node_id(cls):
        node_id = cls.node_count
        cls.node_count += 1
        return node_id

    def insert_char(self, value):
        self.head = self.get_next_node_id()
        self.tail = self.get_next_node_id()
        self.edges = {self.head: [Edge(self.tail, value)],
                      self.tail: []}

    def graph_add(self, other):
        join_node = self.get_next_node_id()
        self.join(other)
        self.edges[self.tail].append(empty_edge(join_node))
        self.edges[join_node] = [empty_edge(other.head)]
        self.tail = other.tail

    def graph_repeat(self):
        new_head = self.get_next_node_id()
        new_tail = self.get_next_node_id()
        self.edges[self.tail].extend([empty_edge(self.head), empty_edge(new_tail)])
        self.edges[new_head] = [empty_edge(self.head), empty_edge(new_tail)]
        self.edges[new_tail] = []
        self.head = new_head
        self.tail = new_tail

    def graph_or(self, other):
        new_head = self.get_next_node_id()
        new_tail = self.get_next_node_id()
        self.join(other)
        self.edges[new_head] = [empty_edge(self.head), empty_edge(other.head)]
        self.edges[self.tail].append(empty_edge(new_tail))
        self.edges[other.tail].append(empty_edge(new_tail))
        self.edges[new_tail] = []
        self.head = new_head
        self.tail = new_tail

    def join(self, other):
        for node, edge in other.edges.items():
            if node in self.edges:
                self.edges[node].extend(edge)
            else:
                self.edges[node] = edge

    def get_dfa_char_node_set(self, origin, use_char):
        node_set = set()
        for my_node in origin:
            for edges in self.edges[my_node]:
                if edges.char == use_char:
                    node_set.add(edges.dest)

        return self.get_dfa_zero_node_set(node_set)

    def get_dfa_zero_node_set(self, origin):
        node_set = set(origin)
        processed = set()
        while len(node_set.difference(processed)) > 0:
            my_node = node_set.difference(processed).pop()
            for edges in self.edges[my_node]:
                if edges.char == Alphabet.e:
                    node_set.add(edges.dest)
            processed.add(my_node)
        return frozenset(node_set)


class TranslateGraph:
    language = (Alphabet.a, Alphabet.b)

    def __init__(self, nfa_graph: RegexGraphNFA):
        self.node_count = 0
        self.nfa_graph = nfa_graph
        self.trans_to = {}
        self.trans_from = {}
        self.table = {}

    def get_next_node_id(self):
        node_id = self.node_count
        self.node_count += 1
        return node_id

    def add_translate(self, nfa_ids):
        if len(nfa_ids) == 0:
            return None
        if nfa_ids not in self.trans_from:
            dfa_id = self.get_next_node_id()
            self.trans_to[dfa_id] = nfa_ids
            self.trans_from[nfa_ids] = dfa_id
            self.table[dfa_id] = dict(zip(self.language, [None] * len(self.language)))
        return self.trans_from[nfa_ids]

    def translate(self):
        self.create_translate_table()
        return self.build_dfa()

    def build_dfa(self):
        head = 0
        valid_ends = set()
        adjacency = {}
        for node, edges in self.table.items():
            adjacency[node] = []
            if self.nfa_graph.tail in self.trans_to[node]:
                valid_ends.add(node)
            for my_char, node_dest in edges.items():
                if node_dest is not None:
                    adjacency[node].append(Edge(node_dest, my_char))
        return RegexGraphDFA(head, valid_ends, adjacency)

    def create_translate_table(self):
        nfa_ids = self.nfa_graph.get_dfa_zero_node_set({self.nfa_graph.head})
        self.add_translate(nfa_ids)
        processed = set()

        while len(set(self.table).difference(processed)) > 0:
            my_node = set(self.table).difference(processed).pop()
            for char in self.language:
                next_nodes = self.nfa_graph.get_dfa_char_node_set(self.trans_to[my_node], char)
                dfa_id = self.add_translate(next_nodes)
                self.table[my_node][char] = dfa_id
            processed.add(my_node)


class RegexGraphDFA:
    def __init__(self, head, valid_ends, edges):
        self.edges = edges
        self.head = head
        self.valid_ends = valid_ends
        self.edge_matrix = Matrix.get_from_edges(len(self.edges), self.edges)

    def count_paths(self, length):
        modulo = 1000000007
        edge_walk = self.edge_matrix.pow(length, modulo)
        count = 0
        for end_node in self.valid_ends:
            count += edge_walk.matrix[self.head][end_node]
        return count % modulo


class Matrix:
    @staticmethod
    def get_from_edges(dimension, adj_list):
        my_matrix = Matrix.get_zeros(dimension)
        my_matrix.add_edges(adj_list)
        return my_matrix

    @staticmethod
    def get_zeros(dimension):
        my_matrix = Matrix(dimension)
        my_matrix.pad_zeros()
        return my_matrix

    def copy(self):
        my_matrix = Matrix(self.dimension)
        my_matrix.matrix = []
        for i in range(self.dimension):
            my_matrix.matrix.append([])
            for j in range(self.dimension):
                my_matrix.matrix[i].append(self.matrix[i][j])
        return my_matrix

    def __init__(self, dimension):
        self.matrix = None
        self.dimension = dimension

    def __str__(self):
        my_str = ''
        for row in self.matrix:
            my_str += str(row) + "\n"
        return my_str

    def pad_zeros(self):
        self.matrix = []
        for i in range(self.dimension):
            self.matrix.append([])
            for j in range(self.dimension):
                self.matrix[i].append(0)

    def add_edges(self, adj_list):
        if adj_list is not None:
            for from_node, edge_list in adj_list.items():
                for to_node, my_char in edge_list:
                    self.matrix[from_node][to_node] = 1

    def pow(self, pow_val, mod_val=None):
        started = False
        target = pow_val
        current_pow = 1
        current_val = 0
        while pow_val > 0:
            if current_pow == 1:
                current_pow_matrix = self.copy()
            else:
                current_pow_matrix = current_pow_matrix.mat_square_mult(current_pow_matrix, mod_val)
            if pow_val % (2 * current_pow):
                current_val += current_pow
                if started:
                    result = result.mat_square_mult(current_pow_matrix, mod_val)
                else:
                    result = current_pow_matrix.copy()
                    started = True
                # print(current_pow, current_val, target)
                pow_val -= current_pow
            current_pow *= 2
        return result

    def mat_square_mult(self, other, mod_val=None):
        result = Matrix.get_zeros(self.dimension)
        for i in range(self.dimension):
            for j in range(self.dimension):
                val = 0
                for k in range(self.dimension):
                    val += self.matrix[i][k] * other.matrix[k][j]
                if mod_val is not None:
                    val %= mod_val
                result.matrix[i][j] = val

        return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        r = first_multiple_input[0]

        l = int(first_multiple_input[1])

        my_class = CountStrings(r)

        result = my_class.calculate(l)

        fptr.write(str(result) + '\n')

    fptr.close()
