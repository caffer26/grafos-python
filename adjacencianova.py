def criar_grafo():
    return {}


def inserir_vertice(grafo, vertice):
    if vertice not in grafo:
        grafo[vertice] = []
        print(f"Vértice '{vertice}' inserido.")
    else:
        print(f"Vértice '{vertice}' já existe.")


def inserir_aresta(grafo, origem, destino, nao_direcionado=False):
    if origem not in grafo:
        grafo[origem] = []
    if destino not in grafo:
        grafo[destino] = []

    if destino not in grafo[origem]:
        grafo[origem].append(destino)

    if nao_direcionado:
        if origem not in grafo[destino]:
            grafo[destino].append(origem)

    print(f"Aresta {origem} -> {destino} inserida.")


def listar_vizinhos(grafo, vertice):
    if vertice in grafo:
        print(f"Vizinhos de {vertice}: {grafo[vertice]}")
    else:
        print(f"O vértice '{vertice}' não existe.")


def exibir_grafo(grafo):
    print("\nGrafo:")
    for v in grafo:
        print(f"{v} -> {grafo[v]}")
    print()


def remover_aresta(grafo, origem, destino, nao_direcionado=False):
    if origem in grafo and destino in grafo[origem]:
        grafo[origem].remove(destino)
        print(f"Aresta {origem} -> {destino} removida.")
    else:
        print("Aresta não encontrada.")

    if nao_direcionado and destino in grafo and origem in grafo[destino]:
        grafo[destino].remove(origem)


def remover_vertice(grafo, vertice):
    if vertice not in grafo:
        print(f"Vértice '{vertice}' não existe.")
        return

    for v in list(grafo.keys()):
        if vertice in grafo[v]:
            grafo[v].remove(vertice)

    del grafo[vertice]
    print(f"Vértice '{vertice}' removido.")


def existe_aresta(grafo, origem, destino):
    return origem in grafo and destino in grafo[origem]


def grau_vertices(grafo):
    print("\nGrau dos vértices:")
    for v in grafo:
        grau = len(grafo[v])
        for u in grafo:
            if v in grafo[u]:
                grau += 1
        print(f"{v}: {grau}")
    print()


def percurso_valido(grafo, caminho):
    if len(caminho) < 2:
        return True
    for i in range(len(caminho) - 1):
        if not existe_aresta(grafo, caminho[i], caminho[i + 1]):
            return False
    return True


def bfs(grafo, inicio):
    if inicio not in grafo:
        print(f"O vértice '{inicio}' não existe.")
        return

    visitados = []
    fila = [inicio]

    while len(fila) > 0:
        atual = fila.pop(0)

        if atual not in visitados:
            visitados.append(atual)

            for vizinho in grafo[atual]:
                if vizinho not in visitados:
                    fila.append(vizinho)

    print("Ordem da BFS:", visitados)


def menor_caminho_bfs(grafo, inicio, fim):
    if inicio not in grafo or fim not in grafo:
        print("Algum dos vértices não existe.")
        return

    fila = [inicio]
    visitados = [inicio]
    pai = {inicio: None}

    while len(fila) > 0:
        atual = fila.pop(0)

        if atual == fim:
            break

        for vizinho in grafo[atual]:
            if vizinho not in visitados:
                visitados.append(vizinho)
                fila.append(vizinho)
                pai[vizinho] = atual

    if fim not in pai:
        print(f"Não existe caminho de {inicio} até {fim}.")
        return

    caminho = []
    atual = fim
    while atual is not None:
        caminho.insert(0, atual)
        atual = pai[atual]

    print("Menor caminho:", caminho)


def main():
    grafo = criar_grafo()

    while True:
        print("=== MENU GRAFO ===")
        print("1 - Mostrar Grafo")
        print("2 - Inserir Vértice")
        print("3 - Inserir Aresta")
        print("4 - Remover Vértice")
        print("5 - Remover Aresta")
        print("6 - Listar Vizinhos")
        print("7 - Calcular Grau dos Vértices")
        print("8 - Verificar Aresta")
        print("9 - Verificar Percurso")
        print("10 - Busca em Largura (BFS)")
        print("11 - Menor Caminho (BFS)")
        print("0 - Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            exibir_grafo(grafo)

        elif opcao == "2":
            v = input("Vértice: ")
            inserir_vertice(grafo, v)

        elif opcao == "3":
            o = input("Origem: ")
            d = input("Destino: ")
            nd = input("É não direcionado? (s/n): ").lower() == "s"
            inserir_aresta(grafo, o, d, nd)

        elif opcao == "4":
            v = input("Vértice: ")
            remover_vertice(grafo, v)

        elif opcao == "5":
            o = input("Origem: ")
            d = input("Destino: ")
            nd = input("É não direcionado? (s/n): ").lower() == "s"
            remover_aresta(grafo, o, d, nd)

        elif opcao == "6":
            v = input("Vértice: ")
            listar_vizinhos(grafo, v)

        elif opcao == "7":
            grau_vertices(grafo)

        elif opcao == "8":
            o = input("Origem: ")
            d = input("Destino: ")
            print("Existe aresta?", existe_aresta(grafo, o, d))

        elif opcao == "9":
            caminho = input("Digite o percurso (separado por espaços): ").split()
            print("Percurso válido?", percurso_valido(grafo, caminho))

        elif opcao == "10":
            v = input("Vértice inicial da BFS: ")
            bfs(grafo, v)

        elif opcao == "11":
            inicio = input("Vértice inicial: ")
            fim = input("Vértice final: ")
            menor_caminho_bfs(grafo, inicio, fim)

        elif opcao == "0":
            print("Saindo...")
            break

        else:
            print("Opção inválida!")


if __name__ == "__main__":
    main()