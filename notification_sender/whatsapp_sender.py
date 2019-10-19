
from twilio.rest import Client

# # client credentials are read from TWILIO_ACCOUNT_SID and AUTH_TOKEN
# client = Client('AC65bd2c4c594ae8a95b4eee45a1658080', '2c93326193e112ea5eda1fb62c410e0d')
#
# # this is the Twilio sandbox testing number
# from_whatsapp_number='whatsapp:+14155238886'
# # replace this number with your own WhatsApp Messaging number
# to_whatsapp_number='whatsapp:+554188487372'
#
# client.messages.create(body='Ola tudo bem',
#                        from_=from_whatsapp_number,
#                        to=to_whatsapp_number)


class SendWhatsApp:

    def __init__(self):
        self.client = Client('AC65bd2c4c594ae8a95b4eee45a1658080', '2c93326193e112ea5eda1fb62c410e0d')
        self.from_whatsapp_number = 'whatsapp:+14155238886'

    def sender(self, to_whatsapp_number, message):

        #cliente = Client('AC65bd2c4c594ae8a95b4eee45a1658080', '2c93326193e112ea5eda1fb62c410e0d')
        message = self.client.messages.create(body=message,
                               from_= self.from_whatsapp_number,
                               to='whatsapp:'+to_whatsapp_number)
        print(message)

if __name__ == '__main__':
    SendWhatsApp().sender('+554188487372', 'Envio de mensagem de WhatsApp via software do Spot That Fire')


