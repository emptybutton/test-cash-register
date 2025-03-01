from io import BytesIO

import qrcode
from django.conf import settings
from weasyprint import HTML


def store_check(*, check_html: str, check_number: str) -> None:
    html = HTML(string=check_html)
    html.write_pdf(settings.MEDIA_ROOT / f"{check_number}.pdf")


def png_qrcode_to_stored_check_when(*, check_number: str) -> bytes:
    check_downloading_link = (
        f"{settings.EXTERNAL_HOST_URL_PREFIX}"
        f"{settings.STATIC_URL}{check_number}.pdf"
    )
    qrcode_image = qrcode.make(check_downloading_link)

    with BytesIO() as qrcode_stream:
        qrcode_image.save(qrcode_stream, "png")
        qrcode_stream.seek(0)
        return qrcode_stream.read()
