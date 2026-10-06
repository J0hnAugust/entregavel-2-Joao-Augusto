# Classes
import cv2            
import arquivos                   

class imagem:
    # Definir o nome da imagem e a sua classe
    def __init__(self, nome_arquivo):
        self.nome_arquivo = nome_arquivo
        self.imagem = cv2.imread('dados/' + nome_arquivo)
        self.quantidade_qudrados = 0

    # Desenhar retângulo na imagem
    def desenhar_retangulo(self):
        anotacoes = arquivos.ler_anotacoes()
        for linha in anotacoes:
            if linha[0] == self.nome_arquivo and linha[1] == '0':
                cv2.rectangle(self.imagem, (int(linha[2]), int(linha[3])), (int(linha[4]), int(linha[5])), (13, 9, 232), 1)
                self.quantidade_qudrados += 1
            elif linha[0] == self.nome_arquivo and linha[1] == '1':
                cv2.rectangle(self.imagem, (int(linha[2]), int(linha[3])), (int(linha[4]), int(linha[5])), (240, 10, 10), 1)
                self.quantidade_qudrados += 1


    # Salvar a imagem com o retângulo desenhado
    def salvar_imagem(self,):
        cv2.imwrite(self.nome_arquivo[0:-4] + '_com_bounding_boxes.jpg', self.imagem)

    # Mostrar a imagem e escreve suas informações
    def mostrar_imagem(self):
        cv2.imshow('Imagem', self.imagem)
        print(f'Nome do arquivo: {self.nome_arquivo} e foram desenhados {self.quantidade_qudrados} bounding boxes')
    

        # Esperar até que a tecla espaço seja pressionada para fechar a janela e ir para a próxima imagem, ou a tecla "q" para sair do programa
        while True:
            tecla = cv2.waitKey(1) & 0xFF        
            if tecla == ord(' '):
                cv2.destroyAllWindows()
                break
            elif tecla == ord('q'):
                cv2.destroyAllWindows()
                exit()
