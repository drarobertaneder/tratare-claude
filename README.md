# Tratare

Repositório de **administração** do consultório odontológico Tratare (bairro Ouro
Preto, Belo Horizonte/MG). Reúne duas coisas que trabalham juntas:

1. **Cofre de conhecimento** — base versionada de conhecimento administrativo
   (decisões, financeiro, equipe, fornecedores, procedimentos, conformidade…).
2. **Extração de dados da Clinicorp** — script Python que baixa os dados da
   clínica pela API e exporta para Excel/CSV, alimentando as análises do cofre.

> **Privacidade (LGPD):** este repositório é para a administração do consultório.
> Não contém prontuário nem dados clínicos identificáveis de pacientes. Números de
> pacientes aparecem sempre em forma agregada/anonimizada. As saídas brutas de
> extração (`export/`) e credenciais reais (`.env`) ficam **fora** do versionamento.

---

## 1. Cofre de conhecimento

O comportamento operacional, os princípios e as convenções estão em
[`CLAUDE.md`](./CLAUDE.md). A porta de entrada do conteúdo é o
[`indice.md`](./indice.md).

Estrutura:

- `bruto/` — fontes imutáveis (atas, NFs/orçamentos, relatórios, agenda)
- `decisoes/` — decisões com justificativa
- `financeiro/`, `equipe/`, `fornecedores-e-estoque/`, `marketing/`,
  `procedimentos/`, `conformidade/`, `relacionamento/` — conhecimento trabalhado
- `indice.md` — mapa mestre · `log.md` — histórico · `perguntas-em-aberto.md`

---

## 2. Extração de dados via API da Clinicorp

Script em Python para autenticar na API da Clinicorp, baixar os dados da clínica
e exportar para Excel/CSV para tratar localmente.

### Pré-requisitos

1. **Credenciais de API da Clinicorp.** O acesso é por assinante e **não** sai
   sozinho pela tela do sistema — abra um chamado com o suporte da Clinicorp
   pedindo "acesso à API de integração". Eles enviam o `subscriber` e o token.
2. Python 3.10+ instalado.

### Instalação

```powershell
pip install -r requirements.txt
copy .env.example .env
```

Depois edite o `.env` com as credenciais e confirme a base URL / nomes de header
contra o Swagger oficial: <https://sistema.clinicorp.com/api-docs/>

### Testar a conexão

```powershell
python clinicorp_client.py
```

### Baixar e exportar os dados

```powershell
# Excel (uma aba por domínio)
python pull_data.py --inicio 2026-01-01 --fim 2026-06-06

# CSV (um arquivo por domínio)
python pull_data.py --inicio 2026-01-01 --fim 2026-06-06 --formato csv
```

Os arquivos saem na pasta `export/` (não versionada).

### Domínios cobertos

`analytics`, `appointment` (agenda), `patient`, `estimates` (orçamentos),
`financial`, `sales`, `payment`.

### Importante — ajustar contra o Swagger

Os nomes exatos dos endpoints, parâmetros e headers de autenticação ficam no
Swagger interativo (que exige login). No código, os pontos a confirmar estão
marcados com `# >>> CONFIRMAR`. Ao ver o formato real de uma resposta, ajuste os
wrappers em `clinicorp_client.py` se necessário.
