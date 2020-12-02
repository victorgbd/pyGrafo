import os
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
    g = None

    def __init__(self):
        self.head
        self.g = nx.DiGraph()

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

    def insert_vertice(self, dato):
        nuevo = vertice()
        nuevo.dato = dato
        nuevo.sig = None
        nuevo.ady = None
        aux = self.head
        if(self.vacio()):
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
            print(naux.dato+"->", end='')
            self.g.add_node(naux.dato)
            araux = naux.ady
            while (araux is not None):
                print(araux.ady.dato+"->", end='')
                self.g.add_edge(naux.dato, araux.ady.dato)

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

    def graficar(self):
        naux = self.head
        araux = None
        while (naux is not None):
            self.g.add_node(naux.dato)
            araux = naux.ady
            while (araux is not None):
                self.g.add_edge(naux.dato, araux.ady.dato, weight=araux.peso)
                # print(araux.peso)
                araux = araux.sig
            naux = naux.sig
        #para sacar los labels de los nodos
        labels = {}    
        for node in self.g.nodes():
            labels[node] = node
        pos = nx.layout.spring_layout(self.g)
        nx.draw_networkx_labels(self.g,pos,labels,font_size=16,font_color='white')
        #para sacar los pesos de las aristas
        labels = nx.get_edge_attributes(self.g,'weight')
        # para graficar los labels
        nx.draw_networkx_edge_labels(self.g,pos,edge_labels=labels)
        nodes = nx.draw_networkx_nodes(
            self.g,pos, node_color="blue")
        # para graficar las aristas dirigidas
        edges = nx.draw_networkx_edges(
            self.g,pos,
            arrowstyle="->",
            arrowsize=10,
            width=2,
        )
        plt.show()
