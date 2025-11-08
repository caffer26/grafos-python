def criar_grafo():
    matriz = []
    vertices = []
    return matriz, vertices


def inserir_vertice(matriz, vertices, vertice):
    if vertice in vertices:
        print(f"Vértice '{vertice}' já existe.")
        return

    vertices.append(vertice)
    for linha in matriz:
        linha.append(0)
    nova_linha = [0] * len(vertices)
    matriz.append(nova_linha)
    print(f"Vértice '{vertice}' inserido.")


def inserir_aresta(matriz, vertices, origem, destino, nao_direcionado=False):
    if origem not in vertices:
        inserir_vertice(matriz, vertices, origem)
    if destino not in vertices:
        inserir_vertice(matriz, vertices, destino)

    i = vertices.index(origem)
    j = vertices.index(destino)
    matriz[i][j] = 1

    if nao_direcionado:
        matriz[j][i] = 1

    print(f"Aresta {origem} -> {destino} inserida.")


def remover_vertice(matriz, vertices, vertice):
    if vertice not in vertices:
        print(f"Vértice '{vertice}' não existe.")
        return

    i = vertices.index(vertice)
    matriz.pop(i)
    for linha in matriz:
        linha.pop(i)
    vertices.pop(i)
    print(f"Vértice '{vertice}' removido.")


def remover_aresta(matriz, vertices, origem, destino, nao_direcionado=False):
    if origem not in vertices or destino not in vertices:
        print("Um dos vértices não existe.")
        return

    i = vertices.index(origem)
    j = vertices.index(destino)
    matriz[i][j] = 0

    if nao_direcionado:
        matriz[j][i] = 0

    print(f"Aresta {origem} -> {destino} removida.")


def existe_aresta(matriz, vertices, origem, destino):
    if origem not in vertices or destino not in vertices:
        return False
    i = vertices.index(origem)
    j = vertices.index(destino)
    return matriz[i][j] == 1


def vizinhos(matriz, vertices, vertice):
    if vertice not in vertices:
        return []
    i = vertices.index(vertice)
    lista = []
    for j in range(len(vertices)):
        if matriz[i][j] == 1:
            lista.append(vertices[j])
    return lista


def listar_vizinhos(matriz, vertices, vertice):
    if vertice not in vertices:
        print(f"O vértice '{vertice}' não existe.")
        return
    lista = vizinhos(matriz, vertices, vertice)
    print(f"Vizinhos de {vertice}: {lista}")


def grau_vertices(matriz, vertices):
    print("\nGraus dos vértices:")
    for i in range(len(vertices)):
        grau = sum(matriz[i])
        for linha in matriz:
            grau += linha[i]
        print(f"{vertices[i]}: {grau}")
    print()


def percurso_valido(matriz, vertices, caminho):
    if len(caminho) < 2:
        return True
    for i in range(len(caminho) - 1):
        if not existe_aresta(matriz, vertices, caminho[i], caminho[i + 1]):
            return False
    return True


def exibir_grafo(matriz, vertices):
    print("\nMatriz de Adjacência:")
    print("   ", " ".join(vertices))
    for i in range(len(vertices)):
        linha = " ".join(str(x) for x in matriz[i])
        print(f"{vertices[i]}: {linha}")
    print()


def main():
    matriz, vertices = criar_grafo()

    while True:
        print("=== MENU GRAFO (Matriz de Adjacência) ===")
        print("1 - Mostrar Grafo")
        print("2 - Inserir Vértice")
        print("3 - Inserir Aresta")
        print("4 - Remover Vértice")
        print("5 - Remover Aresta")
        print("6 - Listar Vizinhos")
        print("7 - Calcular Grau dos Vértices")
        print("8 - Verificar Aresta")
        print("9 - Verificar Percurso")
        print("0 - Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            exibir_grafo(matriz, vertices)
        elif opcao == "2":
            v = input("Vértice: ")
            inserir_vertice(matriz, vertices, v)
        elif opcao == "3":
            o = input("Origem: ")
            d = input("Destino: ")
            nd = input("É não direcionado? (s/n): ").lower() == "s"
            inserir_aresta(matriz, vertices, o, d, nd)
        elif opcao == "4":
            v = input("Vértice: ")
            remover_vertice(matriz, vertices, v)
        elif opcao == "5":
            o = input("Origem: ")
            d = input("Destino: ")
            nd = input("É não direcionado? (s/n): ").lower() == "s"
            remover_aresta(matriz, vertices, o, d, nd)
        elif opcao == "6":
            v = input("Vértice: ")
            listar_vizinhos(matriz, vertices, v)
        elif opcao == "7":
            grau_vertices(matriz, vertices)
        elif opcao == "8":
            o = input("Origem: ")
            d = input("Destino: ")
            print("Existe aresta?", existe_aresta(matriz, vertices, o, d))
        elif opcao == "9":
            caminho = input("Digite o percurso (separado por espaços): ").split()
            print("Percurso válido?", percurso_valido(matriz, vertices, caminho))
        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida!")


if __name__ == "__main__":
    main()
