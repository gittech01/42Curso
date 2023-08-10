
## Instruções

A menos que haja uma contradição explícita, as seguintes instruções serão válidas para todos os dias desta Piscina de Python Django.

- Apenas esta página servirá como referência; não confie em rumores.
- Cuidado! Este documento pode potencialmente mudar até uma hora antes da entrega.
- Estes exercícios são cuidadosamente dispostos por ordem de dificuldade - do mais fácil ao mais difícil. Não levaremos em consideração
  um exercício mais difícil que tenha sido concluído com sucesso se um mais fácil não estiver perfeitamente funcional.
- Certifique-se de ter as permissões apropriadas em seus arquivos e diretórios.
- Você deve seguir os procedimentos de entrega para cada exercício.
- Seus exercícios serão verificados e avaliados por seus colegas de classe.
- Além disso, seus exercícios serão verificados e avaliados por um programa chamado Moulinette. Moulinette é muito meticulosa e rigorosa em sua avaliação do seu
  trabalho. É completamente automatizada e não há como negociar com ela. Portanto, se você quiser evitar surpresas desagradáveis, seja o mais minucioso possível.
- Exercícios no Shell devem ser executáveis com /bin/sh.
- Você não pode deixar nenhum arquivo adicional no seu diretório além dos especificados no enunciado.
- Tem uma pergunta? Pergunte ao seu colega à direita. Caso contrário, tente o seu colega à esquerda.
- Seu guia de referência se chama Google / man / a Internet / ....
- Lembre-se de discutir no fórum da piscine do seu Intra e no Slack!
- Examine os exemplos minuciosamente. Eles podem muito bem exigir detalhes que não estão explicitamente mencionados no enunciado...


## Regras

Você deve usar um interpretador Python 3.

- Cada exercício será independente. Se entre os recursos necessários alguns já foram abordados em exercícios anteriores, duplique-os no exercício atual.
- Você deve trabalhar em um banco de dados PostgreSQL chamado "djangotraining" e criar uma função chamada "djangouser",
cuja senha será "secret", e que terá todos os direitos para o banco de dados.
- A pasta do seu repositório deve ser um projeto Django. O projeto deve ser nomeado de acordo com o dia atual.
- Vamos usar o conceito de aplicação do Django para separar os exercícios:
   Os exercícios de hoje devem estar localizados em uma aplicação Django específica, com o nome correspondente ao exercício
   correspondente e localizada na raiz do repositório.
- O projeto Django deve estar configurado corretamente para atender aos requisitos do exercício. Você não poderá alterar as configurações durante a avaliação.
- Você não pode incluir migrações no seu trabalho.
- Em cada exercício que mencionar o ORM, você deve usar o ORM do Django. Não é permitido escrever nenhuma linha de SQL.
- Em cada exercício que mencionar SQL, você deve usar a biblioteca psycopg2 e executar todas as consultas em SQL.

Aqui está um exemplo de estrutura típica para o repositório de um aluno chamado krichard, para o dia d42, incluindo 2 exercícios:

```
|-- krichard
| |-- .
| |-- ..
| |-- .git
| |-- .gitignore
| |-- d42
| | |-- __init__.py
| | |-- settings.py
| | |-- urls.py
| | |-- wsgi.py
| |-- ex00
| | |-- admin.py
| | |-- apps.py
| | |-- forms.py
| | |-- __init__.py
| | |-- models.py
| | |-- tests.py
| | |-- urls.py
| | |-- views.py
| |-- ex01
| | |-- admin.py
| | |-- apps.py
| | |-- forms.py
| | |-- __init__.py
| | |-- models.py
| | |-- tests.py
| | |-- urls.py
| | |-- views.py
| |-- manage.py
```

### Exercício 00: SQL - Construção de Tabela
- Diretório de entrega: ex00/

Crie uma aplicação Django chamada "ex00" e também uma view interna que deve ser acessada na seguinte URL: 127.0.0.1:8000/ex00/init.

Esta view deve criar uma tabela SQL no PostgreSQL com a ajuda da biblioteca psycopg2 e retornar uma página contendo "OK"
se for bem-sucedida. Caso contrário, deve retornar uma mensagem de erro descrevendo o problema.

A tabela SQL deve se encaixar nesta descrição:
- Deve ser nomeada "ex00_movies".
- Deve ser criada apenas se ainda não existir.
- Deve incluir apenas os seguintes campos:
   - title: cadeia de caracteres variável única, com no máximo 64 bytes, não nula.
   - episode_nb: inteiro, CHAVE PRIMÁRIA.
   - opening_crawl: texto, pode ser nulo, sem limite de tamanho.
   - director: cadeia de caracteres variável, não nulo, com no máximo 32 bytes.
   - producer: cadeia de caracteres variável, não nulo, com no máximo 128 bytes.
   - release_date: data (sem hora), não nulo.


### Exercício 01: ORM - construindo uma tabela
- Diretório de entrega: ex01/

