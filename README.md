# OmniTest — Parte 1 (Compiladores, UFC/Russas)

DSL pequena para escrever cenários de teste de API. A assinatura do projeto é a de quem especifica testes HTTP: um bloco nomeado, uma variável tipada com o resultado de um `GET` e uma asserção sobre o status. Os dois programas de exemplo descrevem consultas à API pública JSONPlaceholder (`https://jsonplaceholder.typicode.com`). O reconhecedor só verifica se o texto pertence à gramática. Ele não envia a requisição.

## O que esta versão não faz

| Fora do escopo | Motivo |
| --- | --- |
| Execução HTTP | A Parte 1 trata da análise, não da síntese nem da execução |
| `POST`, payload e literal JSON | Os exemplos usam apenas `GET` com uma URL |
| Tipos `Bool` e `Json`, outros operadores além de `==` | Não aparecem nos programas entregues |
| Análise semântica (tipo, variável declarada, URL existente) | A gramática livre de contexto não garante essas propriedades |

Tipos que permanecem: `String`, `Int` e `Response`. Comandos: `test`, `let` e `assert`.

## Especificação léxica

O analisador léxico lê o texto e produz tokens. Palavra reservada e identificador são separados na leitura: o lexer forma uma palavra e, se ela estiver na tabela abaixo, emite o token reservado. A comparação é exata e diferencia maiúsculas de minúsculas (`GET` é método; `get` é identificador).

Palavras reservadas: `test`, `let`, `assert`, `GET`, `String`, `Int`, `Response`.

| Token | Padrão | Exemplo |
| --- | --- | --- |
| `test`, `let`, `assert`, `GET` | palavra reservada | `GET` |
| `String`, `Int`, `Response` | palavra reservada de tipo | `Response` |
| `IDENTIFIER` | letra ou `_`, depois letras, dígitos ou `_`, e não é palavra reservada | `response` |
| `INT_LITERAL` | um ou mais dígitos | `200` |
| `STRING_LITERAL` | texto entre aspas duplas, na mesma linha; escapes `\"`, `\\`, `\n`, `\t` | `"https://jsonplaceholder.typicode.com/posts/1"` |
| `=` | atribuição | `=` |
| `==` | igualdade | `==` |
| `.` | acesso a um campo | `response.status` |
| `:` | separa nome e tipo, ou fecha o cabeçalho do teste | `let response: Response` |
| `NEWLINE` | fim de uma linha que tem código | gerado pelo lexer |
| `INDENT` | aumento da indentação | gerado pelo lexer |
| `DEDENT` | retorno a um nível anterior | gerado pelo lexer |
| `EOF` | fim do arquivo | gerado pelo lexer |

`INDENT` e `DEDENT` não são escritos no fonte. O programador indenta com espaços.

Regras da indentação:

1. Cada linha é lida por inteiro. Uma linha só com espaços é ignorada.
2. A indentação é a quantidade de espaços antes do primeiro caractere que não é espaço.
3. Uma tabulação na indentação, ou no meio da linha, é erro léxico.
4. Uma pilha começa em 0. Se a linha recua mais do que o topo, o lexer empilha o novo valor e emite `INDENT`.
5. Se recua menos, emite um `DEDENT` para cada nível abandonado. O recuo precisa coincidir com um nível que já está na pilha; caso contrário, a indentação é inconsistente.
6. No fim do arquivo, o lexer emite os `DEDENT` que ainda faltam e, por último, `EOF`.
7. Toda linha com código termina com `NEWLINE`.

## Gramática

Notação BNF. O símbolo inicial é ⟨program⟩.

Terminais: `test`, `let`, `assert`, `GET`, `String`, `Int`, `Response`, `IDENTIFIER`, `INT_LITERAL`, `STRING_LITERAL`, `=`, `==`, `.`, `:`, `NEWLINE`, `INDENT`, `DEDENT`, `EOF`.

Não-terminais: ⟨program⟩, ⟨test_decl_list⟩, ⟨test_decl⟩, ⟨block⟩, ⟨stmt_list⟩, ⟨stmt_tail⟩, ⟨stmt⟩, ⟨let_stmt⟩, ⟨type⟩, ⟨rhs⟩, ⟨http_request⟩, ⟨assert_stmt⟩, ⟨comparison⟩, ⟨primary⟩, ⟨member_access⟩.

