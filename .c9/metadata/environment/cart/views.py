{"filter":false,"title":"views.py","tooltip":"/cart/views.py","undoManager":{"mark":2,"position":2,"stack":[[{"start":{"row":0,"column":0},"end":{"row":2,"column":25},"action":"remove","lines":["from django.shortcuts import render","","# Create your views here."],"id":2},{"start":{"row":0,"column":0},"end":{"row":33,"column":41},"action":"insert","lines":["from django.shortcuts import render, redirect, reverse","","# Create your views here.","def view_cart(request):","    \"\"\"A View that renders the cart contents page\"\"\"","    return render(request, \"cart.html\")","","","def add_to_cart(request, id):","    \"\"\"Add a quantity of the specified product to the cart\"\"\"","    quantity = int(request.POST.get('quantity'))","","    cart = request.session.get('cart', {})","    cart[id] = cart.get(id, quantity)","","    request.session['cart'] = cart","    return redirect(reverse('index'))","","","def adjust_cart(request, id):","    \"\"\"","    Adjust the quantity of the specified product to the specified","    amount","    \"\"\"","    quantity = int(request.POST.get('quantity'))","    cart = request.session.get('cart', {})","","    if quantity > 0:","        cart[id] = quantity","    else:","        cart.pop(id)","    ","    request.session['cart'] = cart","    return redirect(reverse('view_cart'))"]}],[{"start":{"row":0,"column":0},"end":{"row":34,"column":0},"action":"remove","lines":["from django.shortcuts import render, redirect, reverse","","# Create your views here.","def view_cart(request):","    \"\"\"A View that renders the cart contents page\"\"\"","    return render(request, \"cart.html\")","","","def add_to_cart(request, id):","    \"\"\"Add a quantity of the specified product to the cart\"\"\"","    quantity = int(request.POST.get('quantity'))","","    cart = request.session.get('cart', {})","    cart[id] = cart.get(id, quantity)","","    request.session['cart'] = cart","    return redirect(reverse('index'))","","","def adjust_cart(request, id):","    \"\"\"","    Adjust the quantity of the specified product to the specified","    amount","    \"\"\"","    quantity = int(request.POST.get('quantity'))","    cart = request.session.get('cart', {})","","    if quantity > 0:","        cart[id] = quantity","    else:","        cart.pop(id)","    ","    request.session['cart'] = cart","    return redirect(reverse('view_cart'))",""],"id":3},{"start":{"row":0,"column":0},"end":{"row":33,"column":41},"action":"insert","lines":["from django.shortcuts import render, redirect, reverse","","# Create your views here.","def view_cart(request):","    \"\"\"A View that renders the cart contents page\"\"\"","    return render(request, \"cart.html\")","","","def add_to_cart(request, id):","    \"\"\"Add a quantity of the specified product to the cart\"\"\"","    quantity = int(request.POST.get('quantity'))","","    cart = request.session.get('cart', {})","    cart[id] = cart.get(id, quantity)","","    request.session['cart'] = cart","    return redirect(reverse('index'))","","","def adjust_cart(request, id):","    \"\"\"","    Adjust the quantity of the specified product to the specified","    amount","    \"\"\"","    quantity = int(request.POST.get('quantity'))","    cart = request.session.get('cart', {})","","    if quantity > 0:","        cart[id] = quantity","    else:","        cart.pop(id)","    ","    request.session['cart'] = cart","    return redirect(reverse('view_cart'))"]}],[{"start":{"row":0,"column":0},"end":{"row":33,"column":41},"action":"remove","lines":["from django.shortcuts import render, redirect, reverse","","# Create your views here.","def view_cart(request):","    \"\"\"A View that renders the cart contents page\"\"\"","    return render(request, \"cart.html\")","","","def add_to_cart(request, id):","    \"\"\"Add a quantity of the specified product to the cart\"\"\"","    quantity = int(request.POST.get('quantity'))","","    cart = request.session.get('cart', {})","    cart[id] = cart.get(id, quantity)","","    request.session['cart'] = cart","    return redirect(reverse('index'))","","","def adjust_cart(request, id):","    \"\"\"","    Adjust the quantity of the specified product to the specified","    amount","    \"\"\"","    quantity = int(request.POST.get('quantity'))","    cart = request.session.get('cart', {})","","    if quantity > 0:","        cart[id] = quantity","    else:","        cart.pop(id)","    ","    request.session['cart'] = cart","    return redirect(reverse('view_cart'))"],"id":4},{"start":{"row":0,"column":0},"end":{"row":36,"column":41},"action":"insert","lines":["from django.shortcuts import render, redirect, reverse","","# Create your views here.","def view_cart(request):","    \"\"\"A View that renders the cart contents page\"\"\"","    return render(request, \"cart.html\")","","","def add_to_cart(request, id):","    \"\"\"Add a quantity of the specified product to the cart\"\"\"","    quantity = int(request.POST.get('quantity'))","","    cart = request.session.get('cart', {})","    if id in cart:","        cart[id] = int(cart[id]) + quantity      ","    else:","        cart[id] = cart.get(id, quantity) ","","    request.session['cart'] = cart","    return redirect(reverse('index'))","","","def adjust_cart(request, id):","    \"\"\"","    Adjust the quantity of the specified product to the specified","    amount","    \"\"\"","    quantity = int(request.POST.get('quantity'))","    cart = request.session.get('cart', {})","","    if quantity > 0:","        cart[id] = quantity","    else:","        cart.pop(id)","    ","    request.session['cart'] = cart","    return redirect(reverse('view_cart'))"]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":36,"column":41},"end":{"row":36,"column":41},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1564064633627,"hash":"d3326822f6f632505cd9e2150b073d8e2e0e7df5"}