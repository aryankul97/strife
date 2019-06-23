"""bout URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', bout),
    path('strife/', bout),
    path('strife/about-us/', about),
    path('strife/contact-us/', contact),
    path('strife/premium/', getpre),
    path('strife/premium/getpremium/', premium),
    path('strife/superadmin/', superadmin),
    path('strife/superadmin/superadmincheck/', superadmincheck),
    path('strife/superadmin/superadmincheck/changepaid/', changepaid),
    path('strife/superadmin/superadmincheck/getpass/', getpass),
    path('strife/superadmin/superadmincheck/getpass/getadminpassword/', getadminpassword),
    path('strife/file/', fileopen),
    path('strife/file/save/', filedata),
    path('strife/sendquery/', query),
    path('our/', adminactive),
    path('strife/startquiz/', startquiz),
    path('strife/startquiz/checkcandidate/', checkcandidate),
    path('strife/startquiz/checkcandidate/generateresult/', gnerateresult),
    path('strife/register/', saveCan),
    path('adminprofile/', adminprofile),
    path('strife/adminlogin/', adminlogin),
    path('strife/adminlogin/actadmin/', adminact),
    path('strife/adminlogin/forgotpassword/', forgot),
    path('strife/adminlogin/forgotpassword/check/', forgotpassword),
    path('strife/adminlogin/newadmin/saveadmin/adminlogin/', adminlogin),
    path('strife/adminlogin/newadmin/', newadmin),
    path('strife/adminlogin/newadmin/saveadmin/', saveadmin),
    path('strife/adminlogin/checklogin/', checklogin),
    path('strife/adminlogin/checklogin/resetpassword/', resetpass),
    path('strife/adminlogin/checklogin/resetpassword/reset/', resetpassword),
    path('strife/adminlogin/checklogin/startcompetition/', savecomp),
    path('strife/adminlogin/checklogin/activecomp/', compdata),
    path('strife/adminlogin/checklogin/deactivecomp/', deactivecomp),
    path('strife/adminlogin/checklogin/accomp/', activecomp),
    path('strife/adminlogin/backlogin/', backlogin),
    path('strife/adminlogin/checklogin/yourstrifes/compques/', compques),
    path('strife/adminlogin/checklogin/yourstrifes/compques/deleteCan/', deleteCandidate),
    path('strife/adminlogin/checklogin/yourstrifes/compques/deleteCan/delete/', deleteCan),
    path('strife/adminlogin/checklogin/yourstrifes/compques/deleteques/', deleteQues),
    path('strife/adminlogin/checklogin/yourstrifes/compques/deleteques/delete/', deleteQ),
    path('strife/adminlogin/checklogin/yourstrifes/compques/candidatelist/', canlist),
    path('strife/adminlogin/checklogin/yourstrifes/compques/candidatelist/canCSV/', canCSV),
    path('strife/adminlogin/checklogin/yourstrifes/compques/delete/', remcomp),
    path('strife/adminlogin/checklogin/yourstrifes/compques/delete/action/', compdelete),
    path('strife/adminlogin/checklogin/yourstrifes/compques/results/', results),
    path('strife/adminlogin/checklogin/yourstrifes/compques/results/resultsCSV/', resultsCSV),
    path('strife/adminlogin/checklogin/yourstrifes/compques/addques/', addques),
    path('strife/adminlogin/checklogin/yourstrifes/compques/addques/quesPDF/', quesPDF),
    path('strife/adminlogin/checklogin/yourstrifes/compques/addques/deaccomp/', deaccomp),
    path('strife/adminlogin/checklogin/yourstrifes/compques/addques/addmore/', ques),
]
