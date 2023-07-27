
# Common steps

- [Docs](https://splash.readthedocs.io/en/stable/)
- disable JS: Ctrl Shift P
- Install Docker:
+sudo apt-get update
  
sudo apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg-agent \
    software-properties-common

        + curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

sudo add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable"

        + sudo apt-get update
        + sudo apt-get install docker-ce docker-ce-cli containerd.io


    - pull Splash:
        + sudo docker pull scrapinghub/splash
        + sudo docker run -it -p 8050:8050 scrapinghub/splash
        + http://127.0.0.1:8050

# Now try scrapy-playwright
