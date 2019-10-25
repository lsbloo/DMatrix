#!/bin/bash
#Scripter Lsbloo

sudo apt-get install -y toilet
figlet=$(which figlet)
if [ -z $figlet ]; then
    sudo apt-get install -y figlet
fi
figlet Welcome to DistanceMatrix by: Lsbloo

echo ' '
echo '
Distance Matrix é uma ferramenta que tem como 
objetivo coletar e realizar calculos de distancias entre pontos geolocalizados. 
Cria pontos e raios entre uma serie de pontos demarcados.
    '
echo ' ' 
echo '
Distance Matrix is ​​a tool that aims to collect and perform distance calculations between geolocated points. 
Creates points and rays between a demarcated points.
    '

echo 'Como configurar e instalar.'
echo ' '
echo 'How to Build'

echo ' '
function dialog(){
	dialog=$(which dialog)
	path_dialog="/usr/bin/dialog"
	if [ $dialog == $path_dialog ]; then
		echo 'Dialog Installed'
	else
		sudo apt-get install -y dialog
	fi
}
dialog
function export_variables(){
	echo 'Carregue as seguintes variaveis de ambiente...'
	echo " "
	read -p "DATABASE NAME: " DATABASE_NAME
	read -p "DATABASE HOST: " DATABASE_HOST
	read -p "DATABASE USER: " DATABASE_USER
	read -p "DATABASE PASSWORD: " DATABASE_PASSWORD
	read -p "DATABASE PORT: " DATABASE_PORT
	read -p "GOOGLE_KEY_MATRIX: " GOOGLE_KEY_MATRIX
	read -p "GOOGLE_GEOCP_KEY: " GOOGLE_GEOCP_KEY
	read -p "PATH_SAVE_CSV: " PATH_SAVE_CSV

	if [ -z $DATABASE_NAME ]; then
		echo "Preencha o nome do banco de dados corretamente."
	fi
	if [ -z $DATABASE_HOST ]; then
		echo "Preencha o host no qual o bando de dados esta hospedado corretamente"
	fi
	if [ -z $DATABASE_USER ]; then
		echo 'Preencha o usuario do banco de dados corretamente'
	fi
	if [ -z $DATABASE_PASSWORD ]; then
		echo 'Preencha a senha do banco de dados corretamente'
	fi
	if [ -z $DATABASE_PORT ]; then
		echo 'Preencha a porta do bando de dados corretamente'
	fi
	if [ -z $GOOGLE_KEY_MATRIX ]; then
		echo 'Preencha a chave de distancia matrix corretamente'
	fi
	if [ -z $GOOGLE_GEOCP_KEY ]; then
		echo 'Preencha a chave de geolocalização do google corretamente'
	fi
	if [ -z $PATH_SAVE_CSV ]; then
		echo 'Preencha o Path para armazenar os arquivos gerados corretamente'
	fi
	export DATABASE_NAME=$DATABASE_NAME
	export DATABASE_HOST=$DATABASE_HOST
	export DATABASE_USER=$DATABASE_USER
	export DATABASE_PASSWORD=$DATABASE_PASSWORD
	export DATABASE_PORT=$DATABASE_PORT
	export GOOGLE_KEY_MATRIX=$GOOGLE_KEY_MATRIX
	export GOOGLE_GEOCP_KEY=$GOOGLE_GEOCP_KEY
	export PATH_SAVE_CSV=$PATH_SAVE_CSV
}
export_variables
cd .. ; pip install -r requeriments.txt
toilet -F border -F metal "OK!"