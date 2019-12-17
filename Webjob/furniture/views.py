import datetime

from django.contrib.auth import authenticate
from django.core.mail import send_mail
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
import datetime
# Create your views here.
from furniture.models import User, Furn, OrderItem, Order, LookItem


def index(request):
    '''
    函数功能：用在首页index.html
    :param request:
    :return:
    '''
    return render(request, 'index.html')


def register(request):
    '''
    函数功能：用户注册，用在register.html
    :param request:
    :return:
    '''
    if request.method == 'GET':
        return render(request, 'register.html')
    elif request.method == 'POST':
        telephone = request.POST.get("phonenumber", None)
        email = request.POST.get("email", None)
        username = request.POST.get("usernumber", None)
        regist_time = datetime.datetime.now()
        password = request.POST.get("password", None)
        if not telephone or not email or not username or not password:
            return HttpResponse("请按照要求填写相关信息!!!")
        user = User()
        user.username = username
        user.telephone = telephone
        user.email = email
        user.password = password
        user.regist_time = regist_time
        user.save()
        return HttpResponse("%s注册成功!!!" % username)


def login(request):
    '''
    函数功能：用户登陆，设置Cookie,用在index.html
    :param request:
    :return:
    '''
    u_tele = request.POST.get("tele", None)
    u_password = request.POST.get("password", None)
    if not u_tele or not u_password:
        return render(request, 'index.html')
    u = User.objects.get(telephone=u_tele)
    if u.password != u_password:
        return HttpResponse('密码和手机号不匹配')
    if u_tele == 'admin':
        response = HttpResponseRedirect(reverse('furn:myFurn'))
    else:
        response = HttpResponseRedirect(reverse('furn:store'))

    response.set_signed_cookie('telephone', u.telephone, "Rock")  # 加盐，默认关浏览器cookie过期
    response.set_signed_cookie('cart', 0, "Rock")
    return response


def logout(request):
    '''
    函数功能：用户注销，用在所有页面
    :param request:
    :return:
    '''
    response = HttpResponseRedirect(reverse('furn:index'))
    response.set_signed_cookie('telephone', 'None', "Rock")  # 加盐，默认关浏览器cookie过期
    return response


def store(request):
    '''
    函数功能：商品展示,用在store.html
    :param request:
    :return:
    '''
    u_telephone = request.get_signed_cookie('telephone', salt="Rock")
    f = Furn.objects.all()
    if f.count() == 0:
        data = {"msg": "当前无该商品。"}
    else:
        data = {
            "furn_list": f,
            "name": u_telephone
        }
    return render(request, 'store.html', context=data)


def AFurn(request, id):
    '''
    显示该商品的所有信息
    :param request:
    :param id: 商品id
    :return:
    '''
    u_telephone = request.get_signed_cookie('telephone', salt="Rock")
    f = Furn.objects.get(fid__in=[id])
    u = User.objects.get(telephone__in=[u_telephone])
    look = LookItem()
    look.uid = u.uid
    look.fid = id
    look.date = datetime.datetime.today()
    look.lname = f.fname
    look.lcategory = f.fcategory
    look.lprice = f.fprice
    look.save()

    photo_url = '/static/furnphoto/' + f.fphoto.url
    data = {
        'fid': f.fid,
        'fname': f.fname,
        'fprice': f.fprice,
        'fcate': f.fcategory,
        'fnum': f.fnum,
        'fphoto': photo_url,
        'fdes': f.fdescribe,
        'name': u_telephone
    }
    return render(request, 'Afurn.html', context=data)


def myFurn(request):
    '''
    函数功能：商家使用对商品进行增加、删除、修改和查询，用在myFurn.html
    :param request:
    :return:
    '''
    u_telephone = request.get_signed_cookie('telephone', salt="Rock")
    f = Furn.objects.all()
    data = {
        "furn_list": f,
        "name": u_telephone
    }
    return render(request, 'myFurn.html', context=data)


def addFurn(request):
    '''
    函数功能：商家增加商品，用在myFurn.html
    :param request:
    :return:
    '''
    if request.method == 'GET':
        return render(request, 'addFurn.html')
    elif request.method == 'POST':
        f_name = request.POST.get("fname", None)
        f_price = request.POST.get("fprice", None)
        f_cate = request.POST.get("fcate", None)
        f_num = request.POST.get("fnum", None)
        f_photo = request.FILES.get("fphoto", None)
        f_des = request.POST.get("fdes", None)
        if not f_name or not f_price or not f_cate or not f_num or not f_photo:
            msg = "选项不能为空，请输入家具信息!!!"
            data = {"msg": msg}
            return render(request, 'addFurn.html', context=data)

        furn = Furn()
        furn.fname = f_name
        furn.fprice = f_price
        furn.fcategory = f_cate
        furn.fnum = f_num
        furn.fphoto = f_photo
        furn.fdescribe = f_des
        furn.save()
        return HttpResponse("增加家具%s成功!!!" % f_name)


