# proxy.wsgi
python web proxy using nginx and wsgi


debian package to install
  python3 uwsgi_python34 nginx-full



Nginx conf:

add  to your  nginx virtual host

  location /proxy/ {
          include uwsgi_params;
          uwsgi_pass unix:///tmp/web_proxy_uwsgi.sock;
  }

start your Nginx server or relaod conf

  service nginx reload



uwsgi launch command

  cd ~/web_proxy_app/ &&  uwsgi_python34 uwsgi.ini
