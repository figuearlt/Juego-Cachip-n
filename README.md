# Juego-Cachipun
Chilean's name of knowing game where facing 2 players, with 3 options to chose: scissor, paper or stone.

The cachipun.py documment consists on three functions:
  1) The first, called "maquina", stablish what are the moves that python machine does. There are just three options: 
    i) scissor
    ii) paper
    iii) stone
   
  2) The second function, called "match", stablish the interactions between the python machine and the player, by asking the last "what are your move?" with the same options in the step above. 
  At the same time, the function set what are the dominance among the three standard moves: 
    i) scissor > paper
    ii) paper > stone
    iii) stone > scissor
  3) The third function, called "cachipun", gives a counter to each player to acummulating the points of each wins obtained, increasing per 1 unit for it. 
  At the end, the function sum the points of each player and define which player win the match.
