class MinHeap:
    def __init__(self):
        self.heap = []  # Crea una lista vacía para almacenar el heap

    def insert(self, value):
        self.heap.append(value)  # Agrega el valor al final del heap
        self._heapify_up(len(self.heap) - 1)  # Reordena el heap hacia arriba

    def _heapify_up(self, index):
        while index > 0:  # Mientras no sea la raíz
            parent = (index - 1) // 2  # Calcula el índice del padre
            if self.heap[index] < self.heap[parent]:  # Si el hijo es menor que el padre
                self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]  # Intercambia hijo y padre
                index = parent  # Actualiza el índice al del padre
            else:
                break  # Si no, termina el ciclo

# 🧪 Casos de prueba
def test_min_heap_insert():
    h = MinHeap()  # Crea una instancia de MinHeap
    h.insert(5); print("🍀 Test 1:", h.heap == [5])  # Inserta 5 y verifica el heap
    h.insert(3); print("🍀 Test 2:", h.heap == [3, 5])  # Inserta 3 y verifica el heap
    h.insert(4); print("🍀 Test 3:", h.heap == [3, 5, 4])  # Inserta 4 y verifica el heap
    h.insert(1); print("🍀 Test 4:", h.heap == [1, 3, 4, 5])  # Inserta 1 y verifica el heap
    valid = all(
        (h.heap[i] <= h.heap[2*i+1] if 2*i+1 < len(h.heap) else True) and  # Verifica propiedad de heap para hijo izquierdo
        (h.heap[i] <= h.heap[2*i+2] if 2*i+2 < len(h.heap) else True)  # Verifica propiedad de heap para hijo derecho
        for i in range(len(h.heap))
    )
    print("🍀 Test 5:", valid)  # Imprime si el heap es válido

test_min_heap_insert()  # Ejecuta los casos de prueba
