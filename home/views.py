from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods

def home(request): 
    return render(request, "home.html")


@require_http_methods(["POST"])
def validateForm(request): 
    validationResult = {
        "status":"true", 
        "errors": []
    }    
    try:
        text = request.POST.get("textToStyle")
        startIndex = int(request.POST.get("startIndex"))
        endIndex = int(request.POST.get("endIndex"))   
        textLen = len(text)
        if textLen == 0:
            validationResult["status"] = False
            validationResult["errors"].append("Text is empty.")  
        
        if  startIndex < 0 : 
            validationResult["status"] = False
            validationResult["errors"].append("Invalid start index")
        
        if  endIndex >= textLen :
            validationResult["status"] = False
            validationResult["errors"].append("Invalid end index")  
    except: 
        validationResult["status"] = False
        validationResult["errors"].append("Oops! Validation failed.")

        
    return JsonResponse(validationResult)


