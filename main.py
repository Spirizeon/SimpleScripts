import PyPDF2,pyttsx3
pdfreader = PyPDF2.PdfFileReader(open("karna's wife(1).pdf",'rb'))
speaker = pyttsx3.init()

for page_num in range(pdfreader.numPages):
    text = pdfreader.getPage(page_num).extractText()
    clean_text = text.strip().replace('\n',' ')
    print(clean_text)

speaker.save_to_file(clean_text,'story.mp3')
speaker.runAndWait()

speaker.stop()