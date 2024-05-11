def count_ways(n, memo={}):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    
    if n not in memo:
        memo[n] = count_ways(n-1, memo) + count_ways(n-2, memo) + count_ways(n-3, memo)
    
    return memo[n]

# Ejemplo de uso
n = 3
ways = count_ways(n)
print(f"El niño puede subir la escalera de {n} peldaños de {ways} formas diferentes.")
