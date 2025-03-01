from io import BytesIO

from django.conf import settings
from qrcode import make
from weasyprint import HTML

from cash_register.checks.details.logger import Logger


def store_check(*, check_html: str, check_number: str, log: Logger) -> None:
    pdf_path = settings.MEDIA_ROOT / f"{check_number}.pdf"

    html = HTML(string=check_html)
    html.write_pdf(pdf_path)

    log.debug("check stored", check_number=check_number, pdf_path=pdf_path)


def png_qrcode_to_stored_check_when(*, check_number: str, log: Logger) -> bytes:
    check_downloading_link = (
        f"{settings.EXTERNAL_HOST_URL_PREFIX}"
        f"{settings.STATIC_URL}{check_number}.pdf"
    )
    qrcode_image = make(check_downloading_link)

    with BytesIO() as qrcode_stream:
        qrcode_image.save(qrcode_stream, "png")
        qrcode_stream.seek(0)
        qrcode = qrcode_stream.read()

    log.debug(
        "check png qrcode generated",
        check_number=check_number,
        qrcode_text=check_downloading_link,
    )

    return qrcode
