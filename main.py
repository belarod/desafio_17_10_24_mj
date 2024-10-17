from utils import Utils

class Pedido:
    proximo_id = 1
    
    def __init__(self, nome_cliente: str, prioritario: bool, limite_espera: int, id: None):
        self.nome_cliente = nome_cliente
        self.prioritario = prioritario
        self.limite_espera = limite_espera
        self.id = Pedido.proximo_id
        Pedido._proximo_id += 1
        
    def __str__(self):
        prioridade_str = 'Sim' if self.prioritario else 'Não' #se self.priorit for true, prioridade_string recebe 'Sim' e será imprimido assi :D, senão, 'Nao'
        return (f"Pedido ID: {self.id}\n"
                f"Cliente: {self.nome_cliente}\n"
                f"Prioritário: {prioridade_str}\n"
                f"Limite de Espera: {self.limite_espera}\n")
        
        
        
class Node:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None



class Queue:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Queue, cls).__new__(cls)
        return cls._instance
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        
    def __str__(self):
        fila = []
        atual = self.head
        while atual:
            fila.append(str(atual.valor))
            atual = atual.proximo
        return '->'.join(fila)
    
    def is_empty(self):
        return self.head is None
    
    def primeiro_da_fila(self):
        if self.is_empty():
            print('A fila está vazia.')
            return
        return self.head.valor
    
    def comprimento_fila(self):
        return self.length
    
    ##############################
    
    def enqueue(self, valor):
        novo_no = Node(valor)
        
        if self.is_empty():
            self.head = self.tail = novo_no
        else:
            self.tail.next = novo_no
            self.tail = novo_no
        self.length += 1
        
    def dequeue(self):
        if self.is_empty():
            return None
        valor = self.head.valor
        
        self.head = self.head.next

        if self.head is None:
            self.tail = None
        self.length -+ 1
        return valor



class Gerenciador:
    def __init__(self, pedido: Pedido):
        self.pedido = pedido
    
    @staticmethod    
    def adicionar_pedido():
        queue = Queue()
        
        nome_cliente = Utils.input_string_sem_numeros('Nome do cliente:\n')
        prioritario = Utils.opcao_s_n('É prioritario? s/n\n')
        limite_espera = Utils.input_inteiro('Qual o limite de espera?\n')
        
        cria_pedido = Pedido(nome_cliente= nome_cliente, prioritario= prioritario, limite_espera= limite_espera, id= None)
        Queue.enqueue(queue, cria_pedido)
    
    @staticmethod
    def processar_pedido():
        print('Proc pedido')
        # Queue.dequeue()
    
    @staticmethod    
    def imprimir_pedidos(self):
        fila = Queue()
        print(fila)
        
    def qtd_pedidos_na_fila() -> int:
        Queue.comprimento_fila()
        
    def qtd_limite_pedidos_hoje() -> int:
        pass
    
    def qtd_limite_fila() -> int:
        pass
    
    def qtd_pedidos_abandonados() -> int:
        pass

    def qtd_pedidos_finalizados() -> int:
        pass