```
⟨program⟩        ::= ⟨test_decl⟩ ⟨test_decl_list⟩ EOF

⟨test_decl_list⟩ ::= ⟨test_decl⟩ ⟨test_decl_list⟩
                   | ε

⟨test_decl⟩      ::= "test" STRING_LITERAL ":" NEWLINE ⟨block⟩

⟨block⟩          ::= INDENT ⟨stmt_list⟩ DEDENT

⟨stmt_list⟩      ::= ⟨stmt⟩ ⟨stmt_tail⟩

⟨stmt_tail⟩      ::= ⟨stmt⟩ ⟨stmt_tail⟩
                   | ε

⟨stmt⟩           ::= ⟨let_stmt⟩
                   | ⟨assert_stmt⟩

⟨let_stmt⟩       ::= "let" IDENTIFIER ":" ⟨type⟩ "=" ⟨rhs⟩ NEWLINE

⟨type⟩           ::= "String" | "Int" | "Response"

⟨rhs⟩            ::= ⟨http_request⟩
                   | ⟨primary⟩

⟨http_request⟩   ::= "GET" STRING_LITERAL

⟨assert_stmt⟩    ::= "assert" ⟨comparison⟩ NEWLINE

⟨comparison⟩     ::= ⟨primary⟩ "==" ⟨primary⟩

⟨primary⟩        ::= ⟨member_access⟩
                   | INT_LITERAL
                   | STRING_LITERAL

⟨member_access⟩  ::= IDENTIFIER "." IDENTIFIER
```

As listas são recursivas à direita (⟨test_decl_list⟩ e ⟨stmt_tail⟩), para o parser descer sem recursão à esquerda. Em cada alternativa, o primeiro token já decide qual produção usar: `let` ou `assert` em ⟨stmt⟩; `GET` ou um valor em ⟨rhs⟩; `test` ou fim de lista em ⟨test_decl_list⟩. Cada método de `omnitest/parser.py` consome um desses não-terminais.

Um arquivo precisa de ao menos um `test`. O corpo do teste precisa de ao menos um comando.

### Variáveis da gramática

| Não-terminal | Papel | Exemplo |
| --- | --- | --- |
| ⟨program⟩ | Arquivo inteiro. Exige um teste e permite outros em seguida, até o `EOF`. | `examples/get_one.omt` |
| ⟨test_decl_list⟩ | O restante dos testes. A produção vazia existe para o arquivo poder terminar depois do primeiro cenário. | um segundo `test`, ou nada |
| ⟨test_decl⟩ | Um cenário com nome entre aspas. O dois-pontos e a quebra de linha separam o cabeçalho do bloco. | `test "busca um post":` |
| ⟨block⟩ | O corpo indentado. `INDENT` e `DEDENT` marcam o início e o fim sem usar chaves. | as duas linhas dentro do teste |
| ⟨stmt_list⟩ | A sequência de comandos do bloco. Começa com um comando, para um teste vazio não ser aceito. | `let` seguido de `assert` |
| ⟨stmt_tail⟩ | Os comandos seguintes. A produção vazia encerra o bloco quando vem um `DEDENT`. | o `assert` depois do `let` |
| ⟨stmt⟩ | Um comando. Só há declaração ou asserção, que são as duas frases dos exemplos. | `let` ou `assert` |
| ⟨let_stmt⟩ | Liga um nome a um tipo e a um valor. A anotação de tipo fica na sintaxe, como em `response: Response`. | `let response: Response = GET "..."` |
| ⟨type⟩ | A lista fechada de tipos desta versão. Um nome fora dela não passa daqui. | `Response`, `Int`, `String` |
| ⟨rhs⟩ | O valor atribuído. Separa a requisição de um literal, porque só o `GET` tem forma própria. | `GET "https://..."` ou `200` |
| ⟨http_request⟩ | O `GET` com uma URL entre aspas. Não há payload: a URL é o único argumento. | `GET "https://jsonplaceholder.typicode.com/posts"` |
| ⟨assert_stmt⟩ | A verificação do cenário. Existe para o teste declarar o resultado esperado. | `assert response.status == 200` |
| ⟨comparison⟩ | A única comparação desta versão, com `==` obrigatório. | `response.status == 200` |
| ⟨primary⟩ | Um valor: campo, inteiro ou texto. Reúne o que pode aparecer dos dois lados do `==` e, também, um literal no `let`. | `response.status`, `200` |
| ⟨member_access⟩ | Nome, ponto e campo, como o status lido da resposta. Um ponto só: é o que os exemplos escrevem. | `response.status` |

## Análise léxica neste projeto

A gramática acima é livre de contexto, escrita em BNF. O programa em Python faz a análise em duas etapas. O lexer (`omnitest/lexer.py`) transforma caracteres em tokens. O parser (`omnitest/parser.py`) verifica se essa sequência deriva de ⟨program⟩. Não há árvore sintática: a saída é aceitar ou rejeitar.