Crie uma aplicação chamada "ex01". Dentro dela, crie um modelo Django chamado "Movies" com os seguintes campos exatamente:
- title: cadeia de caracteres variável única, com no máximo 64 bytes, não nula.
- episode_nb: inteiro, CHAVE PRIMÁRIA.
- opening_crawl: texto, pode ser nulo, sem limite de tamanho.
- director: cadeia de caracteres variável, não nulo, com no máximo 32 bytes.
- producer: cadeia de caracteres variável, não nulo, com no máximo 128 bytes.
- release_date: data (sem hora), não nula.
Este modelo também deve redefinir o método __str__ de forma que ele retorne o atributo "title".


### Exercício 02: SQL - Inserção de Dados
- Diretório de entrega: ex02/

Você deve criar uma aplicação Django chamada "ex02". Nesta aplicação, as visualizações acessíveis através das seguintes URLs:

- 127.0.0.1:8000/ex02/init: deve criar uma tabela com as mesmas especificações daquela exigida no exercício ex00, exceto que será nomeada "ex02_movies". Deve retornar uma página exibindo "OK" se for bem-sucedido. Caso contrário, deve exibir uma mensagem descrevendo o problema.

- 127.0.0.1:8000/ex02/populate: deve inserir os seguintes dados na tabela criada pela visualização anterior:
   - episode_nb: 1 - title: The Phantom Menace - director: George Lucas - producer: Rick McCallum - release_date: 1999-05-19
   - episode_nb: 2 - title: Attack of the Clones - director: George Lucas - producer: Rick McCallum - release_date: 2002-05-16
   - episode_nb: 3 - title: Revenge of the Sith - director: George Lucas - producer: Rick McCallum - release_date: 2005-05-19
   - episode_nb: 4 - title: A New Hope - director: George Lucas - producer: Gary Kurtz, Rick McCallum - release_date: 1977-05-25
   - episode_nb: 5 - title: The Empire Strikes Back - director: Irvin Kershner - producer: Gary Kurtz, Rick McCallum - release_date: 1980-05-17
   - episode_nb: 6 - title: Return of the Jedi - director: Richard Marquand - producer: Howard G. Kazanjian, George Lucas, Rick McCallum - release_date: 1983-05-25
   - episode_nb: 7 - title: The Force Awakens - director: J. J. Abrams - producer: Kathleen Kennedy, J. J. Abrams, Bryan Burk - release_date: 2015-12-11
   Deve retornar uma página exibindo "OK" para cada inserção bem-sucedida. Caso contrário, deve exibir uma mensagem de erro indicando o problema.

- 127.0.0.1:8000/ex02/display: deve exibir todos os dados incluídos na tabela "ex02_movies" em uma tabela HTML, incluindo os campos vazios eventuais. Se não houver dados disponíveis ou ocorrer um erro, a página deve simplesmente exibir "Nenhum dado disponível".



### Exercício 03: ORM - Inserção de Dados
- Diretório de entrega: ex03/

Crie um novo aplicativo Django chamado "ex03". Dentro dele, crie um modelo Django idêntico ao criado no exercício ex01.

Este aplicativo deve incluir visualizações acessíveis através das seguintes URLs:

- 127.0.0.1:8000/ex03/populate: deve inserir no modelo deste aplicativo os seguintes dados:
   - episode_nb: 1 - title: The Phantom Menace - director: George Lucas - producer: Rick McCallum - release_date: 1999-05-19
   - episode_nb: 2 - title: Attack of the Clones - director: George Lucas - producer: Rick McCallum - release_date: 2002-05-16
   - episode_nb: 3 - title: Revenge of the Sith - director: George Lucas - producer: Rick McCallum - release_date: 2005-05-19
   - episode_nb: 4 - title: A New Hope - director: George Lucas - producer: Gary Kurtz, Rick McCallum - release_date: 1977-05-25
   - episode_nb: 5 - title: The Empire Strikes Back - director: Irvin Kershner - producer: Gary Kurtz, Rick McCallum - release_date: 1980-05-17
   - episode_nb: 6 - title: Return of the Jedi - director: Richard Marquand - producer: Howard G. Kazanjian, George Lucas, Rick McCallum - release_date: 1983-05-25
   - episode_nb: 7 - title: The Force Awakens - director: J. J. Abrams - producer: Kathleen Kennedy, J. J. Abrams, Bryan Burk - release_date: 2015-12-11
   Deve retornar uma página exibindo "OK" para cada inserção bem-sucedida. Caso contrário, deve exibir uma mensagem de erro indicando o problema.

- 127.0.0.1:8000/ex03/display: deve exibir todos os dados incluídos na tabela "Movies" em uma tabela HTML, incluindo os campos vazios eventuais. Se não houver dados disponíveis ou ocorrer um erro, a página deve simplesmente exibir "Nenhum dado disponível".

`Durante a avaliação, a migração será executada antes dos testes.`


### Exercício 04: SQL - Remoção de Dados
- Diretório de entrega: ex04/

Crie um aplicativo chamado "ex04". Ele deve conter visualizações acessíveis através das seguintes URLs:

- 127.0.0.1:8000/ex04/init: deve criar uma tabela com as mesmas especificações daquelas exigidas para o aplicativo ex00, exceto que será nomeada "ex04_movies". Deve retornar uma página exibindo "OK" para cada inserção bem-sucedida. Caso contrário, deve exibir uma mensagem de erro indicando o problema.

