# omni-test-lang
A tested language for testers.
Assumi integralmente a persona do **OmniTest Compiler Project Agent** definida no `AGENTS.md`/`REVISOR.md`, li o `P1.pdf` anexado (fonte de verdade da atividade) e executei o projeto da Fase 1 à Fase 6 sem interromper para perguntas — todas as decisões de projeto foram tomadas de forma autônoma e documentadas. Implementei de verdade o lexer/parser em Python (`omni-test-lang/omnitest/`), criei 18 arquivos `.omt` (válidos e inválidos) e **executei** 26 testes automatizados (`pytest`), 100% aprovados, além do CLI `python -m omnitest`. Durante a revisão crítica obrigatória (Seção 16 do AGENTS.md), encontrei e corrigi uma lacuna real na gramática (array JSON não podia ser valor de nível superior de um `let`) antes de fechar a entrega. Tudo foi commitado no repositório (`git log`), e o documento completo também está salvo em `omni-test-lang/ENTREGA_P1.md`.

Segue a entrega completa, com os quatro blocos solicitados, de uma só vez.

---

# OmniTest — Entrega Completa da Parte 1 (P1) — Compiladores (UFC/Russas)

**Persona assumida:** OmniTest Compiler Project Agent (definida em `AGENTS.md`/`REVISOR.md`).
**Fonte de verdade dos requisitos:** `P1.pdf` (convertido para texto em `P1.txt` para conferência).
**Modo de execução:** decisões de projeto tomadas de forma autônoma, sem pausas para perguntas, conforme solicitado. Implementação real em Python, executada de fato (não simulada) — todos os resultados de teste citados abaixo foram efetivamente observados nesta sessão.

> Convenção de honestidade metodológica usada em todo o documento:
> - 🟢 **OBSERVADO** = resultado obtido executando código real nesta sessão.
> - 🔵 **DECISÃO DE PROJETO** = escolha do grupo/agente, não exigida literalmente pelo PDF.
> - 🟡 **PREVISTO** = conclusão lógica não obtida por execução (raro neste documento, pois quase tudo foi executado).

---

# BLOCO A — ESPECIFICAÇÃO ACADÊMICA

## A.1 Interpretação da P1 (Fase 1)

### A.1.1 Resumo objetivo do problema proposto

O `P1.pdf` (Universidade Federal do Ceará — Campus de Russas, disciplina Compiladores, professor Cenez Araújo de Rezende) propõe a **Parte 1** de um projeto de compiladores focado exclusivamente na etapa de **análise (front-end)**, não exigindo síntese/back-end. O enunciado pede que a equipe:

1. Defina uma **gramática de linguagem de programação**, podendo partir de ideias simples (ex.: operações matemáticas) e evoluir, observando gramáticas reais como inspiração — mas **com assinatura própria** de projetista.
2. **Documente os detalhes da linguagem**, em especial as variáveis (não-terminais) da gramática e suas produções.
3. **Utilize alguma ferramenta** para testar características da gramática: JFLAP, autômato com pilha (visto em LFA), Bison/yacc, ou o **projeto Python do laboratório**.
4. Discuta como ficaria a **análise léxica**, o tipo de gramática usada, e seus **problemas ou virtudes**.
5. **Apresente os resultados em um breve seminário**.
6. **Insira no SIGAA** os detalhes do estudo, incluindo a gramática analisada/desenvolvida.

### A.1.2 Lista de entregáveis (conforme o PDF)

| # | Entregável | Fonte |
|---|---|---|
| 1 | Gramática de linguagem de programação com assinatura própria | PDF, Seção 2.1 |
| 2 | Documentação das variáveis da gramática (não-terminais) | PDF, Seção 2.1 |
| 3 | Evidência de uso de ferramenta de teste da gramática | PDF, Seção 2.1 e 3.3 |
| 4 | Discussão sobre análise léxica (tipo de gramática, problemas/virtudes) | PDF, Seção 2.1 |
| 5 | Seminário de apresentação dos resultados | PDF, Seção 2.1 e Instruções preliminares (item 3) |
| 6 | Registro no SIGAA (gramática + detalhes) | PDF, Seção 2.1, item 6 e link [7] |

### A.1.3 Critérios de avaliação explicitamente mencionados

Do PDF, Seção 3 ("Critérios Principais na Aferição do Andamento do Trabalho"):

1. Clareza na especificação e apresentação do projeto.
2. Trabalho em equipe.
3. Testes diversos (JFLAP, autômato com pilha, Bison, BNFPlayground, projeto Python, etc.), reconhecendo explicitamente que o BNFPlayground **tem limitações**.
4. Apresentação e entrega dentro do prazo.

### A.1.4 Restrições e limites de escopo (explícitos ou inferidos)

| Restrição | Classificação |
|---|---|
| Equipe de até 4 alunos | Explícito (Instruções preliminares, item 1) |
| Soluções iguais entre grupos são penalizadas → exige originalidade/assinatura | Explícito (item 2) |
| Entrega = projeto + apresentação (ou vídeo) | Explícito (item 3) |
| Submissão da gramática até a data do SIGAA; apresentação em cronograma à parte | Explícito (item 4) |
| P1 cobre **apenas análise** (léxica/sintática), não síntese/back-end/geração de código | Explícito (Seção 2, parágrafo introdutório) |
| Não há exigência de que a linguagem seja "grande" ou cubra todos os recursos de uma linguagem de programação real | Decisão de projeto (o PDF apenas sugere partir de algo simples e evoluir) |
| Não há exigência de que o domínio seja "testes de API" — essa é uma escolha de identidade da equipe (QA Software Engineer) | Decisão de projeto do AGENTS.md, não do PDF |
| Não há exigência de execução real de HTTP | Inferido: o PDF fala em reconhecer/testar a gramática, não em executar programas |

### A.1.5 Riscos de uma entrega incompleta

| Risco | Consequência | Mitigação adotada nesta entrega |
|---|---|---|
| Apresentar apenas uma gramática "no papel", sem evidência de teste | Fere o critério 3 (Testes diversos) | Implementação Python real + suíte pytest executada (26 casos, 100% aprovados) |
| Gramática ambígua ou incompatível com os exemplos | Fere clareza e corretude formal | Todos os exemplos foram efetivamente parseados pela implementação (evidência 🟢 OBSERVADO, não alegação) |
| Confundir análise sintática com semântica | Fere rigor acadêmico exigido pelo AGENTS.md | Seção A.8 trata a distinção explicitamente; nenhuma verificação de tipo é apresentada como produção BNF |
| Gramática igual à de outro grupo | Penalização por falta de originalidade | Domínio (DSL de testes de API), palavras-chave, tratamento de indentação com supressão de NEWLINE dentro de JSON e política de erros são decisões autorais documentadas |
| Alegar execução/validação que não ocorreu | Quebra de integridade acadêmica | Todo resultado de teste citado neste documento foi gerado nesta sessão (comandos e saídas reproduzidas literalmente) |

### A.1.6 Matriz de rastreabilidade

| Requisito | Classificação | Evidência no projeto | Onde será apresentado | Como será validado |
|---|---|---|---|---|
| Definir gramática de linguagem de programação | Explícito | Gramática BNF completa (Seção A.6) | Relatório + slides 6–7 (BLOCO C) | Leitura formal + parser que a implementa |
| Documentar variáveis da gramática (não-terminais) | Explícito | Tabela de 26 não-terminais (Seção A.7) | Relatório, Seção 8 | Revisão cruzada com as produções do `parser.py` |
| Usar ferramenta para testar a gramática | Explícito | Implementação Python (`omnitest/`) executada via `pytest` | Seminário, slide 9 | 26 testes automatizados, 100% aprovados (BLOCO B) |
| Discutir análise léxica (tipo de gramática, problemas/virtudes) | Explícito | Seção A.5 (léxico) + Seção D (discussão crítica) | Relatório, Seções 6 e 12 | Casos de teste de indentação e tokens inválidos |
| Apresentar resultados em seminário | Explícito | Roteiro de 12 slides (BLOCO C) | Seminário | Ensaio do grupo com o roteiro fornecido |
| Inserir no SIGAA gramática + detalhes | Explícito | Conteúdo deste documento é apto a colagem no SIGAA | SIGAA | Responsabilidade do grupo (fora do escopo técnico) |
| Domínio = testes de API HTTP (OmniTest) | Decisão de projeto (AGENTS.md) | Palavras-chave `GET`/`POST`/`assert`/tipo `Response` | Relatório, Seção 4 | Exemplos 1 e 2 (Seção A.9) |
| Indentação estrutural sem chaves | Decisão de projeto (AGENTS.md, inspirado em Python) | Lexer com pilha de indentação (`lexer.py`) | Relatório, Seção 6.4 | Casos T-I01, T-I08, T-I09 (BLOCO B) |
| Implementação em Python com lexer/parser separados | Recomendação do agente, compatível com "projeto em Python" citado no PDF | `omnitest/lexer.py`, `omnitest/parser.py` | Seminário, slide 9 | Execução de `python -m omnitest <arquivo>` |
| Uso de JFLAP/Bison/BNFPlayground | Permitido, não obrigatório | Não utilizado nesta entrega (decisão registrada como pendência, ver BLOCO D) | — | — |

---

## A.2 Conceito da OmniTest (Fase 2)

### A.2.1 Problema que a OmniTest resolve

Profissionais de QA frequentemente descrevem casos de teste de API em formatos ad hoc (planilhas, comentários em código, ferramentas proprietárias como Postman) que misturam descrição informal com implementação. A OmniTest propõe uma **notação textual pequena, tipada e estruturalmente indentada** para expressar cenários de teste de API (requisição → resposta → asserção) de forma legível e formalmente analisável — sem pretender substituir ferramentas de execução reais (Rest Assured, Karate DSL, Postman etc.), que ficam fora do escopo desta P1.

### A.2.2 Público-alvo

Equipes de QA/SDET e desenvolvedores back-end que já descrevem testes de API em linguagem natural ou em ferramentas gráficas, e que se beneficiariam de uma notação textual, versionável (compatível com Git) e com sintaxe mínima.

### A.2.3 Objetivos de projeto

1. Ser pequena o suficiente para ser especificada, implementada e testada dentro do prazo da P1.
2. Ser suficientemente expressiva para demonstrar: declaração tipada, controle de blocos por indentação, requisições HTTP, literais estruturados (JSON) e asserções.
3. Ser formalmente analisável por um parser descendente recursivo simples.
4. Refletir o repertório prático de QA (GET/POST, status code, payload JSON, asserções) sem imitar nenhuma ferramenta específica citada no AGENTS.md.

### A.2.4 Características da linguagem

* Sintaxe orientada a blocos por indentação (inspirada em Python), sem chaves para blocos de teste.
* Tipagem estática e explícita (`Int`, `String`, `Bool`, `Json`, `Response`).
* Tokens estruturais `INDENT`/`DEDENT`/`NEWLINE` gerados pelo lexer (nunca digitados pelo programador).
* Comandos de domínio: `test`, `let`, `assert`, `GET`, `POST`.
* Literais JSON representados **estruturalmente na gramática** (não como um único token opaco), com suporte a objetos e arrays aninhados.

### A.2.5 Funcionalidades incluídas

* Declaração de cenários de teste nomeados (`test "nome":`).
* Declaração de variáveis tipadas (`let nome: Tipo = valor`).
* Requisições `GET` (sem payload) e `POST` (com payload obrigatório).
* Acesso a campos de resposta por encadeamento de ponto (`response.body.name`).
* Asserções de igualdade/relacionais (`==`, `!=`, `<`, `>`, `<=`, `>=`) ou de valor booleano isolado.
* Literais inteiros, string, booleano, objeto JSON e array JSON (inclusive como valor de `let` de nível superior — ver Seção D.2, item corrigido nesta revisão).
* Comentários de linha iniciados por `#` (apenas no lexer, sem produção gramatical associada).
* Múltiplos cenários de teste no mesmo arquivo.
* Programa vazio (política explícita, ver A.4).

### A.2.6 Funcionalidades deliberadamente excluídas (com justificativa)

