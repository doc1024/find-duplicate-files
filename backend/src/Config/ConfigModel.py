from pydantic import BaseModel, Field
import json


class DatabaseConfig(BaseModel):
    db_type: str
    db_user: str
    db_password: str
    db_host: str
    db_port: str
    db_name: str


class APIConfig(BaseModel):
    api_host: str = "0.0.0.0"
    api_port: int = 8000
    api_log_level: str = "info"


class AppConfig(BaseModel):
    source: str
    destination: str
    batch_size: int
    api_endpoint: str
    api_token: str
    Database: DatabaseConfig
    API: APIConfig


def load_config(file_path: str) -> AppConfig:
    # Read JSON file
    with open(file_path, 'r') as file:
        config_data = json.load(file)

    # Validate individual configurations
    # AppConfig.model_validate_json(**config_data)
    app_config = AppConfig(**config_data)


    # Return a single object holding all validated configurations
    return AppConfig(app=app_config)