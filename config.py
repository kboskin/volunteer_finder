# -*- coding: utf-8 -*-
import os
import shlex
from dataclasses import dataclass

import sentry_sdk

DEBUG = os.getenv('DEBUG') == 'True'


@dataclass
class CORS:
    allowed_origins = os.getenv("ALLOWED_ORIGINS", "").split(',')


@dataclass
class POSTGRES:
    user = os.getenv("POSTGRES_USERNAME", "postgres")
    password = os.getenv("POSTGRES_PASSWORD", "postgres")
    db = os.getenv("POSTGRES_DB", "finder_db")
    host = os.getenv("POSTGRES_HOST", "localhost")
    port = os.getenv("POSTGRES_PORT", "5432")


SQLALCHEMY_DATABASE_URI = (
    f"postgresql://{POSTGRES.user}:{POSTGRES.password}"
    f"@{POSTGRES.host}:{POSTGRES.port}/{POSTGRES.db}"
)

SQLALCHEMY_ECHO = False

SQLALCHEMY_TRACK_MODIFICATIONS = False


@dataclass
class SENTRY:
    dsn = os.getenv("SENTRY_DSN")
    environment = os.getenv("SENTRY_ENVIRONMENT")
    tags = os.getenv("SENTRY_TAGS")


@dataclass
class TWILIO:
    account_sid = os.getenv('TWILIO_ACCOUNT_SID')
    auth_token = os.getenv('TWILIO_AUTH_TOKEN')
    verify_sid = os.getenv('TWILIO_VERIFY_SID')
    enabled = os.getenv('TWILIO_SMS_CHECK_ENABLED') != 'False'


@dataclass
class AUTH:
    secret_key = os.getenv("SECRET_KEY")
    algorithm = os.getenv("ALGORITHM", "HS256")
    access_token_expire_minutes = os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30)


def init_sentry():
    if SENTRY.dsn:
        sentry_sdk.init(
            dsn=SENTRY.dsn,
            environment=SENTRY.environment
        )

    if SENTRY.tags:
        with sentry_sdk.configure_scope() as scope:
            for token in shlex.split(SENTRY.tags):
                scope.set_tag(*token.split('='))
