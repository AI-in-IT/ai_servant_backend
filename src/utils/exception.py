class DomainError(Exception):
    pass

# --- Семьи ---
class FamilyNotFoundError(DomainError):
    pass

class FamilyFullError(DomainError):
    pass

class InvalidInviteCodeError(DomainError):
    pass

# --- Пользователи ---
class UserNotFoundError(DomainError):
    pass

class AlreadyInFamilyError(DomainError):
    pass

class NotInFamilyError(DomainError):
    pass