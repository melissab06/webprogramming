from django.shortcuts import render, redirect
from board.models import Border
from datetime import datetime
from django.core.paginator import Paginator

# Create your views here.
def index(request, page):
    userAll = Border.objects.values('id', '제목', '작성자', '내용', '조회수').order_by('-id')
    pageNum = 4
    paging = Paginator(userAll,pageNum)
    arrPage = []

    '''
    totalPage = len(userAll) // pageNum
    temp = len(userAll) % pageNum
    if temp != 0:
        totalPage += 1
    '''

    for i in range(paging.num_pages):
        arrPage.append(i+1)
        
    #print("arrPage: ", arrPage)

    #context = {"userAll": userAll}
    context = {"userAll": paging.page(page), "arrPage": arrPage}

    return render(request, "board/index.html", context)

def add(request):
    if request.method == 'POST':
        table = Border()
        table.제목 = request.POST.get('title')
        table.내용 = request.POST.get('context')
        #table.작성자 = request.POST.get('author')
        table.작성자 = request.user
        #table.작성일 = request.POST.get('cdate')
        #table.수정일 = request.POST.get('udate')
        table.작성일 = datetime.now()
        table.수정일 = datetime.now()
        table.조회수 ='0'
        #table.조회수 = request.POST.get('vcount')
        table.save()
        return redirect("BD:index", 1)
    else:
        return render(request, 'board/add.html')

def detail(request, borderId):
    boardCnt = Border.objects.get(id=borderId)
    boardCnt.조회수 = boardCnt.조회수 + 1
    boardCnt.save()

    borderTable = Border.objects.values('id','제목', '작성자', 
                        '조회수', '수정일', '내용').get(id=borderId)

    borderTable['내용'] = borderTable['내용'].replace('\n', '<br>')
    context = {"border": borderTable}
    return render(request, "board/detail.html", context)

def delete(request, delId):
    dele = Border.objects.get(id = delId)
    dele.delete()
    return redirect('BD:index')

def update(request, updateId):
    borderTable = Border.objects.get(id=updateId)
    if request.method == 'POST':
        borderTable.제목 = request.POST.get("title")
        borderTable.내용 = request.POST.get("context")
        borderTable.수정일 = datetime.now()
        borderTable.save()
        return redirect("BD:detail", borderTable.id)
    else:
        context = {'border': borderTable}
        return render(request, 'board/update.html', context)

def borderPaging(request, page):
    borderTable = Border.objects.all()
    print("type: ", type(borderTable))
    print("len: ", len(borderTable))
    print("borderTable: ", borderTable)

    paging = Paginator(borderTable, 2)


    context = {"borderTable": paging.page(page)}
    return render(request, "board/borderPaging.html", context)
