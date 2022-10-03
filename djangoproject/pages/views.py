from asyncio.windows_events import NULL
from typing import final
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_view(request):
    return render(request, "index.html", {})

def cgpa_calc(request):
    if request.method == "POST":
        sem1_sgpa = request.POST.get('sem1sgpa')
        sem2_sgpa = request.POST.get('sem2sgpa')
        sem3_sgpa = request.POST.get('sem3sgpa')
        sem4_sgpa = request.POST.get('sem4sgpa')
        sem5_sgpa = request.POST.get('sem5sgpa')
        sem6_sgpa = request.POST.get('sem6sgpa')
        sem7_sgpa = request.POST.get('sem7sgpa')
        sem8_sgpa = request.POST.get('sem8sgpa')

        if sem1_sgpa and sem2_sgpa and sem3_sgpa and sem4_sgpa and sem5_sgpa and sem6_sgpa and sem7_sgpa and sem8_sgpa:
            sem1_sgpa= float(sem1_sgpa)
            sem2_sgpa= float(sem2_sgpa)
            sem3_sgpa= float(sem3_sgpa)
            sem4_sgpa= float(sem4_sgpa)
            sem5_sgpa= float(sem5_sgpa)
            sem6_sgpa= float(sem6_sgpa)
            sem7_sgpa= float(sem7_sgpa)
            sem8_sgpa= float(sem8_sgpa)
            final_cgpa = (sem1_sgpa+sem2_sgpa+sem3_sgpa+sem4_sgpa+sem5_sgpa+sem6_sgpa+sem7_sgpa+sem8_sgpa)/8  
            final_cgpa = format(final_cgpa, '.2f')  
            return render(request, "cgpa.html", {'my_data': final_cgpa})
        else:
            pass
    
    return render(request, "cgpa.html", {})

    

def sgpa_calc(request):
    return render(request, "semselect.html", {})

def branch_select7(request):
    return render(request, "7branchselect.html", {})

def sgpa_phys(request):
    if request.method == "POST":
        mat = request.POST.get("math12")
        phy = request.POST.get("phy12")
        ele = request.POST.get("ele12")
        civ = request.POST.get("civ12")
        egdl = request.POST.get("egdl12")
        phyl = request.POST.get("phyl12")
        elel = request.POST.get("elel12")
        eng = request.POST.get("eng12")

        
        if mat and phy and ele and civ and egdl and phyl and elel and eng:
            mat = int(mat)
            mat = marks2gpa(mat)
            phy = int(phy)
            phy = marks2gpa(phy)
            ele = int(ele)
            ele = marks2gpa(ele)
            civ = int(civ)
            civ = marks2gpa(civ)
            egdl = int(egdl)
            egdl = marks2gpa(egdl)
            phyl = int(phyl)
            phyl = marks2gpa(phyl)
            elel = int(elel)
            elel = marks2gpa(elel)
            eng = int(eng)
            eng = marks2gpa(eng)
            print(mat,phy,ele,civ,egdl,phyl, elel,eng)
            total = ((3*mat)+(3*phy)+(2*ele)+(2*civ)+(2*egdl)+(2*phyl)+(2*elel)+(2*eng))/18
            total = format(total, '.2f') 
            print(total)
            return render(request, "physgpa.html", {'my_data1':total})
        else:
            pass
    return render(request, "physgpa.html", {})


