---
titulo: Guia Operacional — Cofre de Conhecimento Tratare
proposito: Núcleo enxuto carregado em toda sessão. Define princípios, convenções, roteamento e rituais do cofre.
atualizado: 2026-06-06
---

# Cofre de Conhecimento — Consultório Tratare

Guia operacional **sempre presente**. Toda sessão começa por aqui. Este arquivo é
o núcleo enxuto: carrega leve toda vez. Procedimentos longos vivem em
`procedimentos/` e só são lidos quando o gatilho deles dispara.

## Identidade

- **Clínica:** Tratare — bairro Ouro Preto, Belo Horizonte/MG.
- **Perfil:** clínico geral, ortodontia, implante, estética, prótese, endodontia,
  facetas e lentes, odontopediatria, entre outros. **2 cadeiras. Só particular
  (sem convênio).**
- **Administração:** Roberta (protesista).
- **Equipe:** "equipe Tratare".
- **Vocabulário interno:** recall · manutenção de orto · follow-up.
- **Idioma:** estrutura (pastas, arquivos, etiquetas) em **português**; conteúdo
  das páginas em **português**.

## Os seis princípios (condensados)

1. **O cofre é a memória.** O conhecimento vive em arquivos versionados, não no
   histórico de conversa. Conversas e modelos acabam; o cofre permanece.
2. **Bruto ≠ trabalhado.** Fontes cruas vão para `bruto/` e **nunca** são
   editadas. A IA destila essas fontes em páginas vivas nas demais pastas, sempre
   com rastro de volta à fonte.
3. **Integrar, não acumular.** Cada nova fonte é costurada ao que já existe:
   enriquece uma página, adiciona um link, mantém a coerência. O valor é o mapa
   navegável, não a pilha de arquivos.
4. **Tudo tem um endereço.** Cada tipo de conteúdo tem destino previsível (ver
   Tabela de Roteamento). Nunca crie uma pasta de topo em silêncio.
5. **Núcleo enxuto, detalhe sob demanda.** Este `CLAUDE.md` + `indice.md` +
   últimas linhas do `log.md` bastam para começar. Procedimentos longos só
   carregam sob gatilho.
6. **Só a fonte vira fato.** Nada fora da fonte é escrito como fato. Conflitos
   guardam os dois lados em `perguntas-em-aberto.md`; nunca sobrescreva em
   silêncio. Suposições são marcadas como hipótese.

## Regra de privacidade (LGPD) — inegociável

Este cofre é para a **administração** do consultório, não para prontuário. **Nunca
armazene dados clínicos identificáveis de pacientes** (nome junto de diagnóstico,
imagens, radiografias, histórico de saúde). Dado de saúde é dado pessoal sensível.
Ao trabalhar números de pacientes, use **agregados ou anonimização** (ex.: "23
recalls em maio", não "Maria Fulana, canal no dente 26"). Prontuário e dados
clínicos ficam no sistema próprio do consultório.

## Conduta da IA

- Antes de agir em algo consequente, ambíguo ou difícil de reverter: **declare a
  suposição e apresente alternativas**, em vez de decidir sozinha. Em coisas
  baratas e reversíveis: apenas faça.
- Se encontrar algo estranho ou contraditório ao editar, **sinalize**; não
  "conserte" o que não foi pedido. Conflito vira Pergunta em Aberto, nunca
  sobrescreve.

## Tabela de Roteamento (onde cada coisa mora)

| Conteúdo que chega / é produzido | Destino |
|---|---|
| Atas de reunião (cru) | `bruto/atas/` |
| NFs e orçamentos de fornecedores (cru) | `bruto/notas-e-orcamentos/` |
| Relatórios financeiros, faturamento (cru) | `bruto/relatorios-financeiros/` |
| Exportações de agenda, no-show (cru) | `bruto/agenda/` |
| Decisões com justificativa | `decisoes/` |
| Faturamento, custos, fluxo de caixa, inadimplência, resumo mensal/KPIs | `financeiro/` |
| Escala, funções, treinamentos, avaliações da equipe | `equipe/` |
| Materiais, comparação de fornecedores, controle de estoque, compras | `fornecedores-e-estoque/` |
| Captação, redes sociais, indicações, campanhas | `marketing/` |
| POPs e fluxos (agendamento, confirmação, recall, manutenção de orto, follow-up, cobrança) | `procedimentos/` |
| CRO, Vigilância Sanitária, LGPD, alvarás, contratos | `conformidade/` |
| Satisfação, taxa de retorno, recall (sempre agregado) | `relacionamento/` |
| Hipóteses, conflitos, incógnitas | `perguntas-em-aberto.md` |

## Rituais

### Protocolo de Início (toda sessão, nesta ordem)
1. Ler este `CLAUDE.md`.
2. Ler `indice.md` (o mapa).
3. Ler as últimas entradas do `log.md`.
4. **NÃO re-entrevistar.** A estrutura já existe; siga a partir dela.

### Tríade de Promoção (todo conhecimento durável)
Ao promover algo de bruto para trabalhado, faça os três — pular um quebra a
integração:
1. **Página** — cria/enriquece a página viva no destino certo.
2. **Link no índice** — registra/atualiza a entrada em `indice.md`.
3. **Linha no log** — acrescenta uma linha datada em `log.md`.

## Gatilho `revisar` (manutenção preventiva)

Quando a usuária pedir **`revisar`**, faça uma varredura de saúde do mapa:
- (a) todo link interno resolve (sem links quebrados);
- (b) toda página é alcançável a partir do `indice.md`;
- (c) toda página durável tem uma linha no `log.md` (tríade completa).

**Reporte as quebras; não conserte a estrutura sozinha sem perguntar.**

## Convenções de nome

- Arquivos e pastas em português, minúsculas, com hífen: `resumo-financeiro-2026-05.md`.
- Fontes cruas em `bruto/` recebem prefixo de data quando fizer sentido:
  `2026-05-12-ata-equipe.md`.
- Links internos no estilo `[[arquivo]]` ou caminho relativo Markdown.
- Datas no formato `AAAA-MM-DD`.
