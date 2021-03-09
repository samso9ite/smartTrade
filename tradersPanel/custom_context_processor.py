from tradersPanel.models import TestimonialModel, ProfileDetails, sendFeedBackModel
import datetime

def update(request):
    current_datetime = datetime.datetime.now()
    try:
        # user = TestimonialModel.objects.get(user_id=request.user.id)
        update_profile = ProfileDetails.objects.filter(User_id = request.user.id)
    except ProfileDetails.DoesNotExist:
        # user = None
        update_profile = None
    return{
        'updated':update_profile
    }

def check(request):
    try:
        user = TestimonialModel.objects.get(user_id=request.user.id)
    except TestimonialModel.DoesNotExist :
        user = None
    return{
        'user_testimonial':user
    }
    
def check_feedback(request):
    try: 
        user = sendFeedBackModel.objects.get(User_id=request.user.id)
    except sendFeedBackModel.DoesNotExist:
        user = None
    return{
        'user_feedback':user
    }
