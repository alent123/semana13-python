class MaxHeap:  # Definimos la clase MaxHeap
    def __init__(self):  # Constructor de la clase
        self.heap = []  # Inicializamos el heap como una lista vacía

    def insert(self, value):  # Método para insertar un valor
        self.heap.append(value)  # Agregamos el valor al final de la lista
        self._heapify_up(len(self.heap) - 1)  # Restauramos la propiedad de heap hacia arriba

    def _heapify_up(self, index):  # Método privado para ajustar el heap hacia arriba
        while index > 0:  # Mientras no estemos en la raíz
            parent = (index - 1) // 2  # Calculamos el índice del padre
            if self.heap[index] > self.heap[parent]:  # Si el hijo es mayor que el padre
                self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]  # Intercambiamos
                index = parent  # Subimos al padre
            else:
                break  # Si no, terminamos

    def delete_max(self):  # Método para eliminar el valor máximo
        if not self.heap:  # Si el heap está vacío
            return None  # Retornamos None
        if len(self.heap) == 1:  # Si solo hay un elemento
            return self.heap.pop()  # Lo eliminamos y retornamos
        max_val = self.heap[0]  # Guardamos el valor máximo (raíz)
        self.heap[0] = self.heap.pop()  # Movemos el último elemento a la raíz
        self._heapify_down(0)  # Restauramos la propiedad de heap hacia abajo
        return max_val  # Retornamos el valor máximo

    def _heapify_down(self, index):  # Método privado para ajustar el heap hacia abajo
        length = len(self.heap)  # Longitud del heap
        while True:
            left = 2 * index + 1  # Índice del hijo izquierdo
            right = 2 * index + 2  # Índice del hijo derecho
            largest = index  # Inicialmente el mayor es el actual

            if left < length and self.heap[left] > self.heap[largest]:  # Si el hijo izquierdo es mayor
                largest = left
            if right < length and self.heap[right] > self.heap[largest]:  # Si el hijo derecho es mayor
                largest = right
            if largest == index:  # Si el mayor sigue siendo el actual
                break  # Terminamos
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]  # Intercambiamos
            index = largest  # Bajamos al hijo mayor

# 🧪 Casos de prueba
def test_max_heap():
    h = MaxHeap()
    h.insert(1); print("🦁 Test 1:", h.heap == [1])  # Insertamos 1 y verificamos
    for v in [3, 2, 8, 5]:
        h.insert(v)  # Insertamos más valores
    print("🦁 Test 2:", h.heap[0] == max(h.heap))  # Verificamos que la raíz sea el máximo
    h.delete_max(); print("🦁 Test 3:", h.heap[0] == max(h.heap))  # Eliminamos el máximo y verificamos
    h = MaxHeap()
    for v in [5, 3, 1]:
        h.insert(v)  # Insertamos valores
    h.delete_max(); print("🦁 Test 4:", h.heap == [3, 1])  # Eliminamos el máximo y verificamos el estado
    h = MaxHeap(); h.insert(10)
    print("🦁 Test 5:", h.delete_max() == 10 and h.heap == [])  # Insertamos y eliminamos un solo elemento

test_max_heap()  # Ejecutamos los tests
