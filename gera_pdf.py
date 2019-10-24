import os

path = os.getcwd() #os.path.abspath(__file__)


resolucao= "--window-size=1920,1080"
#resolucao= "--window-size=800,600" #Resolucao menor
#Gera o slide perguntado e pode visualizar a image

#--print-to-pdf
def list_files1(directory, extension):
    return (f for f in os.listdir(directory) if f.endswith('.' + extension))


def gerar_slide_atual():
	for file in list_files1(".", "html"):
		res = input("Neste arquivo "+file+" (s/n)?")
		if (res!="s"):
			continue
		while True:
			slide = int(input("Qual slide gerar em "+file+"?"))
			cmd = "google-chrome --headless --screenshot "+resolucao+"  --default-background-color=0 file://"+path+os.sep+file+"#/"+str(slide)+"/1"
			print(cmd)
			os.system(cmd)
			print("Slide gerado com sucesso, para sair CRTL+D")
			


def gerar_todos_pdf():
	for file in list_files1(".", "html"):
		res = input("Neste arquivo "+file+" (s/n)?")
		if (res!="s"):
			continue
		qtd = int(input("Quantos slides em "+file+"?"))
		
		for i in range(qtd):
			cmd = "google-chrome --headless --screenshot "+resolucao+" --default-background-color=0 file://"+path+os.sep+file+"#/"+str(i)+"/1"
			print(cmd)
			os.system(cmd)
			os.rename('screenshot.png', 'screenshot_'+str(i).zfill(3)+'.png')
				
		os.system("convert *.png "+file+".pdf")
		for i in range(qtd): 
			os.remove('screenshot_'+str(i).zfill(3)+'.png')

# Gerar o pdf de tudo?
if True:
	gerar_todos_pdf()
# Gera o png apenas de um slide?
if False:
	gerar_slide_atual()





