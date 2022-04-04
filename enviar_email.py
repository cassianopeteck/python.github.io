import smtplib
import ssl
import email.message

#from smtplib import (SMTP, ehlo, startls, login, sendmail, quit)
setor = 'B'
equipe = 'Equipe do financeiro'

subject = email.message.Message()
subject['Subject'] = f"Planilha Financeira - departamento: {setor}"
body = f"""
<p>Olá {equipe}! </p>
</p>Segue em anexo a planilha com os resultados deste mês</p>

<p>Atenciosamente,</p>

<p>Gerente ADM</p>
"""


subject['From'] = 'cassianopeteck@gmail.com'
password = 'yuKas27$'
subject['To'] = 'colombo1719cassiano@gmail.com'
subject.add_header('Content-Type', 'text/html')
subject.set_payload(body)


"""conexao = SMTP('smtp.gmail.com', 587)
conexao.ehlo()
conexao.starttls()
conexao.login(de, sen)
conexao.sendmail(de, para, msg)
conexao.quit()
"""
context = ssl.create_default_context()
with smtplib.SMTP('smtp.gmail.com', 587) as conexao:
    conexao.ehlo()
    conexao.starttls(context=context) #TLS é mais seguro que o SSL, é recomendo utilizar ambos pois o sistema fará a criação de certificados de segurança, criptografias e configurações de protocolo
    conexao.login(subject['From'], password)
    conexao.sendmail(subject['From'], subject['To'], msg.as_string().encode('utf-8'))