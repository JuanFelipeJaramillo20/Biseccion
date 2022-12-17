import math

solMatrix = []

def functionTest(x):
    return x**3 + 4*(x**2) - 10


# Comprobamos que haya solucion con el teorema del valor intermedio
def validate_interval(f, x0, x1):
    return f(x0) * f(x1) < 0

# Comprobamos cuantas iteraciones son necesarias para llegar a la raiz (aproximadamente)
def error_bound(a, b, error):
    return math.ceil((math.log10((b-a) / error)) / math.log10(2))

def bisection(f, interval, tol):
    """
    param f: find root for function
    param interval: within range
    param tol: root accuracy tolerance
    """
    # Extraemos los límites del intervalo
    x0, x1 = interval[0], interval[1]

    # Revisamos si hay solución en el intervalo
    if not validate_interval(f, x0, x1):
        return

    # Calculamos las iteraciones necesarias aproximadas para encontrar la raiz
    n = error_bound(x0, x1, tol)

    counter = 1
    # Iniciamos las iteraciones
    while True:

        # Calculamos la aproximación a la raiz en el intervalo
        root_approx = x0 + ((x1 - x0) / 2)

        # Evaluamos la función en la aproximación
        y = f(root_approx)

        # Agregamos los datos de la iteración actual a la tabla de iteraciones
        solMatrix.append([str(counter),  str(x0),  str(x1), str(root_approx), str(y), str(-tol < y < tol) ])

        # Revisamos si el valor es apropiado de acuerdo al error
        if -tol < y < tol:
            # Escribimos los datos de la lista de iteraciones en un archivo para poder revisarlo mas comodamente
            with open("tabla_iteraciones.txt", 'w')as f:
                f.write("n, X_1, X_2, X_n, f(X_n), ¿Error tolerable?")
                f.write("\n")
                for line in solMatrix:
                    f.write(line[0] + ", " + line[1] + ", " + line[2] + ", " + line[3] + ", " + line[4] + ", " + line[5])
                    f.write("\n")

            # Retornamos la aproximación calculada
            return [n, counter, root_approx]

        # Revisamos si debemos modificar el valor a o b del intervalo
        if validate_interval(f, x0, root_approx):
            x1 = root_approx
        else:
            x0 = root_approx

        # increment counter
        counter += 1
        

