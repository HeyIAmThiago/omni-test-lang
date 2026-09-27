# Roteiro da apresentação — OmniTest (P1)

Abra este arquivo na hora de falar e marque cada item. Os comandos, com a saída esperada, estão no `README.md`, na seção **Comandos da apresentação**. Rode tudo na raiz do repositório, no terminal integrado (Ctrl+`).

Ordem sugerida: motivação, os dois exemplos, a gramática, as variáveis, o teste no terminal, a análise léxica, e o que ficou de fora.

## O que dizer se perguntarem de ferramenta

JFLAP, o autômato com pilha de LFA e o Bison não foram usados. O enunciado (parágrafo antes da seção 2.1) também aceita construir elementos recursivos ligados à gramática. O critério 3 aceita o projeto em Python. Foi esse o caminho: `omnitest/lexer.py` e `omnitest/parser.py`.

---

- [ ] **Abertura — por que esta linguagem**

  O documento pede uma gramática de linguagem de programação com assinatura de quem projeta. A assinatura aqui é de QA: no dia a dia um teste de API é um cenário com nome, uma requisição e uma checagem do que voltou.

  Fale isso antes de abrir código:

  - Uma DSL é uma linguagem pequena, feita para um domínio. Não é uma linguagem geral.
  - Em teste de API, o domínio é: descrever o pedido e o resultado esperado, de um jeito que outra pessoa lê.
  - Postman, Karate e Gherkin são referências desse ofício. A OmniTest não integra nenhuma delas. Ela só tem a forma: cenário, `GET`, `assert`.
  - Os exemplos usam a API pública JSONPlaceholder. O programa descreve o teste. Ele não chama a URL.

  Onde clicar: no explorador, abra `examples/get_one.omt` e depois `examples/get_all.omt`. Mostre que a estrutura é a mesma e que muda a URL (`/posts/1` é um recurso, `/posts` é a coleção).

- [ ] **Item 1 do P1 — definir a gramática**

  O documento pede definir uma gramática de linguagem de programação, partindo de algo pequeno e colocando a assinatura do projetista.

  Para implementar isso, a OmniTest ficou com o que os dois exemplos usam: `test`, `let` com tipo, `GET` com uma URL e `assert` com `==`. Blocos por indentação, sem chaves. Ficou de fora `POST`, JSON, execução HTTP e checagem de tipos. A Parte 1 é análise, não execução.

  Onde clicar:

  1. `README.md`, seção **Gramática**. A BNF começa em ⟨program⟩.
  2. `omnitest/parser.py`, método `parse_program`. O comentário logo acima dele repete a mesma produção.
  3. Volte ao `get_one.omt` e aponte, na ordem: `test "..." :`, o bloco indentado, o `let`, o `GET`, o `assert`.

- [ ] **Item 2 do P1 — documentar as variáveis da gramática**

  O documento pergunta o que o grupo pensou sobre as variáveis que fazem as produções. Variável aqui é não-terminal, não variável do programa.

  Onde clicar: `README.md`, seção **Variáveis da gramática**. Escolha três linhas para ler em voz alta, não a tabela inteira:

  - ⟨test_decl⟩ — um cenário com nome.
  - ⟨block⟩ — o corpo, aberto por `INDENT` e fechado por `DEDENT`. Esses tokens o programador não digita.
  - ⟨http_request⟩ — só `GET` e a URL, sem corpo da requisição.

  Se sobrar tempo, abra `omnitest/parser.py` e mostre que cada método (`_test_decl`, `_block`, `_http_request`) consome um não-terminal.

- [ ] **Item 3 do P1 — testar se um código pertence à gramática**

  O documento cita JFLAP, autômato com pilha e Bison como formas de testar a gramática. Não usamos essas ferramentas.

  A forma usada está no próprio enunciado: elementos recursivos. O parser desce um método por não-terminal e decide com o token da frente. O critério 3 também lista o projeto em Python.

  Onde clicar e o que rodar (detalhe no README):

  1. Terminal. `python3 -m omnitest examples/get_one.omt` imprime `ACEITO`.
  2. Em seguida, `python3 -m omnitest examples/get_all.omt` imprime `ACEITO`.
  3. O comando de indentação quebrada imprime `REJEITADO` com estágio `léxico`. Diga: o erro é léxico porque o recuo de 2 espaços não cai em nenhum nível da pilha. O corpo foi aberto com 4.
  4. O comando sem o `:` do tipo imprime `REJEITADO` com estágio `sintático`.
  5. `python3 -m pytest -v`. Os cinco testes passam. Abra `tests/test_reconhecimento.py` só se pedirem onde está o caso da palavra reservada `let test`.

  Diga em uma frase: aceitar o arquivo não consulta a API. Não aparece status HTTP de verdade.

- [ ] **Item 4 do P1 — análise léxica, tipo de gramática, problemas e virtudes**

  O documento pergunta como fica a análise léxica, que tipo de gramática é essa, e quais problemas ou virtudes aparecem.

  Fale nesta ordem:

  - A gramática é livre de contexto, escrita em BNF.
  - O lexer transforma caracteres em tokens. O parser só vê tokens.
  - Palavra reservada e identificador se separam no lexer: a palavra é lida e consultada numa tabela. `GET` é método; `get` seria identificador. `let test` falha no parser porque `test` já chegou como palavra reservada, não como nome.

  Onde clicar:

  1. `omnitest/lexer.py`, método `_scan_word` — a tabela de palavras reservadas.
  2. O mesmo arquivo, método `_adjust_indent` — a pilha. Aumento de recuo emite `INDENT`. Queda emite `DEDENT`. Recuo que não coincide com um nível aberto é erro léxico.
  3. `README.md`, seção **Análise léxica neste projeto**.

  Virtude para dizer: o bloco se vê na indentação, e a gramática dos comandos não precisa de chaves.

  Problema para dizer: a coluna do texto não entra numa produção BNF. Por isso a pilha fica no lexer. Outro limite: `let response: Int = GET "..."` é aceito. `Int` e `GET` existem na sintaxe; combinar os dois seria semântica, e esta P1 não faz isso.

- [ ] **Item 5 do P1 — seminário**

  Este momento é o seminário. O que mostrar já está nos itens acima: exemplo, BNF, uma variável da gramática, um `ACEITO`, um `REJEITADO`, e a pilha de indentação.

- [ ] **Item 6 do P1 — SIGAA**

  Não há clique de código para isso. O texto a inserir no SIGAA é o `README.md`: gramática, variáveis, análise léxica e o que a validação observou. Se perguntarem o que foi entregue por escrito, é esse arquivo.

- [ ] **Se sobrar pergunta**

  - Por que só `GET`? Porque os dois exemplos bastam para a Parte 1: um recurso e uma coleção. `POST` e JSON ficaram de fora para a gramática continuar pequena.
  - Por que JSONPlaceholder? É uma API pública estável, usada para ilustrar teste de API. A URL no fonte é só o literal que a gramática reconhece.
  - O parser é LL(1)? As alternativas foram escritas para o próximo token decidir a produção, sem recursão à esquerda. Não levamos uma tabela de FIRST/FOLLOW para a apresentação.
  - Saímos do escopo? Não geramos código objeto, não montamos árvore e não executamos HTTP. O enunciado pede o passo inicial: a gramática e um jeito de testar se a palavra pertence a ela.
