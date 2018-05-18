from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from .forms import PostForm, SNP_search_form, interval_SNP_search, phenotype_search_form
from django.contrib.auth.decorators import login_required
from django.db.models import Q

# Create your views here.

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'snps/post_list.html', {'posts': posts})

@login_required
def phenotype_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'snps/phenotype_list.html', {'posts': posts})

@login_required
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'snps/post_detail.html', {'post': post})

@login_required
def search_phenotype(request):
    if request.method == "POST":
        form = phenotype_search_form(request.POST)
        if form.is_valid():
            post = get_object_or_404(Post, pk=1)
            posts = Post.objects.filter(DISEASE_TRAIT=form.cleaned_data['my_pheno']).order_by('published_date')
            return render(request, 'snps/short_pheno_list.html', {'posts': posts})
    else:
        form = phenotype_search_form()
    return render(request, 'snps/search_phenotype.html', {'form': form})

@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'snps/post_edit.html', {'form': form})

@login_required
def search(request):
    if request.method == "POST":
        form = SNP_search_form(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            posts = Post.objects.filter(Q(CHR_ID=post.CHR_ID)|Q(CHR_POS=post.CHR_POS)|Q(RSID_CURRENT=post.RSID_CURRENT)).order_by('published_date')
            return render(request, 'snps/post_list.html', {'posts': posts})
    else:
        form = SNP_search_form()
    return render(request, 'snps/search.html', {'form': form})

def search_interval(request):
    if request.method == "POST":
        form = interval_SNP_search(request.POST)
        if form.is_valid():
            post = get_object_or_404(Post, pk=1)
            posts = Post.objects.filter(CHR_POS__gte=form.cleaned_data['min_limit']).filter(CHR_POS__lte=form.cleaned_data['max_limit']).order_by('published_date')
            return render(request, 'snps/post_list.html', {'posts': posts})
    else:
        form = interval_SNP_search()
    return render(request, 'snps/search_interval.html', {'form': form})


@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'snps/post_edit.html', {'form': form})

@login_required
def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')
