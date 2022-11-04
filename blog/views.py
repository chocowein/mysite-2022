# import を追加
# render 関数を import している
from django.shortcuts import render
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from blog.models import Article


# render 関数でテンプレートを表示するように
def index(request):
    return render(request, "blog/index.html")

class AccountCreateView(View):
    def get(self, request):
        return render(request, "blog/register.html")

    # post を追加
    def post(self, request):
    # ユーザー情報を保存する
        User.objects.create_user(
            username=request.POST["username"],
            password=request.POST["password"],
        )
        # 登録完了画面を表示する
        return render(request, "blog/register_success.html")

class AccountLoginView(LoginView):
    """ログインページのテンプレート"""
    template_name = 'blog/login.html'

    def get_default_redirect_url(self):
        """ログインに成功した時に飛ばされるURL"""
        return "/blog"

class MypageView(View):
    def get(self, request):
        return render(request, "blog/mypage.html")

class MypageView(LoginRequiredMixin, View):
    login_url = '/blog/login'

    def get(self, request):
        articles = Article.objects.filter(user=request.user)
        return render(request, "blog/mypage.html", {
            "articles": articles
        })

class AccountLogoutView(LogoutView):
    template_name = 'blog/logout.html'

class ArticleListView(View):
    def get(self, request):
        # Django の機能である model を使ってすべての記事を取得する
        # articles は Article のリストになる
        articles = Article.objects.all()
        
        # 取得した記事一覧をテンプレートにわたす
        # こうすると、テンプレートの中で articles という変数が渡せる
        return render(request, "blog/articles.html", {
            "articles": articles
        })

class ArticleCreateView(LoginRequiredMixin, View):
    login_url = '/blog/login'

    def get(self, request):
        """記事を書く画面を表示するリクエスト"""
        return render(request, "blog/article_new.html")

class MypageArticleView(LoginRequiredMixin, View):
    login_url = '/blog/login'
    
    def post(self, request):
        """記事を保存する"""
        # リクエストで受け取った情報をDBに保存する
        article = Article(
            title=request.POST["title"],
            body=request.POST["body"],
            # user には、現在ログイン中のユーザーをセットする
            user=request.user,
        )
        article.save()
        return render(request, "blog/article_created.html")

def index(request):
    # Article の model を使ってすべての記事を取得する
    # Article.objects.all() は article のリストが返ってくる
    articles = Article.objects.all()

    # こうすることで、article 変数をテンプレートにわたす事ができる
    # {テンプレート上での変数名: 渡す変数}
    return render(request, "blog/index.html", {
        "articles": articles
    })

    # 記事についての View
class ArticleView(View):
    # urls.py の <id> が、 id に入る
    def get(self, request, id):
        # get は条件に合致した記事を一つ取得する
        article = Article.objects.get(id=id)
        return render(request, "blog/article.html", {
            "article": article,
        })

