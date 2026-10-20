# Partida Brasil x México

# Titulares:
# Alisson
# Marquinhos
# Gabriel Magalhães
# Bruno Guimarães
# Raphinha
# Rodrygo
# Vini Jr

# Gols:
# Vini Jr.
# Rodrygo
# Vini Jr.

# Mexico marcou 1 gol

jogadores = [
    "Alisson",
    "Marquinhos",
    "Gabriel Magalhães",
    "Bruno Guimarães",
    "Raphinha",
    "Rodrygo",
    "Vini Jr.",
]

print (jogadores)
print (jogadores[0])
print (jogadores[-1])

jogadores.append("Endrick")
print (jogadores)

jogadores[3] = "Neymar"
print (jogadores)

for i, jogador in enumerate(jogadores):
    print (f" - {jogador} | Posição: {i}")