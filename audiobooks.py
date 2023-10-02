import PyPDF2
import pyttsx3
pdfreader = PyPDF2.PdfReader("bitcoin.pdf")

speaker = pyttsx3.init()

for page_num in range(len(pdfreader.pages)):
    text2 = pdfreader.pages[page_num]
    text = text2.extract_text()
    clean_text = text.strip().replace('\n',' ')
    #print(clean_text)
print("successfully read!")
speaker.save_to_file(clean_text,'podcast.mp3')
print("saved. playing NOW")

speaker.runAndWait()

speaker.stop()
