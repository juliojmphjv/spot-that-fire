
from twilio.rest import Client


class SendWhatsApp:

    def __init__(self):
        pass

    def sender(self, to_whatsapp_number, message):

        #cliente = Client('AC65bd2c4c594ae8a95b4eee45a1658080', '2c93326193e112ea5eda1fb62c410e0d')
        message = self.client.messages.create(body=message,
                               from_= self.from_whatsapp_number,
                               to=to_whatsapp_number)
        print(message)

if __name__ == '__main__':
    SendWhatsApp().sender('+5541988487372', 'Envio de mensagem de WhatsApp via software do Spot That Fire')