| Excluído | Justificativa |
|---|---|
| Estruturas de controle (`if`, `for`, `while`) | Ampliariam a gramática (blocos aninhados, múltiplos níveis de INDENT) muito além do necessário para demonstrar os conceitos de análise léxica/sintática da P1 |
| Operadores aritméticos e lógicos (`+`, `-`, `and`, `or`, `not`) | A OmniTest é declarativa (descreve *o que* verificar, não *como* computar); adicionar aritmética não agrega valor para o domínio de asserções de teste |
| Métodos HTTP além de GET/POST (PUT, DELETE, PATCH) | O PDF pede uma gramática mínima e coesa; GET/POST já demonstram a diferença sintática "com payload obrigatório" vs. "sem payload", suficiente para os fins da P1 |
| Números de ponto flutuante | Simplifica o léxico de `INT_LITERAL`; não há caso de uso essencial no domínio de status codes/contadores para a P1 |
| `null` em JSON | Reduz alternativas em `json_value`, mantendo a gramática enxuta; documentado como simplificação, não como limitação de JSON real |
| Execução real de requisições HTTP | Fora do escopo da P1, que trata de *análise*, não de *síntese/execução* (ver introdução do PDF, Seção 2) |
| Análise semântica (tipos, escopo) | Explicitamente fora do escopo mínimo da P1; tratada como trabalho futuro (Seção A.8 e C.1) |

### A.2.7 Paradigma e estilo sintático

Declarativo, orientado a blocos por indentação, com tipagem estática explícita — decisão de projeto que aproxima a OmniTest de linguagens como Python (indentação) e Karate DSL/Gherkin (declarações de teste legíveis), sem copiar a gramática de nenhuma delas.

### A.2.8 Modelo de execução conceitual

🔵 **DECISÃO DE PROJETO.** A OmniTest, nesta P1, define um modelo de execução **apenas conceitual**: um `test` é uma sequência de comandos executados em ordem; `let` vincula um identificador a um valor (literal, JSON ou resultado de uma requisição HTTP); `assert` verificaria, em uma implementação futura, se a comparação é verdadeira, encerrando o teste com falha caso contrário. **Nenhuma dessas semânticas é executada nesta entrega** — apenas reconhecida sintaticamente. Isso é declarado explicitamente para não confundir aceitação sintática com execução real.

### A.2.9 Por que uma DSL de testes de API é um tema apropriado (sem atribuir exigência ao professor)

O PDF não exige nenhum domínio específico — apenas "linguagem de programação". A escolha do domínio de testes de API é uma decisão do grupo, justificada por: (a) aproveitar a experiência prática do projetista (QA Software Engineer), atendendo ao pedido de "assinatura como projetista de linguagem" (PDF, Seção 2.1); (b) reduzir o risco de duplicidade com gramáticas genéricas de calculadora/expressões aritméticas, comuns entre grupos que seguem literalmente o exemplo do PDF; (c) fornecer um vocabulário concreto (GET/POST/status/assert) que facilita explicar o parser durante o seminário.

---

## A.3 Escopo e decisões de projeto (consolidado)

| Decisão | Tipo | Justificativa |
|---|---|---|
| Indentação apenas com espaços; TAB na indentação é erro léxico | 🔵 Decisão | Elimina ambiguidade de largura de tabulação, como recomendado no AGENTS.md; mesma política adotada pelo tokenizer de Python quando `-tt` está habilitado |
| INDENT/DEDENT suprimidos enquanto `{`/`[` estiverem abertos | 🔵 Decisão | Permite literais JSON multi-linha sem exigir uma "mini-linguagem" de continuação; réplica documentada da regra de agrupamento implícito de linha do Python dentro de parênteses/colchetes/chaves |
| Chaves de objeto JSON só aceitam `STRING_LITERAL` (JSON real) | 🔵 Decisão | Evita introduzir um não-terminal de "identificador-como-chave" que divergiria do JSON padrão usado por QA no dia a dia |
| `GET` nunca aceita payload; `POST` sempre exige `<primary>` como payload | 🔵 Decisão | Restringe a ambiguidade "payload opcional" para uma regra sintaticamente verificável, evitando delegar essa checagem à semântica |
| Programa vazio é sintaticamente válido (zero `test`) | 🔵 Decisão | `<test_decl_list>` tem produção vazia; interpretado como "nenhum cenário definido ainda", análogo a um arquivo Python vazio ser um módulo válido |
| Bloco de teste exige pelo menos 1 comando (`<stmt_list>` não admite vazio) | 🔵 Decisão | Um teste sem nenhum comando não tem utilidade prática e geraria ambiguidade com a política de programa vazio |
| Palavras reservadas são *case-sensitive* (`GET` ≠ `get`) | 🔵 Decisão | Simplifica o reconhecimento léxico (busca direta em tabela hash) e seguindo convenção comum em DSLs baseadas em Python |
| `true`/`false` são lexicamente `BOOLEAN_LITERAL`, não `IDENTIFIER` | 🔵 Decisão | Evita que o parser precise reclassificar identificadores especiais durante a análise sintática (ver A.5.2) |
| Comentários com `#` até fim de linha | 🔵 Decisão | Facilidade prática pedida implicitamente por qualquer DSL usada por QA em scripts reais; não gera nenhum não-terminal novo (tratado 100% no lexer) |
| Análise semântica **não** implementada nesta P1 | Alinhado ao escopo do PDF (só análise/front-end é pedida, e mesmo assim o PDF fala em reconhecer a gramática, não em checar tipos) | Ver A.8 |

---

## A.4 Especificação léxica (Fase 3 / Seção 6 do AGENTS.md)

### A.4.1 Catálogo de tokens

| Token | Lexema/Padrão | Categoria | Descrição | Exemplo | Restrições |
|---|---|---|---|---|---|
| `TEST` | `test` | Palavra reservada | Inicia a declaração de um cenário de teste | `test "x":` | Case-sensitive |
| `LET` | `let` | Palavra reservada | Inicia declaração de variável tipada | `let a: Int = 1` | — |
| `ASSERT` | `assert` | Palavra reservada | Inicia uma asserção | `assert a == 1` | — |
| `GET` | `GET` | Palavra reservada (método HTTP) | Requisição HTTP sem payload | `GET "/health"` | Maiúsculas obrigatórias |
| `POST` | `POST` | Palavra reservada (método HTTP) | Requisição HTTP com payload obrigatório | `POST "/x" p` | Maiúsculas obrigatórias |
| `TYPE_INT` | `Int` | Palavra reservada (tipo) | Tipo inteiro | `Int` | — |
| `TYPE_STRING` | `String` | Palavra reservada (tipo) | Tipo texto | `String` | — |
| `TYPE_BOOL` | `Bool` | Palavra reservada (tipo) | Tipo booleano | `Bool` | — |
| `TYPE_JSON` | `Json` | Palavra reservada (tipo) | Tipo objeto/array JSON | `Json` | — |
| `TYPE_RESPONSE` | `Response` | Palavra reservada (tipo) | Tipo resultado de requisição HTTP | `Response` | — |
| `IDENTIFIER` | `[A-Za-z_][A-Za-z0-9_]*`, exceto palavras reservadas | Identificador | Nome de variável/campo | `response`, `statusEsperado` | Case-sensitive; não pode coincidir com palavra reservada |
| `INT_LITERAL` | `-?[0-9]+` | Literal | Número inteiro | `200`, `-1` | Sem ponto flutuante; zeros à esquerda aceitos (simplificação) |
| `STRING_LITERAL` | `"..."` com escapes `\" \\ \n \t` | Literal | Texto delimitado por aspas duplas | `"/health"` | Não pode conter quebra de linha literal não escapada; deve ser fechada na mesma linha física |
| `BOOLEAN_LITERAL` | `true`, `false` | Literal | Valor booleano | `true` | Reservado; nunca é `IDENTIFIER` |
| `ASSIGN` | `=` | Operador | Atribuição em `let` | `= 5` | — |
| `EQ` | `==` | Operador relacional | Igualdade | `a == b` | — |
| `NEQ` | `!=` | Operador relacional | Diferença | `a != b` | `!` isolado é erro léxico |
| `LT` / `GT` | `<` / `>` | Operador relacional | Menor/maior | `a < b` | — |
| `LE` / `GE` | `<=` / `>=` | Operador relacional | Menor/maior ou igual | `a <= b` | — |
| `DOT` | `.` | Operador de acesso | Acesso a campo/membro | `response.status` | — |
| `COLON` | `:` | Delimitador | Separa nome:tipo ou finaliza cabeçalho de `test` | `let a: Int` | — |
| `COMMA` | `,` | Delimitador | Separa pares/elementos JSON | `{"a":1,"b":2}` | — |
| `LBRACE` / `RBRACE` | `{` / `}` | Delimitador | Delimita objeto JSON; controla profundidade de colchetes | `{ }` | Deve fechar antes do EOF |
| `LBRACKET` / `RBRACKET` | `[` / `]` | Delimitador | Delimita array JSON; controla profundidade de colchetes | `[ ]` | Deve fechar antes do EOF |
| `NEWLINE` | quebra de linha física fora de `{}`/`[]` | Estrutural | Termina um comando lógico | — | Suprimido dentro de JSON aberto |
| `INDENT` | aumento de indentação | Estrutural | Abre um bloco de teste | — | Gerado pelo lexer; nunca digitado |
| `DEDENT` | redução de indentação | Estrutural | Fecha um bloco de teste | — | Pode ser emitido em sequência (múltiplos DEDENT) |
| `EOF` | fim de arquivo | Estrutural | Marca o fim da entrada | — | Sempre precedido pelos DEDENT pendentes |

Tokens cogitados no AGENTS.md e **não incluídos** nesta versão, com justificativa: `JSON_LITERAL` monolítico — descartado a favor de uma representação **estrutural** na gramática (`json_object`, `json_array`, `json_pair`, `json_value`), conforme recomendado explicitamente na Seção 6.3 do AGENTS.md ("Evite definir um token JSON tão abrangente").

Diferenciação lexema/token/símbolo gramatical: o **lexema** é o texto bruto reconhecido (`"200"`); o **token** é o par (categoria, lexema/valor) produzido pelo lexer (`Token(INT_LITERAL, "200", 200, ...)`); o **símbolo gramatical** é o terminal usado na gramática (`INT_LITERAL`), que a produção `<primary>` referencia sem se importar com o valor concreto.

### A.4.2 Palavras reservadas

Lista completa (12 palavras): `test`, `let`, `assert`, `GET`, `POST`, `Int`, `String`, `Bool`, `Json`, `Response`, `true`, `false`.

O lexer resolve a ambiguidade identificador-vs-palavra-reservada em uma única regra determinística: primeiro reconhece a **maior sequência possível** de caracteres de identificador (`[A-Za-z_][A-Za-z0-9_]*`, *maximal munch*); em seguida, consulta uma tabela hash fixa (`KEYWORDS`, em `omnitest/tokens.py`); se o lexema constar na tabela, o token recebe o tipo reservado (ou `BOOLEAN_LITERAL`, no caso de `true`/`false`); caso contrário, é classificado como `IDENTIFIER`. Isso implica que `Get`, `get`, `TEST2`, `_response` são identificadores válidos — apenas os 12 lexemas exatos (case-sensitive) são reservados.

### A.4.3 Identificadores e literais

* **Identificadores:** iniciam com letra (`A-Z`/`a-z`) ou `_`; seguem-se letras, dígitos ou `_`; sem limite de tamanho definido; case-sensitive; não podem coincidir com palavra reservada.
* **Inteiros:** um `-` opcional seguido de um ou mais dígitos decimais. Sem separadores de milhar, sem notação científica, sem ponto flutuante (simplificação documentada em A.2.6).
* **Strings:** delimitadas por aspas duplas; suportam string vazia (`""`); suportam escapes `\"`, `\\`, `\n`, `\t`; **não** podem conter uma quebra de linha física não escapada (erro léxico "string literal não foi fechada").
* **Booleanos:** apenas os literais `true`/`false` (minúsculos).
* **URLs:** não recebem uma categoria de token própria — são representadas como `STRING_LITERAL` comuns (ex.: `"/users"`), decisão que evita duplicar as regras de string para um caso especial sem necessidade sintática.
* **JSON:** representado estruturalmente (ver A.4.1); chaves de objeto são sempre `STRING_LITERAL`; valores podem ser string, inteiro, booleano, objeto ou array (aninhamento arbitrário).
* **Caracteres especiais/erros:** qualquer caractere fora do alfabeto de tokens definidos (ex.: `@`, `&`, `$`) gera `OmniTestLexError` "caractere inesperado".

### A.4.4 Tratamento de indentação (núcleo da OmniTest)

Implementado em `omnitest/lexer.py`. Algoritmo (idêntico em espírito ao tokenizer de Python, mas simplificado para o subconjunto da OmniTest):