A indentação não cabe, sozinha, numa produção livre de contexto, porque a coluna do texto é informação que a BNF não enxerga. O lexer resolve isso com a pilha e entrega `INDENT` e `DEDENT` como tokens comuns. A partir daí, ⟨block⟩ é uma produção comum. Essa divisão é a virtude da abordagem: a gramática dos comandos fica legível, e o seminário pode mostrar o recuo como token. O custo é um lexer mais trabalhoso do que a lista de palavras, e uma mensagem de erro quando o recuo não cai num nível já aberto.

O parser garante a forma do texto. Ele não garante que o tipo do `let` combine com o valor, que a variável do `assert` tenha sido declarada, nem que a URL responda 200. `let response: Int = GET "https://jsonplaceholder.typicode.com/posts/1"` é aceito: `Int` e `GET` estão nas produções, e a compatibilidade entre eles seria semântica.

## Exemplos

`examples/get_one.omt` descreve a busca de um post.

```
test "busca um post":
    let response: Response = GET "https://jsonplaceholder.typicode.com/posts/1"
    assert response.status == 200
```

`examples/get_all.omt` descreve a listagem da coleção.

```
test "lista todos os posts":
    let response: Response = GET "https://jsonplaceholder.typicode.com/posts"
    assert response.status == 200
```

Os dois compartilham a mesma estrutura: cabeçalho, `GET`, asserção de status 200. A diferença é a URL: `/posts/1` é um recurso; `/posts` é a coleção.

## Comandos da apresentação

Rode na raiz do repositório. O que falar em cada item está em `APRESENTACAO.md`. Aceito: `ACEITO` e código 0. Rejeitado: `REJEITADO`, estágio, mensagem, linha e coluna, e código 1.

Estas saídas foram observadas nesta máquina.

**Item 3 do P1 — os dois programas pertencem à gramática**

```
python3 -m omnitest examples/get_one.omt
```

```
ACEITO
```

```
python3 -m omnitest examples/get_all.omt
```

```
ACEITO
```

**Item 3 do P1 — indentação inconsistente (erro léxico)**

O corpo abre com 4 espaços. A linha do `assert` usa 2, que não é um nível da pilha.

```
python3 -m omnitest /dev/stdin <<'EOF'
test "indent":
    let response: Response = GET "https://jsonplaceholder.typicode.com/posts/1"
  assert response.status == 200
EOF
```

```
REJEITADO
léxico: indentação inconsistente: o recuo não coincide com nenhum nível aberto (linha 3, coluna 1)
```

**Item 3 do P1 — comando malformado (erro sintático)**

Falta o `:` entre o nome e o tipo.

```
python3 -m omnitest /dev/stdin <<'EOF'
test "ruim":
    let response Response = GET "https://jsonplaceholder.typicode.com/posts/1"
EOF
```

```
REJEITADO
sintático: esperado :, encontrado Response ('Response') (linha 2, coluna 18)
```

**Item 3 do P1 — a suíte, inclusive a palavra reservada no lugar do nome**

O caso `let test` está em `tests/test_reconhecimento.py` (`test_palavra_reservada_no_lugar_de_variavel_rejeitada`). O lexer classifica `test` como palavra reservada, e o parser rejeita.

```
python3 -m pytest -v
```

```
tests/test_reconhecimento.py::test_get_one_aceito PASSED
tests/test_reconhecimento.py::test_get_all_aceito PASSED
tests/test_reconhecimento.py::test_indentacao_inconsistente_rejeitada PASSED
tests/test_reconhecimento.py::test_comando_malformado_rejeitado PASSED
tests/test_reconhecimento.py::test_palavra_reservada_no_lugar_de_variavel_rejeitada PASSED
5 passed in 0.01s
```

## Validação observada

Comandos executados nesta máquina, sobre o código deste repositório:

```
$ python3 -m omnitest examples/get_one.omt
ACEITO

$ python3 -m omnitest examples/get_all.omt
ACEITO

$ python3 -m pytest -v
tests/test_reconhecimento.py::test_get_one_aceito PASSED
tests/test_reconhecimento.py::test_get_all_aceito PASSED
tests/test_reconhecimento.py::test_indentacao_inconsistente_rejeitada PASSED
tests/test_reconhecimento.py::test_comando_malformado_rejeitado PASSED
tests/test_reconhecimento.py::test_palavra_reservada_no_lugar_de_variavel_rejeitada PASSED
5 passed in 0.01s
```

Uma entrada com corpo em 4 espaços e a linha seguinte em 2 espaços produziu:

```
REJEITADO
léxico: indentação inconsistente: o recuo não coincide com nenhum nível aberto (linha 3, coluna 1)
```

Nenhuma requisição HTTP foi feita. JFLAP, autômato com pilha e Bison não foram usados. A evidência de que uma palavra pertence à gramática é este reconhecedor Python.
