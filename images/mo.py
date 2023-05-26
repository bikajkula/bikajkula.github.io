class Node:
    def __init__(self, parent=None, left=None, right=None, data=None):
        self.parent = parent
        self.left = left
        self.right = right
        self.data = data


class Tree:
    def __init__(self, root=None):
        self.root = root

    def insert(self, node):
        y = None
        x = self.root
        while x is not None:
            y = x
            if node.data[0] < x.data[0]:
                x = x.left
            else:
                x = x.right

        node.parent = y
        if y is None:
            # tree was empty
            self.root = node
        elif node.data < y.data:
            y.left = node
        else:
            y.right = node

        return node

    def inorder_tree_walk(self, node):
        if node is None:
            return
        self.inorder_tree_walk(node.left)
        print(node.data[1])
        self.inorder_tree_walk(node.right)

    '''
    def search_tree(self, lista_enkodovana, node, key):
        if node.data[1] == key:
            return True
        if node == None:
            return
        left = self.search_tree(node.left)
        right = self.search_tree(node.right)
        if left == True:
            '''
    def find_key(self, node, key):
        if node is None:
            return None
        if node.data[1] == key:
            return node
        left = self.find_key(node.left, key)
        right =self.find_key(node.right, key)
        if left is not None:
            return left
        if right is not None:
            return right
        return None

    def search_tree(self, root_node, key):
        node = self.find_key(root_node, key)
        enkodovana_sekvenca = ''
        node_par = None
        while node.parent is not None:
            node_par = node.parent
            if node_par.left == node:
                enkodovana_sekvenca += '.'
            else:
                enkodovana_sekvenca += '-'
            node = node_par
        return enkodovana_sekvenca[::-1]

    def find_character(self, sekvenca):
        node = self.root
        for char in sekvenca:
            if char == '.':
                node = node.left
            else:
                node = node.right
        return node.data[1]

    def dekodovanje(self, ulaz):
        izlaz = ''
        reci = ulaz.split(' / ')
        for rec in reci:
            slova = rec.split(' ')
            for slovo in slova:
                izlaz += self.find_character(slovo)
            izlaz += ' '
        return izlaz

    def enkodovanje(self, ulaz):
        izlaz = ''
        reci = ulaz.split(' ')
        i = len(reci)
        for rec in reci:
            for slovo in rec:
                izlaz += self.search_tree(self.root, slovo)
                izlaz += ' '
            if i > 1:
                izlaz += ' / '
                i -= 1

        return izlaz

    def print_tree(self):
        def display(root):
            """Returns list of strings, width, height, and horizontal coordinate of the root."""
            # No child.
            if root.right is None and root.left is None:
                line = '%s' % root.data[1]
                width = len(line)
                height = 1
                middle = width // 2
                return [line], width, height, middle

            # Only left child.
            if root.right is None:
                lines, n, p, x = display(root.left)
                s = '%s' % root.data[1]
                u = len(s)
                first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
                second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
                shifted_lines = [line + u * ' ' for line in lines]
                return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

            # Only right child.
            if root.left is None:
                lines, n, p, x = display(root.right)
                s = '%s' % root.data[1]
                u = len(s)
                first_line = s + x * '_' + (n - x) * ' '
                second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
                shifted_lines = [u * ' ' + line for line in lines]
                return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

            # Two children.
            left, n, p, x = display(root.left)
            right, m, q, y = display(root.right)
            s = '%s' % root.data[1]
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
            second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
            if p < q:
                left += [n * ' '] * (q - p)
            elif q < p:
                right += [m * ' '] * (p - q)
            zipped_lines = zip(left, right)
            lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
            return lines, n + m + u, max(p, q) + 2, n + u // 2

        lines, *_ = display(self.root)
        for line in lines:
            print(line)


if __name__ == "__main__":
    morzeovo_stablo = ["5", "H", "4", "S", "", "V", "3", "I", "", "F", "", "U", "", "", "2", "E", "", "L", "", "R", "+",
                       "", "", "A", "", "P", "", "W", "", "J", "1", "start", "6", "B", "=", "D", "/", "X", "", "N", "",
                       "C", "", "K", "", "Y", "", "T", "7", "Z", "", "G", "", "Q", "", "M", "8", "", "", "O", "9", "",
                       "0"]
    morze_obj = enumerate(morzeovo_stablo)
    morze_obj = list(morze_obj)
    #print(list(morze_obj))
    insert_order = [31,15,47,7,23,39,55,3,11,19,27,35,43,51,59,1,5,9,13,17,21,25,29,33,37,41,45,49,53,57,61,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62]
    tree = Tree()
    for br in insert_order:
        br2 = morze_obj[br]
        tree.insert(Node(data=br2))

    #tree.print_tree()

    #zadatak pod a
    #tree.inorder_tree_walk(tree.root)

    enkodovani_string = tree.search_tree(tree.root, '')
    #print(enkodovani_string)
    karakter = tree.find_character('-.--')
    #print(karakter)
    dekodovani_string = tree.dekodovanje('.--. . .-. .- / .--. . .-. .. -.-.')
    print(dekodovani_string)
    enkodovani_string = tree.enkodovanje('NA KURCU TE N8')
    print(enkodovani_string)
    
    
    
    
    ----------------------------------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX----------------------------------------------------
    
    
    
