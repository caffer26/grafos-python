def criar_grafo():
    return [], []


def inserir_vertice(vertices, vertice):
    if vertice not in vertices:
        vertices.append(vertice)


def inserir_aresta(vertices, arestas, origem, destino, nao_direcionado=False):
    if origem not in vertices:
        vertices.append(origem)
    if destino not in vertices:
        vertices.append(destino)
    if [origem, destino] not in arestas:
        arestas.append([origem, destino])
    if nao_direcionado and [destino, origem] not in arestas:
        arestas.append([destino, origem])


def remover_aresta(arestas, origem, destino, nao_direcionado=False):
    if [origem, destino] in arestas:
        arestas.remove([origem, destino])
    if nao_direcionado and [destino, origem] in arestas:
        arestas.remove([destino, origem])


def remover_vertice(vertices, arestas, vertice):
    if vertice in vertices:
        vertices.remove(vertice)
        arestas[:] = [a for a in arestas if vertice not in a]


def existe_aresta(arestas, origem, destino):
    return [origem, destino] in arestas


def vizinhos(vertices, arestas, vertice):
    lista = []
    for a in arestas:
        if a[0] == vertice:
            lista.append(a[1])
    return lista


def grau_vertices(vertices, arestas):
    graus = {}
    for v in vertices:
        entrada = sum(1 for a in arestas if a[1] == v)
        saida = sum(1 for a in arestas if a[0] == v)
        graus[v] = {"entrada": entrada, "saida": saida, "total": entrada + saida}
    return graus


def percurso_valido(arestas, caminho):
    for i in range(len(caminho) - 1):
        if [caminho[i], caminho[i + 1]] not in arestas:
            return False
    return True


def listar_vizinhos(vertices, arestas, vertice):
    lista = vizinhos(vertices, arestas, vertice)
    print(f"Vizinhos de {vertice}: {lista}")


def exibir_grafo(vertices, arestas):
    print("Vértices:", vertices)
    print("Arestas:")
    for a in arestas:
        print(f"{a[0]} -> {a[1]}")


def main():
    vertices, arestas = criar_grafo()
    while True:
        print("\n1 - Mostrar Grafo")
        print("2 - Inserir Vértice")
        print("3 - Inserir Aresta")
        print("4 - Remover Vértice")
        print("5 - Remover Aresta")
        print("6 - Ver Grau dos Vértices")
        print("7 - Verificar Aresta")
        print("8 - Listar Vizinhos")
        print("9 - Verificar Percurso")
        print("0 - Sair")
        op = input("Escolha: ")

        if op == "1":
            exibir_grafo(vertices, arestas)
        elif op == "2":
            v = input("Nome do vértice: ")
            inserir_vertice(vertices, v)
        elif op == "3":
            o = input("Origem: ")
            d = input("Destino: ")
            nd = input("Não direcionado? (s/n): ") == "s"
            inserir_aresta(vertices, arestas, o, d, nd)
        elif op == "4":
            v = input("Vértice a remover: ")
            remover_vertice(vertices, arestas, v)
        elif op == "5":
            o = input("Origem: ")
            d = input("Destino: ")
            nd = input("Não direcionado? (s/n): ") == "s"
            remover_aresta(arestas, o, d, nd)
        elif op == "6":
            g = grau_vertices(vertices, arestas)
            for v, info in g.items():
                print(f"{v} -> entrada: {info['entrada']}, saída: {info['saida']}, total: {info['total']}")
        elif op == "7":
            o = input("Origem: ")
            d = input("Destino: ")
            print("Existe aresta?", existe_aresta(arestas, o, d))
        elif op == "8":
            v = input("Vértice: ")
            listar_vizinhos(vertices, arestas, v)
        elif op == "9":
            c = input("Digite o caminho separado por espaço: ").split()
            print("Percurso válido?", percurso_valido(arestas, c))
        elif op == "0":
            break
        else:
            print("Opção inválida!")


if __name__ == "__main__":
    main()
