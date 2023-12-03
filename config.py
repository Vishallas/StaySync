import os

class Config:
    SQLALCHEMY_TRACK_MODIFICATAION = False

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:cAEeCa3Fdb5-4GEC4DABc-g3*52de4f-@viaduct.proxy.rlwy.net:25770/railway"

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    
config={
    'development':DevelopmentConfig,
    'production':ProductionConfig,
    'default':DevelopmentConfig
}