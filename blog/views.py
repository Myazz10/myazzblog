from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView
from .models import Post, Comment, Category, Popular_Article
from .forms import CommentForm
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.core.mail import send_mail


# Home page
class HomeView(ListView):
    model = Post
    template_name = 'blog/home.html'
    ordering = ['-published_date']
    context_object_name = 'posts'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post_items = Post.objects.all()
        # archive_dates = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
        # archive_dates = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

        popular_article = Popular_Article.objects.order_by('-date_added')
        popular_dict = {}

        category = {'Food': [0, 0], 'Fashion': [0, 0], 'Travel': [0, 0], 'Technology': [0, 0], 'Photography': [
            0, 0], 'Sports': [0, 0], 'Weather': [0, 0], 'News': [0, 0], 'Nature': [0, 0], 'Movies': [0, 0], 'Anime': [0, 0]}

        # After getting the objects for my Post model... I'll try and draw the category counters for each category
        # and assign them to the context variable so I can use them in the template to display category details...
        # Note: {'Food' - Category Tag, Index [0] - Post by Category amount & Index [1] - Category ID/PK}

        for item in post_items:
            if item.category_tags.name == 'Food':
                category['Food'][0] += 1
                category['Food'][1] = item.category_tags.pk
            elif item.category_tags.name == 'Weather':
                category['Weather'][0] += 1
                category['Weather'][1] = item.category_tags.pk
            elif item.category_tags.name == 'News':
                category['News'][0] += 1
                category['News'][1] = item.category_tags.pk
            elif item.category_tags.name == 'Nature':
                category['Nature'][0] += 1
                category['Nature'][1] = item.category_tags.pk
            elif item.category_tags.name == 'Movies':
                category['Movies'][0] += 1
                category['Movies'][1] = item.category_tags.pk
            elif item.category_tags.name == 'Anime':
                category['Anime'][0] += 1
                category['Anime'][1] = item.category_tags.pk
            elif item.category_tags.name == 'Sports':
                category['Sports'][0] += 1
                category['Sports'][1] = item.category_tags.pk
            elif item.category_tags.name == 'Travel':
                category['Travel'][0] += 1
                category['Travel'][1] = item.category_tags.pk
            elif item.category_tags.name == 'Fashion':
                category['Fashion'][0] += 1
                category['Fashion'][1] = item.category_tags.pk
            elif item.category_tags.name == 'Technology':
                category['Technology'][0] += 1
                category['Technology'][1] = item.category_tags.pk
            elif item.category_tags.name == 'Photography':
                category['Photography'][0] += 1
                category['Photography'][1] = item.category_tags.pk
            else:
                pass

        # Popular Articles...
        for post in popular_article:
            # Key: Title ---> Value[0: ID/PK, 1: Intro Picture, 2: Number of Comments, 3: Author, 4: Published Date]
            popular_dict[post.popular_post.title] = [post.popular_post.pk, post.popular_post.intro_picture,
                                                     post.popular_post.approved_comments, post.popular_post.author, post.popular_post.published_date]

            # Adding categories and the amount of category related post to the context variable...
        context['categories'] = category
        context['popular_articles'] = popular_dict

        return context


def post_detail(request, pk=None):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


@ login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('post_detail', pk=comment.post.pk)


@ login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('post_detail', pk=comment.post.pk)


