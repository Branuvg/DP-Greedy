def knapsack_01(vms, W):
    n = len(vms)
    # dp[i][c] = valor maximo con las primeras i VMs y capacidad c
    dp = [[0] * (W + 1) for _ in range(n + 1)]

    # Llenado de la tabla (bottom-up)
    for i in range(1, n + 1):
        nombre, w_i, v_i = vms[i - 1]
        for c in range(W + 1):
            if w_i > c:
                # VM no cabe: heredar subproblema anterior
                dp[i][c] = dp[i - 1][c]
            else:
                # Elegir el mejor entre incluir o no incluir la VM i
                dp[i][c] = max(dp[i - 1][c],
                               v_i + dp[i - 1][c - w_i])

    # Reconstruccion de la solucion optima
    seleccionadas = []
    c = W
    for i in range(n, 0, -1):
        if dp[i][c] != dp[i - 1][c]:
            seleccionadas.append(vms[i - 1])
            c -= vms[i - 1][1]

    return dp[n][W], seleccionadas


# Caso de prueba del contraejemplo (seccion 2.1)
if __name__ == "__main__":
    print("CRISIS 2 — Asignacion de Memoria (Mochila 0/1)")

    # Formato de cada VM: (nombre, memoria_GB, valor_computacional)
    vms = [
        ("VM-A", 6, 7),
        ("VM-B", 5, 5),
        ("VM-C", 5, 5),
    ]
    W = 10

    valor, elegidas = knapsack_01(vms, W)
    print(f"\nCapacidad del servidor : {W} GB")
    print(f"Valor maximo           : {valor}")
    print(f"VMs seleccionadas      : {[v[0] for v in elegidas]}")
    print(f"Memoria utilizada      : {sum(v[1] for v in elegidas)}/{W} GB")

    # Caso extendido
    print("")
    print("- Caso extendido")

    vms2 = [
        ("VM-1", 2, 6),
        ("VM-2", 2, 10),
        ("VM-3", 3, 12),
        ("VM-4", 7, 13),
        ("VM-5", 1, 4),
    ]
    W2 = 5

    valor2, elegidas2 = knapsack_01(vms2, W2)
    print(f"\nCapacidad del servidor : {W2} GB")
    print(f"Valor maximo           : {valor2}")
    print(f"VMs seleccionadas      : {[v[0] for v in elegidas2]}")
    print(f"Memoria utilizada      : {sum(v[1] for v in elegidas2)}/{W2} GB")