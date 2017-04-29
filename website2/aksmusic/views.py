from django.contrib.auth import authenticate, login
from django.shortcuts import render, get_object_or_404
from .models import Album, Song
from .forms import UserForm


# Create your views here.
def index(request):
    all_albums =Album.objects.all()
    
    context = {
        'all_albums': all_albums
        }
    
    return render(request,'aksmusic/index.html',context)

def detail(request, album_id):
    album= get_object_or_404(Album, pk=album_id)
    return render(request,'aksmusic/detail.html',{'album':album})

def favorite(request, album_id):
    album= get_object_or_404(Album, pk=album_id)
    try:
        selected_song = album.song_set.get(pk=request.POST['song'])
    except (KeyError, Song.DoesNotExist):
        return render(request, 'aksmusic/detail.html',{
            'album':album,
            'error_message': "you didn't select a valid song",
            })
    else:
        selected_song.is_favorite = True
        selected_song.save()
        return render(request, 'aksmusic/index.html', {'album':album})

class UserFormView(View):
    from_class = UserForm
    template_name = 'music/registration_form.html'


    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form. is valid():

            user = form.save(commit=False)

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('music:index')
        return render(request, self.template_name, {'form':form})
