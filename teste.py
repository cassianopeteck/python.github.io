import pydf

pdf = pydf.generate_pdf('<h1>Meu pdf gerado através do python</h1>')
with open('meu_pdf.pdf','wb') as f:
    f.write(pdf)