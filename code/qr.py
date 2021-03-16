import qrcode
from qrcode.image.pure import PymagingImage
from cv2 import putText, getTextSize, imread


class qrCode:
    def __init__(self, box_size=50, border=10):
        self.box = box_size
        self.border = border
        self.qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=self.box,
            border=self.border,
        )
    
    def simpleQr(self, chave, nome=None):
        if nome == None:
            nome = chave
        self.qr.add_data(chave)
        self.qr.make(fit=True)
        img = self.qr.make_image(fill_color="black", back_color="white")
        with open('qr.png', 'wb') as f:
            img.save(f)
        imagem = imread('qr.png',cv2.IMREAD_UNCHANGED)
        textsize = getTextSize(nome, cv2.FONT_HERSHEY_SIMPLEX, 2, 2)[0]
        textX = (imagem.shape[1] - textsize[0]) / 2 # Centralizar X
        # textY = (imagem.shape[0] + textsize[1]) / 2 # Centralizar Y
        posicao = (int(textX), 50)
        putText(
            imagem, # Array numpy no qual o texto está inserido
            nome, #Texto
            posicao, # Posição de início da escrita
            cv2.FONT_HERSHEY_SIMPLEX, # Font family
            2, # Font Size
            (0, 0, 0, 255), # Font Color
            3) #Font stroke
        imwrite('qr.png', imagem)
        
# qr = qrCode()
# qr.simpleQr('129038139sadsa6dsa51d65a1s51d5*¨¨%$%$##@$#@@!0338093280180')
