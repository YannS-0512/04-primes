"""code prime"""

#### Fonction secondaire


def isprime(p):
    """Module telling if p is prime or not"""
    is_prime = bool(p>1)
    for d in range (2,p-1):
        if p%d==0 :
            is_prime = False
            break
    return is_prime

#### Fonction principale


def main():
    """module main"""
    # vos appels à la fonction secondaire ici

    for n in range(100):
        if isprime(n):
            print(n, end=", ")

    print()


if __name__ == "__main__":
    main()