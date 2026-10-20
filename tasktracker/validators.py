class ValidationError(Exception):
    pass

def validate_task_title(title: str) -> str:
    if not title or not title.strip():
        raise ValidationError("Judul tugas tidak boleh kosong.")
    if len(title) > 100:
        raise ValidationError("Judul tugas tidak boleh melebihi 100 karakter.")
    return title.strip()

def validate_status(status: str) -> str:
    valid_statuses = ["PENDING", "COMPLETED"]
    normalized = status.upper().strip()
    if normalized not in valid_statuses:
        raise ValidationError(f"Status harus salah satu dari: {', '.join(valid_statuses)}")
    return normalized