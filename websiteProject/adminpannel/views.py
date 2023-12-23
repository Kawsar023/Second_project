from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from adminpannel.models import aboutus, speakers, designations
from django.contrib import messages


# def index(request):
#     if request.user.is_authenticated:
#         show_about = aboutus.objects.filter(status = False)
#         # show_speakers = speakers.objects.filter(status = False)
#         # return render(request, 'adminpannel/index.html')
#         return render(request, 'adminpannel/index.html', {'show_about' : show_about })
#     else:
#       return redirect('login')
    
def index(request):
    if request.user.is_authenticated:
        
        
        return render(request, 'adminpannel/index.html')
    else:
        return redirect('login')

def reg_user(request):  
    if request.method == 'POST':
        first_name = request.POST.get('f_name')
        last_name  = request.POST.get('l_name')
        user_name  = request.POST.get('u_name')
        email      = request.POST.get('email')
        password   = request.POST.get('pass_1')
        conf_password = request.POST.get('pass_2')

        if password != conf_password:
            return redirect('register')
        else:
            user_reg = User.objects.create_superuser(user_name,email,password)
            user_reg.first_name = first_name
            user_reg.last_name  = last_name
            user_reg.save()
            return redirect('login')
        
    return render(request, 'adminpannel/register.html')

def login_user(request):
    if request.method == 'POST':
        user_name = request.POST.get('u_name')
        password  = request.POST.get('password')

        user   = authenticate(username = user_name, password = password)
        if user is not None:
            login(request,user)
            return redirect('admin_home')
        else:
            return redirect('login')
        
    return render (request, 'adminpannel/login.html')


def logoutUser(request):
    logout(request)
    return redirect('login')


def create_about(request):

    if request.user.is_authenticated:
        if request.method == 'POST' and request.FILES['about_pic']:
            about_title  = request.POST.get('about_title')
            about_desc_1 = request.POST.get('description_1')
            about_desc_2 = request.POST.get('description_2')
            about_pic    = request.FILES['about_pic']

            about_save = aboutus(

                about_title         = about_title,
                about_description_1 = about_desc_1,
                about_description_2 = about_desc_2,
                about_pic           = about_pic
                
                ).save()
                # about_save.save()
            messages.success(request,"Successfully Inserted")
            return redirect('create_about')
        return render (request, 'adminpannel/about.html')
        
    else:
       return redirect('login')
    

def show_about(request):
    if request.user.is_authenticated:
        about_show = aboutus.objects.all()
        return render(request, 'adminpannel/about_show.html',{'about_show' : about_show})
    else:
        return redirect('login')

    
def about_edit(request,id):
    if request.user.is_authenticated:
       about_edit = aboutus.objects.filter(id=id)
       return render(request,'adminpannel/about_edit.html',{'about_edit' : about_edit})
    
    else:
     return redirect('show_about')


def about_update(request, id):
    if request.method =="POST" and request.FILES: 
        a = request.POST.get('about_title')
        b = request.POST.get('about_description_1')
        c = request.POST.get('about_description_2')
        d = request.FILES['about_pic']

        xyz = aboutus.objects.filter(id=id)
        xyz = aboutus(
            id = id,
            about_title = a,
            about_description_1 = b,
            about_description_2 = c,
            about_pic           = d,

            
        )
        xyz.save()
        return redirect('show_about')
    
def delete_about(request,id):
    del_about = aboutus.objects.filter(id=id).delete()
    return redirect ('show_about')

def about_status(request,id):
    if request.user.is_authenticated:
        about_active = aboutus.objects.get(id=id)
        about_active.is_active = True
        about_active.save()
        return redirect('show_about')
    
    else:
     return redirect('login')
    

def about_inactive(request,id):
    if request.user.is_authenticated:
        about_inactive = aboutus.objects.get(id=id)
        about_inactive.is_active = False
        about_inactive.save()
        return redirect('show_about')
    
    else:
     return redirect('login')
    
    

# def create_speakers(request):

#     desi = designations.objects.all()

#     if request.user.is_authenticated:
#         if request.method == 'POST' and request.FILES['speakers_pic']:
#             speakers_name = request.POST.get('speakers_name')
#             desi  = request.POST.get('speakers_designation')
#             description = request.POST.get('description')
#             facebook = request.POST.get('fb_icon')
#             twitter = request.POST.get('twt_icon')
#             linkedin = request.POST.get('lin_icon')
#             pinterest = request.POST.get('pin_icon')
#             speakers_pic    = request.FILES['speakers_pic']

#             speakers_save = speakers(

#                 speakers_name         = speakers_name,
#                 desi          = desi,
#                 description          = description,
#                 speakers_pic           = speakers_pic,
#                 facebook               = facebook,
#                 twitter             = twitter,
#                 linkedin             =  linkedin,
#                 pinterest              = pinterest,


                
#                 )
#             speakers_save .save()
#             messages.success(request,"Successfully Inserted")
#             return redirect('create_speakers')
#         return render (request, 'adminpannel/speakers.html')
        
#     else:
#        return redirect('login')
    

# def show_speakers(request):
#     desi = designations.objects.all()
#     if request.user.is_authenticated:
        
