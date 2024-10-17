import os

class Utils:
    
    @staticmethod
    def input_inteiro(msg):
        opcao_valida = False
        resultado = None
        
        while not opcao_valida:
            try:
                valor = input(msg)
                resultado = int(valor)
                opcao_valida = True
            except:
                print('Deve ser um número inteiro, tente novamente.')
        return resultado
    
    @staticmethod
    def input_string_sem_numeros(msg):
        opcao_valida = False
        resultado = None
        
        while not opcao_valida:
            valor = input(msg)
            
            if valor and not any(char.isdigit() for char in valor):
                resultado = valor
                opcao_valida = True
            else:
                print('A entrada não pode conter números, tente novamente.')
        return resultado
    
    @staticmethod
    def clear_screen():
        os.system('cls' if os.name == 'nt' else 'clear')
    
    @staticmethod
    def sleep(seconds):
        if seconds < 0:
            raise ValueError("O tempo deve ser um valor não negativo.")
        if os.name == 'posix':
            os.system(f"sleep {seconds}")
        elif os.name == 'nt':
            os.system(f"timeout {seconds}")
        else:
            pass
        
    @staticmethod
    def opcao_p_n(msg):
        from main import Gerenciador
        
        opcao_valida = False
        
        while not opcao_valida:
            valor = input(msg).lower()
        
            if valor == 'n':
                Gerenciador.adicionar_pedido()
                opcao_valida = True
            elif valor == 'p':
                Gerenciador.processar_pedido()
                opcao_valida = True
            else:
                print('Apenas -N- ou -P- são aceitos, tente novamente')
                
    @staticmethod
    def opcao_s_n(msg):
        opcao_valida = False
        
        while not opcao_valida:
            valor = input(msg).lower()
        
            if valor == 's':
                resultado = True
                opcao_valida = True
            elif valor == 'n':
                resultado = False
                opcao_valida = True
            else:
                print('Apenas -S- ou -N- são aceitos, tente novamente')
        return resultado