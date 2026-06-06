"""
Cliente HTTP para a API da Clinicorp.

A autenticacao e a base URL sao configuraveis via variaveis de ambiente (.env),
porque a Clinicorp libera as credenciais por assinante e o esquema exato
(nomes de headers / basic auth) vem junto com elas.

Referencia oficial dos endpoints: https://sistema.clinicorp.com/api-docs/

Pontos marcados com  # >>> CONFIRMAR  devem ser checados contra o Swagger /
contra o e-mail de credenciais que o suporte da Clinicorp enviar.
"""

import os
from typing import Any, Optional

import requests
from dotenv import load_dotenv

load_dotenv()


class ClinicorpError(RuntimeError):
    """Erro de chamada a API da Clinicorp (status != 2xx)."""


class ClinicorpClient:
    def __init__(
        self,
        base_url: Optional[str] = None,
        subscriber: Optional[str] = None,
        api_key: Optional[str] = None,
        auth_mode: Optional[str] = None,
        username: Optional[str] = None,
        password: Optional[str] = None,
        timeout: int = 30,
    ):
        self.base_url = (base_url or os.getenv("CLINICORP_BASE_URL", "")).rstrip("/")
        self.subscriber = subscriber or os.getenv("CLINICORP_SUBSCRIBER", "")
        self.api_key = api_key or os.getenv("CLINICORP_API_KEY", "")
        self.auth_mode = (auth_mode or os.getenv("CLINICORP_AUTH_MODE", "headers")).lower()
        self.username = username or os.getenv("CLINICORP_USERNAME", "")
        self.password = password or os.getenv("CLINICORP_PASSWORD", "")
        self.timeout = timeout

        if not self.base_url:
            raise ValueError("CLINICORP_BASE_URL nao configurada (veja o .env).")

        self.session = requests.Session()
        self._configure_auth()

    def _configure_auth(self) -> None:
        """Monta headers / auth conforme o modo escolhido."""
        self.session.headers.update({"Accept": "application/json"})

        if self.auth_mode == "basic":
            # Basic Auth: usuario:senha
            self.session.auth = (self.username, self.password)
        else:
            # Modo "headers": subscriber + chave de API.
            # >>> CONFIRMAR os nomes exatos dos headers no Swagger.
            #     Comumente sao "subscriber" e "x-api-key".
            self.session.headers.update(
                {
                    "subscriber": self.subscriber,
                    "x-api-key": self.api_key,
                }
            )

    def get(self, path: str, params: Optional[dict] = None) -> Any:
        """GET generico em qualquer endpoint da API. `path` ex.: '/appointment'."""
        url = f"{self.base_url}/{path.lstrip('/')}"
        resp = self.session.get(url, params=params, timeout=self.timeout)
        if not resp.ok:
            raise ClinicorpError(
                f"{resp.status_code} {resp.reason} em GET {url}\n"
                f"params={params}\nresposta={resp.text[:500]}"
            )
        return resp.json()

    # ------------------------------------------------------------------ #
    # Wrappers por dominio. Os paths e parametros abaixo seguem os modulos
    # documentados (analytics, appointment, patient, estimates, financial,
    # sales, payment). >>> CONFIRMAR cada path/param no Swagger.
    # ------------------------------------------------------------------ #

    def analytics(self, start_date: str, end_date: str, **extra) -> Any:
        """Indicadores consolidados no periodo (orcamentos, vendas, despesas...)."""
        return self.get("/analytics", {"start_date": start_date, "end_date": end_date, **extra})

    def appointments(self, start_date: str, end_date: str, **extra) -> Any:
        """Agendamentos no periodo (total, faltas, ocupacao da agenda...)."""
        return self.get("/appointment", {"start_date": start_date, "end_date": end_date, **extra})

    def patients(self, **params) -> Any:
        """Cadastro de pacientes."""
        return self.get("/patient", params)

    def estimates(self, start_date: str, end_date: str, **extra) -> Any:
        """Orcamentos (status, profissional, valor, procedimentos)."""
        return self.get("/estimates", {"start_date": start_date, "end_date": end_date, **extra})

    def financial(self, start_date: str, end_date: str, **extra) -> Any:
        """Lancamentos financeiros no periodo."""
        return self.get("/financial", {"start_date": start_date, "end_date": end_date, **extra})

    def sales(self, start_date: str, end_date: str, **extra) -> Any:
        """Vendas no periodo."""
        return self.get("/sales", {"start_date": start_date, "end_date": end_date, **extra})

    def payments(self, start_date: str, end_date: str, **extra) -> Any:
        """Pagamentos no periodo."""
        return self.get("/payment", {"start_date": start_date, "end_date": end_date, **extra})


if __name__ == "__main__":
    # Teste rapido de conexao/autenticacao.
    client = ClinicorpClient()
    print("Base URL:", client.base_url)
    print("Modo de auth:", client.auth_mode)
    try:
        print(client.analytics("2026-01-01", "2026-01-31"))
    except ClinicorpError as e:
        print("Falhou a chamada de teste:\n", e)