#         speakers_show = speakers.objects.all()
#         return render(request, 'adminpannel/speakers_show.html',{'speakers_show' : speakers_show, 'desi' : desi })
#     else:
#         return redirect('login')
    

# def speakers_edit(request,id):
#     desi          = designations.objects.all()
#     if request.user.is_authenticated:
       
#        speakers_edit = speakers.objects.filter(id=id)
#        return render(request,'adminpannel/speakers_edit.html',{'speakers_edit' : speakers_edit, 'desi' : desi})
    
#     else:
#      return redirect('show_speakers')


# def speakers_update(request, id):
#     if request.method =="POST" and request.FILES: 
#         a = request.POST.get('speakers_name')
#         b = request.POST.get('designations')
#         c = request.POST.get('description')
#         d = request.POST.get('facebook')
#         e = request.POST.get('twitter')
#         f = request.POST.get('linkedin')
#         g = request.POST.get('pinterest')
#         h = request.FILES['speakers_pic']

#         xyz = speakers.objects.filter(id=id)
#         xyz = speakers(
#             id = id,
#             speakers_name = a,
#             designations = b,
#             description = c,
#             facebook = d,
#             twitter = e,
#             linkedin = f,
#             pinterest = g,
#             speakers_pic           = h,

            
#         )
#         xyz.save()
#         return redirect('show_speakers')
    
# def delete_speakers(request,id):
#     del_speakers = speakers.objects.filter(id=id).delete()
#     return redirect ('show_speakers')

# def speakers_status(request,id):
#     if request.user.is_authenticated:
#         speakers_active = speakers.objects.get(id=id)
#         speakers_active.is_active = True
#         speakers_active.save()
#         return redirect('show_speakers')
    
#     else:
#      return redirect('login')
    

# def speakers_inactive(request,id):
#     if request.user.is_authenticated:
#         speakers_inactive = speakers.objects.get(id=id)
#         speakers_inactive.is_active = False
#         speakers_inactive.save()
#         return redirect('show_speakers')
    
#     else:
#      return redirect('login')


def create_speakers(request):
    designations = designations.objects.all()
    if request.user.is_authenticated:
        if request.method == 'POST' and request.FILES ['speaker_pic']:
        

            speaker_name  = request.POST.get('speaker_name')
            speaker_description_1 = request.POST.get('description_1')
            designations                  = request.POST.get('designations')
            facebook              = request.POST.get('facebook')
            twitter               = request.POST.get('twitter')
            linkedin               = request.POST.get('linkedin')
            pinterest               = request.POST.get('pinterest')
            speaker_pic    = request.FILES['speaker_pic']

            speaker_save = speakers(

                speaker_name         = speaker_name,
                speaker_description_1 = speaker_description_1,
                designations                  = designations,
                facebook              = facebook,
                twitter               = twitter,
                linkedin               = linkedin,
                pinterest               = pinterest,
                speaker_pic           = speaker_pic
                
                )
            speaker_save.save()
            messages.success(request,"Successfully Insert")
            return redirect('create_speakers')
        return render (request, 'adminpannel/speakers.html')
        
    else:
       return redirect('login')
    

def show_speakers(request):
    designations = designations.objects.all()
    if request.user.is_authenticated:
        speakers_show = speakers.objects.all()
        return render(request, 'adminpannel/speakers_show.html', {'speakers_show': speakers_show})
    else:
        return redirect('login')

    
def speakers_edit(request,id):
    if request.user.is_authenticated:
       speakers_edit = speakers.objects.filter(id=id)
       return render(request,'adminpannel/speakers_edit.html',{'speakers_edit' : speakers_edit})
    
    else:
     return redirect('show_speakers')


def speakers_update(request, id):
    designations = designations.objects.all()
    if request.method =="POST" and request.FILES: 
        a = request.POST.get('speaker_name')
        b = request.POST.get('speaker_description_1')
        c = request.POST.get('designations')
        d = request.POST.get('facebook')
        e = request.POST.get('twitter')
        f = request.POST.get('linkedin')
        g = request.POST.get('pinterest')
        e = request.FILES['speaker_pic']

        xyz = speakers.objects.filter(id=id)
        xyz = speakers(
            id = id,
            speaker_name = a,
            speaker_description_1 = b,
            designations                   = c,
            facebook              = d,
            twitter              = e,
            linkedin              = f,
            pinterest              = g,
            speaker_pic           = e,

            
        )
        xyz.save()
        return redirect('show_speakers')
    
def delete_speakers(request,id):
    del_speakers = speakers.objects.filter(id=id).delete()
    return redirect ('show_speakers')

def speakers_status(request,id):
    if request.user.is_authenticated:
        speaker_active = speakers.objects.get(id=id)
        speaker_active.is_active = True
        speaker_active.save()
        return redirect('show_speakers')
    
    else:
     return redirect('login')
    

def speakers_inactive(request,id):
    if request.user.is_authenticated:
        speaker_inactive = speakers.objects.get(id=id)
        speaker_inactive.is_active = False
        speaker_inactive.save()
        return redirect('show_speakers')
    
    else:
     return redirect('login')


