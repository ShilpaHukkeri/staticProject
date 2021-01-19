from django.shortcuts import render
def view(r):
    myName='Shilpa'
    favActor='Nani'
    favAnimal='Dog'
    favSubject='Python'
    favBird='Peacock'
    d={'Name':myName,'Actor':favActor,'Animal':favAnimal,'Subject':favSubject,'Bird':favBird}
    return render(r,'staticApp/1.html',d)

