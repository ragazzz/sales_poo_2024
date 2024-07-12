from django.urls import path
from app.core.views.home import HomeTemplateView
from app.security.views import auth
from app.security.views import menu, module, groupmodulepermission
app_name = "security"
# security
urlpatterns = [
    path('auth/login/', auth.SigninView.as_view(), name="auth_login"),
    path('auth/logout/', auth.SignoutView.as_view(), name='auth_logout'),
    path('auth/signup/', auth.SignupView.as_view(), name='auth_signup'),
    path('auth/profile/', auth.ProfileView.as_view(), name='auth_profile'),
    path('auth/change_password/', auth.ChangePasswordView.as_view(), name='auth_change_password'),
    path('auth/update_profile/', auth.UpdateProfileView.as_view(), name='auth_update_profile'),
    path('', HomeTemplateView.as_view(), name='home'),
    #URLs menu
    path('menu_list/',menu.MenuListView.as_view(),name='menu_list'),
    path('menu_create/',menu.MenuCreateView.as_view(),name='menu_create'),
    path('menu_update/<int:pk>/',menu.MenuUpdateView.as_view(),name='menu_update'),
    path('menu_delete/<int:pk>/',menu.MenuDeleteView.as_view(),name='menu_delete'),
    #URLs modulo
    path('module_list/',module.ModuleListView.as_view(),name='module_list'),
    path('module_create/',module.ModuleCreateView.as_view(),name='module_create'),
    path('module_update/<int:pk>/',module.ModuleUpdateView.as_view(),name='module_update'),
    path('module_delete/<int:pk>/',module.ModuleDeleteView.as_view(),name='module_delete'),
    #URLs grupomodulopermiso
    path('groupmodulepermission_list/',groupmodulepermission.GroupModulePermissionListView.as_view(),name='groupmodulepermission_list'),
    path('groupmodulepermission_create/',groupmodulepermission.GroupModulePermissionCreateView.as_view(),name='groupmodulepermission_create'),
    path('groupmodulepermission_update/<int:pk>/',groupmodulepermission.GroupModulePermissionUpdateView.as_view(),name='groupmodulepermission_update'),
    path('groupmodulepermission_delete/<int:pk>/',groupmodulepermission.GroupModulePermissionDeleteView.as_view(),name='groupmodulepermission_delete'),
]

