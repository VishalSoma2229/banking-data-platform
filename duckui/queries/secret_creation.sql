DROP SECRET IF EXISTS minio;

CREATE SECRET minio (
    TYPE S3,
    KEY_ID 'PASTE_MINIO_USERNAME',
    SECRET 'PASTE_MINIO_PASSWORD',
    REGION 'us-east-1',
    ENDPOINT 'localhost:8050',
    URL_STYLE 'path',
    USE_SSL false
);