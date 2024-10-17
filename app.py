import time
from utils import Utils
from main import Gerenciador, Queue

class App:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(App, cls).__new__(cls)
        return cls._instance
    
    def inicia_app(self):
        queue = Queue()
        
        limite_pedidos = Utils.input_inteiro('Digite o limite de pedidos que serão aceitos hoje.\n')
        self.limite_pedidos = limite_pedidos
        
        fila_max_length = Utils.input_inteiro('Digite o tamanho máximo da fila.\n')
        self.fila_max_length = fila_max_length
        
        print(f"Limite de pedidos definido para: {limite_pedidos}")
        print(f'Tamanho máximo da fila definido em: {fila_max_length}')
        
        Utils.sleep(5)
        Utils.clear_screen()
        self.mostra_tela_inicial(queue)
        
    def mostra_tela_inicial(self, queue: Queue):
        if Queue.comprimento_fila(queue) == 0:
            print('Ainda não há pedidos na fila.')
            Utils.opcao_p_n('Digite -N- para novo pedido, ou -P- para processar pedido.\n')
        else: 
            print(f'A fila possui {Gerenciador.qtd_pedidos_na_fila} pedidos.')


    
app = App()
app.inicia_app()