def sgpa_chem(request):
    if request.method == "POST":
        mat = request.POST.get("math21")
        chem = request.POST.get("chem12")
        cps = request.POST.get("cps12")
        eln = request.POST.get("eln12")
        me = request.POST.get("me12")
        cheml = request.POST.get("cheml12")
        cpl = request.POST.get("cpl12")
        eng = request.POST.get("eng21")

        
        if mat and chem and cps and eln and me and cheml and cpl and eng:
            mat = int(mat)
            mat = marks2gpa(mat)
            chem = int(chem)
            chem = marks2gpa(chem)
            cps = int(cps)
            cps = marks2gpa(cps)
            eln = int(eln)
            eln = marks2gpa(eln)
            me = int(me)
            me = marks2gpa(me)
            cheml = int(cheml)
            cheml = marks2gpa(cheml)
            cpl = int(cpl)
            cpl = marks2gpa(cpl)
            eng = int(eng)
            eng = marks2gpa(eng)
            
            total = ((3*mat)+(3*chem)+(2*cps)+(2*eln)+(2*me)+(2*cheml)+(2*cpl)+(2*eng))/18
            total = format(total, '.2f') 
            print(total)
            return render(request, "chemsgpa.html", {'my_data2':total})
        else:
            pass
    return render(request, "chemsgpa.html", {})

def sgpa_3(request):
    if request.method == "POST":
        mat = request.POST.get("math3")
        xx32 = request.POST.get("3sem2")
        xx33 = request.POST.get("3sem3")
        xx34 = request.POST.get("3sem4")
        xx35 = request.POST.get("3sem5")
        xx36 = request.POST.get("3sem6")
        xx37 = request.POST.get("3sem7")
        xx38 = request.POST.get("3sem8")
        kan = request.POST.get("kan34")

        
        if mat and xx32 and xx33 and xx34 and xx35 and xx36 and xx37 and xx38 and kan:
            mat = int(mat)
            mat = marks2gpa(mat)
            xx32 = int(xx32)
            xx32 = marks2gpa(xx32)
            xx33 = int(xx33)
            xx33 = marks2gpa(xx33)
            xx34 = int(xx34)
            xx34 = marks2gpa(xx34)
            xx35 = int(xx35)
            xx35 = marks2gpa(xx35)
            xx36 = int(xx36)
            xx36 = marks2gpa(xx36)
            xx37 = int(xx37)
            xx37 = marks2gpa(xx37)
            xx38 = int(xx38)
            xx38 = marks2gpa(xx38)
            kan = int(kan)
            kan = marks2gpa(kan)
            
            total = ((3*mat)+(4*xx32)+(3*xx33)+(3*xx34)+(3*xx35)+(3*xx36)+(2*xx37)+(2*xx38)+(kan))/24
            total = format(total, '.2f') 
            print(total)
            return render(request, "3sgpa.html", {'my_data3':total})
        else:
            pass
    return render(request, "3sgpa.html", {})

def sgpa_4(request):
    if request.method == "POST":
        mat = request.POST.get("math4")
        xx42 = request.POST.get("4sem2")
        xx43 = request.POST.get("4sem3")
        xx44 = request.POST.get("4sem4")
        xx45 = request.POST.get("4sem5")
        xx46 = request.POST.get("4sem6")
        xx47 = request.POST.get("4sem7")
        xx48 = request.POST.get("4sem8")
        kan = request.POST.get("kan34")

        
        if mat and xx42 and xx43 and xx44 and xx45 and xx46 and xx47 and xx48 and kan:
            mat = int(mat)
            mat = marks2gpa(mat)
            xx42 = int(xx42)
            xx42 = marks2gpa(xx42)
            xx43 = int(xx43)
            xx43 = marks2gpa(xx43)
            xx44 = int(xx44)
            xx44 = marks2gpa(xx44)
            xx45 = int(xx45)
            xx45 = marks2gpa(xx45)
            xx46 = int(xx46)
            xx46 = marks2gpa(xx46)
            xx47 = int(xx47)
            xx47 = marks2gpa(xx47)
            xx48 = int(xx48)
            xx48 = marks2gpa(xx48)
            kan = int(kan)
            kan = marks2gpa(kan)
            
            total = ((3*mat)+(4*xx42)+(3*xx43)+(3*xx44)+(3*xx45)+(3*xx46)+(2*xx47)+(2*xx48)+(kan))/24
            total = format(total, '.2f') 
            print(total)
            return render(request, "4sgpa.html", {'my_data4':total})
        else:
            pass
    return render(request, "4sgpa.html", {})
    
