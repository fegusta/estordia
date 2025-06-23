# Estordia

Aplicação para acompanhar inventário da Steam e preços em mercados externos.

## Backend

### Instalação

1. Crie um ambiente virtual:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
2. Instale dependências:
   ```bash
   pip install -r requirements.txt
   ```
3. Configure a variável `STEAM_API_KEY` com sua chave da Steam Web API e opcionalmente `DATABASE_URL` para usar PostgreSQL.
4. Execute o servidor:
   ```bash
   python -m backend.app
   ```

## Frontend

A pasta `frontend/` contém uma aplicação React simples.

### Instalação

1. Entre na pasta `frontend` e instale as dependências `npm`:
   ```bash
   npm install
   ```
2. Inicie o servidor de desenvolvimento:
   ```bash
   npm start
   ```

## Coleta periódica

O script `scripts/update_data.py` deve ser executado periodicamente (ex.: via cron) para atualizar os preços e armazenar no banco.

## Estrutura

```
backend/
  app.py          # API Flask
  models.py       # Modelos SQLAlchemy
  database.py     # Conexão com banco
frontend/
  src/            # Código React
scripts/
  update_data.py  # Coletor periódico
requirements.txt  # Dependências Python
```
