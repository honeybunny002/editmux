
import os

class Config:

    BOT_TOKEN = '5816246888:AAFlxo_PL-2Ea-rwlYRz5Nb8mWtyr64EgbM'
    APP_ID = '5080899'
    API_HASH = '6fc7f813cf96e6692990b752b43fd9c7'
    USERS = '1472904517, 1226841901, 1671626669, 866649963, 5160169373, 1958851206, 778988294, 947859478, 1157557110, 1772988300, 2135072465, 1363236962, 956022686, 5443081541'
    #comma seperated user id of users who are allowed to use
    ALLOWED_USERS = [x.strip(' ') for x in USERS.split(',')]

    DOWNLOAD_DIR = 'downloads'
