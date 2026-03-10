import app.core.exceptions as e


def test_app_exception_default_detail():
    exc = e.AppException()

    assert exc.status_code == 400
    assert exc.detail == "Application error"


def test_app_exception_custom_detail():
    exc = e.AppException(detail="Custom message")

    assert exc.detail == "Custom message"


def test_invalid_file_type_error_defaults():
    exc = e.InvalidFileTypeError()

    assert exc.status_code == 400
    assert exc.detail == "Invalid file type"


def test_file_not_provided_defaults():
    exc = e.FileNotProvided()

    assert exc.status_code == 400
    assert exc.detail == "File not provided"


def test_configs_not_provided_defaults():
    exc = e.ConfigsNotProvided()

    assert exc.status_code == 400
    assert exc.detail == "Configurations not provided"


def test_invalid_file_type_custom_detail():
    exc = e.InvalidFileTypeError(detail="Only CSV allowed")

    assert exc.detail == "Only CSV allowed"