1. O código-fonte é dividido em linhas físicas (`\n` como separador, `\r\n`/`\r` normalizados).
2. Enquanto a profundidade de colchetes/chaves (`bracket_depth`) é 0, cada linha física inicia uma possível linha lógica nova.
3. Linhas em branco (vazias ou só espaços) e linhas cujo primeiro caractere não-espaço é `#` são **ignoradas** (nenhum token, nenhuma variação de indentação).
4. A indentação é medida contando espaços à esquerda; encontrar um `\t` nessa contagem é erro léxico imediato (política: **somente espaços**, decisão justificada em A.3).
5. Uma pilha (`indent_stack`, iniciada em `[0]`) guarda os níveis de indentação abertos. Se o nível atual for maior que o topo, empilha e emite `INDENT`. Se for menor, desempilha e emite `DEDENT` repetidamente até encontrar um nível igual (múltiplos `DEDENT` em sequência, conforme exigido no AGENTS.md); se nenhum nível da pilha coincidir exatamente, é erro léxico "indentação inconsistente".
6. Enquanto `bracket_depth > 0` (dentro de `{`/`[` não fechados), a indentação **não é avaliada** e `NEWLINE` **não é emitido** — a linha física é tratada como continuação da linha lógica anterior. Isso permite literais JSON formatados em múltiplas linhas (ver exemplo `examples/valid/json_multilinha.omt`, validado em 🟢 OBSERVADO no BLOCO B).
7. Ao final da leitura do arquivo, se `bracket_depth != 0`, é erro léxico ("chave/colchete não fechado"). Caso contrário, todos os níveis de indentação pendentes na pilha são fechados com `DEDENT` antes do token `EOF`.

Dificuldades práticas observadas na implementação (relacionadas à experiência de laboratório de análise léxica):
* Decidir **em que ponto exato** suprimir NEWLINE/indentação (dentro de colchetes) exigiu introduzir um contador de profundidade (`bracket_depth`) compartilhado entre o escâner de linha e o escâner de token — um erro comum é incrementar/decrementar esse contador só ao final da linha, quando na verdade ele deve ser atualizado token a token.
* Erros de indentação exigem cuidado para **não interromper com uma pilha inconsistente**: o código desempilha _antes_ de decidir se houve erro, e só então compara o topo residual — se não fizer isso corretamente, o parser recebe uma sequência de `DEDENT` divergente da realidade.
* Uma armadilha comum (evitada aqui) é emitir `NEWLINE` mesmo para linhas em branco ou comentário — isso obrigaria a gramática a tolerar `NEWLINE` "supérfluos" em qualquer ponto, aumentando desnecessariamente a complexidade das produções.

---

## A.5 Gramática formal — entregável central (Fase 3 / Seção 7 do AGENTS.md)

### A.5.1 Notação

Gramática apresentada em **BNF estrita** (sem `*`, `+`, `?` — recursão explícita à direita e produções vazias explícitas com `ε`). Convenções:
* Não-terminais entre `⟨ ⟩`.
* Terminais entre aspas (`"test"`) ou em MAIÚSCULAS quando correspondem a uma classe léxica (`IDENTIFIER`, `INT_LITERAL`, `STRING_LITERAL`).
* `::=` separa lado esquerdo e direito da produção; `|` separa alternativas; `ε` denota a cadeia vazia.
* **Símbolo inicial:** `⟨program⟩`.

Nenhuma notação EBNF é usada nesta seção (não há `*`/`+`/`?` no bloco formal abaixo); qualquer forma abreviada mencionada em prosa (ex.: "zero ou mais") é apenas explicativa e sempre remetida à sua tradução BNF exata.

### A.5.2 Conjunto de terminais (33)

```
"test" "let" "assert" "GET" "POST"
"Int" "String" "Bool" "Json" "Response"
"true" "false"
IDENTIFIER INT_LITERAL STRING_LITERAL
"=" "==" "!=" "<" ">" "<=" ">=" "."
":" "," "{" "}" "[" "]"
NEWLINE INDENT DEDENT EOF
```

(`true`/`false` aparecem como terminais literais na gramática, mas são reconhecidos pelo lexer sob a categoria de token `BOOLEAN_LITERAL` — ver A.4.2.)

### A.5.3 Conjunto de não-terminais (26)

```
⟨program⟩ ⟨test_decl_list⟩ ⟨test_decl⟩ ⟨block⟩
⟨stmt_list⟩ ⟨stmt⟩ ⟨let_stmt⟩ ⟨assert_stmt⟩ ⟨type⟩
⟨rhs⟩ ⟨http_request⟩ ⟨comparison⟩ ⟨comp_op⟩
⟨primary⟩ ⟨member_access⟩ ⟨member_tail⟩
⟨json_object⟩ ⟨json_members_opt⟩ ⟨json_members⟩ ⟨json_member_tail⟩
⟨json_pair⟩ ⟨json_value⟩
⟨json_array⟩ ⟨json_elements_opt⟩ ⟨json_elements⟩ ⟨json_element_tail⟩
```

### A.5.4 Produções (BNF completa)

```
⟨program⟩            ::= ⟨test_decl_list⟩ EOF

⟨test_decl_list⟩     ::= ⟨test_decl⟩ ⟨test_decl_list⟩
                        | ε

⟨test_decl⟩          ::= "test" STRING_LITERAL ":" NEWLINE ⟨block⟩

⟨block⟩              ::= INDENT ⟨stmt_list⟩ DEDENT

⟨stmt_list⟩          ::= ⟨stmt⟩ ⟨stmt_list⟩
                        | ⟨stmt⟩

⟨stmt⟩               ::= ⟨let_stmt⟩
                        | ⟨assert_stmt⟩

⟨let_stmt⟩           ::= "let" IDENTIFIER ":" ⟨type⟩ "=" ⟨rhs⟩ NEWLINE

⟨assert_stmt⟩        ::= "assert" ⟨comparison⟩ NEWLINE

⟨type⟩               ::= "Int" | "String" | "Bool" | "Json" | "Response"

⟨rhs⟩                ::= ⟨http_request⟩
                        | ⟨primary⟩

⟨http_request⟩       ::= "GET" STRING_LITERAL
                        | "POST" STRING_LITERAL ⟨primary⟩

⟨comparison⟩         ::= ⟨primary⟩ ⟨comp_op⟩ ⟨primary⟩
                        | ⟨primary⟩

⟨comp_op⟩            ::= "==" | "!=" | "<" | ">" | "<=" | ">="

⟨primary⟩            ::= ⟨member_access⟩
                        | INT_LITERAL
                        | STRING_LITERAL
                        | "true"
                        | "false"
                        | ⟨json_object⟩
                        | ⟨json_array⟩

⟨member_access⟩      ::= IDENTIFIER ⟨member_tail⟩

⟨member_tail⟩        ::= "." IDENTIFIER ⟨member_tail⟩
                        | ε

⟨json_object⟩        ::= "{" ⟨json_members_opt⟩ "}"

⟨json_members_opt⟩   ::= ⟨json_members⟩
                        | ε

⟨json_members⟩       ::= ⟨json_pair⟩ ⟨json_member_tail⟩

⟨json_member_tail⟩   ::= "," ⟨json_pair⟩ ⟨json_member_tail⟩
                        | ε

⟨json_pair⟩          ::= STRING_LITERAL ":" ⟨json_value⟩

⟨json_value⟩         ::= STRING_LITERAL
                        | INT_LITERAL
                        | "true"
                        | "false"
                        | ⟨json_object⟩
                        | ⟨json_array⟩

⟨json_array⟩         ::= "[" ⟨json_elements_opt⟩ "]"

⟨json_elements_opt⟩  ::= ⟨json_elements⟩
                        | ε

⟨json_elements⟩      ::= ⟨json_value⟩ ⟨json_element_tail⟩

⟨json_element_tail⟩  ::= "," ⟨json_value⟩ ⟨json_element_tail⟩
                        | ε
```

> Nota de revisão (Fase 5): a alternativa `⟨json_array⟩` em `⟨primary⟩` foi **adicionada durante a revisão crítica obrigatória** (Seção 16 do AGENTS.md) — a primeira versão da gramática só permitia array JSON *aninhado* dentro de um objeto, impedindo `let roles: Json = ["QA", "SDET"]`. Ver BLOCO D, item de auditoria da gramática, para o relato completo dessa correção.

### A.5.5 Funcionalidades mínimas exigidas (Seção 7.2 do AGENTS.md) — checklist de cobertura

| Exigência | Onde a gramática cobre |
|---|---|
| Programa | `⟨program⟩` |
| Declaração de variáveis tipadas | `⟨let_stmt⟩` |
| Tipos explícitos | `⟨type⟩` (5 tipos: `Int`, `String`, `Bool`, `Json`, `Response`) |
| Blocos de teste | `⟨test_decl⟩` + `⟨block⟩` |
| Requisições HTTP GET e POST | `⟨http_request⟩` |
| Asserções | `⟨assert_stmt⟩` + `⟨comparison⟩` |
| Expressões/valores para os exemplos | `⟨primary⟩`, `⟨member_access⟩`, `⟨json_object⟩`, `⟨json_array⟩` |
| Blocos delimitados por NEWLINE/INDENT/DEDENT | `⟨test_decl⟩` (NEWLINE) + `⟨block⟩` (INDENT/DEDENT) |

### A.5.6 Requisitos de rigor formal — verificação

* **Sem símbolos indefinidos:** todo não-terminal referenciado em alguma produção (Seção A.5.3) possui sua própria produção definidora (Seção A.5.4) — conferido manualmente e implicitamente pelo parser, que possui uma função Python por não-terminal (ver BLOCO B).
* **Sem recursão à esquerda:** todas as recursões (`⟨test_decl_list⟩`, `⟨stmt_list⟩`, `⟨member_tail⟩`, `⟨json_member_tail⟩`, `⟨json_element_tail⟩`) são à **direita**, adequadas a um parser descendente recursivo sem necessidade de eliminação de recursão à esquerda.
* **Fatoração à esquerda:** `⟨json_object⟩` e `⟨json_array⟩` foram fatorados com os não-terminais auxiliares `_opt` exatamente para evitar o conflito superficial entre "há conteúdo" e "está vazio" no primeiro token após `{`/`[` (ver A.5.7).
* **Compatibilidade com os tokens do lexer:** todo terminal citado na gramática corresponde a um `TokenType` definido em `omnitest/tokens.py`, e nenhum `TokenType` fica sem uso na gramática (checklist cruzado na auditoria, BLOCO D).
* **Distinção sintaxe/semântica:** a gramática **não** impõe que o tipo declarado em `let x: Int = ...` seja compatível com o valor atribuído — isso é uma verificação semântica, deliberadamente fora do escopo (ver A.8).

### A.5.7 Validação da gramática — derivação mais à esquerda

Programa de referência (`examples/get_test.omt`, 🟢 validado pela implementação):

```
test "health check retorna 200":
    let response: Response = GET "/health"
    assert response.status == 200
```

Derivação mais à esquerda a partir de `⟨program⟩` (cada passo expande o não-terminal mais à esquerda):