# Post Detail View
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_details.html'
    context_object_name = 'post'
    ordering = ['-published_date']

    # This get_object will do the math for the total number of views that a specific post received...
    def get_object(self):
        object = super(PostDetailView, self).get_object()
        object.view_count += 1
        object.save()
        return object

    def get_queryset(self):
        return Post.objects.order_by('-published_date')

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        popular_article = Popular_Article.objects.order_by('-date_added')
        popular_dict = {}

        # This operation 'order_by' will take the data from the database and allow it be sorted by the latest date for
        # the Popular Articles section...
        post_items = Post.objects.order_by('-published_date')

        category = {'Food': [0, 0], 'Fashion': [0, 0], 'Travel': [0, 0], 'Technology': [0, 0], 'Photography': [
            0, 0], 'Sports': [0, 0], 'Weather': [0, 0], 'News': [0, 0], 'Nature': [0, 0], 'Movies': [0, 0], 'Anime': [0, 0]}

        # After getting the objects for my Post model... I'll try and draw the category counters for each category
        # and assign them to the context variable so I can use them in the template to display category details...
        # Note: {'Food' - Category Tag, Index [0] - Post by Category amount & Index [1] - Category ID/PK}

        for item in post_items:
            if item.category_tags.name == 'Food':
                category['Food'][0] += 1
                category['Food'][1] = item.category_tags.pk
            elif item.category_tags.name == 'Weather':
                category['Weather'][0] += 1
                category['Weather'][1] = item.category_tags.pk
            elif item.category_tags.name == 'News':
                category['News'][0] += 1
                category['News'][1] = item.category_tags.pk
            elif item.category_tags.name == 'Nature':
                category['Nature'][0] += 1
                category['Nature'][1] = item.category_tags.pk
            elif item.category_tags.name == 'Movies':
                category['Movies'][0] += 1
                category['Movies'][1] = item.category_tags.pk
            elif item.category_tags.name == 'Anime':
                category['Anime'][0] += 1
                category['Anime'][1] = item.category_tags.pk
            elif item.category_tags.name == 'Sports':
                category['Sports'][0] += 1
                category['Sports'][1] = item.category_tags.pk
            elif item.category_tags.name == 'Travel':
                category['Travel'][0] += 1
                category['Travel'][1] = item.category_tags.pk
            elif item.category_tags.name == 'Fashion':
                category['Fashion'][0] += 1
                category['Fashion'][1] = item.category_tags.pk
            elif item.category_tags.name == 'Technology':
                category['Technology'][0] += 1
                category['Technology'][1] = item.category_tags.pk
            elif item.category_tags.name == 'Photography':
                category['Photography'][0] += 1
                category['Photography'][1] = item.category_tags.pk
            else:
                pass

        # Popular Articles...
        for post in popular_article:
            # Key: Title ---> Value[0: ID/PK, 1: Intro Picture, 2: Number of Comments, 3: Author, 4: Published Date]
            popular_dict[post.popular_post.title] = [post.popular_post.pk, post.popular_post.intro_picture,
                                                     post.popular_post.approved_comments, post.popular_post.author, post.popular_post.published_date]

        # Adding categories and the amount of category related post to the context variable...
        context['categories'] = category
        context['posts'] = post_items
        context['popular_articles'] = popular_dict

        return context


