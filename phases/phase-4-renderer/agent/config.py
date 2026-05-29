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


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_prefix="PULSE_",
        env_file=".env",
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
    llm_provider: str = "groq"               # "groq" | "anthropic" | "openai"
    llm_model: str = "llama-3.3-70b-versatile"
    groq_api_key: Optional[str] = None
    anthropic_api_key: Optional[str] = None
    openai_api_key: Optional[str] = None
    max_body_tokens: int = 512               # EC3-3: truncate long reviews before LLM

    # MCP server commands / URLs (populated in Phase 5/6)
    docs_mcp_command: Optional[str] = None
    docs_mcp_url: Optional[str] = None
    gmail_mcp_command: Optional[str] = None
    gmail_mcp_url: Optional[str] = None


def load_products(products_file: Path) -> list[ProductConfig]:
    """Load product configs from a YAML file."""
    if not products_file.exists():
        return []
    with products_file.open(encoding="utf-8") as f:
        data = yaml.safe_load(f) or {}
    return [ProductConfig.model_validate(p) for p in data.get("products", [])]


def get_product(key: str, products_file: Path) -> ProductConfig:
    """Look up a product by key, raising KeyError if not found."""
    products = load_products(products_file)
    by_key = {p.key: p for p in products}
    if key not in by_key:
        available = ", ".join(by_key.keys())
        raise KeyError(f"Product '{key}' not found. Available: {available}")
    return by_key[key]


settings = Settings()