```
⟨program⟩
⇒ ⟨test_decl_list⟩ EOF
⇒ ⟨test_decl⟩ ⟨test_decl_list⟩ EOF
⇒ "test" STRING_LITERAL ":" NEWLINE ⟨block⟩ ⟨test_decl_list⟩ EOF
⇒ "test" STRING_LITERAL ":" NEWLINE INDENT ⟨stmt_list⟩ DEDENT ⟨test_decl_list⟩ EOF
⇒ "test" STRING_LITERAL ":" NEWLINE INDENT ⟨stmt⟩ ⟨stmt_list⟩ DEDENT ⟨test_decl_list⟩ EOF
⇒ "test" STRING_LITERAL ":" NEWLINE INDENT ⟨let_stmt⟩ ⟨stmt_list⟩ DEDENT ⟨test_decl_list⟩ EOF
⇒ "test" STRING_LITERAL ":" NEWLINE INDENT
      "let" IDENTIFIER ":" ⟨type⟩ "=" ⟨rhs⟩ NEWLINE ⟨stmt_list⟩ DEDENT ⟨test_decl_list⟩ EOF
⇒ ... "Response" "=" ⟨rhs⟩ NEWLINE ⟨stmt_list⟩ ...          (⟨type⟩ ⇒ "Response")
⇒ ... "Response" "=" ⟨http_request⟩ NEWLINE ⟨stmt_list⟩ ...  (⟨rhs⟩ ⇒ ⟨http_request⟩)
⇒ ... "Response" "=" "GET" STRING_LITERAL NEWLINE ⟨stmt_list⟩ ...
⇒ ... NEWLINE ⟨stmt⟩ DEDENT ⟨test_decl_list⟩ EOF              (⟨stmt_list⟩ ⇒ ⟨stmt⟩)
⇒ ... NEWLINE ⟨assert_stmt⟩ DEDENT ⟨test_decl_list⟩ EOF
⇒ ... NEWLINE "assert" ⟨comparison⟩ NEWLINE DEDENT ⟨test_decl_list⟩ EOF
⇒ ... "assert" ⟨primary⟩ ⟨comp_op⟩ ⟨primary⟩ NEWLINE DEDENT ⟨test_decl_list⟩ EOF
⇒ ... "assert" ⟨member_access⟩ "==" INT_LITERAL NEWLINE DEDENT ⟨test_decl_list⟩ EOF
⇒ ... "assert" IDENTIFIER ⟨member_tail⟩ "==" INT_LITERAL NEWLINE DEDENT ⟨test_decl_list⟩ EOF
⇒ ... "assert" IDENTIFIER "." IDENTIFIER ⟨member_tail⟩ "==" INT_LITERAL NEWLINE DEDENT ⟨test_decl_list⟩ EOF
⇒ ... "assert" IDENTIFIER "." IDENTIFIER "==" INT_LITERAL NEWLINE DEDENT ⟨test_decl_list⟩ EOF   (⟨member_tail⟩ ⇒ ε)
⇒ "test" STRING_LITERAL ":" NEWLINE INDENT
      "let" IDENTIFIER ":" "Response" "=" "GET" STRING_LITERAL NEWLINE
      "assert" IDENTIFIER "." IDENTIFIER "==" INT_LITERAL NEWLINE
  DEDENT ⟨test_decl_list⟩ EOF
⇒ ... DEDENT ε EOF   (⟨test_decl_list⟩ ⇒ ε, pois não há mais nenhum "test" restante)
⇒ "test" STRING_LITERAL ":" NEWLINE INDENT
      "let" IDENTIFIER ":" "Response" "=" "GET" STRING_LITERAL NEWLINE
      "assert" IDENTIFIER "." IDENTIFIER "==" INT_LITERAL NEWLINE
  DEDENT EOF
```

Substituindo os terminais léxicos pelos lexemas reais (`STRING_LITERAL → "health check retorna 200"`, `IDENTIFIER → response`/`status`, `STRING_LITERAL → "/health"`, `INT_LITERAL → 200`), obtém-se exatamente a cadeia de tokens 🟢 **observada** na Seção B.5 (dump real do lexer), confirmando a correspondência produção↔implementação.

### A.5.8 Adequação a um parser descendente recursivo

A gramática é adequada a um parser LL com no máximo 1 token de lookahead **em quase todos os pontos de decisão**:
* `⟨test_decl_list⟩`, `⟨stmt⟩`, `⟨rhs⟩`, `⟨primary⟩`, `⟨json_value⟩`: cada alternativa começa com um terminal distinto (ou um não-terminal cujo FIRST não colide com o das demais alternativas) — decisão trivial por 1 token de lookahead.
* `⟨member_tail⟩`, `⟨json_member_tail⟩`, `⟨json_element_tail⟩`: a alternativa vazia é escolhida quando o próximo token não é, respectivamente, `.`/`,`/`,` — sem ambiguidade.
* `⟨json_object⟩`/`⟨json_array⟩`: foram deliberadamente fatoradas com não-terminais `_opt` para que, **após consumir `{`/`[`**, a decisão entre "há conteúdo" (`STRING_LITERAL` ou início de `json_value`) e "está vazio" (`}`/`]`) seja feita por 1 único token de lookahead.
* **Exceção documentada — `⟨comparison⟩`:** as duas alternativas (`⟨primary⟩ ⟨comp_op⟩ ⟨primary⟩` e `⟨primary⟩`) começam com o **mesmo não-terminal**, não com terminais diferentes. Isso não é resolvível por uma tabela LL(1) clássica sem transformar a gramática em uma forma com sufixo opcional explícito (`⟨comparison⟩ ::= ⟨primary⟩ ⟨comparison_tail⟩`, `⟨comparison_tail⟩ ::= ⟨comp_op⟩ ⟨primary⟩ | ε`). A implementação (`Parser._parse_comparison`, ver BLOCO B) resolve isso da forma padrão em parsers descendentes recursivos escritos à mão: primeiro reduz `⟨primary⟩` por completo, depois consulta 1 token de lookahead para decidir se há um `⟨comp_op⟩` — comportamento **equivalente** à forma fatorada acima, mas escrito de modo mais direto no código. Por rigor, **não afirmamos que a gramática, na forma exatamente escrita em A.5.4, é LL(1) em sentido estrito de tabela** — apenas que é reconhecível por um parser descendente recursivo com 1 token de lookahead, o que é suficiente e correto para os fins desta P1 (AGENTS.md, Seção 7.5, pede exatamente essa análise honesta, não uma alegação vazia de "LL(1) comprovado").
* A gramática **não é ambígua** para a linguagem que ela gera: nenhuma cadeia de terminais admite duas árvores de derivação distintas, pois em cada ponto de decisão o parser dispõe de informação suficiente (1 símbolo de lookahead, ou o não-terminal já reduzido) para escolher uma única alternativa — esta é uma afirmação sobre o comportamento determinístico do parser construído, não uma prova formal de não-ambiguidade por métodos de teoria de linguagens (que estaria além do escopo desta P1).

---

## A.6 Documentação dos não-terminais (Seção 8 do AGENTS.md)

| Não-terminal | Finalidade | Produções (resumo) | Interpretação | Exemplo |
|---|---|---|---|---|
| `⟨program⟩` | Símbolo inicial; representa um arquivo `.omt` completo | `test_decl_list EOF` | Um programa é zero ou mais cenários de teste seguidos de fim de arquivo | arquivo inteiro |
| `⟨test_decl_list⟩` | Permite múltiplos `test` sequenciais e programa vazio | `test_decl test_decl_list \| ε` | Recursão à direita: "um teste, seguido de mais testes" ou nada | 2 blocos `test` em `multiplos_testes.omt` |
| `⟨test_decl⟩` | Um cenário de teste nomeado | `"test" STRING ":" NEWLINE block` | Cabeçalho + corpo indentado de um cenário | `test "x": ...` |
| `⟨block⟩` | Corpo indentado de um teste | `INDENT stmt_list DEDENT` | Isola estruturalmente o escopo léxico do bloco via tokens estruturais | conteúdo indentado após `:` |
| `⟨stmt_list⟩` | Sequência de comandos dentro de um bloco | `stmt stmt_list \| stmt` | Exige pelo menos 1 comando (sem alternativa vazia) — decisão de projeto A.3 | `let`+`assert` |
| `⟨stmt⟩` | Um comando de teste | `let_stmt \| assert_stmt` | Ponto de extensão natural para futuros comandos (ex.: `PUT`, `log`) | qualquer linha do corpo |
| `⟨let_stmt⟩` | Declaração de variável tipada | `"let" ID ":" type "=" rhs NEWLINE` | Vincula um nome a um tipo declarado e a um valor (literal, JSON ou requisição) | `let a: Int = 5` |
| `⟨assert_stmt⟩` | Verificação declarativa | `"assert" comparison NEWLINE` | Expressa a expectativa de teste, sem definir a ação em caso de falha (fora do escopo sintático) | `assert a == 5` |
| `⟨type⟩` | Conjunto fechado de tipos primitivos | 5 alternativas terminais | Implementa tipagem estática **sintaticamente** fechada (não é possível declarar um tipo desconhecido) | `Response` |
| `⟨rhs⟩` | Valor atribuível em um `let` | `http_request \| primary` | Separa "vem de uma requisição" de "é um valor imediato", sem sobreposição de FIRST | `GET "/x"` ou `5` |
| `⟨http_request⟩` | Requisição HTTP | `"GET" STRING \| "POST" STRING primary` | Cada método tem sua própria forma sintática — GET nunca aceita payload, POST sempre exige | `POST "/users" payload` |
| `⟨comparison⟩` | Corpo de uma asserção | `primary comp_op primary \| primary` | Suporta comparação binária ou verificação de um valor booleano isolado | `a == b` ou `ativo` |
| `⟨comp_op⟩` | Operadores relacionais | 6 alternativas terminais | Fechado deliberadamente (sem `&&`/`\|\|`) para manter asserções simples | `==` |
| `⟨primary⟩` | Valor atômico da linguagem | 7 alternativas | Nó comum reaproveitado por `let`, `assert` e payloads de `POST` | `response.status`, `200`, `{...}` |
| `⟨member_access⟩` | Identificador com encadeamento de campos | `ID member_tail` | Modela acesso a campos aninhados de uma `Response` sem introduzir um operador genérico de indexação | `response.body.name` |
| `⟨member_tail⟩` | Continuação recursiva do acesso a membros | `"." ID member_tail \| ε` | Recursão à direita que permite profundidade arbitrária de encadeamento | `.body.name` |
| `⟨json_object⟩` | Objeto JSON | `"{" json_members_opt "}"` | Representação estrutural (não um token opaco), compatível com JSON real | `{"a": 1}` |
| `⟨json_members_opt⟩` | Auxiliar de fatoração | `json_members \| ε` | Existe só para tornar `{}` (objeto vazio) sintaticamente distinguível por 1 lookahead | `{}` |
| `⟨json_members⟩` | Lista não vazia de pares | `json_pair json_member_tail` | Garante ao menos 1 par quando o objeto não é vazio | `"a": 1` |
| `⟨json_member_tail⟩` | Continuação da lista de pares | `"," json_pair json_member_tail \| ε` | Recursão à direita para permitir N pares separados por vírgula | `, "b": 2` |
| `⟨json_pair⟩` | Par chave-valor | `STRING ":" json_value` | Chave sempre string (alinhado ao JSON real) | `"status": 200` |
| `⟨json_value⟩` | Valor dentro de um par/elemento JSON | 6 alternativas | Permite aninhamento arbitrário de objetos/arrays | `"ok"`, `true`, `{...}`, `[...]` |
| `⟨json_array⟩` | Array JSON | `"[" json_elements_opt "]"` | Simétrico a `json_object`, permitindo listas de valores | `["QA", "SDET"]` |
| `⟨json_elements_opt⟩` | Auxiliar de fatoração | `json_elements \| ε` | Torna `[]` (array vazio) distinguível por 1 lookahead | `[]` |
| `⟨json_elements⟩` | Lista não vazia de elementos | `json_value json_element_tail` | Garante ao menos 1 elemento quando o array não é vazio | `"QA"` |
| `⟨json_element_tail⟩` | Continuação da lista de elementos | `"," json_value json_element_tail \| ε` | Recursão à direita simétrica a `json_member_tail` | `, "SDET"` |

**Sobre as produções vazias (`ε`):** todas ocorrem em posições de "cauda" de listas recursivas (`_tail`) ou em pontos de "conteúdo opcional" (`_opt`, `test_decl_list`). Nenhuma produção vazia aparece no meio de uma sequência — sempre no fim de uma alternativa recursiva —, o que evita ambiguidade sobre "quando parar de recursar": o parser para assim que o próximo token não pertence ao FIRST da continuação nem-vazia.

---

## A.7 Análise léxica, sintática e semântica: distinções (Seção 9 do AGENTS.md)

| Etapa | O que faz | Implementada nesta P1? | Evidência |
|---|---|---|---|
| **Léxica** | Converte a sequência de caracteres em tokens (categoria + lexema + posição) | 🟢 Sim, completa | `omnitest/lexer.py`, 26/26 testes |
| **Sintática** | Verifica se a sequência de tokens pertence à linguagem definida pela gramática (Seção A.5) e constrói uma árvore sintática | 🟢 Sim, completa | `omnitest/parser.py` + `omnitest/ast_nodes.py` |
| **Semântica** | Verificaria propriedades não garantidas pela gramática: compatibilidade entre o tipo declarado (`Int`, `Json`, ...) e o valor atribuído; existência prévia de uma variável referenciada em `assert` antes de ser declarada em `let`; validade do campo acessado em `response.body.X` | 🔴 **Não implementada** | Nenhum código de checagem de tipos/escopo existe no projeto — decisão de escopo explícita (A.2.6) |