# Post by Category...
class PostByCategory(ListView):
    model = Post
    template_name = 'blog/post_by_category.html'
    context_object_name = 'posts'
    paginate_by = 10

    # This will reset and order the post to be filtered by category and ordered by the latest date...
    def get_queryset(self):
        self.category = get_object_or_404(Category, pk=self.kwargs['pk'])
        return Post.objects.filter(category_tags=self.category).order_by('-published_date')

    def get_context_data(self, **kwargs):
        context = super(PostByCategory, self).get_context_data(**kwargs)

        popular_article = Popular_Article.objects.order_by('-date_added')
        popular_dict = {}

        # post_items = Post.objects.all()
        post_items = Post.objects.order_by('-published_date')

        category = {'Food': [0, 0], 'Fashion': [0, 0], 'Travel': [0, 0], 'Technology': [0, 0], 'Photography': [
            0, 0], 'Sports': [0, 0], 'Weather': [0, 0], 'News': [0, 0], 'Nature': [0, 0], 'Movies': [0, 0], 'Anime': [0, 0]}

        # After getting the objects for my Post model... I'll try and draw the category counters for each category
        # and assign them to the context variable so I can use them in the template to display category details...
        # Note: {'Food' - Category Tag, Index [0] - Post by Category amount & Index [1] - Category ID/PK}

        for item in post_items:
            if item.category_tags.name == 'Food':
                category['Food'][0] += 1
                category['Food'][1] = item.category_tags.pk
            elif item.category_tags.name == 'Weather':
                category['Weather'][0] += 1
                category['Weather'][1] = item.category_tags.pk
            elif item.category_tags.name == 'News':
                category['News'][0] += 1
                category['News'][1] = item.category_tags.pk
            elif item.category_tags.name == 'Nature':
                category['Nature'][0] += 1
                category['Nature'][1] = item.category_tags.pk
            elif item.category_tags.name == 'Movies':
                category['Movies'][0] += 1
                category['Movies'][1] = item.category_tags.pk
            elif item.category_tags.name == 'Anime':
                category['Anime'][0] += 1
                category['Anime'][1] = item.category_tags.pk
            elif item.category_tags.name == 'Sports':
                category['Sports'][0] += 1
                category['Sports'][1] = item.category_tags.pk
            elif item.category_tags.name == 'Travel':
                category['Travel'][0] += 1
                category['Travel'][1] = item.category_tags.pk
            elif item.category_tags.name == 'Fashion':
                category['Fashion'][0] += 1
                category['Fashion'][1] = item.category_tags.pk
            elif item.category_tags.name == 'Technology':
                category['Technology'][0] += 1
                category['Technology'][1] = item.category_tags.pk
            elif item.category_tags.name == 'Photography':
                category['Photography'][0] += 1
                category['Photography'][1] = item.category_tags.pk
            else:
                pass

        # Popular Articles...
        for post in popular_article:
            # Key: Title ---> Value[0: ID/PK, 1: Intro Picture, 2: Number of Comments, 3: Author, 4: Published Date]
            popular_dict[post.popular_post.title] = [post.popular_post.pk, post.popular_post.intro_picture,
                                                     post.popular_post.approved_comments, post.popular_post.author, post.popular_post.published_date]

        # Adding categories and the amount of category related post to the context variable...
        context['categories'] = category
        context['popular_articles'] = popular_dict

        # This context variable will be the Category Tag header on the post by category page...
        context['category_tags'] = self.category
        return context


# Post Date View Method to add comment to a specific post
def add_comment_to_post(request, pk=None):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        comment = Comment(post=post, reply=None, approved_comment=True)
        comment.post_id = post.pk
        comment.author = request.POST.get('name')
        comment.text = request.POST.get('message')
        post.post_id = comment.save()
        post.save()
        return redirect('post_detail', post.pk)

    else:
        post_info = post
    return render(request, 'blog/post_details.html', {'posts': post_info})


# Post Date View Method to add replies to a specific comment
def add_reply_to_comment(request, pk=None):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        comment = Comment(post=post, reply=None)
        comment.post_id = post.pk
        comment.author = request.POST.get('name')
        comment.text = request.POST.get('message')
        reply_id = request.POST['comment_id']
        comment_qs = None
        if reply_id:
            comment_qs = Comment.objects.get(id=reply_id)
            comment.reply = comment_qs
            comment.approved_comment = False
        post.post_id = comment.save()
        post.save()
        return redirect('post_detail', post.pk)
    else:
        post_info = post
    return render(request, 'blog/post_details.html', {'post': post_info})


def news_letter(request):
    if request.method == "POST":
        subscriber = request.POST['subscriber']
        message = f'Please add this email - {subscriber} - to the News Letter list Sir!'

        # Set up to send an email...
        send_mail(
            'Moi\'s Blog: News Letter Subscriber',  # Subject
            message,  # Message
            subscriber,  # From email
            ['moimyazz@gmail.com'],  # To email
            fail_silently=False,
        )

        return redirect('home')


# About Page
def about(request):
    template = 'blog/about.html'
    context = {

    }

    return render(request, template, context)


