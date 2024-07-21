from base64 import b64encode
import json
import segno
import zlib

settings = {
    "general": {
        "server_url": "https://odk.dev.fmtm.hotosm.org/v1/key/Bwo51ECW4vR4Z$PvI8YMs5wo4l!1iTDhBUYTlZbKzV1ZBQpcV1r$ujBjtgOeZE8d/projects/56",
        "form_update_mode": "match_exactly",
        "basemap_source": "osm",
        "autosend": "wifi_and_cellular",
        "metadata_email": "NOT IMPLEMENTED",
        "metadata_username": "svcfmtm"
    },
    "project": {
        "name": "Kigali Example (@mit)"
    },
    "admin": {}
}

qr_data = b64encode(zlib.compress(json.dumps(settings).encode("utf-8")))

print(qr_data)

print(qr_data.decode('utf-8'))

code = segno.make(qr_data, micro=False)
code.save('settings.png', scale=5)