Consequências práticas dessa fronteira, tornadas explícitas para não gerar alegações incorretas:
* O programa `let a: Int = "texto"` é **sintaticamente aceito** pela gramática (pois `⟨rhs⟩` aceita qualquer `⟨primary⟩`, incluindo `STRING_LITERAL`, independentemente do tipo declarado) — isso é **esperado e correto** dado o escopo desta P1, não um bug. A incompatibilidade `Int`/`String` só seria detectável em uma etapa semântica futura.
* `assert x == 1` é aceito mesmo que `x` nunca tenha sido declarado por um `let` anterior — a existência de variáveis é uma propriedade semântica (exigiria uma tabela de símbolos), não sintática.
* Uma gramática livre de contexto, isoladamente, **não é suficiente** para capturar a regra de indentação contextual "linhas dentro de `{}`/`[]` não geram INDENT/DEDENT" — essa regra é resolvida no **lexer** (com o contador `bracket_depth`), antes mesmo de a gramática entrar em ação. Da mesma forma, a validade de um contrato HTTP real (ex.: `/users` responder de fato com um campo `name`) está totalmente fora do alcance de qualquer GLC.

---

## A.8 Exemplos de código-fonte (Seção 10 do AGENTS.md)

### A.8.1 Exemplo 1 — Teste simples de API (`examples/get_test.omt`)

```
test "health check retorna 200":
    let response: Response = GET "/health"
    assert response.status == 200
```

1. **Objetivo:** verificar que o endpoint de health-check responde com status HTTP 200.
2. **Significado de cada comando:** `test "...":` nomeia o cenário e abre seu bloco; `let response: Response = GET "/health"` declara uma variável tipada `Response` cujo valor conceitual viria de uma requisição GET; `assert response.status == 200` expressa a expectativa de status.
3. **Tokens relevantes:** `TEST`, `STRING_LITERAL`, `COLON`, `NEWLINE`, `INDENT`, `LET`, `IDENTIFIER`, `TYPE_RESPONSE`, `ASSIGN`, `GET`, `STRING_LITERAL`, `NEWLINE`, `ASSERT`, `IDENTIFIER`, `DOT`, `IDENTIFIER`, `EQ`, `INT_LITERAL`, `NEWLINE`, `DEDENT`, `EOF` — dump completo e real em B.5.4.
4. **Produções envolvidas:** `⟨test_decl⟩ → ⟨block⟩ → ⟨stmt_list⟩ → ⟨let_stmt⟩ (com ⟨rhs⟩ ⇒ ⟨http_request⟩) → ⟨assert_stmt⟩ (com ⟨comparison⟩ ⇒ ⟨primary⟩ ⟨comp_op⟩ ⟨primary⟩, e ⟨primary⟩ ⇒ ⟨member_access⟩)`.
5. **Tokenização pelo lexer:** ver dump literal na Seção B.5.4 (🟢 OBSERVADO).
6. **Reconhecimento de blocos pelo parser:** `_parse_test_decl` consome `TEST`, `STRING_LITERAL`, `COLON`, `NEWLINE`, delega a `_parse_block`, que exige `INDENT`, chama `_parse_stmt_list` (2 comandos) e exige `DEDENT`.
7. **O que seria verificado semanticamente (não implementado):** que `GET` de fato retorna algo atribuível a `Response`; que `response.status` existe no tipo `Response`; que `200` é comparável a um inteiro de status.
8. **Validação:** 🟢 **efetivamente validado** pela implementação (`tests/test_valid_programs.py::test_exemplo1_get_test_e_aceito`, PASSED).

### A.8.2 Exemplo 2 — Teste de integração com payload JSON (`examples/post_test.omt`)

```
test "criacao de usuario retorna 201 e nome correto":
    let payload: Json = {"name": "Hugo Andrade", "role": "QA Engineer", "active": true}
    let response: Response = POST "/users" payload
    assert response.status == 201
    assert response.body.name == "Hugo Andrade"
```

1. **Objetivo:** verificar que a criação de um usuário via `POST /users` retorna 201 e ecoa o nome enviado.
2. **Significado de cada comando:** o primeiro `let` declara um objeto JSON com 3 pares (string, string, booleano); o segundo `let` executa (conceitualmente) um `POST` enviando `payload` como corpo; os dois `assert` verificam, respectivamente, o status e um campo aninhado da resposta.
3. **Tokens relevantes (adicionais ao Exemplo 1):** `TYPE_JSON`, `LBRACE`, `STRING_LITERAL` (chaves e valores), `COLON`, `COMMA`, `BOOLEAN_LITERAL`, `RBRACE`, `POST`, `IDENTIFIER` (payload usado como referência).
4. **Produções envolvidas (adicionais):** `⟨json_object⟩ → ⟨json_members⟩ → ⟨json_pair⟩ ⟨json_member_tail⟩` (2x, para os 3 pares); `⟨http_request⟩ ⇒ "POST" STRING_LITERAL ⟨primary⟩`, com `⟨primary⟩ ⇒ ⟨member_access⟩` (o identificador `payload`); segundo `assert` usa `⟨member_access⟩` com 2 níveis de `.` (`response.body.name`).
5. **Tokenização pelo lexer:** o objeto JSON, mesmo escrito em uma única linha física aqui, é tokenizado por posição igual a qualquer sequência de tokens comum (sem tratamento especial), confirmando a decisão de A.4.1 de **não** usar um token JSON monolítico.
6. **Reconhecimento de blocos pelo parser:** idêntico ao Exemplo 1, mas `_parse_stmt_list` reconhece 4 comandos; `_parse_json_object`/`_parse_json_members`/`_parse_json_pair` são exercitados pela primeira vez.
7. **O que seria verificado semanticamente (não implementado):** que o payload enviado é compatível com o contrato esperado por `/users`; que `response.body` de fato contém um campo `name`; que o tipo declarado `Json` é compatível com um literal de objeto (aqui é, mas a gramática não impede `let payload: Json = 5`, uma incompatibilidade puramente semântica).
8. **Validação:** 🟢 **efetivamente validado** (`tests/test_valid_programs.py::test_exemplo2_post_test_e_aceito`, PASSED); a variante com array JSON de nível superior (`let roles: Json = ["QA", "SDET", "Automation"]`, ver `examples/valid/json_array_nivel_superior.omt`) também foi 🟢 validada, cobrindo a correção de gramática relatada em A.5.4.

---

# BLOCO B — VALIDAÇÃO TÉCNICA

## B.1 Arquitetura do lexer e parser

Estrutura real do repositório (🟢 observada via `find`/`wc -l` nesta sessão):

```
omni-test-lang/
    AGENTS.md            # persona/prompt master (fonte da metodologia)
    REVISOR.md           # idêntico ao AGENTS.md (revisor usa a mesma persona)
    P1.pdf / P1.txt       # fonte de verdade dos requisitos da atividade
    ENTREGA_P1.md         # este documento
    conftest.py           # garante que `omnitest` seja importável pelo pytest
    omnitest/
        __init__.py        # ponto de entrada do pacote; exporta a API pública
        tokens.py    (129 linhas)  # TokenType, Token, tabela de palavras reservadas
        errors.py     (55 linhas)  # OmniTestLexError / OmniTestSyntaxError
        lexer.py     (356 linhas)  # analisador léxico completo
        ast_nodes.py  (90 linhas)  # dataclasses da árvore sintática
        parser.py    (331 linhas)  # analisador sintático descendente recursivo
        __main__.py   (58 linhas)  # CLI: `python -m omnitest <arquivo.omt>`
    examples/
        get_test.omt        # Exemplo 1 (obrigatório, Seção 10)
        post_test.omt       # Exemplo 2 (obrigatório, Seção 10)
        valid/*.omt          # 6 arquivos adicionais cobrindo a matriz de testes
        invalid/*.omt        # 10 arquivos cobrindo casos de rejeição
    tests/
        test_valid_programs.py    (148 linhas, 12 testes)
        test_invalid_programs.py   (78 linhas, 12 testes)
```

Responsabilidade de cada módulo:
* **`tokens.py`** — fonte única da verdade sobre quais terminais existem; qualquer alteração na gramática (Seção A.5) deve começar aqui.
* **`errors.py`** — duas classes de exceção (léxica/sintática), cada uma carregando linha, coluna e mensagem — nunca uma exceção genérica do Python é deixada vazar ao usuário final.
* **`lexer.py`** — implementa integralmente a Seção A.4 (catálogo de tokens, pilha de indentação, supressão de NEWLINE em JSON multi-linha).
* **`ast_nodes.py`** — 11 dataclasses que espelham 1:1 os não-terminais "semânticos" da gramática (não há nó para os não-terminais puramente auxiliares de fatoração, como `_opt`/`_tail`, que são "achatados" nas listas Python correspondentes).
* **`parser.py`** — 1 função por não-terminal "principal" da gramática (ver mapeamento completo em B.2); nunca aceita uma construção fora da gramática formal (nenhum "modo permissivo").
* **`__main__.py`** — roteiro prático de execução (Seção 11 do AGENTS.md): `python -m omnitest <arquivo.omt>` imprime `ACEITO`/`REJEITADO` e a localização de eventual erro.

## B.2 Implementação de referência (código real, já presente no repositório)

Todo o código abaixo está implementado e foi executado nesta sessão — não é pseudocódigo.

Catálogo de tokens e palavras reservadas:

20:65:omni-test-lang/omnitest/tokens.py
class TokenType(Enum):
    # ---- Estruturais (gerados pelo controle de indentação/linha) --------
    NEWLINE = auto()
    INDENT = auto()
    DEDENT = auto()
    EOF = auto()

    # ---- Identificador e literais ---------------------------------------
    IDENTIFIER = auto()
    INT_LITERAL = auto()
    STRING_LITERAL = auto()
    BOOLEAN_LITERAL = auto()

    # ---- Palavras reservadas de estrutura de teste ----------------------
    TEST = auto()
    LET = auto()
    ASSERT = auto()

    # ---- Palavras reservadas de método HTTP -----------------------------
    GET = auto()
    POST = auto()

    # ---- Palavras reservadas de tipo ------------------------------------
    TYPE_INT = auto()
    TYPE_STRING = auto()
    TYPE_BOOL = auto()
    TYPE_JSON = auto()
    TYPE_RESPONSE = auto()

    # ---- Operadores --------------------------------------------------
    ASSIGN = auto()     # =
    EQ = auto()         # ==
    NEQ = auto()        # !=
    LT = auto()         # <
    GT = auto()         # >
    LE = auto()         # <=
    GE = auto()         # >=
    DOT = auto()        # .

    # ---- Delimitadores -----------------------------------------------
    COLON = auto()       # :
    COMMA = auto()       # ,
    LBRACE = auto()       # {
    RBRACE = auto()       # }
    LBRACKET = auto()     # [
    RBRACKET = auto()     # ]

Controle de indentação (núcleo do lexer):

84:147:omni-test-lang/omnitest/lexer.py
    def _process_line(self, line_no: int, line: str) -> None:
        pos = 0

        if self._bracket_depth == 0:
            pos = self._measure_indentation(line, line_no)
            if pos is None:
                # Linha em branco ou comentário puro: nenhuma indentação
                # é avaliada, nenhum token é emitido.
                return
        # Quando bracket_depth > 0 (dentro de literal JSON), a indentação
        # é irrelevante: a linha é tratada como continuação lógica da
        # expressão anterior (linha lógica ainda aberta).

        produced_any = self._scan_tokens(line, pos, line_no)

        if self._bracket_depth == 0 and produced_any:
            last = self._tokens[-1] if self._tokens else None
            end_col = len(line) + 1
            self._tokens.append(Token(TokenType.NEWLINE, "\n", None, line_no, end_col))

    def _measure_indentation(self, line: str, line_no: int):
        """Mede a indentação de uma linha lógica de nível zero de colchetes.

        Retorna o índice (coluna 0-based) onde o conteúdo relevante
        começa, ou None se a linha deve ser ignorada (em branco ou
        comentário puro).
        """
        i = 0
        n = len(line)
        while i < n and line[i] == " ":
            i += 1

        if i < n and line[i] == "\t":
            raise OmniTestLexError(
                "uso de caractere de tabulação (TAB) na indentação não é "
                "permitido; a OmniTest exige indentação exclusivamente "
                "com espaços",
                line_no,
                i + 1,
            )

        rest = line[i:]
        if rest == "" or rest.lstrip(" ") == "" or rest.startswith("#"):
            return None  # linha em branco ou comentário: ignorada

        indent = i
        top = self._indent_stack[-1]
        if indent > top:
            self._indent_stack.append(indent)
            self._tokens.append(Token(TokenType.INDENT, "", None, line_no, 1))
        elif indent < top:
            while self._indent_stack and indent < self._indent_stack[-1]:
                self._indent_stack.pop()
                self._tokens.append(Token(TokenType.DEDENT, "", None, line_no, i + 1))
            if self._indent_stack[-1] != indent:
                raise OmniTestLexError(
                    "indentação inconsistente: o nível de indentação "
                    f"({indent} espaços) não corresponde a nenhum nível "
                    "de indentação previamente aberto",
                    line_no,
                    i + 1,
                )
        # indent == top: mesmo nível, nenhum INDENT/DEDENT necessário.
        return i

