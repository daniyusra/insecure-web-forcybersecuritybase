from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db import connection
from .models import Account, Scores

@login_required
def inputScoreView(request):
	studentid = request.POST.get("studentid")
	subjectname = request.POST.get("subjectname")
	score = str(request.POST.get("score"))

	if (studentid == "" or  subjectname == "" or score == ""):
		return redirect('/')

	sqlstatement = "INSERT INTO insecure_web_scores (student_id_id, subject, scores) VALUES ('" + studentid + "','" + subjectname + "'," + score + ")"
	print(sqlstatement)
	with connection.cursor() as cursor:
		cursor.execute(sqlstatement)
	
	return redirect('/')


@login_required
def getScoreListView(request):
	context = {}
	currentloggedaccount = Account.objects.get(owner = request.user)

	studentid = request.GET.get("studentid")
	subjectname = request.GET.get("subjectname")

	sqlstatement = "SELECT * FROM insecure_web_scores WHERE student_id_id=" + studentid + " AND subject LIKE '%" + subjectname +  "%'"  
	
	

	data = []

	for p in Account.objects.raw(sqlstatement):
		data.append({p.subject: p.scores})
	
	if(currentloggedaccount.accountType == 2):
		context["type"] = "student"
	else:
		context["type"] = "teacher"
	context["score_data"] = data;
	
	return render(request, 'scoreres.html', context)


def homePageView(request):
	context = {}

	if not request.user.is_authenticated or request.user.is_superuser:
		return render(request, 'home.html', context)
	
	currentloggedaccount = Account.objects.get(owner = request.user)
	if(currentloggedaccount.accountType == 2): #if student
		all_scores = Scores.objects.filter(student_id = currentloggedaccount)
		data = [{ score.subject : score.scores} for score in all_scores ]
		context["type"] = "student"
		context["score_data"] = data;
		print(data);
		print(context["score_data"])

	if(currentloggedaccount.accountType == 1): #if teacher
		context["type"] = "teacher"
		students = Account.objects.filter(accountType=2)
		context["students"] = students
		print(context["students"])
		
	return render(request, 'home.html', context)
