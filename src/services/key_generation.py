import secrets
import string

def generate_key(length: int = 64) -> str:
    """
    Генерирует криптографически безопасный случайный ключ.
    
    Args:
        length: длина ключа (по умолчанию 64 символа)
    
    Returns:
        Строка из букв и цифр указанной длины
    """
    alphabet = string.ascii_letters + string.digits
    return ''.join(secrets.choice(alphabet) for _ in range(length))