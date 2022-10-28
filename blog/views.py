# import を追加
# render 関数を import している
from django.shortcuts import render
from django.views import View
from django.contrib.auth.models import User

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