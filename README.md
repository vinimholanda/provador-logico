# Provador Lógico

Provador de sentenças básicas criado para a disciplina de Inteligência Artificial da UFAL.

## Como rodar

Para rodar a aplicação é necessário ter o Python 3.0 ou superior instalado e executar o arquivo **main.py**, mantendo a pasta **csv** dentro do mesmo diretório. É lá que poderão ser adicionados mais exemplos ou até mesmo editar os existentes seguindo regras de sintaxe.

## Sintaxe e como adicionar um exemplo

Se você quiser adicionar um exemplo novo a aplicação, é necessário alterar um aquivo **base.csv** e um **fato.csv**, com a mesma identificação dentro dos disponíveis na pasta. O arquivo base guardará a base de conhecimento da sua senteça, lá poderão ser adicionadas regras de SE, ENTÃO junto com operador & ou ^ (e), seguindo a sintaxe:

- **Linha 1:** IF, THEN
- **Linha 2:** A & B, C (Se A e B então C)
- **Linha 3:** D ^ E, B (Se D e E então)
- **Linha 4:** F, G (Se F então G)

  **...**

No fato.csv serão colocadas sentenças singulares que terão um valor inicial. Elas devem ser verdadeiras e serão usadas para fazer a verificação das senteças compostas posteriormente. Deve ser feita na seguinte forma:

- **Linha 1:** FACT, VALUE
- **Linha 2:** A, True
- **Linha 3:** B, True

   **...**

A vírgula é necessária nos dois arquivos pois é ela que faz a separação de antecedentes e resultados, e variável e valor.

## Ao executar

Quando executado, será solicitado para o usuário escolher qual base e fatos que serão usados naquela execução. Quando selecionado no menu, será impresso na tela todos os dados daquele exemplo, ele mostrará:

- **Base de conhecimento, incluindo resultados possíveis;**
- **Valores do fatos iniciais (Colocados no fatos.csv);**
- **Alfabeto (Todas as letras que compoem as regras + resultados);**
- **Antecedentes (SE x)**
- **Descendentes (ENTÃO y)**
- **Todos os valores verdadeiros até então**

Após isso, um usuário digitará uma letra que será verificada como derivada/provada, ou não. Em seguida, todos os resultados que podem e não podem ser provados para aquelas regras serão exibidos, incluindo o resultado se a letra digitada poderá ou não ser gerada.

