U
    �%�^4  �                	   @   s�  d dl mZmZmZmZ d dlmZmZ d dlm	Z	 d dl
mZ d dl
mZ d dlmZ d dlZd dlZd dlZd dlZd dlZd dlZd dlZd dlZd dlZd dlZd dlmZ d d	l mZmZ d dlm	Z	 d d
lmZmZmZ d dlmZmZmZ d d	l mZmZ d dlm	Z	 d dlmZ d dlmZ d dlm Z m!Z" d dlmZ d dl#Z#e�$� Z%e%j&Z'e%j(Z)e%j*Z+d�,e'e)e+�Z-�zd dlZd dlm Z m.Z.m/Z/ ej!dd� e/j0e/j1 e j2 Z3e/j0Z4e/j5e j6 Z7e/j0e/j1 e j8 Z9e/j:e j; Z<e/j0e/j1 e j; Z=e/j:e j2 Z>e/j:e j? Z@e/j0e/j1 e j? ZAe/j:e jB ZCe/j0e/j1 e jB ZDe/j1e jE ZFe/j:e jE ZGe/j1e j2 d ZHe/j1e jB d ZIe/j1e jB d ZJW n   eKd� e�L�  Y nX e�MejNdk�r�dnd� e�O� ZPdZQdZRejSd ZTejU�Vd��s�e�Wd� eXejS�dk �r$eKd� eKd � eYd!�ZZeLd� eKe<d" � eKe>d# eT � eKe@d$ � eKd%� e[d&d'��Z\e\�]� Z^W 5 Q R X e�_e^�Z`e`d( Zae`d) Zbe`d* Zce`d+ Zde`d, Zee`d- Zfe`d. Zge`d/ Zhe`d0 Zie`d1 Zje`d2 Zke`d3 Zle`d4 Zme`d5 Zne`d6 Zoed7eT eQeR�Zpep�q�  ep�r� �s`zep�seT� ep�teTeYd8��ZuW n* ek
�r^   eYd9�Zvep�weTev�ZuY nX eKe3d: � ed� e�MejNdk�r�dnd� d;d<� ZxdVd>d?�ZyeKeDd@ e4 dA � ep�z� Z{eKe3� dBe{j|� �� eKeF� dCeT� �� ed� eKe3dD � ed� eKe3dE � ed� eKe3dF � ed� eKe3dG � ed� eKe3dH � eKe4dI � eKe=� dJe@� dKef� �� z*epeefefegdL�� eKeA� dJe3� dM�� W n   eKeDdN � Y nX ed� eKe=� dJe@� dKeh� �� z*epeeheheidL�� eKeA� dJe3� dM�� W n   eKeDdN � Y nX ed� eKe=� dJe@� dKej� �� z*epeejejekdL�� eKeA� dJe3� dM�� W n   eKeDdN � Y nX ed� eKe=� dJe@� dKel� �� z*epeelelemdL�� eKeA� dJe3� dM�� W n   eKeDdN � Y nX ed� eKe=� dJe@� dKen� �� z*epeeneneodL�� eKeA� dJe3� dM�� W n   eKeDdN � Y nX ed� eKd%� ep�}�  eKdO� ed� e�MdPeT� dQ�� e�MdPeT� dR�� e�MdPeT� dS�� e�MdPeT� dT�� e�MdPeT� dU�� dS )W�    )�TelegramClient�sync�events�errors)�GetHistoryRequest�GetBotCallbackAnswerRequest)�JoinChannelRequest)�SessionPasswordNeededError)�FloodWaitError)�sleepN)�BeautifulSoup)r   r   )r   r   �StartBotRequest)�UpdateShortMessage�ReplyInlineMarkup�KeyboardButtonUrl)r   )�datetime)�Fore�initz{}:{}:{})r   �Back�StyleT)Z	autoresetu
   『🔥』�[�]z"Please Install Modul Colorama!!


�nt�cls�cleari�� Z 7bbcc59e37d2f3a9a8d5acbfb6c22c2c�   �session�   z!Usage: python bch.py phone_numberzA-> Input number in international format (example: +639162995600)
zPress any key to exit...Z_____________zMencoba LogIn >>  z-------------� zcfg.json�rZ	walletbtcZ	walletltcZ	walletbchZ	walletzecZ
walletdoge�link1�code1�link2�code2�link3�code3�link4�code4�link5�code5zsession/z


[1;0mEnter Your Code : z[1;0mYour 2fa Password : zlogin berhasil 
c                 C   s2   t dtj t�� �d��  tj d| � � � d S )Nr   z%H:%M:%Sz] )�printr   �CYANr   Znow�strftimeZRESET)�message� r.   �main.py�print_msg_timeo   s    r0   �GETc                 C   s*   t j|| ddidd�}|j}|j}||gS )Nz
User-AgentzrMozilla/5.0 (Windows NT 10.0; Win32; x86) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36�   )Zheaders�timeout)�requestsZrequest�text�status_code)Zurl�methodZresponseZtext_responser6   r.   r.   r/   �get_responser   s    r8   uk  ╔══╗─╔══╗╔════╗╔═══╗╔═══╗╔═══╗╔═══╗╔═══╗
║╔╗║─╚╣─╝║╔╗╔╗║║╔═╗║║╔═╗║║╔══╝║╔═╗║║╔═╗║
║╚╝╚╗─║║─╚╝║║╚╝║║─║║║╚═╝║║╚══╗║╚═╝║║╚══╗
uk  ║╔═╗║─║║───║║──║║─║║║╔══╝║╔══╝║╔╗╔╝╚══╗║
║╚═╝║╔╣─╗──║║──║╚═╝║║║───║╚══╗║║║╚╗║╚═╝║
╚═══╝╚══╝──╚╝──╚═══╝╚╝───╚═══╝╚╝╚═╝╚═══╝
zWELCOME  : zNOMOR HP : u   
Fitur Script ⬇️
z#  Autorefferalz#  AutoVisitz#  AutoJoin Bot & Channelz#  5clickbot in 1scriptz4
##################################################
z[+]z  Mencoba Refferal )ZbotZpeerZstart_paramu     Succses 💯zSomething wrong.....zdissconnected....zpython mains.py z ltcz dogez zecz btcz bch)r1   )~Ztelethonr   r   r   r   Ztelethon.tl.functions.messagesr   r   Ztelethon.tl.functions.channelsr   Ztelethon.errorsr	   r
   �timer   Zjson�re�sys�osr4   ZrandomZcolorama�	threading�	itertoolsZbs4r   r   Ztelethon.tl.typesr   r   r   r   r   r   Z	color_amaZasyncio�	localtime�a�tm_hour�hr�tm_minZmn�tm_secZsc�formatZxtimer   r   Z	RESET_ALLZBRIGHTZGREENZhijau�resZDIMZWHITEZabu2ZBLUEZbiruZNORMALZMAGENTAZungu2ZunguZhijau2ZYELLOWZyellow2ZyellowZREDZred2Zredr+   ZcyanZcyan2ZdesZkur1Zkur2r*   �exit�system�namer   �cZapi_idZapi_hash�argvZphone_number�path�exists�makedirs�len�input�e�openZmyfile�read�data�loads�objZ
wallet_btcZ
wallet_ltcZ
wallet_bchZ
wallet_zecZwallet_doger    r!   r"   r#   r$   r%   r&   r'   r(   r)   ZclientZconnectZis_user_authorizedZsend_code_requestZsign_in�meZpassw�startr0   r8   Zget_meZmyselfZ
first_nameZ
disconnectr.   r.   r.   r/   �<module>   s2  P





