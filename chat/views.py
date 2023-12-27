from django.shortcuts import render,redirect,get_object_or_404
from chat.models import Room,Message
from django.http import HttpResponse,JsonResponse
# from django.utils import timezone

def home(request):
    return render(request, 'home.html')

def room(request,room):
    username=request.GET.get('username')
    room_object = get_object_or_404(Room, name=room)
    # if room_object.exists():
    return render(request, 'room.html', {'room' : room_object, 'username': username }) 

def checkview(request):
    room_name=request.POST['room_name']
    username=request.POST['username']
    if Room.objects.filter(name=room_name).exists():
        return redirect('/'+room_name+'/?username='+username)
    else:
        new_room =Room.objects.create(name=room_name)
        new_room.save()
        # new_room_name=new_room.name
        return redirect('/'+room_name+'/?username='+username)
    
def send(request):
    message = request.POST['message']
    username = request.POST['username']
    room_id = request.POST['room_id'] 

    new_message=Message.objects.create(value=message, username=username, room_name=room_id)
    new_message.save()
    return HttpResponse('Message sent')

def getMessages(request, room):
    room_details=Room.objects.get(name=room)
    # room_object = get_object_or_404(Room, name=room)
    messages=Message.objects.filter(room_name = room_details.id)
    return JsonResponse({ "messages": list(messages.values())})