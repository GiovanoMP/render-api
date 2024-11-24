# teste.py
from app.config.settings import get_settings
from app.database import get_db, engine
from sqlalchemy import text

def test_database_connection():
    try:
        # Teste de conexão direto com o engine
        with engine.connect() as connection:
            result = connection.execute(text('SELECT COUNT(*) FROM transactions_sample'))
            print("Conexão bem sucedida!")
            print(f"Total de registros: {result.scalar()}")
    except Exception as e:
        print(f"Erro na conexão: {str(e)}")

if __name__ == "__main__":
    # Verificar configurações
    settings = get_settings()
    print("Configurações carregadas:")
    print(f"SUPABASE_URL: {'*' * len(settings.SUPABASE_URL)}")  # Por segurança
    print(f"DATABASE_URL: {'*' * len(settings.DATABASE_URL)}")   # Por segurança
    
    # Testar conexão
    test_database_connection()
