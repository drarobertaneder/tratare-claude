"""
Baixa os dados da Clinicorp e exporta para Excel/CSV na pasta ./export.

Uso:
    python pull_data.py --inicio 2026-01-01 --fim 2026-06-06
    python pull_data.py --inicio 2026-01-01 --fim 2026-06-06 --formato csv

Os dados puxados: analytics, agendamentos, pacientes, orcamentos,
financeiro, vendas e pagamentos (conforme prioridade definida).
"""

import argparse
import os
from datetime import date

import pandas as pd

from clinicorp_client import ClinicorpClient, ClinicorpError

EXPORT_DIR = "export"


def to_dataframe(data) -> pd.DataFrame:
    """Normaliza a resposta da API (lista ou dict) em DataFrame."""
    if data is None:
        return pd.DataFrame()
    if isinstance(data, dict):
        # Tenta achar a lista dentro do dict (ex.: {"items": [...]}).
        for value in data.values():
            if isinstance(value, list):
                return pd.json_normalize(value)
        return pd.json_normalize(data)
    if isinstance(data, list):
        return pd.json_normalize(data)
    return pd.DataFrame()


def main():
    parser = argparse.ArgumentParser(description="Extrai dados da Clinicorp via API.")
    parser.add_argument("--inicio", required=True, help="Data inicial AAAA-MM-DD")
    parser.add_argument("--fim", default=date.today().isoformat(), help="Data final AAAA-MM-DD")
    parser.add_argument("--formato", choices=["excel", "csv"], default="excel")
    args = parser.parse_args()

    client = ClinicorpClient()
    os.makedirs(EXPORT_DIR, exist_ok=True)

    # (nome, funcao) -> cada item vira uma aba/arquivo
    tarefas = [
        ("analytics", lambda: client.analytics(args.inicio, args.fim)),
        ("agendamentos", lambda: client.appointments(args.inicio, args.fim)),
        ("pacientes", lambda: client.patients()),
        ("orcamentos", lambda: client.estimates(args.inicio, args.fim)),
        ("financeiro", lambda: client.financial(args.inicio, args.fim)),
        ("vendas", lambda: client.sales(args.inicio, args.fim)),
        ("pagamentos", lambda: client.payments(args.inicio, args.fim)),
    ]

    resultados: dict[str, pd.DataFrame] = {}
    for nome, fn in tarefas:
        try:
            df = to_dataframe(fn())
            resultados[nome] = df
            print(f"[ok]   {nome}: {len(df)} linhas")
        except ClinicorpError as e:
            print(f"[erro] {nome}: {e}\n")

    if not resultados:
        print("Nenhum dado retornado. Verifique credenciais e endpoints no .env.")
        return

    periodo = f"{args.inicio}_a_{args.fim}"
    if args.formato == "excel":
        caminho = os.path.join(EXPORT_DIR, f"clinicorp_{periodo}.xlsx")
        with pd.ExcelWriter(caminho, engine="openpyxl") as writer:
            for nome, df in resultados.items():
                (df if not df.empty else pd.DataFrame({"vazio": []})).to_excel(
                    writer, sheet_name=nome[:31], index=False
                )
        print(f"\nExportado: {caminho}")
    else:
        for nome, df in resultados.items():
            caminho = os.path.join(EXPORT_DIR, f"clinicorp_{nome}_{periodo}.csv")
            df.to_csv(caminho, index=False, encoding="utf-8-sig")
            print(f"Exportado: {caminho}")


if __name__ == "__main__":
    main()
