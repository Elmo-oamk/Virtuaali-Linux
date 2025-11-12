[Unit]
Description=Gunicorn instance to serve Flask LEMP app
After=network.target

[Service]
User=elmo
Group=www-data
WorkingDirectory=/home/elmo/lemp-app
Environment="PATH=/home/elmo/lemp-app/venv/bin"
ExecStart=/home/elmo/lemp-app/venv/bin/gunicorn --workers 3 --bind 127.0.0.1:5000 app:app
Restart=always
RestartSec=5

[Install]
WantedBy=multi-user.target
