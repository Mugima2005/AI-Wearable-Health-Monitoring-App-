from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, get_user_model
from django.contrib import messages
from django.http import JsonResponse, HttpResponseServerError
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.views.decorators.csrf import csrf_exempt
import json
import requests
import pyttsx3
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from datetime import datetime, timedelta

from .forms import SignupForm, LoginForm
from .models import HealthData
from auth import get_access_token  # Ensure you have this function implemented

# ✅ Signup View
def signup_view(request):
    if request.method == 'POST':
        fullname = request.POST['fullname']
        email = request.POST['email']
        password = request.POST['password']
        
        User = get_user_model()
        try:
            user = User.objects.create_user(email=email, password=password, fullname=fullname)
            messages.success(request, "Account created successfully.")
            return redirect('login')
        except IntegrityError:
            messages.error(request, "Email is already in use.")
        except ValueError as ve:
            messages.error(request, str(ve))
        except Exception as e:
            messages.error(request, f"Error creating account: {e}")
        return redirect('signup')
    
    return render(request, 'signup.html')

# ✅ Login View
def login_view(request):
    try:
        if request.method == 'POST':
            form = LoginForm(request.POST)
            if form.is_valid():
                email = form.cleaned_data['email']
                password = form.cleaned_data['password']
                user = authenticate(request, username=email, password=password)
                if user:
                    login(request, user)
                    return redirect('setup')
                else:
                    messages.error(request, "Invalid credentials")
            else:
                messages.error(request, "Invalid form submission")
        else:
            form = LoginForm()

        return render(request, 'login.html', {'form': form})
    except Exception as e:
        print(e)
        return HttpResponseServerError("An error occurred during login.")

# ✅ Home Page View
def home(request):
    return render(request, 'home.html')

# ✅ Setup View
def setup_view(request):
    if request.method == "POST":
        request.session['health_data'] = request.POST
        return redirect('dashboard')
    return render(request, 'setup.html')

# ✅ Save Health Data
@login_required
@csrf_exempt
def save_health_data(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        request.session['user_health_data'] = data
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error'}, status=400)

# ✅ Dashboard View
@login_required
def dashboard(request):
    return render(request, 'setup/dashboard.html')

# ✅ Forgot Password View
def forgot_password(request):
    return render(request, 'forgot.html')

# ✅ Additional Feature Views
def healthMetrics(request):
    return render(request, 'healthMetrics.html')

def chatAI(request):
    return render(request, 'chatAI.html')

def visualInsights(request):
    return render(request, 'visualInsights.html')

def setGoals(request):
    return render(request, 'setGoals.html')

def trackProgress(request):
    return render(request, 'trackProgress.html')

def dietPlan(request):
    return render(request, 'dietPlan.html')

# ✅ News API Config
NEWS_API_KEY = "01eb45eb9ff64428bb33acebd2a1414b"

# ✅ Fetch Health News
def get_health_news(request):
    page = int(request.GET.get("page", 1))
    url = f"https://newsapi.org/v2/top-headlines?category=health&pageSize=5&page={page}&apiKey={NEWS_API_KEY}"
    
    response = requests.get(url)
    data = response.json()

    return JsonResponse(data)

# ✅ OAuth Callback
def oauth_callback(request):
    error = request.GET.get("error")
    if error:
        return JsonResponse({"status": "error", "message": error})
    return JsonResponse({"status": "success", "message": "OAuth callback received"})


# ✅ Fetch Google Fit Data
def fetch_google_fit_data(request):
    access_token = get_access_token()
    url = "https://www.googleapis.com/fitness/v1/users/me/dataset:aggregate"
    
    now = datetime.utcnow()
    start_time = now - timedelta(days=1)  
    start_timestamp = int(start_time.timestamp() * 1000)
    end_timestamp = int(now.timestamp() * 1000)

    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
    
    body = {
        "aggregateBy": [{"dataTypeName": "com.google.step_count.delta"}],
        "bucketByTime": {"durationMillis": 86400000},
        "startTimeMillis": str(start_timestamp),
        "endTimeMillis": str(end_timestamp)
    }

    response = requests.post(url, json=body, headers=headers)

    if response.status_code == 200:
        return JsonResponse(response.json(), safe=False)
    return JsonResponse({"error": "Failed to fetch data"}, status=400)

# ✅ Save Google Fit Data
@csrf_exempt
def save_google_fit_data(request):
    if request.method == "POST":
        data = json.loads(request.body)
        token = data.get("token")
        google_fit_data = data.get("googleFitData")

        if token and google_fit_data:
            return JsonResponse({"status": "success", "message": "Google Fit data saved!"})
        else:
            return JsonResponse({"status": "error", "message": "Invalid request"}, status=400)
