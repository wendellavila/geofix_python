# geofix_python
## Descrição
Script para padronizar arquivos de linhas vetorizadas e georreferenciadas.

## Funcionalidades
- Leitura de arquivos GeoJSON, KML ou .zip contendo arquivos Shapefile.
- Converte linhas do tipo MultiLineString para LineString.
- Preenche falhas em linhas e curvas, conectando pares de linhas colineares.
- Padroniza coordenadas no formato WGS84 (EPSG:4326).
- Exporta dados resultantes no formato Shapefile contidos em um arquivo .zip.

## Instalação
Para o desenvolvimento do script, o Python foi utilizado na versão 3.12.4, mas qualquer versão a partir da 3.6 deve ser compatível.
As dependências utilizadas estão detalhadas no arquivo requirements.txt.

## Utilização
O script pode ser executado via linha de comando através do arquivo geofix.py:

```
python geofix.py caminho_para_o_arquivo_de_entrada.zip
```

Ao executar desta forma, o arquivo de saída será criado no mesmo diretório do arquivo de entrada.

Caso queira definir o caminho para o arquivo de saída, pode-se executar da seguinte forma:

```
python geofix.py caminho_para_o_arquivo_de_entrada.zip --output caminho_para_o_arquivo_de_saida.zip
```

É possível ler estas mesmas instruções através do comando abaixo:

```
python geofix.py --help
```