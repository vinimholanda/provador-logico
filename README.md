# Provador Lógico

Provador de sentenças básicas criado para a disciplina de Inteligência Artificial da UFAL.

## Como rodar

Para rodar a aplicação é necessário ter o Python 3.0 ou superior instalado e executar o arquivo **main.py**, mantendo a pasta **csv** dentro do mesmo diretório. È lá que poderão ser adicionados mais exemplos ou até mesmo editar os existentes seguindo regras de sintaxe.

## Sintaxe e como adicionar um exemplo

Se você quiser adicionar um exemplo novo a aplicação é necessário alterar um aquivo **base.csv** e uma **fato.csv** com a mesma identificação, dentro dos disponíveis na pasta. O arquivo base guardará a base de conhecimento da sua senteça, lá poderão ser adicionadas regras de SE, ENTÃO junto com operador &, ^ (e), seguindo a sintaxe:

- **Linha 1:** IF, THEN
- **Linha 2:** A & B, C (Se A e B então C)
- **Linha 3:** D ^ E, B (Se D e E então)
- **Linha 4:** F, G (Se F então G)

No fato.csv serão colocadas sentenças singulares que terão um valor inicial. Elas devem ser verdadeiras e serão usadas para fazer a verificação das senteças compostas posteriormente. Ela deve ser feita na seguinte sintaxe:

- **Linha 1:** FACT, VALUE
- **Linha 2:** A, True
- **Linha 3:** B, True

A vírgula é necessária nos dois arquivos pois é ela que faz a separação de antecedentes e resultados, e variável e valor.

