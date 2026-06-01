1. Nome provisório do jogo
Pyguntas
2. Integrantes do grupo
•	Gabriel do Carmo Assis
•	Fernando Gomes
•	Davi Martins
3. Tipo de jogo
Um jogo de perguntas no estilo “Quem Quer Ser um Milionário?”.
4. Descrição geral do jogo
Será um jogo de perguntas e respostas no qual o jogador deverá acertar o maior número possível de questões. Em cada fase haverá uma pergunta com quatro opções de resposta, sendo apenas uma correta. Ao acertar, o jogador acumulará pontos, e sua pontuação final será armazenada em um ranking para que possa ser superada em futuras tentativas.
Também haverá bônus por sequência de acertos e, possivelmente, a opção de escolher o tema das perguntas, a quantidade de questões e o nível de dificuldade.
5. Objetivo do jogador
O objetivo do jogador será alcançar sua melhor pontuação possível, acertando o máximo de perguntas.
6. Regras principais
•	Regra 1: A cada resposta correta, o jogador acumula pontos.
•	Regra 2: Ao acertar perguntas em sequência, o jogador recebe pontos bônus.
•	Regra 3: Caso erre uma pergunta, o jogador não perde o jogo e passa para a próxima questão.
•	Regra 4: Poderá haver penalidades ao errar uma questão.
•	Regra 5: Poderão existir poderes de ajuda para auxiliar na resposta das perguntas.
7. Condição de vitória
O jogo termina quando o jogador responder todas as perguntas. Ao final, sua pontuação será exibida, e ele será considerado vencedor ao alcançar uma pontuação alta ou superior às suas tentativas anteriores.
8. Condição de derrota ou encerramento
O jogo termina quando o jogador responder todas as perguntas. Ao final, sua pontuação será exibida, e ele será considerado derrotado ao obter uma pontuação baixa ou inferior às suas tentativas anteriores.
9. Elementos previstos no jogo
Elemento principal
Uma tela contendo a pergunta e quatro opções de resposta.
Elementos secundários
•	Temporizador com limite de tempo para responder às perguntas;
•	Bônus por sequência de acertos;
•	Exibição da pontuação acumulada.
10. Controles previstos
O jogo será praticamente todo controlado pelo mouse. O jogador utilizará cliques para selecionar a resposta que considerar correta, reiniciar a partida e navegar pelas telas do jogo.
11. Organização inicial do código
•	main.py: inicia o jogo;
•	src/jogo.py: contém o loop principal;
•	src/config.py: guarda configurações como dificuldade, quantidade de perguntas e tema das questões;
•	src/funcoes.py: contém funções auxiliares;
•	src/dados.py: contém funções de leitura e escrita de arquivos.
12. Recursos externos previstos
Pretendemos utilizar uma API para obter as perguntas do jogo e imagens para tornar a interface mais atrativa. Dependendo do tempo disponível, também poderemos adicionar sons de acerto e erro.
13. Principais dificuldades esperadas
•	Dificuldade 1: Controle do tempo;
•	Dificuldade 2: Criação do ranking;
•	Dificuldade 3: Organização do código;
•	Dificuldade 4: Uso do GitHub;
•	Dificuldade 5: Utilização do Pygame;
•	Dificuldade 6: Consumo da API;
•	Dificuldade 7: Armazenamento dos dados.
14. Escopo mínimo para a entrega final
O projeto deverá entregar, no mínimo, um jogo com pelo menos 10 perguntas, contabilizando corretamente acertos, erros e pontuação final. Além disso, as pontuações deverão ser armazenadas e exibidas ao jogador.
15. Possíveis melhorias, caso haja tempo
•	Melhoria 1: Ranking aprimorado;
•	Melhoria 2: Sons de acerto e erro;
•	Melhoria 3: Poderes para auxiliar nas respostas;
•	Melhoria 4: Escolha de tema e quantidade de perguntas;
•	Melhoria 5: Limite de tempo para responder às questões.


## Como executar o projeto

### 1. Clonar o repositório

```bash
git clone LINK_DO_REPOSITORIO
cd NOME_DA_PASTA
pip install -r requirements.txt
python main.py
```

## Como executar os testes

```bash
python -m pytest
```

## Checklist mínimo para entrega

- Preencher este README com nome final, descrição real, regras e controles do jogo.
- Atualizar `docs/proposta.MD` com a proposta do grupo.
- Garantir que o jogo executa com `python main.py`.
- Garantir que os testes passam com `pytest`.

## Observações para os alunos

- Mantenham o código organizado em módulos pequenos e com responsabilidade clara.
- Comentem partes importantes da lógica, principalmente regras do jogo.
- Registrem decisões técnicas no README do grupo ao longo do desenvolvimento.
