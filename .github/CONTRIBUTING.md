# Regras de conduta do Projeto Caipora

Para contribuir com o projeto Caipora, comece lendo o [README](https://github.com/deeplearningunb/caipora/blob/master/README.md) para conhecer melhor o projeto. Outro documento importante a ser lido é o Código de Conduta.

Obrigada por contribuir! :smile: :tada:

## Como contribuir?

### Reportando um defeito

Primeiro verifique se não há um defeito semelhante registrado nas issues do repositório. Caso não exista um registro, abra uma [Nova Issue](https://github.com/deeplearningunb/caipora/issues).

### Sugerir novas adições de funcionalidades

* Primeiro verifique se não existe alguma issue semelhante aberta no registro de issues do repositório;
* Caso não exista, crie uma Nova Issue. Dê um título significativo a ela, coloque uma descrição e pelo menos uma label.

### Submetendo alterações

As mudanças devem ser submetidas através de [Pull Requests](https://github.com/deeplearningunb/caipora/pulls) referenciando a issue relativa a modificação.

## Padrão de Commit

Para padronizar as entregas é recomendado que seja seguido um padrão de commit:
* Os commits devem ser descritos em inglês;
* Os commits devem conter um resumo do seu conteúdo com as ações realizadas e os objetos envolvidos;
* Caso esteja trabalhando em com algum associado assine nos seus commits os seus parceiros.

**Exemplo:**
```
Creating project community files (Título curto e objetivo)

Adds project license (Descrição de uma das atividades)
Co-authored-by: Fulano de Tal <fulanodetal@gmail.com> (Assinatura de parceria)
```

## Política de Branches

Essa Política de Branches deverá guiar os desenvolvedores na forma de organização de suas contribuições ao repositório. 

**development -** Branch principal do repositório onde será permitida somente a integração de software consolidado. Essa branch visa receber os Pull Requests para serem validados e homologados antes de enviados à master.

**bugfix/ -** Branch utilizada para corrigir defeitos de baixa/média severidade e que não estão presentes na branch development. Para nomear a branch inicie com *bugfix/<nome-da-issue>*. É necessário que a branch esteja relacionada a uma issue, pois antes do Pull Request ser validados, será necessário a verificação a existência da issue aberta.

**hotfix/ -** Branch utilizada para corrigir defeitos de alta severidade. Caso não exista uma issue aberta referente ao defeito, é necessário que uma nova issue seja submetida.  Para nomear a branch inicie com *hotfix/<nome-da-issue>*

**feature/ -** Para a adição de novas features é necessário criar uma nova branch nomeada *feature/<número-da-issue>*. Observer que é necessário a existência de uma issue relativa a nova feature.



