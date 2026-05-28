def calc(a, b, op):
    if op == "sum":
        return a + b
    if op == "sub":
        return a - b
    if op == "mul":
        return a * b
    if op == "div":
        if b != 0:
            return a / b
        return 0
    return 0


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) != 4:
        print("Uso: python function.py <a> <b> <operazione>")
        print("Operazioni disponibili: sum, sub, mul, div")
        sys.exit(1)
    
    try:
        a = float(sys.argv[1])
        b = float(sys.argv[2])
        op = sys.argv[3]
        
        result = calc(a, b, op)
        print(f"Risultato: {result}")
    except ValueError:
        print("Errore: i parametri a e b devono essere numeri")
        sys.exit(1)
