# AppleStore

#### Requerimentos
-----------------
* Ative o ambiente quando estiver no diretório do projeto: source ven_apple/bin/activate
* Com ambiente ativado, instale as dependências do projeto:  pip install -r requirements.txt
* Na pasta raiz do projeto, procure pelo diretório ‘servico’, e no arquivo twitter.exemplo mude para extensão .py, 
  e depois insira suas credenciais.
  
  
  
#### Executando a API
-----------------
No diretório raiz execute o seguinte comando

      python app.py


#### Estrutura do projeto
-----------------
::

    AppleStore
    ├── modulos          - estrutura do codigo fonte dos end-points.
    │   ├── avaliacao    - sub-modulo do end-point procurar por app mais acessado com genero news.
    │   ├── citacao      - sub-modulo de conexao com api do twitter.
    │   ├── genero       - sub-modulo dos top 10 apps com genero book e music.
    │   ├── saida        - sub-modulo de saida de arquivos como csv.
    ├── servico          - modulo de configuracao da api twitter
    ├── ultis            - modulo de acesso ao dados base de consumo csv
    
    
   

    
    
