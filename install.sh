echo Installing pip
sudo apt-get -y install python3-pip

echo Installing Flask
pip3 install flask

echo Installing Flask for Sudo to use during bootup
sudo pip3 install flask

echo Setting server to autostart
sudo sed -i "`wc -l < /etc/rc.local`i\\python3 $PWD/main.py &\\" /etc/rc.local

