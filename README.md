# Labirinto Dinâmico

Este projeto é uma simulação de um labirinto dinâmico usando o Pygame, onde três Pac-Mans (cada um usando um algoritmo de busca diferente: BFS, A* e DFS) tentam navegar pelo labirinto enquanto novos obstáculos são adicionados dinamicamente.


## Instalação

Para rodar este projeto, você precisa ter o Python 3.x instalado. Você também deve instalar as bibliotecas necessárias. Você pode fazer isso usando o `pip`:

```bash
pip install pygame
```

### Execute 
Execute o script Python com o comando abaixo:
```bash
python3 main.py
```

## Funcionalidade

- **Labirinto**: O labirinto é um grid 50x50 onde células podem ser obstáculos fixos e novos.
- **Três Agentes**: Estão configurados 3 agentes com algoritmos de busca diferentes (A*, BFS e DFS) para encontrar o caminho da entrada à saída.
- **Obstáculos**: São adicionados dinamicamente ao labirinto em um intervalo definido.
- **Tela**: É exibido na tela o caminho de cada agente, sendo atualizado a cada recalculo.

## Funcionalidade
- O labirinto é visualizado em uma janela Pygame com um tamanho de 1000x1000 pixels.
- O intervalo de criação de novos obstáculos pode ser ajustado na variável OBSTACLE_CREATION_INTERVAL.
  
## Autores

- **Thomás T. Pereira**
- **Ygor S. Viera** - [Perfil GitHub](https://github.com/eplaie)

