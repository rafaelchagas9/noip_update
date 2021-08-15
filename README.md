# Atualizar IPV6 na plataforma NO IP

## Info
Este script foi criado para resolver um problema incomum que eu tinha. Minha provedora de internet utiliza CGNAT e meu IPv6 muda com frequência, então utilizo o serviço NO IP 
para criar um DNS dinâmico, porém o programa disponibilizado por eles atualiza apenas o IPv4, por isso criei esse script simples que utiliza a API gratuito deles
para atualizar o meu IPv6.

## Observações
O repositório vem com um arquivo config que deve ser alterado de acordo com seu usuário e hostname, se você não tiver um você pode ver [aqui](https://www.noip.com/support/knowledgebase/create-hostname-ipv6-address-aaaa-record-support-question-day/) como criar.
Este script não atualiza apenas o IPv6, ele também atualiza o IPv4.
### IPv4
Lembre-se que se você quiser acessar sua rede local através da internet você irá precisar redirecionar as portas no seu roteador.
### IPv6
Caso você esteja utilizando IPv6 você precisa apenas certificar-se de que a configuração do firewall do seu roteador permite solicitações de fora da rede local.



## API's  utilizadas
* [NO IP API](https://www.noip.com/integrate/request)
* [API para obter o IPV6](http://v6.ipv6-test.com/api/myip.php)
