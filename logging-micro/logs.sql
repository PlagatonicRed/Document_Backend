CREATE TABLE IF NOT EXISTS logs (
log_time TEXT NOT NULL DEFAULT( STRFTIME('%Y-%m-%d %H:%M:%f', 'now')),
event TEXT NOT NULL,
username TEXT NOT NULL,
filename TEXT);

DROP TABLE IF EXISTS logs;