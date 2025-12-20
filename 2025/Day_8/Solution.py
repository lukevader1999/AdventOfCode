from __future__ import annotations
from math import sqrt

#Read sampleInput.txt file
#input_path = '2025/Day_8/sampleInput.txt'
input_path = '2025/Day_8/input.txt'
with open(input_path, 'r') as file:
    input = file.read().splitlines()

class Node:
    def __init__(self, x,y,z, circuit):
        self.x = x
        self.y = y
        self.z = z
        self.circuit: Circuit = circuit

    def calc_straight_line_distance(self, other: Node) -> float:
        return sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2 + (self.z - other.z) ** 2)

class Connection:
    def __init__(self, node_a: Node, node_b: Node):
        self.node_a = node_a
        self.node_b = node_b
        self.distance = node_a.calc_straight_line_distance(node_b)
        self.activated = False
    
    def print_connection(self):
        print(f'Connection from Node {self.node_a.x, self.node_a.y, self.node_a.z} to Node {self.node_b.x, self.node_b.y, self.node_b.z} with distance {self.distance:.2f}')

class Circuit:
    def __init__(self, id):
        self.id = id
        self.nodes: set[Node] = set()

    def merge_circuit(self, other: Circuit):
        for node in other.nodes:
            node.circuit = self
            self.nodes.add(node)
    
    def size(self) -> int:
        return self.nodes.__len__()

class Node_Set:
    def __init__(self):
        self.nodes: set[Node] = set()
        self.connections: list[Connection] = list()
        self.circuits: dict[int, Circuit] = dict()

        self.init_nodes_connections_and_circuits()

        #self.activate_connections()
        #self.print_product_of_largest_circuits()
        self.activate_connections_until_1_circuit_left()

    def activate_connections_until_1_circuit_left(self):
        while self.circuits.__len__() > 1:
            connection = self.activate_shortest_not_active_connection()
            print(f'Number of circuits left: {self.circuits.__len__()}')
        product = connection.node_a.x * connection.node_b.x
        print(f'product of last connection nodes x values: {product}')
    
    def activate_connections(self):
        number_of_connections_to_activate = 1000
        for _ in range(number_of_connections_to_activate):
            #self.activate_shortest_connection_between_different_circuits()
            if _ % 50 == 0:
                print(f'Activating connection {_+1} of {number_of_connections_to_activate}')
            self.activate_shortest_not_active_connection()

    def print_product_of_largest_circuits(self):
        number_of_circles_to_count = 3
        product = self.count_product_of_largest_circuits(number_of_circles_to_count)
        print(f'Product of sizes of the {number_of_circles_to_count} largest circuits: {product}')
    
    def count_product_of_largest_circuits(self, number_of_circles_to_count: int) -> int:
        sorted_circuits = sorted(self.circuits.values(), key=lambda circuit: circuit.size(), reverse=True)
        product = 1
        for i in range(number_of_circles_to_count):
            size = sorted_circuits[i].size()
            print(f' Circuit {i+1} size: {size}')
            product *= sorted_circuits[i].size()
        return product

    #Not needed, I the problem doesnt want to ignore the count of connections on the same circle, but leaving it here for reference. 
    def activate_shortest_connection_between_different_circuits(self):
        for connection in self.connections:
            if connection.node_a.circuit != connection.node_b.circuit:
                #print('Activating connection:')
                connection.print_connection()
                circuit_a = connection.node_a.circuit
                circuit_b = connection.node_b.circuit
                circuit_a.merge_circuit(circuit_b)
                del self.circuits[circuit_b.id]
                break
    
    def activate_shortest_not_active_connection(self):
        for connection in self.connections:
            if connection.activated == False:
                print('Activating connection:')
                connection.print_connection()
                connection.activated = True
                if not connection.node_a.circuit == connection.node_b.circuit:
                    circuit_a = connection.node_a.circuit
                    circuit_b = connection.node_b.circuit
                    circuit_a.merge_circuit(circuit_b)
                    del self.circuits[circuit_b.id]
                return connection
                break

    def init_nodes_connections_and_circuits(self):
        connections = set[Connection]()
        for line in input:
            x, y, z = line.split(',')
            circuit_number = self.nodes.__len__()
            circuit = Circuit(id= circuit_number)
            node = Node(int(x), int(y), int(z), circuit)
            circuit.nodes.add(node)

            for existing_node in self.nodes:
                connection = Connection(existing_node, node)
                connections.add(connection)

            self.nodes.add(node)
            self.circuits[circuit_number] = circuit
        #Order connections by distance
        self.connections = sorted(connections, key=lambda conn: conn.distance)
        
node_set = Node_Set()