import heapq

def GetHistogram(ulazni_karakteri):
    histogram_dict = {}
    for slovo in ulazni_karakteri:
        if slovo in histogram_dict:
            histogram_dict[slovo] += 1
        else:
            histogram_dict[slovo] = 1
    return histogram_dict


class Node:
    def __init__(self, parent=None, left=None, right=None, data=None, freq=None):
        self.parent = parent
        self.left = left
        self.right = right
        self.data = data
        self.freq = freq

    def __lt__(self,other):
        return self.freq < other.freq


class Tree:
    def __init__(self, root = None):
        self.root = root

    def initialize(self, histogram_dict):
        node_list = []
        for key,value in histogram_dict.items():
            node_list.append(Node(data=key,freq=value))

        node_list_sorted = sorted(node_list, key=lambda x: x.freq, reverse=True)
        priority_queue = []
        for node in node_list_sorted:
            heapq.heappush(priority_queue, node)

        while len(priority_queue) > 1:
            left_node = heapq.heappop(priority_queue)
            right_node = heapq.heappop(priority_queue)
            new_freq = left_node.freq + right_node.freq
            new_node = Node(data=None, freq=new_freq)
            new_node.left = left_node
            new_node.right = right_node
            left_node.parent = new_node
            right_node.parent = new_node
            heapq.heappush(priority_queue, new_node)

        return heapq.heappop(priority_queue)

    def get_min(self, node):
        if node.data != None:
            return node
        left = self.get_min(node.left)
        right = self.get_min(node.right)
        if left.freq < right.freq:
            return left
        else:
            return right

    def find_el(self, key, node):
        if node == None:
            return None
        if node.data == key:
            return node
        left = self.find_el(key, node.left)
        right =self.find_el(key, node.right)
        if left != None:
            return left
        if right != None:
            return right
        return None

    def delete_el(self, key):
        node = self.find_el(key,self.root)

        parent = node.parent.parent
        if node.parent.left == node:
            brother = node.parent.right
        else:
            brother = node.parent.left

        if parent.left == node.parent:
            parent.left = brother
        else:
            parent.right = brother

        while parent != None:
            parent.freq -= node.freq
            parent = parent.parent

    def encode(self, node):
        encoded_string = ''
        parent = node
        while parent.parent is not None:
            parent = parent.parent
            if parent.left == node:
                encoded_string += '0'
            else:
                encoded_string += '1'
            node = parent
        return encoded_string[::-1]

    def huffman_coding(self, sequence):
        histogram = {}
        histogram_dict = GetHistogram(sequence)
        self.root = self.initialize(histogram_dict)
        for key, value in histogram_dict.items():
            node = self.find_el(key, self.root)
            kod = self.encode(node)
            print(node.data, kod)
            histogram[node.data] = kod
        output_str = ''
        for slovo in sequence:
            output_str += histogram[slovo]
        return output_str


    def print_tree(self):
        def display(root):
            """Returns list of strings, width, height, and horizontal coordinate of the root."""
            # No child.
            if root.right is None and root.left is None:
                line = '%s (%s)' % (root.data, root.freq)
                width = len(line)
                height = 1
                middle = width // 2
                return [line], width, height, middle

            # Only left child.
            if root.right is None:
                lines, n, p, x = display(root.left)
                s = '%s (%s)' % (root.data, root.freq)
                u = len(s)
                first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
                second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
                shifted_lines = [line + u * ' ' for line in lines]
                return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

            # Only right child.
            if root.left is None:
                lines, n, p, x = display(root.right)
                s = '%s (%s)' % (root.data, root.freq)
                u = len(s)
                first_line = s + x * '_' + (n - x) * ' '
                second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
                shifted_lines = [u * ' ' + line for line in lines]
                return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

            # Two children.
            left, n, p, x = display(root.left)
            right, m, q, y = display(root.right)
            s = '%s (%s)' % (root.data, root.freq)
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
            second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
            if p < q:
                left += [n * ' '] * (q - p)
            elif q < p:
                right += [m * ' '] * (p - q)
            zipped_lines = zip(left, right)
            lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
            return lines, n + m + u, max(p, q) + 2, n + u // 2

        lines, *_ = display(self.root)
        for line in lines:
            print(line)

