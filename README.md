# Raspagem de dados (web scraping) - TripAdvisor

## Projeto
Esse código foi desenvolvido com o objetivo de coletar informações de uma página de um estabelecimento do TripAdvisor e salvar em um arquivo xls (excel). A URL para a raspagem precisa necessariamente ser do TripAdvisor e ser uma página de um estabelecimento. O programa irá coletar as seguintes informações:
- Nome do estabelecimento
- Nota do estabelecimento
- Quantidade de avaliações do estabelecimento
- Serviços do estabelecimento

Caso o usuário queira, também é possível coletar as avaliações dos clientes. Ao executar será perguntado quantas avaliações o usuário quer coletar. Das avaliações será coletado:
- Nome do cliente
- Título da avaliação
- A avaliação
- Data da estadia

## Desenvolvido com
> Python, Selenium


## Como utilizar
- Baixe o programa <a href="https://github.com/giuseppeusn/tripadvisor_scraping/releases/tag/v1.0.0">aqui</a>
- Descompacte o arquivo `.zip`
- Execute o arquivo `tripadvisor_scraping.exe`
- Informe a URL para fazer a raspagem
- Informe o nome do arquivo para salvar
- Informe e quantidade de comentários (informando 0 não irá coletar nenhum)
