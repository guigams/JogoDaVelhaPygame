#Autor: Guilherme Morais de Souza
#Finalizado dia: 02/12/2021
#Professor: Julio Favero Miranda

import pygame
import sys
import time

pygame.init()

size = width, height = 600, 600 #tamanho da tela

janela = pygame.display.set_mode(size)

#definção da cor
black = 0, 0, 0 
white = 255, 255, 255 
red = 255, 0, 0
green = 0, 255, 0
blue = 0, 0, 255
cores = [black, white, red, green, blue]

#Quadrantes
quadrante_linha = [50, 250, 450]
quadrante_coluna = [50, 250, 450]
matriz_paralela = [['_', '_', '_'],
                   ['_', '_', '_'],
                    ['_', '_', '_']]

#imagens 
xis = pygame.image.load("xis.png")
bola = pygame.image.load("circulo.png")
veia = pygame.image.load("velha.jpg")

#tamanho da forma
xis = pygame.transform.scale(xis, (100,100))  
bola = pygame.transform.scale(bola, (100,100))
velha = pygame.transform.scale(bola, (600,600))

vez = 'X'
rodada = 0
vencedor1 = ''

#background/janela
janela.fill(cores[1]) 

#linha e posição
def desenha_quadro():
    pygame.draw.line(janela, black, (200,0),(200,600), 10) 
    pygame.draw.line(janela, black, (400,0),(400,600), 10)
    pygame.draw.line(janela, black, (0,200),(600,200), 10)
    pygame.draw.line(janela, black, (0,400),(600,400), 10)

#posição das jogadas
def faz_jogada_bola(pos):
    index_linha = int(pos[0]/200)
    index_coluna = int(pos[1]/200)
    if(matriz_paralela[index_coluna][index_linha] == '_'):
        janela.blit(bola,(quadrante_linha[index_linha], quadrante_coluna[index_coluna]))
        matriz_paralela[index_coluna][index_linha] = 'O'
        return True
    else:
        print("Posição ocupada")
        return False
       
def faz_jogada_xis(pos):
    index_linha = int(pos[0]/200)
    index_coluna = int(pos[1]/200)
    if(matriz_paralela[index_coluna][index_linha] == '_'):
        janela.blit(xis,(quadrante_linha[index_linha], quadrante_coluna[index_coluna]))
        matriz_paralela[index_coluna][index_linha] = 'X'
        return True
    else:
        print("Posição ocupada")
        return False

#Função para definir as jogadas

def ganhou1():
    vencedor = ''
    
    if (matriz_paralela [0][0]== "X") and (matriz_paralela [0][1]== "X") and (matriz_paralela [0][2]== "X"):
        print ("JOGADOR X GANHOU!!!")
        pygame.draw.line(janela, green,(0,100), (600,100), 15)
        vencedor = 'X'
    if (matriz_paralela [1][0] == "X") and (matriz_paralela [1][1]== "X") and (matriz_paralela [1][2] == "X"):
        print ("JOGADOR X GANHOU!!!")
        pygame.draw.line(janela, green,(0,300), (600,300), 15)
        vencedor = 'X'
    if (matriz_paralela [2][0] == "X") and (matriz_paralela [2][1] == "X") and(matriz_paralela [2][2] == "X"):
        print ("JOGADOR X GANHOU!!!")
        pygame.draw.line(janela, green,(0,500), (600,500), 15)
        vencedor = 'X'
  
    if (matriz_paralela [0][0] == "X") and (matriz_paralela [1][0] == "X") and(matriz_paralela [2][0] == "X"):
        print ("JOGADOR X GANHOU!!!")
        pygame.draw.line(janela, green,(100, 0), (100,600), 15)
        vencedor = 'X'
    if (matriz_paralela [0][1] == "X") and (matriz_paralela [1][1] == "X") and(matriz_paralela [2][1] == "X"):
        print ("JOGADOR X GANHOU!!!")
        pygame.draw.line(janela, green,(300,0), (300,600), 15)
        vencedor = 'X'
    if (matriz_paralela [0][2] == "X") and (matriz_paralela [1][2] == "X") and(matriz_paralela [2][2] == "X"):
        print ("JOGADOR X GANHOU!!!")
        pygame.draw.line(janela, green,(500,0), (500,600), 15)
        vencedor = 'X'

    if (matriz_paralela [0][0] == "X") and (matriz_paralela [1][1] == "X") and (matriz_paralela [2][2] == "X"):
        print ("JOGADOR X GANHOU!!!")
        pygame.draw.line(janela, green,(0,0), (600,600), 15)
        vencedor = 'X'
    if (matriz_paralela [0][2] == "X") and (matriz_paralela [1][1] == "X") and (matriz_paralela [2][0] == "X"):
        print ("JOGADOR X GANHOU!!!")
        pygame.draw.line(janela, green,(0,600), (600,0), 15)
        vencedor = 'X'    
    return vencedor

