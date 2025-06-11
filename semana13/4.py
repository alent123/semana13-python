class MinHeap:
    def __init__(self):
        self.heap = []  # Crea una lista vacía para almacenar el heap

    def build_heap(self, array):
        self.heap = array[:]  # Copia el arreglo dado al heap
        # Comienza desde el último nodo padre y aplica heapify hacia abajo
        for i in range((len(self.heap) // 2) - 1, -1, -1):
            self._heapify_down(i)  # Reorganiza para mantener la propiedad de heap

    def _heapify_down(self, index):
        length = len(self.heap)  # Obtiene el tamaño del heap
        while True:
            left = 2 * index + 1  # Calcula el índice del hijo izquierdo
            right = 2 * index + 2  # Calcula el índice del hijo derecho
            smallest = index  # Supone que el nodo actual es el más pequeño

            # Si el hijo izquierdo existe y es menor que el actual, actualiza 'smallest'
            if left < length and self.heap[left] < self.heap[smallest]:
                smallest = left
            # Si el hijo derecho existe y es menor que el actual, actualiza 'smallest'
            if right < length and self.heap[right] < self.heap[smallest]:
                smallest = right
            # Si el nodo actual ya es el más pequeño, termina el ciclo
            if smallest == index:
                break
            # Intercambia el nodo actual con el más pequeño encontrado
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            index = smallest  # Continúa heapificando hacia abajo

# 🧪 Casos de prueba
def test_build_heap():
    h = MinHeap()
    h.build_heap([5, 3, 8, 1, 2]); print("🔨 Test 1:", h.heap[0] == 1)  # El mínimo debe ser 1
    h.build_heap([7, 6, 5, 4, 3, 2, 1]); print("🔨 Test 2:", h.heap[0] == 1)  # El mínimo debe ser 1
    h.build_heap([2, 1]); print("🔨 Test 3:", h.heap == [1, 2])  # El heap debe ser [1, 2]
    h.build_heap([10]); print("🔨 Test 4:", h.heap == [10])  # El heap debe ser [10]
    h.build_heap([]); print("🔨 Test 5:", h.heap == [])  # El heap debe ser []

test_build_heap()  # Ejecuta los casos de prueba