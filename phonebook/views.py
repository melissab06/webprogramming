
from django.shortcuts import render, redirect
from phonebook.models import PhoneBook


def test(request):
    #print("GET userId : " +request.GET.get('userId'))
    #print("GET userPw : " +request.GET.get('userPw'))

    #print("POST userId : " +request.POST.get('userId'))
    #print("POST userPw : " +request.POST.get('userPw'))
    return render(request, "PBook/test.html")

def index(request):
    alluser = PhoneBook.objects.values('id','이름', '전화번호')

    context = {"phonebook": alluser}
    print(alluser)
    return render(request, "PBook/index.html", context)

def add(request):
    if request.user.is_active == False:
        return redirect('login')
    else:
        if request.method == 'POST':
            table = PhoneBook()
            table.이름 = request.POST.get('name')
            table.전화번호 = request.POST.get('phNum')
            table.이메일 = request.POST.get('email')
            table.주소 = request.POST.get('addr')
            table.생년월일 = request.POST.get('bir')
            table.작성자 = request.user.username
            table.save()
            return redirect('PB:index')
            #print("name: " + request.POST.get('name'))
            #print("phNum: " + request.POST.get('phNum'))
            #print("email: " + request.POST.get('email'))
            #print("addr: " + request.POST.get('addr'))
            #print("bir: " + request.POST.get('bir'))
            
            #return render(request, "PBook/index.html")
        else:
            return render(request, "PBook/add.html")

def delete(request, delId):
    dele = PhoneBook.objects.get(id = delId)
    dele.delete()
    #return render(request, "PBook/delete.html", context)
    return redirect('PB:index')

def detail(request, userId):
    userInfo = PhoneBook.objects.values('id','이름', '전화번호', 
                        '이메일', '주소', '생년월일', '작성자').get(id=userId)
    print(userInfo)
    context = {"phonebook": userInfo}
    return render(request, "PBook/detail.html", context)

def update(request, updateId):
    table = PhoneBook.objects.get(id=updateId)
    context = {"phonebook":table}
    if request.user.is_active == False:
        return redirect('login')
    if request.method == 'POST':
        table.이름 = request.POST.get('name')
        table.전화번호 = request.POST.get('phNum')
        table.이메일 = request.POST.get('email')
        table.주소 = request.POST.get('addr')
        table.생년월일 = request.POST.get('bir')
        table.save()
        return redirect('PB:index')
    else:
        print("table.작성자: ", type(table.작성자))
        if table.작성자 == request.user.username:
            return render(request, "PBook/update.html", context)
        else:
            return redirect("PB:index")

