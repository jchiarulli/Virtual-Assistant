import subprocess
#subprocess.call(['pdftohtml', 'ECE_current-handbook.pdf'])

sauce = open('/home/jason/Repo/Virtual-Assistant/ENG_UG_HBs/ECE_current-handbooks.html')

textFile = open('ECE_current-handbook.txt', 'w')

import bs4 as bs

soup = bs.BeautifulSoup(sauce, 'lxml')

textFile.write(soup.body.text)
