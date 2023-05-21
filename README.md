# Projeto-Carol-ILE
prjeto programação
Descrição do Problema:

Natália é uma aluna muito desleixada monetariamente falando.
Constantemente ela se perde em suas contas e acaba devendo ao banco. Você,
como um bom programador, decidiu ajudá-la montando um sistema de Rastreamento
de Despesas Pessoais.

Requisitos funcionais:
1. O sistema deve ser baseado em transações, que guardam (pelo menos)
informações sobre o nome, uma categoria (exemplo: Casa, comida, transporte,
etc...) e a quantidade de dinheiro envolvida. Vale lembrar que o sistema deve
rastrear entradas e saídas de dinheiro!
2. Deve permitir o CRUD (Adição, leitura, atualização e deleção) de transações
manualmente com a utilização de um menu.
a. O programa deve também permitir leitura de transações filtradas por
categoria.

3. Deve guardar as informações adicionadas em um "banco de dados", para que
estas persistam além da execução do programa. Então, se o usuário rodar o
programa uma vez, adicionar 2 transações e acabar a execução do programa,
ao abrir o programa novamente e listar as transações, as duas adicionadas
anteriormente devem aparecer.
4. Deve ser possível mostrar um extrato do sistema agrupando despesas por
categoria.
5. Ter pelo menos uma outra funcionalidade a mais que não está descrita aqui
neste documento. Sejam criativos e divirtam-se!

Requisitos não funcionais:
1. Deve ser feito em Python sem o uso de bibliotecas adicionais.
a. Utilizar a linha de comando para entrada e saída;
b. Exceções de bibliotecas:

Ciências da Computação
Fundamentos de Programação 2023.1
Professores: Ana Carolina e Mateus Valgueiro

■ os -> os.system("clear") ou “cls”

2. Os dados devem ser salvos em um arquivo no formato .csv Comma-separated
values, valores separados por vírgulas)
a. Perceba que o formato deste arquivo define que os valores estão
separados por vírgula. Então, o que acontece quando o usuário quiser
adicionar um nome de uma transferência com vírgula?
3. O trabalho deve ser feito em trios (turma B) ou quartetos (turma A).
a. Trabalhos que não forem feitos em grupo perderão 50% da nota.
4. O código deve estar organizado, portanto, deve conter:
a. Funções para dividir o código de forma lógica e evitar repetições;
b. Tratamento de exceções, para garantir que seu código está pronto para
tratar casos inesperados �
c. Legibilidade do código, incluindo nomeação de variáveis e funções.
5. Deve ser feito um manual do usuário, explicando como utilizar a ferramenta e
restrições gerais que a aplicação tenha.
a. Fiquem à vontade para escolher como será feito esse manual. Pode ser
um pdf, site, vídeo, carta...
6. Não será aceito entregas atrasadas.
7. Apresentação:
a. A equipe deve apresentar o projeto feito para os professores.
b. Todos envolvidos da equipe devem explicar alguma parte, e perguntas
direcionadas serão feitas durante a apresentação.
c. Deve conter partes do código, diagramas e as explicações de como ele
foi feito, exemplos de resultados, definições e escolhas feitas pela
equipe.
d. Deve conter uma conclusão com a opinião do grupo sobre os
resultados.

8. A entrega será em uma atividade do classroom
a. O que deve ser entregue:
■ Código da aplicação
■ Manual do usuário e documentação

Ciências da Computação
Fundamentos de Programação 2023.1
Professores: Ana Carolina e Mateus Valgueiro

Critérios de avaliação:
● Apresentação (50 pontos - nota individual):
○ Legibilidade
○ Apresentação da ferramenta e manual do usuário
○ Perguntas durante a apresentação
● Código (50 pontos - nota por grupo):
○ Legibilidade e Organização do código (15 pontos)
○ Tratamento de erros (10 pontos)
○ Utilização de Arquivos (15 pontos)
○ Funcionalidade extra (10 pontos)
