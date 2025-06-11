class MinHeap:  # Define una clase llamada MinHeap (Montículo mínimo)
    def __init__(self):  # Método constructor, se llama al crear una instancia
        self.heap = []  # Inicializa el montículo como una lista vacía

    def delete_min(self):  # Elimina y retorna el valor mínimo del montículo
        if self.is_empty():  # Si el montículo está vacío
            return None  # Retorna None (no hay nada que eliminar)
        if len(self.heap) == 1:  # Si solo hay un elemento en el montículo
            return self.heap.pop()  # Elimina y retorna ese único elemento
        min_val = self.heap[0]  # Guarda el valor mínimo (raíz del montículo)
        self.heap[0] = self.heap.pop()  # Mueve el último elemento a la raíz y elimina el último
        self._heapify_down(0)  # Restaura la propiedad de montículo desde la raíz hacia abajo
        return min_val  # Retorna el valor mínimo eliminado

    def _heapify_down(self, index):  # Restaura la propiedad de montículo hacia abajo desde un índice dado
        length = len(self.heap)  # Obtiene el tamaño del montículo
        while True:  # Bucle infinito hasta que se rompa manualmente
            left = 2 * index + 1  # Calcula el índice del hijo izquierdo
            right = 2 * index + 2  # Calcula el índice del hijo derecho
            smallest = index  # Supone que el más pequeño es el nodo actual

            if left < length and self.heap[left] < self.heap[smallest]:  # Si el hijo izquierdo existe y es menor
                smallest = left  # Actualiza el más pequeño al hijo izquierdo
            if right < length and self.heap[right] < self.heap[smallest]:  # Si el hijo derecho existe y es menor
                smallest = right  # Actualiza el más pequeño al hijo derecho
            if smallest == index:  # Si el nodo actual ya es el más pequeño
                break  # Sale del bucle
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]  # Intercambia el nodo actual con el más pequeño
            index = smallest  # Actualiza el índice para continuar bajando

    def is_empty(self):  # Verifica si el montículo está vacío
        return len(self.heap) == 0  # Retorna True si la lista está vacía, False en caso contrario

# 🧪 Casos de prueba
def test_min_heap_delete_min():
    h = MinHeap()  # Crea una instancia de MinHeap
    print("🧹 Test 1:", h.delete_min() is None)  # Prueba eliminar de un montículo vacío
    h.heap = [1]; print("🧹 Test 2:", h.delete_min() == 1 and h.heap == [])  # Prueba eliminar cuando hay un solo elemento
    h.heap = [1, 3, 2]; print("🧹 Test 3:", h.delete_min() == 1 and h.heap == [2, 3])  # Prueba eliminar con tres elementos
    h.heap = [1, 3, 4, 5]; print("🧹 Test 4:", h.delete_min() == 1 and h.heap == [3, 5, 4])  # Prueba eliminar con cuatro elementos
    h.heap = [1, 2, 3, 4, 5]
    print("🧹 Test 5:", h.delete_min() == 1)  # Prueba eliminar con cinco elementos

test_min_heap_delete_min()  # Ejecuta los casos de prueba