def ganhou2():
    vencedor = ''
    if (matriz_paralela [0][0]== "O") and (matriz_paralela [0][1]== "O") and (matriz_paralela [0][2]== "O"):
        print ("JOGADOR O GANHOU!!!")
        pygame.draw.line(janela, green,(0,100), (600,100), 15)
        vencedor = 'O'
    if (matriz_paralela [1][0] == "O") and (matriz_paralela [1][1]== "O") and (matriz_paralela [1][2] == "O"):
        print ("JOGADOR 1 GANHOU!!!")
        pygame.draw.line(janela, green,(0,300), (600,300), 15)
        vencedor = 'O'
    if (matriz_paralela [2][0] == "O") and (matriz_paralela [2][1] == "O") and(matriz_paralela [2][2] == "O"):
        print ("JOGADOR 1 GANHOU!!!")
        pygame.draw.line(janela, green,(0,500), (600,500), 15)
        vencedor = 'O'
   
    if (matriz_paralela [0][0] == "O") and (matriz_paralela [1][0] == "O") and(matriz_paralela [2][0] == "O"):
        print ("JOGADOR O GANHOU!!!")
        pygame.draw.line(janela, green,(100,0), (100,600), 15)
        vencedor = 'O'
    if (matriz_paralela [0][1] == "O") and (matriz_paralela [1][1] == "O") and(matriz_paralela [2][1] == "O"):
        print ("JOGADOR O GANHOU!!!")
        pygame.draw.line(janela, green,(300,0), (300,600), 15)
        vencedor = 'O'
    if (matriz_paralela [0][2] == "O") and (matriz_paralela [1][2] == "O") and(matriz_paralela [2][2] == "O"):
        print ("JOGADOR O GANHOU!!!")
        pygame.draw.line(janela, green,(500,0), (500,600), 15)
        vencedor = 'O'

    if (matriz_paralela [0][0] == "O") and (matriz_paralela [1][1] == "O") and (matriz_paralela [2][2] == "O"):
        print ("JOGADOR O GANHOU!!!")
        pygame.draw.line(janela, green,(0,0), (600,600), 15)
        vencedor = 'O'
    if (matriz_paralela [0][2] == "O") and (matriz_paralela [1][1] == "O") and (matriz_paralela [2][0] == "O"):
        print ("JOGADOR O GANHOU!!!")
        pygame.draw.line(janela, green,(0,600), (600,0), 15)
        vencedor = 'O'    
    return vencedor
        
while True:
    desenha_quadro()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            click_pos = pygame.mouse.get_pos()

            if (vez=='X'):
                print("Vez de X")
                fez_jogada = faz_jogada_xis(click_pos)
                vencedor1 = ganhou1()
                if (fez_jogada == True):
                    vez='O'
                    rodada = rodada + 1
                elif (fez_jogada == False):
                    vez = 'X'
        
            elif (vez=='O'):
                print("Vez de O")
                fez_jogada = faz_jogada_bola(click_pos)
                vencedor1 = ganhou2()
                if (fez_jogada == True):
                    vez = 'X'
                    rodada = rodada + 1
                elif (fez_jogada == False):
                    vez = 'O'
                    
    pygame.display.flip()
    
    if (rodada>=9) and (vencedor1==''):
        print ('Deu velha!')
        janela.fill(cores[1])
        janela.blit(veia,(0,100))
        pygame.display.flip() 
        print(matriz_paralela)
        break

    elif (vencedor1!=''):
        print ('Fim de jogo!')
        print(matriz_paralela)
        break

                

    
  