def editFurn(request, id):
    '''
    函数功能：商家修改商品信息，用在editFurn.html和myFurn.html
    :param request:
    :param id: 家具id
    :return:
    '''
    if request.method == 'GET':
        return render(request, 'editFurn.html')
    elif request.method == 'POST':
        f_price = request.POST.get("fprice", None)
        f_num = request.POST.get("fnum", None)
        f_des = request.POST.get("fdes", None)

        f = Furn.objects.get(fid__in=[id])
        f.fprice = f_price
        f.fnum = f_num
        f.fdescribe = f_des
        f.save()
        msg = "修改家具%s成功!!!" % f.fname
        data = {"msg": msg}
        return render(request, 'editFurn.html', context=data)


def editf(request, id):
    '''
    函数功能：商家修改商品信息，用在editFurn.html和myFurn.html
    :param request:
    :param id: 家具id
    :return:
    '''
    u_telephone = request.get_signed_cookie('telephone', salt="Rock")
    f = Furn.objects.get(fid__in=[id])
    data = {
        "fid": f.fid,
        "furnname": f.fname,
        "furncate": f.fcategory,
        "name": u_telephone
    }
    return render(request, 'editFurn.html', context=data)


def deleteFurn(request, id):
    '''
    函数功能：商家删除商品信息，用在myFurn.html
    :param request:
    :param id: 家具id
    :return:
    '''
    f = Furn.objects.get(fid__in=[id])
    f.delete()
    # return render(request,'myFurn.html')
    response = HttpResponseRedirect(reverse('furn:myFurn'))
    return response


def showBed(request):
    '''
    函数功能：展示所有的床，用在store.html
    :param request:
    :return:
    '''
    u_telephone = request.get_signed_cookie('telephone', salt="Rock")
    f_list = Furn.objects.filter(fcategory__in=["床"])
    for f in f_list:
        print(f.fname)

    data = {
        "furn_list": f_list,
        "name": u_telephone
    }

    return render(request, 'store.html', context=data)


def showFood(request):
    '''
    函数功能：展示所有的餐桌椅，用在store.html
    :param request:
    :return:
    '''
    u_telephone = request.get_signed_cookie('telephone', salt="Rock")
    f_list = Furn.objects.filter(fcategory__in=["餐桌椅"])
    for f in f_list:
        print(f.fname)

    data = {
        "furn_list": f_list,
        "name": u_telephone
    }

    return render(request, 'store.html', context=data)


def showRobe(request):
    '''
    函数功能：展示所有的衣柜，用在store.html
    :param request:
    :return:
    '''
    u_telephone = request.get_signed_cookie('telephone', salt="Rock")
    f_list = Furn.objects.filter(fcategory__in=["衣柜"])
    for f in f_list:
        print(f.fname)

    data = {
        "furn_list": f_list,
        "name": u_telephone
    }

    return render(request, 'store.html', context=data)


def showLocker(request):
    '''
    函数功能：展示所有的储物家居，用在store.html
    :param request:
    :return:
    '''
    u_telephone = request.get_signed_cookie('telephone', salt="Rock")
    f_list = Furn.objects.filter(fcategory__in=["储物家具"])
    for f in f_list:
        print(f.fname)

    data = {
        "furn_list": f_list,
        "name": u_telephone
    }

    return render(request, 'store.html', context=data)


def addOrderitem(request, fid):
    '''
    函数功能：增加订单项，用在AFurn.html
    :param request:
    :param fid:商品id
    :param oid:订单id
    :param num:购买商品个数
    :return:
    '''
    f = Furn.objects.get(fid__in=[fid])
    num = request.POST.get("num", None)
    f.fnum = f.fnum - int(num)
    f.save()
    orderitem = OrderItem()
    cart = request.get_signed_cookie('cart', salt="Rock")
    print("cart:" + cart)
    if cart == '0':
        order = Order()
        tel = request.get_signed_cookie('telephone', salt="Rock")
        u = User.objects.get(telephone__in=[tel])
        print("u.uid:" + str(u.uid))
        pay = int(num) * f.fprice
        order.pay = pay
        order.uid = u.uid
        order.save()
        orderitem.o_oid = order.oid
    else:
        orderitem.o_oid = cart
        o = Order.objects.get(oid__in=[orderitem.o_oid])
        o.pay = o.pay + int(num) * f.fprice
        o.save()

    orderitem.o_fid = fid
    orderitem.buynum = num
    orderitem.name = f.fname
    orderitem.price = f.fprice
    orderitem.category = f.fcategory
    orderitem.num = f.fnum
    orderitem.save()

    response = HttpResponseRedirect(reverse('furn:store'))
    response.set_signed_cookie('cart', orderitem.o_oid, "Rock")
    return response