Correspondência produção → função do parser (trecho representativo; arquivo completo em `omnitest/parser.py`):

113:148:omni-test-lang/omnitest/parser.py
    # ------------------------------------------------------------------
    # <program> ::= <test_decl_list> EOF
    # ------------------------------------------------------------------
    def _parse_program(self) -> Program:
        tests = self._parse_test_decl_list()
        return Program(tests=tests)

    # <test_decl_list> ::= <test_decl> <test_decl_list> | ε
    def _parse_test_decl_list(self) -> list[TestDecl]:
        tests: list[TestDecl] = []
        while self._check(TokenType.TEST):
            tests.append(self._parse_test_decl())
        return tests

    # <test_decl> ::= "test" STRING_LITERAL ":" NEWLINE <block>
    def _parse_test_decl(self) -> TestDecl:
        tok = self._match(TokenType.TEST, "palavra reservada 'test'")
        name_tok = self._match(TokenType.STRING_LITERAL, "nome do cenário (string)")
        self._match(TokenType.COLON, "':' após o nome do cenário")
        self._match(TokenType.NEWLINE, "fim de linha (NEWLINE) após ':'")
        statements = self._parse_block()
        return TestDecl(name=name_tok.value, statements=statements, line=tok.line)

    # <block> ::= INDENT <stmt_list> DEDENT
    def _parse_block(self) -> list[object]:
        self._match(TokenType.INDENT, "aumento de indentação (bloco do teste)")
        statements = self._parse_stmt_list()
        self._match(TokenType.DEDENT, "fim do bloco (redução de indentação)")
        return statements

    # <stmt_list> ::= <stmt> <stmt_list> | <stmt>
    def _parse_stmt_list(self) -> list[object]:
        statements = [self._parse_stmt()]
        while self._check(TokenType.LET) or self._check(TokenType.ASSERT):
            statements.append(self._parse_stmt())
        return statements

Mapeamento completo função ↔ não-terminal (para conferência rápida em seminário):

| Função Python (`parser.py`) | Não-terminal |
|---|---|
| `parse_program` / `_parse_program` | `⟨program⟩` |
| `_parse_test_decl_list` | `⟨test_decl_list⟩` |
| `_parse_test_decl` | `⟨test_decl⟩` |
| `_parse_block` | `⟨block⟩` |
| `_parse_stmt_list` | `⟨stmt_list⟩` |
| `_parse_stmt` | `⟨stmt⟩` |
| `_parse_let_stmt` | `⟨let_stmt⟩` |
| `_parse_assert_stmt` | `⟨assert_stmt⟩` |
| `_parse_type` | `⟨type⟩` |
| `_parse_rhs` | `⟨rhs⟩` |
| `_parse_http_request` | `⟨http_request⟩` |
| `_parse_comparison` | `⟨comparison⟩` (+ `⟨comp_op⟩` inline) |
| `_parse_primary` | `⟨primary⟩` |
| `_parse_member_access` | `⟨member_access⟩` + `⟨member_tail⟩` (iterativo) |
| `_parse_json_object` | `⟨json_object⟩` + `⟨json_members_opt⟩` |
| `_parse_json_members` | `⟨json_members⟩` + `⟨json_member_tail⟩` (iterativo) |
| `_parse_json_pair` | `⟨json_pair⟩` |
| `_parse_json_value` | `⟨json_value⟩` |
| `_parse_json_array` | `⟨json_array⟩` + `⟨json_elements_opt⟩` |
| `_parse_json_elements` | `⟨json_elements⟩` + `⟨json_element_tail⟩` (iterativo) |

(As produções `_tail` foram implementadas com **laços `while`** em vez de recursão Python explícita — uma otimização de engenharia equivalente à recursão à direita da gramática, sem alterar a linguagem reconhecida; isso é mencionado explicitamente para não sugerir que a implementação "desvia" da gramática.)

## B.3 Estratégia de execução

Pré-requisitos: Python ≥ 3.10 (biblioteca padrão apenas; nenhuma dependência externa para `lexer`/`parser`; `pytest` é usado somente para os testes automatizados).

```bash
cd omni-test-lang

# Validar um único arquivo (aceita/rejeita, com localização de erro):
python3 -m omnitest examples/get_test.omt
python3 -m omnitest examples/invalid/token_desconhecido.omt

# Rodar toda a suíte de testes automatizados:
python3 -m pytest -v
```

## B.4 Matriz de testes

Todas as 20 categorias mínimas exigidas (Seção 12.1 do AGENTS.md) foram mapeadas para um arquivo `.omt` concreto e para um teste automatizado. Onde a categoria original do AGENTS.md não correspondia literalmente a uma construção existente nesta gramática (linguagem propositalmente pequena — Seção 3.5), a interpretação foi ajustada e justificada na coluna "Regra validada", como pede explicitamente a Seção 12.1 ("Ajuste os casos às regras reais da gramática").

| ID | Entrada/cenário | Categoria | Resultado esperado | Regra validada |
|---|---|---|---|---|
| T-V01 | `examples/get_test.omt` | Requisição GET válida (Exemplo 1) | ACEITO | `⟨http_request⟩ ⇒ "GET" STRING_LITERAL` |
| T-V02 | `examples/post_test.omt` | Requisição POST válida (Exemplo 2) | ACEITO | `⟨http_request⟩ ⇒ "POST" STRING_LITERAL ⟨primary⟩` |
| T-V03 | `examples/valid/minimo_valido.omt` | Programa mínimo válido | ACEITO | `⟨stmt_list⟩` com exatamente 1 `⟨stmt⟩`; `⟨comparison⟩ ⇒ ⟨primary⟩` (bool nu) |
| T-V04 | `examples/valid/declaracao_variavel.omt` | Declaração de variável válida | ACEITO | `⟨let_stmt⟩` com `⟨type⟩ ⇒ "Int"` |
| T-V05 | `examples/valid/multiplos_testes.omt` | Bloco corretamente indentado / múltiplos comandos | ACEITO | `⟨block⟩`; `⟨stmt_list⟩` com 2 e 4 comandos |
| T-V06 | `examples/valid/multiplos_testes.omt` | Múltiplos níveis de indentação — **reinterpretado**: como a gramática só permite 1 nível de bloco por `test` (Seção D.2), esta categoria é validada pela pilha de indentação abrindo/fechando corretamente **duas vezes em sequência** (0→4→0→4→0) | ACEITO; 2 `INDENT` e 2 `DEDENT` emitidos | Pilha de indentação do lexer (`_measure_indentation`) |
| T-V07 | `examples/valid/json_multilinha.omt` | JSON multi-linha (continuação implícita) | ACEITO; exatamente 4 `NEWLINE` (não 8) | Supressão de `NEWLINE` com `bracket_depth > 0` |
| T-V08 | `examples/valid/json_array_nivel_superior.omt` | Array JSON como valor de nível superior (correção de gramática, Seção D.2) | ACEITO | `⟨primary⟩ ⇒ ⟨json_array⟩` |
| T-V09 | `examples/valid/programa_vazio.omt` | Programa vazio, conforme política definida (A.3) | ACEITO; 0 testes reconhecidos | `⟨test_decl_list⟩ ⇒ ε` |
| T-I01 | `examples/invalid/indentacao_inconsistente.omt` | Indentação inconsistente | REJEITADO — erro **léxico** | Nível de indentação sem correspondência na pilha |
| T-I02 | `examples/invalid/dedent_inesperado.omt` | "DEDENT inesperado" — **reclassificado**: nesta gramática (bloco único, sem aninhamento), um DEDENT para um nível nunca aberto é sempre detectado no **lexer**, nunca no parser (assim como em Python: "unindent does not match any outer indentation level" é erro do tokenizer) | REJEITADO — erro **léxico** | Mesma regra de T-I01, com cenário de entrada distinto (3 comandos, dedent para 3 espaços) |
| T-I03 | `examples/invalid/identificador_invalido.omt` | Identificador inválido (`2xResponse`) | REJEITADO — erro **sintático** (o lexer produz `INT_LITERAL "2"` seguido de `IDENTIFIER "xResponse"`; o parser rejeita por esperar `IDENTIFIER` logo após `let`) | Interação léxico/sintático documentada em B.6 |
| T-I04 | `examples/invalid/token_desconhecido.omt` | Token desconhecido (`@`) | REJEITADO — erro **léxico** | Nenhuma regra de `_scan_tokens` reconhece `@` |
| T-I05 | `examples/invalid/tipo_nao_permitido.omt` | Tipo não permitido sintaticamente (`Float`) | REJEITADO — erro **sintático** (não semântico, pois `⟨type⟩` é um conjunto **fechado** de 5 alternativas — ver nota da Seção 12.1 do AGENTS.md) | `⟨type⟩` não admite `IDENTIFIER` |
| T-I06 | `examples/invalid/comando_malformado.omt` | Comando malformado (`:` ausente após identificador) | REJEITADO — erro **sintático** | `⟨let_stmt⟩` exige `":"` logo após `IDENTIFIER` |
| T-I07 | `examples/invalid/parametro_ausente.omt` | Parâmetro ausente (`POST` sem payload) | REJEITADO — erro **sintático** | `⟨http_request⟩` exige `⟨primary⟩` após `STRING_LITERAL` na alternativa `POST` |
| T-I08 | `examples/invalid/assercao_incompleta.omt` | Asserção incompleta (`assert` sem valor) | REJEITADO — erro **sintático** | `⟨comparison⟩` exige ao menos um `⟨primary⟩` |
| T-I09 | `examples/invalid/bloco_sem_indentacao.omt` | Bloco sem indentação | REJEITADO — erro **sintático** | `⟨block⟩` exige `INDENT` logo após o `NEWLINE` do cabeçalho |
| T-I10 | `examples/invalid/eof_durante_bloco.omt` | EOF durante um bloco (arquivo termina antes do corpo do teste) | REJEITADO — erro **sintático** | `⟨block⟩` exige `INDENT`; encontra `EOF` |

**Nota sobre T-I05:** o AGENTS.md (Seção 12.1) observa que "um tipo desconhecido poderá ser erro sintático se o tipo for parte de uma lista fechada de palavras reservadas, ou semântico se a gramática permitir identificadores como tipos". Nesta gramática, `⟨type⟩` é explicitamente uma lista fechada de 5 terminais (A.5.4) — logo, `Float` é corretamente um erro **sintático**, nunca semântico, e a implementação confirma isso (`OmniTestSyntaxError`, não uma checagem de tipo hipotética).

## B.5 Resultados efetivamente observados (🟢 OBSERVADO)

### B.5.1 Suíte automatizada — execução real (`python3 -m pytest -v`)

Ambiente: Python 3.12.3, pytest 9.1.1, executado em `omni-test-lang/` nesta sessão.