- 127.0.0.1:8000/ex04/populate: deve inserir os dados descritos no exercício ex02 na tabela criada na visualização anterior. Esta visualização deve reinserir quaisquer dados deletados. Deve retornar uma página exibindo "OK" para cada inserção bem-sucedida. Caso contrário, deve exibir uma mensagem de erro indicando o problema.

- 127.0.0.1:8000/ex04/display: deve exibir todos os dados incluídos na tabela "ex04_movies" em uma tabela HTML, incluindo os campos vazios eventuais. Se não houver dados disponíveis ou ocorrer um erro, a página deve simplesmente exibir "Nenhum dado disponível".

- 127.0.0.1:8000/ex04/remove: deve exibir um formulário HTML contendo uma lista suspensa (drop-down) de títulos de filmes e um botão de envio (submit) chamado "remover". Os títulos dos filmes são aqueles contidos na tabela "ex04_movies".

Quando o formulário é validado, o filme selecionado é excluído do banco de dados e o formulário é redisplayed com a lista atualizada contendo os filmes restantes. Se não houver dados disponíveis ou ocorrer um erro, a página deve simplesmente exibir "Nenhum dado disponível".


### Exercício 05: ORM - Exclusão de Dados
- Diretório de entrega: ex05/

Crie um novo aplicativo Django chamado "ex05". Crie um modelo idêntico ao do exercício ex01 dentro dele.

Este aplicativo deve incluir visualizações acessíveis através das seguintes URLs:

- 127.0.0.1:8000/ex05/populate: deve inserir os dados descritos no exercício ex03 na aplicação criada. Esta visualização deve reinserir quaisquer dados excluídos. Deve retornar uma página exibindo "OK" para cada inserção bem-sucedida. Caso contrário, deve exibir uma mensagem de erro indicando o problema.

- 127.0.0.1:8000/ex05/display: deve exibir todos os dados incluídos na tabela "Movies" em uma tabela HTML, incluindo os campos vazios eventuais. Se não houver dados disponíveis ou ocorrer um erro, a página deve simplesmente exibir "Nenhum dado disponível".

- 127.0.0.1:8000/ex05/remove: deve exibir um formulário HTML contendo uma lista suspensa (drop-down) de títulos de filmes e um botão de envio (submit) chamado "remover". Os títulos dos filmes são aqueles contidos no modelo "Movies" deste aplicativo.

Quando o formulário é validado, o filme selecionado é excluído do banco de dados e o formulário é redisplayed com a lista atualizada contendo os filmes restantes. Se não houver dados disponíveis ou ocorrer um erro, a página deve simplesmente exibir "Nenhum dado disponível".

Durante a avaliação, a migração será executada antes dos testes.


### Exercício 06: SQL - Atualização de Dados
- Diretório de entrega: ex06/

Crie um novo aplicativo Django chamado "ex06". Ele deve conter visualizações acessíveis através das seguintes URLs:

- 127.0.0.1:8000/ex06/init: deve criar uma tabela com as mesmas especificações daquelas exigidas para o aplicativo ex00, exceto que será nomeada "ex06_movies" e incluirá os seguintes campos adicionais:
   - created: um campo do tipo datetime (data e hora), que, quando criado, deve ser automaticamente definido para a data e hora atual.
   - updated: um campo do tipo datetime (data e hora), que, quando criado, deve ser automaticamente definido para a data e hora atual e atualizado automaticamente a cada atualização graças ao gatilho a seguir:
      ```sql
      CREATE OR REPLACE FUNCTION update_changetimestamp_column()
      RETURNS TRIGGER AS $$
      BEGIN
      NEW.updated = now();
      NEW.created = OLD.created;
      RETURN NEW;
      END;
      $$ language 'plpgsql';
      CREATE TRIGGER update_films_changetimestamp BEFORE UPDATE
      ON ex06_movies FOR EACH ROW EXECUTE PROCEDURE
      update_changetimestamp_column();
      ```
- 127.0.0.1:8000/ex06/populate: deve popular a tabela criada na visualização anterior com os dados descritos no exercício ex02. Deve retornar uma página exibindo "OK" para cada inserção bem-sucedida. Caso contrário, deve exibir uma mensagem de erro indicando o problema.

- 127.0.0.1:8000/ex06/display: deve exibir todos os dados incluídos na tabela "ex06_movies" em uma tabela HTML. Se não houver dados disponíveis ou ocorrer um erro, a página deve simplesmente exibir "Nenhum dado disponível".

- 127.0.0.1:8000/ex06/update: deve gerenciar o envio e o recebimento de um formulário. Este último deve permitir escolher um filme em um menu suspenso (drop-down) contendo os filmes incluídos na tabela "ex06_movies" e escrever texto no segundo campo. Ao validar o formulário, a visualização deve substituir o campo "opening_crawl" do filme selecionado pelo texto digitado no formulário na tabela "ex06_movies". Se não houver dados disponíveis ou ocorrer um erro, a página deve simplesmente exibir "Nenhum dado disponível".