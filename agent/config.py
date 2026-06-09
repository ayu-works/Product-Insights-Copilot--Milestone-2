from pathlib import Path
from typing import Optional

import yaml
from pydantic import BaseModel, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class ProductConfig(BaseModel):
    key: str
    display: str
    appstore_id: Optional[str] = None
    play_package: Optional[str] = None
    gdoc_id: Optional[str] = None
    gmail_to: str = ""

    @field_validator("key")
    @classmethod
    def key_must_be_slug(cls, v: str) -> str:
        if not v.replace("-", "").replace("_", "").isalnum():
            raise ValueError(f"Product key must be alphanumeric: '{v}'")
        return v.lower()


# Single .env used by all phases — lives at phases/.env
# Falls back to project root .env so either location works.
_PHASES_DIR = Path(__file__).parent.parent.parent     # phases/
_ROOT_DIR   = _PHASES_DIR.parent                      # project root

ENV_FILE = _PHASES_DIR / ".env"   # canonical single location


def _env_files() -> tuple[Path, ...]:
    """Ordered list of .env files to load (later entry wins on conflict)."""
    return (_ROOT_DIR / ".env", ENV_FILE)


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_prefix="PULSE_",
        env_file=_env_files(),
        env_file_encoding="utf-8",
        extra="ignore",
    )

    db_path: Path = Path("data/pulse.db")
    log_level: str = "INFO"
    products_file: Path = Path("products.yaml")
    max_llm_cost_usd: float = 1.0
    max_tokens_per_run: int = 100_000
    confirm_send: bool = False
    random_seed: int = 42
    embedding_provider: str = "openai"
    live_network: bool = False

    # Phase 3 — LLM
    llm_provider: str = "groq"
    llm_model: str = "llama-3.3-70b-versatile"
    groq_api_key: Optional[str] = None
    anthropic_api_key: Optional[str] = None
    openai_api_key: Optional[str] = None
    max_body_tokens: int = 512

    # Phase 5 — Google Docs MCP
    docs_mcp_command: Optional[str] = None
    docs_mcp_url: Optional[str] = None
    # Default Google Doc ID — used when products.yaml has no gdoc_id for the product
    gdoc_id: Optional[str] = None

    # Phase 6 — Gmail MCP
    gmail_mcp_command: Optional[str] = None
    gmail_mcp_url: Optional[str] = None
    # Default recipient — used when products.yaml has no gmail_to for the product
    gmail_to: Optional[str] = None
    # Sender address shown in the From header (must match the OAuth account)
    gmail_from: str = ""

    # Phase 7 — orchestration & observability
    otel_exporter_endpoint: Optional[str] = None
    mcp_retry_wait_seconds: int = 10
    mcp_max_retries: int = 1
    cost_spike_multiplier: float = 3.0


def load_products(products_file: Path) -> list[ProductConfig]:
    if not products_file.exists():
        return []
    with products_file.open(encoding="utf-8") as f:
        data = yaml.safe_load(f) or {}
    return [ProductConfig.model_validate(p) for p in data.get("products", [])]


def get_product(key: str, products_file: Path) -> ProductConfig:
    products = load_products(products_file)
    by_key = {p.key: p for p in products}
    if key not in by_key:
        available = ", ".join(by_key.keys())
        raise KeyError(f"Product '{key}' not found. Available: {available}")
    return by_key[key]


settings = Settings()
