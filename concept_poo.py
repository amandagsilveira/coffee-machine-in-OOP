# from turtle import Turtle, Screen
# lex = Turtle()
# print(lex)
# lex.shape("turtle")
# lex.color("LightGreen")
# lex.forward(100)
#
# my_screen = Screen()
# print(my_screen.canvheight)
# # permite a execução até clicar na tela para sair
# my_screen.exitonclick()
#


from prettytable import PrettyTable
table = PrettyTable()

table.add_column("Pokémon name", ["Pikachu","Squirtle","Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"

print(table)