def mycart(request):
    '''
    函数功能：购物车，用在mycart.html
    :param request:
    :return:
    '''
    u_telephone = request.get_signed_cookie('telephone', salt="Rock")  # 解密
    cart = request.get_signed_cookie('cart', salt="Rock")
    if cart == '0':
        data = {
            "msg": "当前购物车为空。",
            "money": 0,
            "name": u_telephone
        }
        return render(request, 'mycart.html', context=data)
    else:
        flist = OrderItem.objects.filter(o_oid__in=[cart])
        o = Order.objects.get(oid__in=[cart])

        data = {
            "flist": flist,
            "money": o.pay,
            "name": u_telephone
        }
        return render(request, 'mycart.html', context=data)


def deleteorderitem(request, id):
    '''
    函数功能：删除订单项，用在mycart.html
    :param request:
    :param id: 订单项id
    :return:
    '''
    Ot = OrderItem.objects.get(id__in=[id])
    f = Furn.objects.get(fid__in=[Ot.o_fid])
    f.fnum = f.fnum + Ot.buynum
    f.save()
    o = Order.objects.get(oid__in=[Ot.o_oid])
    o.pay = o.pay - Ot.buynum * f.fprice
    o.save()
    Ot.delete()
    response = HttpResponseRedirect(reverse('furn:mycart'))
    return response


def pay(request):
    '''
    支付
    发邮件确认
    :param request:
    :return:
    '''
    return render(request, 'pay.html')


def addData(request):
    '''
    支付成功后，修改订单状态，发送确认邮件，修改销售额
    :param request:
    :return:
    '''
    if request.method == 'GET':
        return render(request, 'editFurn.html')
    elif request.method == 'POST':
        rname = request.POST.get("rname", None)
        raddress = request.POST.get("raddress", None)
        rphone = request.POST.get("rphone", None)
        cart = request.get_signed_cookie('cart', salt="Rock")
        #修改订单状态
        o = Order.objects.get(oid__in=[cart])
        o.rname = rname
        o.raddress = raddress
        o.rphone = rphone
        o.paystate = True
        o.order_time = datetime.datetime.today()
        o.save()
        #发邮件确认
        tel = request.get_signed_cookie('telephone', salt="Rock")
        u = User.objects.get(telephone__in=[tel])
        subject = "Furn Store"
        mes = "<h1>您好," + u.username + "</h1>" + "<p>您已经成功支付了订单，支付金额:" + str(o.pay) + "元。</p>"
        rdata = "<p>收货人：" + str(o.rname) + "</p><p>收货地址：" + str(o.raddress) + "</p><p>收货人电话：" + str(o.rphone) + "</p>"
        message = mes + rdata
        from_email = 'IngridWBY@163.com'
        to_list = [u.email, ]
        send_mail(subject=subject, message=message, html_message=message, from_email=from_email,
                  recipient_list=to_list, )
        #修改销售额
        olist = OrderItem.objects.filter(o_oid__in=[cart])
        for i in range(olist.count()):
            f = Furn.objects.get(fid__in=[olist[i].o_fid])
            f.fsale = f.fsale + olist[i].buynum
            f.save()

        response = HttpResponseRedirect(reverse('furn:paySuccess'))
        response.set_signed_cookie('cart', 0, "Rock")
        return response


def paySuccess(request):
    tel = request.get_signed_cookie('telephone', salt="Rock")
    data = { "name" : tel}
    return render(request,'paySuccess.html',context=data)


def sale(request):
    '''
    函数功能：销售记录,用在sale.html
    :param request:
    :return:
    '''
    f = Furn.objects.all()
    data = {
        "flist": f
    }
    return render(request, 'sale.html', context=data)


def mine(request):
    '''
    函数功能：个人中心,用在mine.html,购买记录
    :param request:
    :return:
    '''
    tel = request.get_signed_cookie('telephone', salt="Rock")  # 解密
    u = User.objects.get(telephone__in=[tel])
    olist = Order.objects.filter(uid__in=[u.uid])
    k = []  # 购买记录
    for i in range(olist.count()):
        if olist[i].paystate:
            tlist = OrderItem.objects.filter(o_oid__in=[olist[i].oid])
            for j in range(tlist.count()):
                t = OrderItem.objects.get(id__in=[tlist[j].id])
                k.append(t)

    data = {
        "glist": k,
        "name": tel
    }
    return render(request, 'mine.html', context=data)


def look(request):
    tel = request.get_signed_cookie('telephone', salt="Rock")  # 解密
    u = User.objects.get(telephone__in=[tel])
    llist = LookItem.objects.filter(uid__in=[u.uid])  # 浏览记录
    data = {
        "llist": llist,
        "name": tel
    }
    return render(request, 'look.html', context=data)