# Contact Page
def contact(request):
    # The method whenever a there is a form on the page to fill out...
    if request.method == "POST":
        # This is how to get the information from the form on the frontend to the backend...
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        text = request.POST['message']

        message = f'Moi\'s Blog: Contact Form...\n\nName: {name}\nEmail: {email}\nMessage: {text}\n\n'
        #message = "Moi's Blog: Contact Form...\n\nName: " + name + "\nEmail: " + email + "\nMessage: " + text + "\n\n"

        if subject == '':
            subject = 'Moi\'s Blog: Contact Form'

        # Set up to send an email...
        send_mail(
            subject,  # Subject
            message,  # Message
            email,  # From email
            ['moimyazz@gmail.com'],  # To email
        )

        context = {
            'name': name,
        }
        return render(request, 'blog/contact.html', context)
    else:
        context = {

        }
        return render(request, 'blog/contact.html', context)


# Single Page
def single(request):
    template = 'blog/single.html'
    context = {

    }

    return render(request, template, context)


# Fashion Page
def fashion(request):
    template = 'blog/fashion.html'
    context = {

    }

    return render(request, template, context)


# Travel Page
def travel(request):
    template = 'blog/travel.html'
    context = {

    }

    return render(request, template, context)


class TravelView(ListView):
    model = Post
    template_name = 'blog/travel.html'
    ordering = ['-published_date']
    context_object_name = 'posts'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post_items = Post.objects.all()
        # archive_dates = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
        # archive_dates = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

        popular_article = Popular_Article.objects.order_by('-date_added')
        popular_dict = {}

        category = {'Food': [0, 0], 'Fashion': [0, 0], 'Travel': [0, 0], 'Technology': [0, 0], 'Photography': [
            0, 0], 'Sports': [0, 0], 'Weather': [0, 0], 'News': [0, 0], 'Nature': [0, 0], 'Movies': [0, 0], 'Anime': [0, 0]}

        # After getting the objects for my Post model... I'll try and draw the category counters for each category
        # and assign them to the context variable so I can use them in the template to display category details...
        # Note: {'Food' - Category Tag, Index [0] - Post by Category amount & Index [1] - Category ID/PK}

        for item in post_items:
            if item.category_tags.name == 'Food':
                category['Food'][0] += 1
                category['Food'][1] = item.category_tags.pk
            elif item.category_tags.name == 'Weather':
                category['Weather'][0] += 1
                category['Weather'][1] = item.category_tags.pk
            elif item.category_tags.name == 'News':
                category['News'][0] += 1
                category['News'][1] = item.category_tags.pk
            elif item.category_tags.name == 'Nature':
                category['Nature'][0] += 1
                category['Nature'][1] = item.category_tags.pk
            elif item.category_tags.name == 'Movies':
                category['Movies'][0] += 1
                category['Movies'][1] = item.category_tags.pk
            elif item.category_tags.name == 'Anime':
                category['Anime'][0] += 1
                category['Anime'][1] = item.category_tags.pk
            elif item.category_tags.name == 'Sports':
                category['Sports'][0] += 1
                category['Sports'][1] = item.category_tags.pk
            elif item.category_tags.name == 'Travel':
                category['Travel'][0] += 1
                category['Travel'][1] = item.category_tags.pk
            elif item.category_tags.name == 'Fashion':
                category['Fashion'][0] += 1
                category['Fashion'][1] = item.category_tags.pk
            elif item.category_tags.name == 'Technology':
                category['Technology'][0] += 1
                category['Technology'][1] = item.category_tags.pk
            elif item.category_tags.name == 'Photography':
                category['Photography'][0] += 1
                category['Photography'][1] = item.category_tags.pk
            else:
                pass

        # Popular Articles...
        for post in popular_article:
            # Key: Title ---> Value[0: ID/PK, 1: Intro Picture, 2: Number of Comments, 3: Author, 4: Published Date]
            popular_dict[post.popular_post.title] = [post.popular_post.pk, post.popular_post.intro_picture,
                                                     post.popular_post.approved_comments, post.popular_post.author, post.popular_post.published_date]

            # Adding categories and the amount of category related post to the context variable...
        context['categories'] = category
        context['popular_articles'] = popular_dict

        return context