def sgpa_5(request):
    if request.method == "POST":
        xx51 = request.POST.get("5sem1")
        xx52 = request.POST.get("5sem2")
        xx53 = request.POST.get("5sem3")
        xx54 = request.POST.get("5sem4")
        xx55 = request.POST.get("5sem5")
        xx56 = request.POST.get("5sem6")
        xx57 = request.POST.get("5sem7")
        xx58 = request.POST.get("5sem8")
        env = request.POST.get("env")

        
        if xx51 and xx52 and xx53 and xx54 and xx55 and xx56 and xx57 and xx58 and env:
            xx51 = int(xx51)
            xx51 = marks2gpa(xx51)
            xx52 = int(xx52)
            xx52 = marks2gpa(xx52)
            xx53 = int(xx53)
            xx53 = marks2gpa(xx53)
            xx54 = int(xx54)
            xx54 = marks2gpa(xx54)
            xx55 = int(xx55)
            xx55 = marks2gpa(xx55)
            xx56 = int(xx56)
            xx56 = marks2gpa(xx56)
            xx57 = int(xx57)
            xx57 = marks2gpa(xx57)
            xx58 = int(xx58)
            xx58 = marks2gpa(xx58)
            env = int(env)
            env = marks2gpa(env)
            
            total = ((3*xx51)+(4*xx52)+(4*xx53)+(3*xx54)+(3*xx55)+(3*xx56)+(2*xx57)+(2*xx58)+(env))/25
            total = format(total, '.2f') 
            print(total)
            return render(request, "5sgpa.html", {'my_data5':total})
        else:
            pass
    return render(request, "5sgpa.html", {})

def sgpa_6(request):
    if request.method == "POST":
        xx61 = request.POST.get("6sem1")
        xx62 = request.POST.get("6sem2")
        xx63 = request.POST.get("6sem3")
        xx64 = request.POST.get("6sem4")
        xx65 = request.POST.get("6sem5")
        xx66 = request.POST.get("6sem6")
        xx67 = request.POST.get("6sem7")
        xx68 = request.POST.get("6sem8")
        

        
        if xx61 and xx62 and xx63 and xx64 and xx65 and xx66 and xx67 and xx68:
            xx61 = int(xx61)
            xx61 = marks2gpa(xx61)
            xx62 = int(xx62)
            xx62 = marks2gpa(xx62)
            xx63 = int(xx63)
            xx63 = marks2gpa(xx63)
            xx64 = int(xx64)
            xx64 = marks2gpa(xx64)
            xx65 = int(xx65)
            xx65 = marks2gpa(xx65)
            xx66 = int(xx66)
            xx66 = marks2gpa(xx66)
            xx67 = int(xx67)
            xx67 = marks2gpa(xx67)
            xx68 = int(xx68)
            xx68 = marks2gpa(xx68)
            
            total = ((4*xx61)+(4*xx62)+(4*xx63)+(3*xx64)+(3*xx65)+(2*xx66)+(2*xx67)+(2*xx68))/24
            total = format(total, '.2f') 
            print(total)
            return render(request, "6sgpa.html", {'my_data6':total})
        else:
            pass
    return render(request, "6sgpa.html", {})

