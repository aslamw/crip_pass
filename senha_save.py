import random, string, pyaes

class Senha(object):
    def __init__(self,comando):
        self.senha = ''
        if comando == 'gerar senha':
            self.gerar_senha()
        elif comando == 'ver senha':
            self.ver_senha()
        else: 
            print('Comando invalido!')
    
    def gerar_senha(self):
        tamanho = int(input('Digite o tamanho da sua senha: '))   

        chars = string.ascii_letters + string.digits + 'ç_!%$#@'
        rnd = random.SystemRandom()

        print('Senha gerada!')
        
        self.senha = ''.join(rnd.choice(chars) for i in range(tamanho))
        
        print(self.senha)  
        self.salvar_senha()
        
    def salvar_senha(self):
        
        file_name = input('Digite o nome do arquivo para salvar a senha Ex:. teste.txt>> ')
        ## chave de criptografia
        password = input('Digite sua senha de 16 caracteres: ')
        
        key = bytes(password,'utf-8')
        aes = pyaes.AESModeOfOperationCTR(key)

        ## criptografar o arquivo
        crypto_data = aes.encrypt(self.senha)

        ## salvar o arquivo criptografado
        new_file = open(f'{file_name}','ab')
        new_file.write(crypto_data)      
        new_file.close()

    def ver_senha(self):
        ## abrir o arquivo criptografado
        file_name = input("nome do arquivo Ex:. teste.txt_>> ")
        file = open(file_name, "rb")
        file_data = file.read()
        file.close()

        ## chave para descriptografia
        key = input('Digite sua senha: ')
        
        aes = pyaes.AESModeOfOperationCTR(key)
        decrypt_data = aes.decrypt(file_data)
        
        return print(decrypt_data.decode('ISO-8859-1'))


if __name__ == '__main__':
    while True:
        comando = input('Digite -- ver senha -- ou -- gerar senha --: ')
        Senha(comando)