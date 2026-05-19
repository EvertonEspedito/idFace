# IdFace - Sistema de Reconhecimento Facial com Python e OpenCV

## 📌 Descrição

Este projeto realiza:

- Cadastro de pessoas
- Captura de rostos pela webcam
- Treinamento de reconhecimento facial
- Reconhecimento facial em tempo real
- Integração com banco de dados SQLite

O sistema utiliza:

- Python
- OpenCV
- SQLite
- LBPH Face Recognizer

---

# 📂 Estrutura do Projeto

```text
idFacet/
│
├── fotos/
│   ├── 1/
│   ├── 2/
│
├── banco.db
├── classificadorLBPH_V1.yml
│
├── main.py
├── cadastrar.py
├── capturar.py
├── treinar.py
└── reconhecer.py
```

---

# ⚙️ Tecnologias Utilizadas

- Python 3
- OpenCV
- SQLite
- NumPy
- Pillow

---

# 📦 Instalação

## 1. Clonar projeto

```bash
git clone https://github.com/seuusuario/idFace.git
```

---

## 2. Criar ambiente virtual

Linux/Mac:

```bash
python -m venv .venv
source .venv/bin/activate
```

Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

---

## 3. Instalar dependências

```bash
pip install opencv-contrib-python pillow numpy
```

---

# 🚀 Como Executar

```bash
python main.py
```

---

# 🧠 Funcionalidades

## ✅ Cadastro de Pessoas

Permite cadastrar:

- ID
- Nome
- Cargo

Cargos disponíveis:

- Professor
- Aluno
- TAE
- Diretor
- Gestor

---

## 📸 Captura Facial

O sistema:

- abre a webcam
- detecta o rosto
- salva várias imagens automaticamente

As imagens ficam em:

```text
fotos/ID_DA_PESSOA/
```

---

## 🧠 Treinamento Facial

O treinamento utiliza:

```text
LBPH (Local Binary Patterns Histograms)
```

Após o treinamento é criado:

```text
classificadorLBPH_V1.yml
```

---

## 🎥 Reconhecimento Facial

O sistema:

- detecta o rosto
- compara com o modelo treinado
- busca os dados no banco SQLite
- exibe nome e cargo na tela

---

# 🗄 Banco de Dados

Tabela:

```sql
CREATE TABLE pessoas (
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    cargo TEXT NOT NULL
)
```

---

# ▶️ Fluxo do Sistema

```text
Cadastrar Pessoa
        ↓
Capturar Faces
        ↓
Treinar Modelo
        ↓
Reconhecer Face
```

---

# 📷 Exemplo de Reconhecimento

```text
Everton - Professor
```

---

# 🔧 Melhorias Futuras

- Sistema Web com Django
- Login facial
- Controle de presença
- Dashboard administrativo
- API REST
- Reconhecimento em tempo real via navegador
- Integração com ESP32

---

# 👨‍💻 Autor

Projeto desenvolvido por Everton Espedito Silva Santos.