if __name__ == "__main__":
    niz = "david i danilo"
    print(GetHistogram(niz))
    tree = Tree()
    tree.root = tree.initialize(GetHistogram(niz))
    tree.print_tree()
    node = tree.get_min(tree.root)
    print(node.freq, node.data)
    tree.delete_el('o')
    tree.print_tree()
    encoded_sequence = tree.huffman_coding(niz)
    print(encoded_sequence)

    // SMRK
    
    class Node:
    def __init__(self, parent=None, left=None, right=None, data=None):
        self.parent = parent
        self.left = left
        self.right = right
        self.data = data

    def __str__(self):
        str = f"Node: {self.data}"
        if self.parent:
            str += f', parent: {self.parent.data}'
        if self.left:
            str += f', left: {self.left.data}'
        if self.right:
            str += f', right: {self.right.data}'

        return str


class Tree:
    def __init__(self, root=None):
        self.root = root

    def insert(self, node):
        y = None
        x = self.root
        while x is not None:
            y = x
            if node.data < x.data:
                x = x.left
            else:
                x = x.right

        node.parent = y
        if y is None:
            # tree was empty
            self.root = node
        elif node.data < y.data:
            y.left = node
        else:
            y.right = node

    def inorder_tree_walk(self, node):
        if node is not None:
            self.inorder_tree_walk(node.left)
            print(node.data)
            self.inorder_tree_walk(node.right)

    def search(self, node, value):
        if node is None or value == node.data:
            return node

        if value < node.data:
            return self.search(node.left, value)
        else:
            return self.search(node.right, value)

    def search_iterative(self, value):
        x = self.root
        while x is not None and value != x.data:
            if value < x.data:
                x = x.left
            else:
                x = x.right
        return x

    def minimum(self, min):
        while min.left is not None:
            min = min.left
        return min

    def maximum(self, max):
        while max.right is not None:
            max = max.right
        return max

    def successor(self, x):
        if x.right is not None:
            return self.minimum(x.right)

        y = x.parent
        while y is not None and x == y.right:
            x = y
            y = y.parent

        return y

    def transplant(self, u, v):
        if u.parent is None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v

        if v is not None:
            v.parent = u.parent

    def delete(self, node):
        if node.left is None:
            self.transplant(node, node.right)
        elif node.right is None:
            self.transplant(node, node.left)
        else:
            y = self.minimum(node.right)

            if y.parent != node:
                self.transplant(y, y.right)
                y.right = node.right
                y.right.parent = y

            self.transplant(node, y)
            y.left = node.left
            y.left.parent = y

    def print_tree(self):
        def display(root):
            """Returns list of strings, width, height, and horizontal coordinate of the root."""
            # No child.
            if root.right is None and root.left is None:
                line = '%s' % root.data
                width = len(line)
                height = 1
                middle = width // 2
                return [line], width, height, middle

            # Only left child.
            if root.right is None:
                lines, n, p, x = display(root.left)
                s = '%s' % root.data
                u = len(s)
                first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
                second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
                shifted_lines = [line + u * ' ' for line in lines]
                return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

            # Only right child.
            if root.left is None:
                lines, n, p, x = display(root.right)
                s = '%s' % root.data
                u = len(s)
                first_line = s + x * '_' + (n - x) * ' '
                second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
                shifted_lines = [u * ' ' + line for line in lines]
                return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

            # Two children.
            left, n, p, x = display(root.left)
            right, m, q, y = display(root.right)
            s = '%s' % root.data
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
            second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
            if p < q:
                left += [n * ' '] * (q - p)
            elif q < p:
                right += [m * ' '] * (p - q)
            zipped_lines = zip(left, right)
            lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
            return lines, n + m + u, max(p, q) + 2, n + u // 2

        lines, *_ = display(self.root)
        for line in lines:
            print(line)


if __name__ == "__main__":
    array = [50, 20, 75, 2, 27, 32, 80, 90, 26, 25]
    nodes = []
    T = Tree()
    for x in array:
        node = Node(data=x)
        nodes.append(node)

    for node in nodes:
        T.insert(node)

    T.inorder_tree_walk(T.root)

    find = 75
    print(f'Searching for {find}: {T.search(T.root, find)}')
    print(f'Searching for {find}: {T.search_iterative(find)}')

    print('Minimum value =', T.minimum(T.root).data)
    print('Maximum value =', T.maximum(T.root).data)

    node_32 = T.root.left.right.right
    print(f'Tree successor of node {node_32.data} is {T.successor(node_32).data}')

    T.print_tree()

    #node_26 = T.search(T.root, 26)
    #T.delete(node_26)

    #node_80 = T.search(T.root, 80)
    #T.delete(node_80)

    node_20 = T.search(T.root, 20)
    T.delete(node_20)

    T.print_tree()
