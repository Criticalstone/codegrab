from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from codes.models import Code
from django.shortcuts import redirect

def index(request):
    code = Code.objects.filter(claimed=0).first()
    if code == None:
        return render(request, 'index.html', {'error': "No codes left :("})
    else:
        code.claimed = 1
        code.save()
        return render(request, 'index.html', {'code': code})

@login_required(login_url='/admin/login')
def codes(request):
    codes = Code.objects.all()

    context = {
        'codes': codes, 
    }

    return render(request, 'codes.html', context)

@login_required(login_url='/admin/login')
def addCodes(request):
    if "GET" == request.method:
        return render(request, "add_codes.html", {})

    csv_file = request.FILES["codes"]
    if not csv_file.name.endswith('.csv'):
        messages.error(request,'File is not CSV type')
        return HttpResponseRedirect(reverse("myapp:upload_csv"))
    #if file is too large, return
    if csv_file.multiple_chunks():
        messages.error(request,"Uploaded file is too big (%.2f MB)." % (csv_file.size/(1000*1000),))
        return HttpResponseRedirect(reverse("myapp:upload_csv"))

    file_data = csv_file.read().decode("utf-8")

    lines = file_data.split(",")
    #loop over the lines and save them in db. If error , store as string and then display
    for line in lines:
        print("line: {}".format(line))
        if line != "":
            code = Code()
            code.code = line
            code.claimed = 0
            code.save()

    return redirect('/codes')