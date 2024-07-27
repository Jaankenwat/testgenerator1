from django.shortcuts import render
from Home.models import QuestionData
import random
from django.core.paginator import Paginator

def Test(request):
      UserName=request.POST.get("UserName")
      ExamType=request.POST.get("ExamType")
      if ExamType=="jee (Mains)":
            global QuesDataPhy
            QuesDataPhy= list(QuestionData.objects.filter(QuestionType="jee",QuestionSubject="phy"))
            QuesDataPhy= random.sample(QuesDataPhy,1)
            global QuesDataChem
            QuesDataChem= list(QuestionData.objects.filter(QuestionType="jee",QuestionSubject="chem"))
            QuesDataChem= random.sample(QuesDataChem,1)
            # QuesDataMath= list(QuestionData.objects.filter(QuestionSubject="math"))
            # QuesDataMath= random.sample(QuesDataMath,2)
            global QuesData
            QuesData= QuesDataPhy + QuesDataChem 
      elif ExamType=="neet":
            QuesDataPhy= list(QuestionData.objects.filter(QuestionType="neet",QuestionSubject="phy"))
            QuesDataPhy= random.sample(QuesDataPhy,1)
            QuesDataChem= list(QuestionData.objects.filter(QuestionType="neet",QuestionSubject="chem"))
            QuesDataChem= random.sample(QuesDataChem,1)

      
      data={"ques":QuesData,"username":UserName,"examtype":ExamType}
      return render(request,"TestPage1.html",data)
def ResultPage(request):
      TotalScore =0
      AttempedQuestions=0
      PhyAttempedQuestions=0
      ChemAttempedQuestions=0
      DropedQuestion=0
      PhyDropedQuestion=0
      ChemDropedQuestion=0
      CorrectAnswer=0
      PhyCorrectAnswer=0
      ChemCorrectAnswer=0
      PhyTotalScore=0
      ChemTotalScore=0
      PhyTotalScore=0
      data={}
      QuesDatajee= QuestionData.objects.filter(QuestionType="jee")
      if request.method=="POST":
            for i in QuesDataPhy:
                  UserOption = request.POST.get(str(i.id))
                  if UserOption != None :
                        PhyAttempedQuestions+=1
                  else:
                        PhyDropedQuestion+=1
                  if UserOption==i.CorrectOptionText or UserOption== i.CorrectOptionImg :
                        PhyCorrectAnswer+=1
                        PhyTotalScore+=5
                  elif UserOption != i.CorrectOptionText or UserOption != i.CorrectOptionImg :
                        PhyTotalScore-=1
            for i in QuesDataChem:
                  UserOption = request.POST.get(str(i.id))
                  if UserOption != None :
                        ChemAttempedQuestions+=1
                  else:
                        ChemDropedQuestion+=1
                  if UserOption==i.CorrectOptionText or UserOption== i.CorrectOptionImg :
                        ChemCorrectAnswer+=1
                        ChemTotalScore+=5
                  elif UserOption != i.CorrectOptionText or UserOption != i.CorrectOptionImg :
                        ChemTotalScore-=1

            for i in QuesData:
                  UserOption = request.POST.get(str(i.id))
                  if UserOption != None :
                        AttempedQuestions+=1
                  else:
                        DropedQuestion+=1
                  if UserOption==i.CorrectOptionText or UserOption== i.CorrectOptionImg :
                        CorrectAnswer+=1
                        TotalScore+=5
                  elif UserOption != i.CorrectOptionText or UserOption != i.CorrectOptionImg :
                        TotalScore-=1

            data={
                  "TotalScore":TotalScore,"AttempedQuestions":AttempedQuestions,"CorrectAnswer":CorrectAnswer,"DroppedQuestion":DropedQuestion,
                  "PhyTotalScore":PhyTotalScore,"PhyAttempedQuestions":PhyAttempedQuestions,"PhyCorrectAnswer":PhyCorrectAnswer,"PhyDroppedQuestion":PhyDropedQuestion,
                  "ChemTotalScore":ChemTotalScore,"ChemAttempedQuestions":ChemAttempedQuestions,"ChemCorrectAnswer":ChemCorrectAnswer,"ChemDroppedQuestion":ChemDropedQuestion,}
      return render(request,"Result.html",data)
def InstructionBox(request):
      return render(request,"TestInstructionform.html")