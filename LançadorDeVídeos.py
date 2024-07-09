import time
import subprocess
import webbrowser
import ctypes

def abrir_video_local(caminho_video):
    if caminho_video:
        subprocess.Popen(['start', caminho_video], shell=True)  
    else:
        abrir_video()


def abrir_video():
    url = "https://www.youtube.com/watch?v=b3QSl1Ixd4I&pp=ygUWNSBtaW4gZXNjb2xhIHNhYmF0aW5hIA%3D%3D"  
    webbrowser.open(url)


def exibir_alerta(mensagem):
    ctypes.windll.user32.MessageBoxW(0, mensagem, "Alerta", 0x40 | 0x1)  # 0x40 = MB_ICONINFORMATION, 0x1 = MB_OK


hora_desejada = "10:00"
caminho_video = r"C:\Users\Lucasptrick\Videos\EscolaSabatina.mp4"  
while True:
    hora_atual = time.strftime("%H:%M") 
    if hora_atual == hora_desejada:
        mensagem = '''O vídeo de 5Min finais da Escola Sabatina será iniciado! 
Lembre-se de transmitir para o telão: [Windows - Shift - Seta]'''
        exibir_alerta(mensagem)
        abrir_video_local(caminho_video)
        time.sleep(5*60)
        break
    
    time.sleep(1)
