import os
from typing import Any

from config.settings import (
    SiteSettings, ApplicationSettings, DataBaseCredentials, AuthSettings,
    CORSSettings, SuperUsersSettings, DataBaseSettings
)

base_dir: str = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

app_config: dict[str, Any] = ApplicationSettings().dict()
site_config: dict[str, Any] = SiteSettings().dict()
cors_config: dict[str, Any] = CORSSettings().dict()
auth_config: dict[str, Any] = AuthSettings().dict()
super_users_config: dict[str, Any] = SuperUsersSettings().dict()
database_config: dict[str, Any] = DataBaseSettings().dict()