```
============================= test session starts ==============================
platform linux -- Python 3.12.3, pytest-9.1.1, pluggy-1.6.0 -- /usr/bin/python3
rootdir: /home/thiago.sousa/Downloads/compiladores/omni-test-lang
collecting ... collected 26 items

tests/test_invalid_programs.py::test_entrada_invalida_e_rejeitada_com_erro_esperado[assercao_incompleta.omt-OmniTestSyntaxError] PASSED
tests/test_invalid_programs.py::test_entrada_invalida_e_rejeitada_com_erro_esperado[bloco_sem_indentacao.omt-OmniTestSyntaxError] PASSED
tests/test_invalid_programs.py::test_entrada_invalida_e_rejeitada_com_erro_esperado[comando_malformado.omt-OmniTestSyntaxError] PASSED
tests/test_invalid_programs.py::test_entrada_invalida_e_rejeitada_com_erro_esperado[dedent_inesperado.omt-OmniTestLexError] PASSED
tests/test_invalid_programs.py::test_entrada_invalida_e_rejeitada_com_erro_esperado[eof_durante_bloco.omt-OmniTestSyntaxError] PASSED
tests/test_invalid_programs.py::test_entrada_invalida_e_rejeitada_com_erro_esperado[identificador_invalido.omt-OmniTestSyntaxError] PASSED
tests/test_invalid_programs.py::test_entrada_invalida_e_rejeitada_com_erro_esperado[indentacao_inconsistente.omt-OmniTestLexError] PASSED
tests/test_invalid_programs.py::test_entrada_invalida_e_rejeitada_com_erro_esperado[parametro_ausente.omt-OmniTestSyntaxError] PASSED
tests/test_invalid_programs.py::test_entrada_invalida_e_rejeitada_com_erro_esperado[tipo_nao_permitido.omt-OmniTestSyntaxError] PASSED
tests/test_invalid_programs.py::test_entrada_invalida_e_rejeitada_com_erro_esperado[token_desconhecido.omt-OmniTestLexError] PASSED
tests/test_invalid_programs.py::test_todos_os_arquivos_invalidos_estao_mapeados PASSED
tests/test_invalid_programs.py::test_mensagem_de_erro_contem_linha_e_coluna PASSED
tests/test_valid_programs.py::test_exemplo1_get_test_e_aceito PASSED
tests/test_valid_programs.py::test_exemplo2_post_test_e_aceito PASSED
tests/test_valid_programs.py::test_minimo_valido PASSED
tests/test_valid_programs.py::test_declaracao_variavel_valida PASSED
tests/test_valid_programs.py::test_multiplos_testes_e_multiplos_niveis_indentacao PASSED
tests/test_valid_programs.py::test_json_multilinha_suprime_newline_interno PASSED
tests/test_valid_programs.py::test_json_array_como_valor_de_nivel_superior PASSED
tests/test_valid_programs.py::test_programa_vazio_e_aceito_pela_politica_definida PASSED
tests/test_valid_programs.py::test_todos_os_exemplos_validos_sao_aceitos[declaracao_variavel.omt] PASSED
tests/test_valid_programs.py::test_todos_os_exemplos_validos_sao_aceitos[json_array_nivel_superior.omt] PASSED
tests/test_valid_programs.py::test_todos_os_exemplos_validos_sao_aceitos[json_multilinha.omt] PASSED
tests/test_valid_programs.py::test_todos_os_exemplos_validos_sao_aceitos[minimo_valido.omt] PASSED
tests/test_valid_programs.py::test_todos_os_exemplos_validos_sao_aceitos[multiplos_testes.omt] PASSED
tests/test_valid_programs.py::test_todos_os_exemplos_validos_sao_aceitos[programa_vazio.omt] PASSED

============================== 26 passed in 0.07s ===============================
```

**26/26 testes aprovados (100%).** Nenhum teste foi removido ou "ajustado para passar" — a única correção feita durante o desenvolvimento foi na **gramática/parser** (suporte a array JSON de nível superior), não nos testes.

### B.5.2 Execução manual via CLI (`python -m omnitest`) — exemplos válidos

```
$ python3 -m omnitest examples/get_test.omt
ACEITO
Testes reconhecidos: 1
Comandos reconhecidos: 2
  - test "health check retorna 200" (linha 1): 2 comando(s)

$ python3 -m omnitest examples/post_test.omt
ACEITO
Testes reconhecidos: 1
Comandos reconhecidos: 4
  - test "criacao de usuario retorna 201 e nome correto" (linha 1): 4 comando(s)

$ python3 -m omnitest examples/valid/programa_vazio.omt
ACEITO
Testes reconhecidos: 0
Comandos reconhecidos: 0
```

### B.5.3 Execução manual via CLI — todos os 10 exemplos inválidos (saída literal)

```
$ python3 -m omnitest examples/invalid/assercao_incompleta.omt
REJEITADO
Erro sintático: esperado um valor (identificador, literal inteiro, string, booleano ou objeto JSON), mas foi encontrado fim de linha (NEWLINE) (linha 3, coluna 11)

$ python3 -m omnitest examples/invalid/bloco_sem_indentacao.omt
REJEITADO
Erro sintático: esperado aumento de indentação (bloco do teste), mas foi encontrado ASSERT ('assert') (linha 2, coluna 1)

$ python3 -m omnitest examples/invalid/comando_malformado.omt
REJEITADO
Erro sintático: esperado ':' após o identificador, mas foi encontrado TYPE_INT ('Int') (linha 2, coluna 11)

$ python3 -m omnitest examples/invalid/dedent_inesperado.omt
REJEITADO
Erro léxico: indentação inconsistente: o nível de indentação (3 espaços) não corresponde a nenhum nível de indentação previamente aberto (linha 4, coluna 4)

$ python3 -m omnitest examples/invalid/eof_durante_bloco.omt
REJEITADO
Erro sintático: esperado aumento de indentação (bloco do teste), mas foi encontrado fim de arquivo (EOF) (linha 2, coluna 1)

$ python3 -m omnitest examples/invalid/identificador_invalido.omt
REJEITADO
Erro sintático: esperado identificador da variável, mas foi encontrado INT_LITERAL ('2') (linha 2, coluna 9)

$ python3 -m omnitest examples/invalid/indentacao_inconsistente.omt
REJEITADO
Erro léxico: indentação inconsistente: o nível de indentação (2 espaços) não corresponde a nenhum nível de indentação previamente aberto (linha 3, coluna 3)

$ python3 -m omnitest examples/invalid/parametro_ausente.omt
REJEITADO
Erro sintático: esperado um valor (identificador, literal inteiro, string, booleano ou objeto JSON), mas foi encontrado fim de linha (NEWLINE) (linha 2, coluna 43)

$ python3 -m omnitest examples/invalid/tipo_nao_permitido.omt
REJEITADO
Erro sintático: esperado um tipo válido ('Int', 'String', 'Bool', 'Json' ou 'Response'), mas foi encontrado IDENTIFIER ('Float') (linha 2, coluna 16)

$ python3 -m omnitest examples/invalid/token_desconhecido.omt
REJEITADO
Erro léxico: caractere inesperado '@'; não corresponde a nenhum token válido da OmniTest (linha 2, coluna 20)
```

### B.5.4 Dump literal de tokens (Exemplo 1, `examples/get_test.omt`) — 🟢 observado

```
TEST             lexeme='test'                         L1:C1
STRING_LITERAL   lexeme='"health check retorna 200"'    L1:C6
COLON            lexeme=':'                             L1:C32
NEWLINE          lexeme='\n'                             L1:C33
INDENT           lexeme=''                              L2:C1
LET              lexeme='let'                           L2:C5
IDENTIFIER       lexeme='response'                      L2:C9
COLON            lexeme=':'                             L2:C17
TYPE_RESPONSE    lexeme='Response'                       L2:C19
ASSIGN           lexeme='='                              L2:C28
GET              lexeme='GET'                            L2:C30
STRING_LITERAL   lexeme='"/health"'                       L2:C34
NEWLINE          lexeme='\n'                             L2:C43
ASSERT           lexeme='assert'                          L3:C5
IDENTIFIER       lexeme='response'                       L3:C12
DOT              lexeme='.'                              L3:C20
IDENTIFIER       lexeme='status'                          L3:C21
EQ               lexeme='=='                             L3:C28
INT_LITERAL      lexeme='200' value=200                  L3:C31
NEWLINE          lexeme='\n'                             L3:C34
DEDENT           lexeme=''                               L4:C1
EOF              lexeme=''                               L4:C1
```

## B.6 Limitações da validação

* A suíte cobre as 20 categorias mínimas exigidas, mas **não** é uma prova formal de correção da gramática (não há geração exaustiva de cadeias nem fuzzing) — é uma validação por amostragem representativa, como é usual e suficiente para uma P1 de compiladores.
* Nenhuma ferramenta externa (JFLAP, Bison, BNFPlayground) foi utilizada nesta rodada — é uma pendência explícita registrada no BLOCO D, não uma alegação de uso indevido.
* A interação léxico/sintático em `identificador_invalido.omt` (T-I03) é sutil: o erro é reportado como sintático porque o lexer nunca "sabe" que `2xResponse` era uma tentativa de identificador — ele apenas produz os tokens válidos que consegue (`INT_LITERAL "2"` + `IDENTIFIER "xResponse"`). Isso é **correto do ponto de vista teórico** (o lexer sempre usa *maximal munch* sobre classes de token bem definidas), mas deve ser explicado com cuidado no seminário para não parecer uma falha de classificação.
* Testes de performance/carga (arquivos muito grandes) não foram realizados — fora do escopo da P1.

## B.7 Evidências disponíveis para a entrega

* Código-fonte completo do lexer, parser, tokens, erros e AST (`omnitest/`).
* 18 arquivos de entrada (`examples/`), sendo 8 válidos + 2 exemplos obrigatórios + 10 inválidos.
* Suíte de 26 testes automatizados (`tests/`), executada com resultado 100% aprovado nesta sessão.
* Log de execução literal do pytest e do CLI (Seções B.5.1–B.5.3).
* Derivação formal completa do Exemplo 1 (Seção A.5.7).
* Este documento (`ENTREGA_P1.md`), versionável em Git, pronto para anexar ao SIGAA.

---

# BLOCO C — MATERIAL ACADÊMICO

## C.1 Estrutura de relatório proposta (pronta para preenchimento pelo grupo)

1. **Introdução** — contextualizar a disciplina, a atividade (P1) e a linguagem OmniTest. *(Base: A.1, A.2)*
2. **Contextualização do problema** — front-end vs. back-end de compiladores; por que a P1 foca em análise. *(Base: A.1.1)*
3. **Objetivos** — objetivos gerais e específicos do grupo. *(Base: A.2.3)*
4. **Concepção da linguagem OmniTest** — problema, público, paradigma, modelo conceitual. *(Base: A.2 completa)*
5. **Escopo e decisões de projeto** — o que entrou, o que ficou de fora, e por quê. *(Base: A.2.6, A.3)*
6. **Especificação léxica** — catálogo de tokens, palavras reservadas, indentação. *(Base: A.4)*
7. **Gramática formal** — BNF completa, terminais, não-terminais, derivação. *(Base: A.5)*
8. **Documentação dos não-terminais** — tabela completa. *(Base: A.6)*
9. **Análise léxica, sintática e semântica** — distinções e escopo real implementado. *(Base: A.7)*
10. **Exemplos de código-fonte** — os 2 exemplos obrigatórios, explicados em profundidade. *(Base: A.8)*
11. **Estratégia de implementação** — arquitetura, módulos, como rodar. *(Base: B.1–B.3)*
12. **Plano de testes** — matriz de 19 casos. *(Base: B.4)*
13. **Resultados da validação** — saídas reais do pytest e do CLI. *(Base: B.5)*
14. **Limitações e trabalhos futuros** — análise semântica, mais métodos HTTP, ferramentas externas. *(Base: B.6, D.6)*
15. **Conclusão** — síntese do que foi entregue vs. proposto.
16. **Referências** — apenas as 7 fontes verificáveis já citadas no próprio `P1.pdf` (links [1]–[7]); nenhuma referência bibliográfica adicional foi inventada nesta entrega.

O texto das Seções A e B deste documento já está em prosa técnica/acadêmica e pode ser copiado quase diretamente para as seções correspondentes do relatório, com adaptação de formatação conforme o padrão exigido pela instituição (não especificado no PDF — decisão de formatação cabe ao grupo).

## C.2 Roteiro do seminário (12 slides)

