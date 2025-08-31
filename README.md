# EmailGPT

-Projeto de um site que classifica emails automáticamente com uso de IA, supondo que a resposta vem do setor financeiro de uma empresa
-Feito para o processo seletivo da AutoU
-IA usada foi uma versão gratuita do DeepSeek, mas é possivel usar várias LLMs diferentes, veja mais afundo no site da openrouter.ai

-Intruções de uso:
Enviar um arquivo pdf ou txt para o site, ou escrever uma mensagem diretamente no site
Clique enviar
Em segundos a IA ira apresentar uma resposta possivel do email que pode ser alterada diretamente no site, ou baixar em txt.

Para uso direto o site está online em: https://rodperoba.pythonanywhere.com/

Para download do código e uso local:
Todo o código necessário está na pasta MainFolder
Precisa de um ambiente que rode python 3.13>=
Instale as bibliotecas listadas no arquivo MainFolder/Backend/requirements.txt
Crie um arquivo .env de acordo com o modelo .env.exemplo que está em MainFolder/DockerFolder
Nesse arquivo .env, precisaa de uma key para a API do https://openrouter.ai/
Para rodar o site localmente vá a pasta MainFolder/Backend e rode o arquivo app.py

OBS: Há arquivos para criar um conteiner do app, consegui fazer ele funcionar localmente mas não na nuvem, não identifiquei a solução para isso ainda, mas deixei os arquivos no repositório.

Há arquivos que foram usados como testes dentro de Miscellaneous/TestesDeEmails
