# 🎰 Niquel

Um pequeno projeto de estudo feito em Python simulando uma máquina de caça-níquel pelo terminal.

O objetivo principal deste projeto não é ser um cassino completo ou um sistema profissional. Ele foi criado para praticar conceitos básicos de programação, principalmente:

* `while`
* `for`
* `if / elif / else`
* listas
* variáveis
* `random`
* `time.sleep()`
* entrada de dados com `input()`
* conversão de valores com `int()`
* comparação de strings
* controle de saldo
* probabilidade básica

## 💡 Ideia do projeto

O jogador começa escolhendo quanto dinheiro fictício terá no banco.

Esse valor representa o dinheiro total disponível para aquela "vida".

Por exemplo:

```text
Banco: 500
```

O jogador pode então transferir uma parte desse valor para a casa:

```text
Banco: 400
Casa: 100
```

Dentro da casa, ele escolhe quanto deseja apostar em cada giro.

Por exemplo:

```text
Valor na casa: 100
Aposta: 20
```

Depois escolhe quantos giros quer fazer.

```text
Quantidade de giros: 5
```

A máquina então executa os giros individualmente, mostrando uma pequena animação antes de apresentar o resultado.

## 🍓 Resultados

A máquina possui cinco símbolos:

```text
🍓 Strawberry
🍇 Grape
🥭 Mango
💣 Bomb
🔄 Retry
```

Cada resultado possui uma consequência diferente:

| Resultado |                 Multiplicador |
| --------- | ----------------------------: |
| 🍓🍓🍓    |                            x2 |
| 🍇🍇🍇    |                            x5 |
| 🥭🥭🥭    |                           x10 |
| 💣💣💣    |                perde a aposta |
| 🔄🔄🔄    | tenta novamente gratuitamente |

Qualquer combinação diferente das combinações especiais também representa uma derrota.

## 🎲 Como funcionam as chances

A máquina utiliza `random.choice()` para escolher aleatoriamente cada símbolo.

No modo normal:

```python
niquel = ["🍓", "🍇", "🥭", "💣", "🔄"]
```

Existem cinco símbolos possíveis.

Como cada símbolo aparece uma vez na lista, cada um possui aproximadamente:

```text
20%
```

de chance de ser escolhido em **cada rolo**.

Como existem três rolos independentes, conseguir três símbolos iguais é muito menos provável do que simplesmente conseguir um símbolo.

Por exemplo, a chance matemática de obter:

```text
🍓🍓🍓
```

é:

```text
1/5 × 1/5 × 1/5 = 1/125
```

ou aproximadamente:

```text
0,8%
```

O mesmo princípio vale para os outros resultados especiais no modo normal.

## 🔐 Modo VIP

Existe também um pequeno sistema secreto.

Ao iniciar o programa, se o jogador digitar:

```text
VIP
```

em vez de colocar imediatamente o valor do banco, o programa ativa o modo VIP.

Depois disso, o jogador escolhe normalmente o valor inicial do banco.

No modo VIP, a lista utilizada pelo `random.choice()` possui alguns símbolos repetidos:

```python
vip_niquel = [
    "🍓", "🍓", "🍓",
    "🍇", "🍇",
    "🥭",
    "💣",
    "🔄"
]
```

Isso altera as probabilidades.

A ideia é demonstrar que a própria estrutura de uma lista pode ser utilizada para modificar a probabilidade de um resultado.

## 🎰 Sistema de giros

O jogador pode escolher quantos giros deseja realizar.

Por exemplo:

```text
How many spins do you want? 5
```

O programa executará:

```text
SPIN 1
SPIN 2
SPIN 3
SPIN 4
SPIN 5
```

Cada giro possui uma pequena animação utilizando `time.sleep()` para dar a impressão de que os símbolos estão realmente girando.

## 🏦 Banco e Casa

O projeto separa o dinheiro em dois lugares:

### Banco

Representa o dinheiro que o jogador possui e ainda não colocou na casa.

### Casa

Representa o dinheiro que foi colocado no jogo.

Isso permite que o jogador tenha controle sobre quanto deseja colocar na máquina.

Depois dos giros, o dinheiro da casa pode ser transferido novamente para o banco.

Exemplo:

```text
Banco: 400
Casa: 140
```

Depois da transferência:

```text
Banco: 540
Casa: 0
```

## 💀 Game Over

Se o banco chegar a:

```text
0
```

o jogador quebra e a sessão termina.

Isso cria uma espécie de sistema de "vida", em que o valor inicial escolhido determina quanto dinheiro fictício o jogador possui para aquela partida.

## 📚 Objetivo de aprendizado

Este projeto começou como um exercício pessoal de programação.

A primeira versão foi construída manualmente, utilizando conceitos que estavam sendo estudados naquele momento.

Depois, algumas partes foram desenvolvidas com auxílio do ChatGPT para finalizar sistemas que ainda não estavam implementados.

A intenção não é esconder essa parte.

O projeto representa justamente um processo de aprendizado: construir uma base, encontrar problemas, tentar entender como resolver e utilizar ferramentas para aprender e terminar aquilo que ainda não estava ao alcance.

O código continua propositalmente simples para que seja possível acompanhar a lógica sem transformar o projeto em uma aplicação profissional.

## 🚧 Possíveis melhorias futuras

Algumas ideias que poderiam ser implementadas futuramente:

* calcular as probabilidades automaticamente;
* adicionar mais símbolos;
* criar diferentes níveis de dificuldade;
* adicionar histórico dos giros;
* criar estatísticas da sessão;
* melhorar a animação;
* adicionar sons;
* salvar o progresso em um arquivo;
* criar um sistema de ranking;
* criar uma interface gráfica.

Por enquanto, o objetivo principal é aprender Python através do próprio projeto.

---

**Projeto de estudo — Python 🎰🐍**
