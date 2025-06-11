class MinHeap:  # Definir la clase MinHeap
    # 📦 Estructura de datos MinHeap usando una lista
    def __init__(self):  # Método constructor
        # Inicializar una lista vacía para el heap
        self.heap = []

    def is_empty(self):  # Método para verificar si el heap está vacío
        # Retornar True si el heap está vacío
        return len(self.heap) == 0

# 🧪 Casos de prueba
def test_min_heap_init_and_empty():  # Definir función de prueba
    h = MinHeap()  # Crear una instancia de MinHeap
    print("🌱 Test 1:", h.is_empty() == True)  # Verificar si está vacío (debe ser True)
    h.heap.append(1)  # Agregar un elemento al heap
    print("🌱 Test 2:", h.is_empty() == False)  # Verificar si está vacío (debe ser False)
    h.heap.clear()  # Vaciar el heap
    print("🌱 Test 3:", h.is_empty() == True)  # Verificar si está vacío (debe ser True)
    h.heap.extend([2, 3, 4])  # Agregar varios elementos al heap
    print("🌱 Test 4:", h.is_empty() == False)  # Verificar si está vacío (debe ser False)
    h.heap.pop(); h.heap.pop(); h.heap.pop()  # Quitar todos los elementos del heap
    print("🌱 Test 5:", h.is_empty() == True)  # Verificar si está vacío (debe ser True)

test_min_heap_init_and_empty()  # Ejecutar la función de prueba
