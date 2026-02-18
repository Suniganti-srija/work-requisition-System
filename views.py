from django.shortcuts import render, redirect, get_object_or_404
from .models import WorkRequisition, PROJECT_CHOICES
from .forms import WorkRequisitionForm
from django.db.models import Q

def summary_view(request):
    requisitions = WorkRequisition.objects.all().order_by('-date', '-created_at')
    total_count = requisitions.count()
    
    # Recent addition (just the last one for display if needed)
    last_added = requisitions.first() 
    
    context = {
        'requisitions': requisitions,
        'total_count': total_count,
        'last_added': last_added,
    }
    return render(request, 'requisition/summary.html', context)

def search_view(request):
    query = request.GET.get('q')
    
    requisitions = WorkRequisition.objects.all().order_by('-date')
    
    if query:
        requisitions = requisitions.filter(
            Q(nomenclature__icontains=query) | 
            Q(work_no__icontains=query) |
            Q(project__icontains=query) |
            Q(indentor_name__icontains=query)
        )
            
    context = {
        'requisitions': requisitions,
        'query': query,
    }
    return render(request, 'requisition/search.html', context)

def new_requisition_view(request):
    if request.method == 'POST':
        form = WorkRequisitionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('summary')
    else:
        form = WorkRequisitionForm()
        
    return render(request, 'requisition/form.html', {'form': form, 'title': 'New Requisition'})

def edit_requisition_view(request, pk):
    req = get_object_or_404(WorkRequisition, pk=pk)
    if request.method == 'POST':
        form = WorkRequisitionForm(request.POST, instance=req)
        if form.is_valid():
            form.save()
            return redirect('summary')
    else:
        form = WorkRequisitionForm(instance=req)
    
    return render(request, 'requisition/form.html', {'form': form, 'title': 'Edit Requisition', 'edit_mode': True, 'req_id': pk})

def view_requisition_view(request, pk):
    req = get_object_or_404(WorkRequisition, pk=pk)
    return render(request, 'requisition/detail.html', {'req': req})

def delete_requisition_view(request, pk):
    req = get_object_or_404(WorkRequisition, pk=pk)
    if request.method == 'POST':
        req.delete()
        return redirect('summary')
    return render(request, 'requisition/delete_confirm.html', {'req': req})

def cancel_view(request):
    return redirect('summary')

def home(request):
    return redirect('summary')
