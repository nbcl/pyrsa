import math

def pcar(p, q):
    """Returns Carmichael prime-variation 
    of n for p,q primes

    Given n = pq 
    λ(n) = lcm(λ(p),λ(q))
    λ(p) = φ(p) = p − 1
    λ(q) = φ(q) = q − 1
    Hence λ(n) = lcm(p − 1, q − 1)
    """
    p -= 1
    q -= 1
    return lcm(p,q)

def lcm(a: int, b: int) -> int:
    """Least common multiple function"""
    return abs(a*b) // math.gcd(a, b)
    
