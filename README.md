# Django Rest Api - Clientes

API para o cadastro de clientes desenvolvida por meio do Django Rest Framework

## Como desenvolver (Windows)?

1. Clone o repositório
2. Crie um virtualenv com Python 3.7.4
3. Ative o virtualenv
4. Instale as dependências
5. Configure a instância com o .env
6. Execute os testes

```console
git clone git@github.com:felipeabreu86/python-django-rest-api-clientes.git
cd python-django-rest-api-clientes
python -m venv .venv
source .venv/scripts/activate
pip install -r requirements.txt
cp dev-contrib/env-sample .env
python manage.py test
```

## Como fazer o Deploy (Windows)?

1. Crie uma conta no Fly.io
2. Configure as variáveis de ambiente não-sensíveis em fly.toml
3. Instale o Fly CLI (flyctl)
4. Autentique-se via flyctl
5. Realize o Deploy
6. Configure uma variável de ambiente sensível chamada SECRET_KEY
7. Configure um super usuário
8. Consulte todas as variáveis de ambiente configuradas

```console
3. iwr https://fly.io/install.ps1 -useb | iex
4. flyctl auth login
5. flyctl deploy
6. flyctl secrets set SECRET_KEY=<chave-secreta-aqui>
7. flyctl ssh console -C 'python /code/manage.py createsuperuser'
8. flyctl ssh console -C "printenv"
```