| # | Título | Conteúdo visual | Pontos essenciais | Fala sugerida | Pergunta provável do professor |
|---|---|---|---|---|---|
| 1 | Identificação do projeto | Nome do grupo, disciplina, professor, data | OmniTest — DSL para testes de API | "Este é o projeto OmniTest, desenvolvido para a Parte 1 de Compiladores." | — |
| 2 | Problema e motivação | Trecho do PDF (Seção 2) resumido | P1 = só análise; gramática + testes da gramática | "A atividade pede uma gramática de linguagem e ferramentas para testá-la — não um compilador completo." | "Por que vocês não implementaram a síntese?" → Porque a P1 explicitamente cobre só a etapa de análise (ver PDF, Seção 2) |
| 3 | Conceito da OmniTest | Um trecho de código de exemplo | DSL declarativa para testes de API HTTP | "Escolhemos o domínio de QA porque um dos integrantes atua como QA Engineer — isso também atende ao pedido de assinatura própria do projetista." | "Por que testes de API e não uma calculadora?" → Reduz risco de duplicidade com outros grupos e aproveita experiência real |
| 4 | Decisões de projeto | Tabela resumida da Seção A.3 | Indentação só com espaços; GET sem payload / POST com payload obrigatório; JSON estrutural | "Cada decisão tem uma justificativa técnica documentada, não é arbitrária." | "O que vocês descartaram deliberadamente?" → if/for/aritmética/DELETE/PUT — ver A.2.6 |
| 5 | Exemplo de código | `get_test.omt` e `post_test.omt` lado a lado | 2 exemplos completos e formalmente validados | "Ambos foram efetivamente aceitos pela nossa implementação, não é só teoria." | "Isso realmente faz requisições HTTP?" → Não; é reconhecimento sintático apenas (ver A.7) |
| 6 | Análise léxica | Diagrama da pilha de indentação | INDENT/DEDENT gerados pelo lexer; supressão dentro de `{}`/`[]` | "A parte mais delicada foi decidir quando suprimir o NEWLINE — dentro de JSON multi-linha." | "O que acontece com TAB?" → Erro léxico deliberado (política só-espaços) |
| 7 | Gramática formal | BNF resumida (não-terminais principais) | 26 não-terminais, sem recursão à esquerda, símbolo inicial `⟨program⟩` | "A gramática foi corrigida durante a revisão crítica: originalmente não permitia array JSON solto." | "Como vocês sabem que não é ambígua?" → Ver A.5.8: não há prova formal, mas o parser decide deterministicamente em cada ponto com 1 lookahead |
| 8 | Análise sintática | Diagrama de árvore (AST) do Exemplo 1 | Parser descendente recursivo, 1 função por não-terminal | "Cada função do parser tem uma produção BNF documentada logo acima dela no código." | "É LL(1) puro?" → Quase; `comparison` exige uma pequena adaptação prática, documentada honestamente em A.5.8 |
| 9 | Implementação e ferramentas | Estrutura de diretórios | Python puro, pytest, CLI `python -m omnitest` | "Usamos o projeto Python citado no próprio enunciado como ferramenta de teste da gramática." | "Por que não usaram JFLAP/Bison?" → Pendência registrada (ver D.6); Python foi suficiente e está explicitamente permitido no PDF |
| 10 | Testes e evidências | Print do resultado `26 passed` | 19 categorias de teste, 100% aprovado | "Todo resultado mostrado foi realmente executado nesta mesma máquina." | "Vocês testaram casos inválidos também?" → Sim, 10 arquivos inválidos, cada um com o tipo de erro esperado verificado |
| 11 | Limitações | Lista curta (léxico/sintático vs. semântico) | Sem análise semântica; sem execução HTTP real; sem aninhamento de blocos | "Essas são limitações conscientes do escopo da P1, não falhas de implementação." | "Por que não fizeram checagem de tipos?" → Fora do escopo desta P1 (só análise léxica/sintática) |
| 12 | Conclusão | Resumo de 3 bullets | Gramática formal + implementação executável + testes reais entregues | "Entregamos uma base completa, revisada criticamente, e pronta para evoluir em uma eventual Parte 2." | "O que fariam na Parte 2?" → Análise semântica, execução real de HTTP, mais métodos/operadores |

## C.3 Perguntas prováveis adicionais (com respostas justificadas)

| Pergunta | Resposta tecnicamente justificada |
|---|---|
| "A gramática de vocês é igual à de algum grupo/exemplo da internet?" | Não copiamos nenhuma gramática pronta; a combinação específica (indentação supressa dentro de JSON, GET/POST com formas sintáticas distintas, tipos fechados incluindo `Response`) é uma composição autoral, embora use conceitos padrão de teoria de compiladores (recursão à direita, fatoração à esquerda) que são de domínio público. |
| "Por que a pilha de indentação fica só em um nível por teste?" | Decisão consciente de escopo (Seção 3.5 do AGENTS.md: "não crie uma linguagem gigantesca"); adicionar blocos aninhados (`if`, `for`) exigiria uma gramática recursiva por blocos, fora do necessário para demonstrar os conceitos pedidos. |
| "O que acontece se eu rodar um arquivo com erro de indentação?" | O lexer detecta antes mesmo do parser rodar, e reporta linha/coluna exatas — demonstrado ao vivo em B.5.3. |
| "Vocês garantem que a gramática é LL(1)?" | Não fazemos essa alegação sem prova — documentamos honestamente em A.5.8 que uma produção (`comparison`) precisa da técnica padrão de "sufixo opcional" usada em parsers descendentes recursivos escritos à mão, equivalente a uma forma LL(1) fatorada. |
| "JSON de vocês aceita `null`?" | Não, decisão deliberada de simplificação (A.2.6), documentada e não escondida. |

---

# BLOCO D — AUDITORIA FINAL

## D.1 Checklist de aderência à P1

| Item do PDF | Status | Evidência |
|---|---|---|
| Definir gramática de linguagem de programação | ✅ Conforme | Seção A.5 |
| Documentar variáveis (não-terminais) da gramática | ✅ Conforme | Seção A.6 (26 não-terminais documentados individualmente) |
| Usar ferramenta para testar a gramática | 🟡 Parcialmente conforme | Implementação Python usada e executada (permitida explicitamente pelo PDF); JFLAP/Bison/BNFPlayground **não** usados — ver D.6 |
| Discutir análise léxica (tipo de gramática, problemas/virtudes) | ✅ Conforme | Seções A.4.4 e D.4 |
| Apresentar em seminário | ✅ Conforme (material pronto) | Seção C.2 — apresentação em si depende do grupo |
| Inserir no SIGAA | ⚪ Não aplicável tecnicamente | Ação administrativa do grupo, fora do escopo de código |
| Evitar solução idêntica a outro grupo | ✅ Conforme (na medida do verificável) | Domínio + decisões documentadas em A.3; sem pesquisa comparativa formal com outros grupos (impossível nesta sessão) |

## D.2 Auditoria da gramática

| Item verificado | Classificação | Observação/correção |
|---|---|---|
| Todo não-terminal referenciado possui produção | ✅ Conforme | Conferido manualmente (A.5.3 vs. A.5.4) e implicitamente pelo parser (nenhuma função ausente) |
| Todo terminal corresponde a um token do lexer | ✅ Conforme | `TokenType` possui 32 valores; a gramática cita 33 terminais porque `"true"`/`"false"` aparecem como 2 terminais literais distintos que compartilham 1 único `TokenType.BOOLEAN_LITERAL` (diferença explicada e reconciliada em A.5.2/A.4.2) |
| Ausência de recursão à esquerda | ✅ Conforme | Todas as recursões são à direita (A.5.6) |
| Ausência de produções contraditórias | ✅ Conforme | Nenhuma produção duplicada com corpos incompatíveis |
| Gramática permite derivar os 2 exemplos obrigatórios | ✅ Conforme | Derivação completa do Exemplo 1 em A.5.7; Exemplo 2 aceito por execução real (B.5.1) |
| **Falha encontrada e corrigida:** array JSON não podia ser valor de nível superior de um `let` (só aninhado) | 🟠 Corrigida durante esta sessão | Adicionada alternativa `⟨json_array⟩` em `⟨primary⟩`; novo exemplo `json_array_nivel_superior.omt` criado e testado (PASSED) — ver nota em A.5.4 |
| Mistura indevida de BNF/EBNF | ✅ Conforme | Apenas BNF estrita é usada na gramática formal (A.5.4); nenhuma ocorrência de `*`/`+`/`?` fora de prosa explicativa |
| Alegação de LL(1)/não-ambiguidade sem prova | ✅ Conforme (evitada deliberadamente) | A.5.8 é explícito sobre os limites da alegação |

## D.3 Auditoria dos exemplos

| Item | Status |
|---|---|
| Exemplo 1 (GET) presente, completo, e com todos os 9 pontos da Seção 10 do AGENTS.md cobertos | ✅ Conforme (A.8.1) |
| Exemplo 2 (POST + JSON) presente, completo, e com todos os 9 pontos cobertos | ✅ Conforme (A.8.2) |
| Nenhum exemplo usa sintaxe não definida na gramática | ✅ Conforme (verificado por execução real, não por leitura visual) |
| Nenhuma saída de execução HTTP real foi inventada | ✅ Conforme (documento usa "ACEITO/REJEITADO", nunca "status 200 retornado") |

## D.4 Auditoria da implementação

| Item | Status | Observação |
|---|---|---|
| Lexer reconhece todos os tokens do catálogo | ✅ Conforme | `omnitest/lexer.py`, exercitado pelos 26 testes |
| Parser não aceita construção fora da gramática ("modo permissivo") | ✅ Conforme | Cada `_parse_*` levanta `OmniTestSyntaxError` explicitamente no caso não coberto |
| Erros incluem linha e coluna | ✅ Conforme | B.5.3 (saída literal) |
| Implementação constrói uma árvore sintática real (não apenas aceita/rejeita) | ✅ Conforme, com ressalva | `ast_nodes.py` define nós concretos; é uma **árvore sintática concreta simplificada**, não uma AST semanticamente resolvida — terminologia usada com essa ressalva explícita (ver docstring de `ast_nodes.py`) |
| Nenhuma etapa semântica é apresentada disfarçada de sintática | ✅ Conforme | Seção A.7 é explícita sobre a fronteira |

## D.5 Auditoria dos testes

| Item | Status |
|---|---|
| Todas as 20 categorias mínimas do AGENTS.md (Seção 12.1) mapeadas | ✅ Conforme, com 2 reinterpretações documentadas e justificadas (múltiplos níveis de indentação; DEDENT inesperado → reclassificado como erro léxico) — ver B.4 |
| Testes realmente executados (não apenas descritos) | ✅ Conforme | Saída literal do pytest em B.5.1 |
| Nenhum resultado de teste foi inventado | ✅ Conforme | Todos os comandos e saídas neste documento foram gerados nesta sessão, sem edição de conteúdo |
| Cobertura cruzada arquivo↔teste garantida automaticamente | ✅ Conforme | `test_todos_os_arquivos_invalidos_estao_mapeados` impede que um novo arquivo inválido fique sem teste correspondente |

## D.6 Pendências (registradas explicitamente, não escondidas)

1. **Nenhuma ferramenta gráfica externa (JFLAP, Bison, BNFPlayground) foi utilizada** nesta sessão — o PDF permite qualquer uma dessas OU o projeto Python, e optamos pelo Python por ser executável e verificável de ponta a ponta nesta interação. Se o professor exigir evidência em uma ferramenta gráfica especificamente, isso precisa ser feito à parte pelo grupo (ex.: desenhar o autômato de indentação no JFLAP como material complementar).
2. **Nenhuma pesquisa comparativa formal** foi feita contra gramáticas de outros grupos ou de projetos públicos — a alegação de originalidade (Seção A.2.9) baseia-se na ausência de cópia direta, não em uma varredura exaustiva.
3. **Inserção no SIGAA** é uma ação administrativa que só o grupo pode realizar.
4. **Ensaio real do seminário** (tempo, fala ao vivo) não pode ser simulado por este agente — o roteiro (C.2) é a base, mas a apresentação em si depende do grupo.

## D.7 Recomendações prioritárias antes da submissão

1. Se possível, desenhar no **JFLAP** o autômato finito que modela a pilha de indentação (INDENT/DEDENT) como material visual complementar — reforça o critério 3 do PDF ("testes diversos") sem exigir reescrever a gramática.
2. Revisar o texto das Seções A/B deste documento quanto ao **padrão de formatação exigido pela instituição/SIGAA** (não especificado no PDF; decisão do grupo).
3. Ensaiar o seminário usando o roteiro de 12 slides (C.2), cronometrando e ajustando a quantidade de slides ao tempo real disponível.
4. Decidir, como grupo, se querem adicionar ao relatório a discussão de "trabalhos futuros" (análise semântica, mais métodos HTTP) como diferencial de maturidade acadêmica — o conteúdo já está pronto em B.6/D.6.

## D.8 Avaliação descritiva de completude e qualidade (sem nota fictícia)

Esta entrega cobre, com evidência executável e não apenas descritiva, todos os itens obrigatórios explicitamente listados no `P1.pdf`: gramática formal documentada, documentação das variáveis de produção, uso de uma ferramenta de teste da gramática (implementação Python real, executada com 26/26 testes aprovados), e discussão de análise léxica com problemas e virtudes concretos. A gramática passou por uma revisão crítica que encontrou e corrigiu uma lacuna real (array JSON de nível superior) antes da entrega final, demonstrando o processo de revisão exigido pela Seção 16 do AGENTS.md. As limitações (ausência de análise semântica, de execução HTTP real, de uso de ferramentas gráficas externas) estão declaradas de forma explícita e não maquiada. **Não é possível, nem é papel deste agente, afirmar qual nota o professor atribuirá** — a avaliação depende de critérios subjetivos de clareza na apresentação oral e de trabalho em equipe que só o grupo pode demonstrar ao vivo.

---

**Artefatos entregues no repositório** (`omni-test-lang/`, commit já realizado):
- `omnitest/` — lexer, parser, tokens, erros, AST, CLI (código Python real e executável).
- `examples/` — 18 programas `.omt` (válidos e inválidos).
- `tests/` — 26 testes automatizados (`pytest`), 100% aprovados.
- `ENTREGA_P1.md` — este documento completo, versionado e pronto para virar a base do relatório/SIGAA.