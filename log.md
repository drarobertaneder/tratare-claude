---
titulo: Log de Operações — Cofre Tratare
proposito: Histórico append-only. Toda página durável criada/alterada deixa uma linha aqui.
atualizado: 2026-06-06
---

# Log de Operações

Append-only (só acrescenta, no topo da lista). Formato: `AAAA-MM-DD — descrição`.

- 2026-06-06 — Versionamento: instalado Git 2.54, `git init` (branch `main`), `.gitignore` protegendo `.env` e `export/`, README mesclado (cofre + extração Clinicorp), commit inicial e remote `origin` → github.com/drarobertaneder/tratare-claude.git. Renomeação da pasta para `tratare-claude` pendente (bloqueada com a sessão aberta).
- 2026-06-06 — Achado: a pasta já continha um projeto Python de extração da API Clinicorp (`clinicorp_client.py`, `pull_data.py`, `requirements.txt`, `.env.example`, README próprio), criado antes do cofre. Mantido e incluído no repositório; README mesclado para cobrir os dois. Ver [[perguntas-em-aberto]].
- 2026-06-06 — Inicialização do cofre. Criados `CLAUDE.md`, `AGENTS.md`, `indice.md`, `log.md`, `perguntas-em-aberto.md` e o esqueleto de pastas (`bruto/`, `decisoes/`, `financeiro/`, `equipe/`, `fornecedores-e-estoque/`, `marketing/`, `procedimentos/`, `conformidade/`, `relacionamento/`). Taxonomia confirmada por Roberta. Consultório só particular (sem convênio).
