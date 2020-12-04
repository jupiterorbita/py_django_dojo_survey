from django.shortcuts import render, redirect

def index(req):
  print("\n░▒▓ INDEX ▓▒░ ")
  return render(req, 'index.html')

def result(req):
  print("\n░▒▓ --- Result --- ▓▒░ ")
  if req.method == "GET":
    return redirect('/')

  if req.method == "POST":
    print('======== POST =======')
    print(req.POST)
    name = req.POST["name"]
    loc = req.POST["location"]
    comment = req.POST["comment"]
    
    context = {
      "name" : name,
      "loc": loc,
      "comment": comment
    }
    return render(req, 'result.html', context)