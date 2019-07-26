{"filter":false,"title":"views.py","tooltip":"/cart/views.py","undoManager":{"mark":0,"position":0,"stack":[[{"start":{"row":0,"column":0},"end":{"row":36,"column":41},"action":"remove","lines":["from django.shortcuts import render, redirect, reverse","","# Create your views here.","def view_cart(request):","    \"\"\"A View that renders the cart contents page\"\"\"","    return render(request, \"cart.html\")","","","def add_to_cart(request, id):","    \"\"\"Add a quantity of the specified product to the cart\"\"\"","    quantity = int(request.POST.get('quantity'))","","    cart = request.session.get('cart', {})","    if id in cart:","        cart[id] = int(cart[id]) + quantity      ","    else:","        cart[id] = cart.get(id, quantity) ","","    request.session['cart'] = cart","    return redirect(reverse('index'))","","","def adjust_cart(request, id):","    \"\"\"","    Adjust the quantity of the specified product to the specified","    amount","    \"\"\"","    quantity = int(request.POST.get('quantity'))","    cart = request.session.get('cart', {})","","    if quantity > 0:","        cart[id] = quantity","    else:","        cart.pop(id)","    ","    request.session['cart'] = cart","    return redirect(reverse('view_cart'))"],"id":2},{"start":{"row":0,"column":0},"end":{"row":37,"column":41},"action":"insert","lines":["from django.shortcuts import render, redirect, reverse","","# Create your views here.","def view_cart(request):","    \"\"\"A View that renders the cart contents page\"\"\"","    return render(request, \"cart.html\")","","","def add_to_cart(request, id):","    \"\"\"Add a quantity of the specified product to the cart\"\"\"","    quantity = int(request.POST.get('quantity'))","","    cart = request.session.get('cart', {})","    if id in cart:","        cart[id] = int(cart[id]) + quantity      ","    else:","        cart[id] = cart.get(id, quantity) ","","    request.session['cart'] = cart","    return redirect(reverse('index'))","","","def adjust_cart(request, id):","    \"\"\"","    Adjust the quantity of the specified product to the specified","    amount","    \"\"\"","    print(request.POST)","    quantity = int(request.POST.get('quantity'))","    cart = request.session.get('cart', {})","","    if quantity > 0:","        cart[id] = quantity","    else:","        cart.pop(id)","    ","    request.session['cart'] = cart","    return redirect(reverse('view_cart'))"]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":37,"column":41},"end":{"row":37,"column":41},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":2,"state":"start","mode":"ace/mode/python"}},"timestamp":1564147664783,"hash":"a11f65175617403ff24b9c749b723ea6b0bd7808"}