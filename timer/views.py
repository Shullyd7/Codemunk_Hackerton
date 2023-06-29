from django.http import JsonResponse
from rest_framework.decorators import api_view
from .models import Timer

# Create your views here.

@api_view(['POST'])
def start_timer(request):
    duration = request.data.get('duration')  # Get the duration from the request data
    timer = Timer.objects.first()
    timer.is_running = True
    timer.duration = duration  # Update the duration if provided
    timer.remaining_time = duration * 60  # Convert duration to seconds
    timer.save()

    response_data = {
        'status': 'success',
        'message': 'Timer started successfully.',
        'remaining_time': timer.remaining_time,
        'is_running': timer.is_running
    }
    return JsonResponse(response_data)

@api_view(['POST'])
def stop_timer(request):
    timer = Timer.objects.first()
    timer.is_running = False
    if timer.start_time is not None:
        elapsed_time = time.time() - timer.start_time  # Calculate elapsed time
        timer.remaining_time -= int(elapsed_time)  # Update remaining time
    timer.start_time = None  # Reset start time
    timer.save()

    response_data = {
        'status': 'success',
        'message': 'Timer stopped successfully.',
        'remaining_time': timer.remaining_time,
        'is_running': timer.is_running
    }
    return JsonResponse(response_data)


@api_view(['POST'])
def reset_timer(request):
    timer = Timer.objects.first()
    timer.is_running = False
    timer.start_time = None  # Reset start time
    timer.remaining_time = timer.duration * 60  # Reset remaining time to original duration
    timer.save()

    response_data = {
        'status': 'success',
        'message': 'Timer reset successfully.',
        'remaining_time': timer.remaining_time,
        'is_running': timer.is_running
    }
    return JsonResponse(response_data)


