import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)  # Define o tamanho da tela
screen.title("Turtle Crossing")  # Define o título da tela
screen.tracer(0)  # Desliga a animação

player = Player()  # Cria o jogador
car_manager = CarManager()  # Cria o gerenciador de carros
scoreboard = Scoreboard()  # Cria o placar

screen.listen()  # Escuta os comandos do teclado
screen.onkey(player.move, "Up")  # Quando a tecla "Up" é pressionada, o jogador move

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()  # Atualiza a tela

    # Detectar a colisão com a parede superior
    if player.ycor() > 280:
        player.goto(0, -280)  # Move o jogador para a posição inicial
        car_manager.move_distance += 5  # Aumenta a velocidade dos carros
        scoreboard.increase_level()  # Aumenta o nível

screen.exitonclick()  # Fecha a tela ao clicar
