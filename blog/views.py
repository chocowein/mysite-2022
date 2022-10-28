# import を追加
# render 関数を import している
from django.shortcuts import render
from django.views import View

# render 関数でテンプレートを表示するように
def index(request):
    return render(request, "blog/index.html")

class AccountCreateView(View):
    def get(self, request):
        return render(request, "blog/register.html")