def sgpa_71(request):
    if request.method == "POST":
        xx71 = request.POST.get("7sem1")
        xx72 = request.POST.get("7sem2")
        xx73 = request.POST.get("7sem3")
        xx74 = request.POST.get("7sem4")
        xx75 = request.POST.get("7sem5")
        xx76 = request.POST.get("7sem6")
        xx77 = request.POST.get("7sem7")
        
        

        
        if xx71 and xx72 and xx73 and xx74 and xx75 and xx76 and xx77:
            xx71 = int(xx71)
            xx71 = marks2gpa(xx71)
            xx72 = int(xx72)
            xx72 = marks2gpa(xx72)
            xx73 = int(xx73)
            xx73 = marks2gpa(xx73)
            xx74 = int(xx74)
            xx74 = marks2gpa(xx74)
            xx75 = int(xx75)
            xx75 = marks2gpa(xx75)
            xx76 = int(xx76)
            xx76 = marks2gpa(xx76)
            xx77 = int(xx77)
            xx77 = marks2gpa(xx77)
            
            
            total = ((4*xx71)+(4*xx72)+(3*xx73)+(3*xx74)+(3*xx75)+(2*xx76)+(xx77))/20
            total = format(total, '.2f') 
            print(total)
            return render(request, "7csesgpa.html", {'my_data71':total})
        else:
            pass
    return render(request, "7csesgpa.html", {})

def sgpa_72(request):
    if request.method == "POST":
        xx71 = request.POST.get("7sem1")
        xx72 = request.POST.get("7sem2")
        xx73 = request.POST.get("7sem3")
        xx74 = request.POST.get("7sem4")
        xx75 = request.POST.get("7sem5")
        xx76 = request.POST.get("7sem6")
        xx77 = request.POST.get("7sem7")
        xx78 = request.POST.get("7sem8")
        
        

        
        if xx71 and xx72 and xx73 and xx74 and xx75 and xx76 and xx77 and xx78:
            xx71 = int(xx71)
            xx71 = marks2gpa(xx71)
            xx72 = int(xx72)
            xx72 = marks2gpa(xx72)
            xx73 = int(xx73)
            xx73 = marks2gpa(xx73)
            xx74 = int(xx74)
            xx74 = marks2gpa(xx74)
            xx75 = int(xx75)
            xx75 = marks2gpa(xx75)
            xx76 = int(xx76)
            xx76 = marks2gpa(xx76)
            xx77 = int(xx77)
            xx77 = marks2gpa(xx77)
            xx78 = int(xx78)
            xx78 = marks2gpa(xx78)
            
            
            total = ((3*xx71)+(3*xx72)+(3*xx73)+(3*xx74)+(3*xx75)+(2*xx76)+(2*xx77)+(xx78))/20
            total = format(total, '.2f') 
            print(total)
            return render(request, "7ecesgpa.html", {'my_data72':total})
        else:
            pass
    return render(request, "7ecesgpa.html", {})

def sgpa_8(request):
    if request.method == "POST":
        xx81 = request.POST.get("8sem1")
        xx82 = request.POST.get("8sem2")
        xx83 = request.POST.get("8sem3")
        xx84 = request.POST.get("8sem4")
        xx85 = request.POST.get("8internship")
        
        
        if xx81 and xx82 and xx83 and xx84 and xx85:
            xx81 = int(xx81)
            xx81 = marks2gpa(xx81)
            xx82 = int(xx82)
            xx82 = marks2gpa(xx82)
            xx83 = int(xx83)
            xx83 = marks2gpa(xx83)
            xx84 = int(xx84)
            xx84 = marks2gpa(xx84)
            xx85 = int(xx85)
            xx85 = marks2gpa(xx85)
            
            
            
            total = ((3*xx81)+(3*xx82)+(8*xx83)+(1*xx84)+(3*xx85))/18
            total = format(total, '.2f') 
            print(total)
            return render(request, "8sgpa.html", {'my_data8':total})
        else:
            pass
    return render(request, "8sgpa.html", {})

def contact_us(request):
    return render(request, "contact.html", {})



def marks2gpa(t):
    if t>=90 and t<=100:
        return 10
    if t>=80 and t<=89:
        return 9
    if t>=70 and t<=79:
        return 8
    if t>=60 and t<=69:
        return 7
    if t>=50 and t<=59:
        return 6
    if t>=40 and t<=49:
        return 5
    if t>=35 and t<=39:
        return 4
    else:
        return 0
    
