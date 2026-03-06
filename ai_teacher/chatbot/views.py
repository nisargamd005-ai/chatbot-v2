from django.shortcuts import render
from google import genai
import os

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

def home(request):
    answer = ""

    if request.method == "POST":
        question = request.POST.get("question")

        try:
            response = client.models.generate_content(
                model="gemini-2.0-flash",
                contents=question,
            )

            answer = response.text

        except Exception as e:
            answer = "⚠️ API quota exceeded. Please try again later."

    return render(request, "index.html", {"answer": answer})
