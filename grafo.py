import networkx as nx
import matplotlib.pyplot as plt


class vertice():
    sig = None  # tipo nodo o vertice
    ady = None  # tipo arista
    dato = None

    def __init__(self):
        self.sig
        self.ady
        self.dato

    def __repr__(self):
        return "vertice[pos[{}],dato[{}]]".format(hex(id(self)), self.dato)


class arista():
    sig = None  # tipo arista
    ady = None  # tipo nodo o vertice
    peso = None

    def __init__(self):
        self.sig
        self.ady
        self.peso

    def __repr__(self):
        return "arista[pos[{}],peso[{}]]".format(hex(id(self)), self.peso)


class grafo():
    head = None  # tipo nodo o vertice

    def __init__(self):
        self.head

    @property
    def vacio(self):
        return (self.head is None)

    def size(self):
        cont = 0
        aux = self.head
        while (aux is not None):
            aux = aux.sig
            cont += 1
        return cont

    def get_vertice(self, dato):
        aux = self.head
        while (aux is not None):
            if(aux.dato == dato):
                return aux
            aux = aux.sig
        return None

    def get_aristas(self, origen):
        lista = []
        arista_aux = origen.ady
        while (arista_aux is not None):
            lista.append(arista_aux)
            arista_aux = arista_aux.sig
        return lista

    def insert_vertice(self, dato):
        nuevo = vertice()
        nuevo.dato = dato
        nuevo.sig = None
        nuevo.ady = None
        aux = self.head
        if(self.vacio):
            self.head = nuevo
        else:
            while (aux.sig is not None):
                aux = aux.sig
            aux.sig = nuevo

    def insert_arista(self, origen, destino, peso):
        nuevo = arista()
        nuevo.peso = peso
        nuevo.sig = None
        nuevo.ady = None
        aux = origen.ady
        if(aux is None):
            origen.ady = nuevo
            nuevo.ady = destino
        else:
            while (aux.sig is not None):
                aux = aux.sig
            aux.sig = nuevo
            nuevo.ady = destino

    def print_grafo(self):
        naux = self.head
        araux = None
        while (naux is not None):
            print("{} -> ".format(naux.dato), end='')
            araux = naux.ady
            while (araux is not None):
                print(araux.ady.dato+" {} ->".format(araux.peso), end='')

                araux = araux.sig
            naux = naux.sig
            print('')

    def eliminar_vertice(self, vertice):
        actual = self.head
        anterior = None
        aux = None

        while (actual is not None):
            aux = actual.ady
            while(aux is not None):
                if(aux.ady == vertice):
                    self.eliminar_arista(actual, aux.ady)
                    break
                aux = aux.sig
            actual = actual.sig
        actual = self.head
        if(self.head == vertice):
            self.head = self.head.sig
        else:
            while(actual is not vertice):
                anterior = actual
                actual = actual.sig
            anterior.sig = actual.sig

    def eliminar_arista(self, origen, destino):
        flag = True
        anterior = None
        actual = origen.ady
        if(actual is None):
            print("el vertice actual no tiene aristas")
        elif(actual.ady == destino):
            origen.ady = actual.sig
        else:
            while (actual is not None):
                if(actual.ady == destino):
                    flag = False
                    anterior.sig = actual.sig
                    break
                anterior = actual
                actual = actual.sig
            if(flag):
                print("los vertices no estan enlazados")

    # implementacion dfs iterativo

    def recorrido_profundidad(self, origen):
        flag1, flag2 = True, True
        actual = None  # nodo o arista
        pila = []
        listav = []  # lista visitados
        pila.append(origen)
        while pila:
            actual = pila[-1]
            pila.pop()
            for i in listav:
                if(i == actual):
                    flag1 = False
            if(flag1):
                listav.append(actual)
                arista_aux = actual.ady
                while(arista_aux != None):
                    flag2 = True
                    for i in listav:
                        if(arista_aux.ady == i):
                            flag2 = False
                    if(flag2):
                        pila.append(arista_aux.ady)
                    arista_aux = arista_aux.sig
        for i, e in enumerate(listav):
            if(i == len(listav)-1):
                print(e.dato, end='')
                break
            print('{} -> '.format(e.dato), end='')
        print('')

    # implementacion bfs iterativo

    def recorrido_anchura(self, origen):
        flag1, flag2 = True, True
        actual = None
        cola = []
        listav = []  # lista visitados
        cola.append(origen)
        while cola:
            actual = cola[0]
            cola.pop(0)
            for i in listav:
                if(i == actual):
                    flag1 = False
            if(flag1):
                listav.append(actual)
                arista_aux = actual.ady
                while(arista_aux != None):
                    flag2 = True
                    for i in listav:
                        if(arista_aux.ady == i):
                            flag2 = False
                    if(flag2):
                        cola.append(arista_aux.ady)
                    arista_aux = arista_aux.sig
        for i, e in enumerate(listav):
            if(i == len(listav)-1):
                print(e.dato, end='')
                break
            print('{} -> '.format(e.dato), end='')
        print('')

    def dijkstra(self, source, target):
        g = nx.DiGraph()
        naux = self.head
        araux = None
        while (naux is not None):
            g.add_node(naux.dato)
            araux = naux.ady
            while (araux is not None):
                g.add_edge(naux.dato, araux.ady.dato, weight=araux.peso)
                araux = araux.sig
            naux = naux.sig
        print("largo:{} ruta:{}".format(nx.dijkstra_path_length(g, source=source, target=target,
              weight=True), nx.dijkstra_path(g, source=source, target=target, weight=True)))

    def astar(self, source, target):
        g = nx.DiGraph()
        naux = self.head
        araux = None
        while (naux is not None):
            g.add_node(naux.dato)
            araux = naux.ady
            while (araux is not None):
                g.add_edge(naux.dato, araux.ady.dato, weight=araux.peso)
                araux = araux.sig
            naux = naux.sig
        print("largo:{} ruta:{}".format(nx.astar_path_length(g, source=source, target=target,
              weight=True), nx.astar_path(g, source=source, target=target, weight=True)))

    def graficar(self):
        g = nx.DiGraph()
        naux = self.head
        araux = None
        while (naux is not None):
            g.add_node(naux.dato)
            araux = naux.ady
            while (araux is not None):
                g.add_edge(naux.dato, araux.ady.dato, weight=araux.peso)
                araux = araux.sig
            naux = naux.sig
        # para sacar los labels de los nodos
        labels = {}
        for node in g.nodes():
            labels[node] = node

        pos = nx.layout.circular_layout(g)
        # print(pos)
        nx.draw_networkx_labels(g, pos, labels,
                                font_size=16, font_color='white')
        # para sacar los pesos de las aristas
        label = nx.get_edge_attributes(g, 'weight')
        # para graficar los labels
        nx.draw_networkx_edge_labels(g, pos, edge_labels=label)
        nx.draw_networkx_nodes(
            g, pos, node_color="blue")
        # para graficar las aristas dirigidas
        nx.draw_networkx_edges(
            g, pos,
            arrowstyle="->",
            arrowsize=10,
            width=2,
        )
        plt.show()
