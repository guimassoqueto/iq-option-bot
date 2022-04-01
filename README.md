# iq-option-bot
IQ Option Trading Bot

Token
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


python setup.py install
pip install -U git+git://github.com/iqoptionapi/iqoptionapi.git
pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
  
Adicionar em crontab -e:
# fecha os robos operando OTC (eurusd-otc eurjpy-otc usdjpy-otc), de segunda a quinta as 20:30
30 20 * * 1-4 /home/guilherme/Desktop/iq-option-bot/end.sh

# fecha os robos rodando OTC(eurusd-otc eurjpy-otc usdjpy-otc), domingo as 20:30
30 20 * * 7 /home/guilherme/Desktop/iq-option-bot/end.sh

# fecha os robos operando Forex (eurusd eurjpy usdjpy), sexta as 15:00
00 15 * * 5 /home/guilherme/Desktop/iq-option-bot/end.sh

