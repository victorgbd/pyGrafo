from grafo import grafo


g = grafo()
g.insert_vertice("a")
g.insert_vertice("b")
g.insert_vertice("c")
g.insert_vertice("d")
g.insert_vertice("e")
g.insert_vertice("f")
g.insert_vertice("g")
g.insert_vertice(3)

g.insert_arista(g.get_vertice("a"), g.get_vertice("a"), 13)
g.insert_arista(g.get_vertice("a"), g.get_vertice("d"), 8)
g.insert_arista(g.get_vertice("d"), g.get_vertice("a"), 8)
g.insert_arista(g.get_vertice("b"), g.get_vertice("b"), 52)
g.insert_arista(g.get_vertice("b"), g.get_vertice("c"), 17)
g.insert_arista(g.get_vertice("b"), g.get_vertice("d"), 23)
g.insert_arista(g.get_vertice("d"), g.get_vertice("b"), 23)
g.insert_arista(g.get_vertice("b"), g.get_vertice("f"), 10)
g.insert_arista(g.get_vertice("f"), g.get_vertice("b"), 10)
g.insert_arista(g.get_vertice("b"), g.get_vertice("g"), 60)
g.insert_arista(g.get_vertice("c"), g.get_vertice("a"), 4)
g.insert_arista(g.get_vertice("d"), g.get_vertice("c"), 37)
g.insert_arista(g.get_vertice("d"), g.get_vertice("d"), 22)
g.insert_arista(g.get_vertice("d"), g.get_vertice("e"), 41)
g.insert_arista(g.get_vertice("d"), g.get_vertice("g"), 34)
g.insert_arista(g.get_vertice("g"), g.get_vertice("d"), 34)
g.insert_arista(g.get_vertice("e"), g.get_vertice("b"), 8)
g.insert_arista(g.get_vertice("e"), g.get_vertice("e"), 45)
g.insert_arista(g.get_vertice("f"), g.get_vertice("a"), 12)
g.insert_arista(g.get_vertice("f"), g.get_vertice("e"), 41)
g.insert_arista(g.get_vertice("e"), g.get_vertice("f"), 41)
g.insert_arista(g.get_vertice(3), g.get_vertice("f"), 15)
g.insert_arista(g.get_vertice("f"), g.get_vertice(3), 15)
# g.recorrido_anchura(g.get_vertice('b'))
# g.graficar()
# g.print_grafo()
# g.eliminar_arista(g.get_vertice("a"), g.get_vertice("d"))
# g.eliminar_arista(g.get_vertice("d"), g.get_vertice("a"))
# g.eliminar_vertice(g.get_vertice("a"))
# g.eliminar_vertice(g.get_vertice("b"))
# g.eliminar_vertice(g.get_vertice("c"))
# g.eliminar_vertice(g.get_vertice("d"))


# g.print_grafo()

# g.recorrido_profundidad(g.get_vertice("b"))
# g.graficar()
# print(g.get_aristas(g.get_vertice('b')))
# g.dijkstra(source='a', target='c')
# g.astar(source='a', target='c')
# i = 100
# while True:
#     print(i)
#     if(i == 0):
#         break
#     i -= 1
