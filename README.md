# proxy.wsgi
python web proxy using nginx and wsgi


deb package to install
python3 uwsgi_python34 nginx-full



Nginx conf:

add  to your  nginx virtual host

location /api/ {
        include uwsgi_params;
        uwsgi_pass unix:///tmp/uwsgi.sock;
}

start your Nginx server or relaod conf



uwsgi launch command
cd folder
uwsgi_python34  uwsgi.ini
