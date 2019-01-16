import unicodedata
from random import shuffle

QusetionFileName="ques"

######## finding number of questin in MyExam.tex in line 25
NumberOfQuestion=30
import re
pattern = re.compile("\\\\newcommand{\\\\questionCount}{[0-9]*")
for i, line in enumerate(open('MyExam.tex', encoding='utf-8',mode="r")):
    match = pattern.search(line)
    if match:
    	pattern=re.compile("[0-9]+")
    	match = pattern.search(match.group())
    	if match:
        	NumberOfQuestion=int(match.group())
        	break


######## generating all question files which each one should be completed by examiner later
for i in range(1, NumberOfQuestion+1): 
	myfile = open("{:s}{:02d}0.tex".format(QusetionFileName,i), encoding='utf-8',mode="w") 
	print("{}{}\n\\\\\n{}\n\\\\\n{}\n\\\\\n{}\n".format("سوال",i,"خط دوم","خط سوم","خط چهارم"),file=myfile)
	if i==1:
		print("\\renewcommand{\\qestionType}{op2}",file=myfile)
	myfile.close()
	for j in range(1,5):
		myfile = open("{:s}{:02d}{:d}.tex".format(QusetionFileName,i,j), encoding='utf-8',mode="w") 
		if j==1:
			print("\\correct% یعنی گزینه صحیح",file=myfile)
		print("{}{}".format("گزینه",j),file=myfile)
		myfile.close()

######## puttings a shuffled list of questins in QuestionListFile
shuffledQuestion = [i for i in range(1,NumberOfQuestion+1)]
for j in range(1,5):
	myfile = open("Myquestionlist{}.tex".format(j), encoding='utf-8',mode="w") 
	print("\\input{MyHeader}",file=myfile)
	for i in shuffledQuestion: 
		print("\\quest\\renewcommand{{\\questName}}{{{0:s}{1:02d}}}\\input{{{0:s}{1:02d}0}}\\input{{\\qestionType}}\\questEnd".format(QusetionFileName,i),file=myfile)
	myfile.close()
	shuffle(shuffledQuestion)




