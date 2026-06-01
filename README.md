# Detetor de Viés de Confirmação

Web app para deteção de viés de confirmação em questões, usando Llama 4 Maverick via Groq API.

## Tipos de Viés Detetados
- Sem Viés
- Seleção de Evidência
- Fechamento Prematuro
- Efeito de Primazia
- Interpretação Assimétrica

## Instalação

### 1. Obtém a tua Groq API Key
- Vai a https://console.groq.com
- Cria uma conta gratuita
- Gera uma API Key

### 2. Configura o ambiente
```bash
# Copia o ficheiro de variáveis de ambiente
cp .env.example .env

# Abre o .env e substitui pela tua chave
# GROQ_API_KEY=a_tua_chave_aqui
```

### 3. Instala as dependências
```bash
pip install -r requirements.txt
```

### 4. Corre a aplicação
```bash
python app.py
```

### 5. Abre no browser
```
http://localhost:5000
```

## Estrutura do Projeto
```
bias-detector/
├── app.py              ← Backend Flask
├── prompt.py           ← System prompt (framework de viés)
├── requirements.txt    ← Dependências Python
├── .env                ← Chave API (não partilhar!)
└── templates/
    └── index.html      ← Frontend
```
