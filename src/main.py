import modelos
from pathlib import Path
# Programa principal
#acha todas as fotos
pasta = Path('dados/')
for arquivo in pasta.glob('*.jpg'):
    imagem = modelos.imagem(arquivo.name)
    imagem.desenhar_retangulo()
    imagem.salvar_imagem()
    imagem.mostrar_imagem()