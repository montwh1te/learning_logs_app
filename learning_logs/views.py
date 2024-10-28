from django.shortcuts import render
from .models import Topic, Notes
from .forms import TopicForm, NotesForm
from django.http import HttpResponseRedirect
from django.urls import reverse

def index(request):
    """ Página principal do Learning Log (Projeto) para fazer a requisição de renderização do index.html no learning_logs (app) """
    return render(request, 'learning_logs/index.html')

def topics(request):
    """ Mostra todos os assuntos """
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

def topic(request, topic_id):
    """ Mostra um único assunto e todas as suas entradas """
    topic = Topic.objects.get(id = topic_id)
    entries = topic.notes_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)

def new_topic(request):
    """ Adiciona um novo assunto """
    if request.method != 'POST':
        # Nenhum dado submetido; cria um formulário em branco
        form = TopicForm()
    else:
        # Dados de POST submetidos; processa os dados
        form = TopicForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse('topics'))
    
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)

def new_notes(request, topic_id):
    """ Acrescenta uma nova entrada para um assunto em particular """
    topic = Topic.objects.get(id = topic_id)
    
    if request.method != 'POST':
        # Nenhum dado submetido; cria um formulário em branco
        form = NotesForm()
    else: 
        # Dados de POST submetidos; processa os dados
        form = NotesForm(data=request.POST)
        if form.is_valid():
            new_notes = form.save(commit=False)
            new_notes.note = topic
            new_notes.save()
            return HttpResponseRedirect(reverse('topic', args=[topic_id]))
        
    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_notes.html', context)

def edit_notes(request, notes_id):
    """ Edita uma nota existente """
    note = Notes.objects.get(id = notes_id)
    topic = note.note
    
    if request.method != 'POST':
        form = NotesForm(instance = note) # colocar.text
    else:
        form = NotesForm(instance = note, data = request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('topic', args=[topic.id]))
        
    context = {'note': note, 'topic': topic, 'form': form}
    return render(request, 'learning_logs/edit_notes.html', context)
            
            
        
    