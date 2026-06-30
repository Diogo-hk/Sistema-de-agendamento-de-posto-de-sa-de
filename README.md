# Sistema de Agendamento para Postos de Saúde

Sistema em Python para gerenciamento de consultas em unidades básicas de
saúde, desenvolvido como projeto da disciplina de Engenharia de Software —
UDESC (Universidade do Estado de Santa Catarina).

**Autores:** Diogo Silva de Carvalho e Victor Alexandre Silva Perim

---

## 📋 Sobre o projeto

O sistema permite que pacientes agendem, cancelem e visualizem consultas
em unidades de saúde, que funcionários gerenciem a agenda de profissionais
e confirmem presenças, e que administradores cadastrem e gerenciem
unidades de saúde. O projeto segue um modelo de classes orientado a
objetos com três perfis de usuário (Paciente, Funcionário e Administrador),
todos herdando de uma classe base `Usuario`.

## 🗂️ Estrutura do projeto

```
.
├── main.py                      # Ponto de entrada — menu interativo via terminal
├── src/
│   ├── usuario.py                # Classe base: autenticação e login
│   ├── paciente.py                # Perfil Paciente (herda de Usuario)
│   ├── administrador.py           # Perfil Administrador (herda de Usuario)
│   ├── funcionario.py             # Perfil Funcionário (herda de Usuario)
│   ├── unidadeSaude.py            # Unidades de saúde
│   ├── agenda.py                  # Vagas/horários disponíveis por profissional
│   ├── consulta.py                # Consultas agendadas
│   ├── cpf.py                     # Validação de CPF/CNPJ
│   └── notificacaoFactory.py      # Esqueleto do padrão Factory Method (lembretes)
└── tests/
    ├── test_usuario.py
    ├── test_usuarios_especializados.py
    ├── test_consulta.py
    ├── test_agenda.py
    ├── test_unidade_saude.py
    └── test_cpf.py
```

## ✅ Pré-requisitos

- **Python 3.10 ou superior** (testado em 3.12)
- Nenhuma biblioteca externa é necessária — o projeto usa apenas a
  biblioteca padrão do Python (`datetime`, `time`, `re`, `unittest`).

Para verificar se o Python está instalado e a versão:

```bash
python3 --version
```

## 🚀 Como executar o sistema

Clone o repositório e rode o `main.py` a partir da pasta raiz do projeto:

```bash
git clone https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git
cd SEU_REPOSITORIO
python3 main.py
```

O sistema abre um menu interativo no terminal. Use os usuários de teste já
cadastrados no código para explorar o sistema, ou cadastre um novo
paciente pela opção **"2. Cadastrar-se"**.

> ⚠️ É importante rodar o comando de dentro da pasta raiz do projeto
> (onde está o `main.py`), pois os módulos são importados como
> `from src.consulta import Consulta` — rodar de outro diretório causa
> erro de importação.

## 🧪 Como executar os testes

Os testes unitários também usam apenas a biblioteca padrão (`unittest`),
sem necessidade de instalar nada:

```bash
python3 -m unittest discover -s tests -v
```

- `discover` busca automaticamente todos os arquivos `test_*.py` dentro de `tests/`
- `-s tests` indica a pasta onde procurar
- `-v` (opcional) mostra o resultado de cada teste individualmente

Para rodar apenas um arquivo de teste específico:

```bash
python3 -m unittest tests.test_consulta -v
```

Resultado esperado: **48 testes, todos passando**.

### Cobertura de testes (opcional)

Se quiser gerar um relatório de cobertura, instale o pacote `coverage`:

```bash
pip install coverage
coverage run -m unittest discover -s tests
coverage report -m
```

## 📐 Padrões adotados

- **Estilo de código:** PEP 8 (nomes em `snake_case`, duas linhas em
  branco entre classes/funções, etc.)
- **Encapsulamento:** atributos privados (`self.__atributo`) expostos via
  `@property`
- **Padrão de projeto:** Factory Method (em desenvolvimento) para o envio
  de notificações/lembretes

## 📄 Licença

Projeto acadêmico desenvolvido para fins educacionais na disciplina de
Engenharia de Software (UDESC).
