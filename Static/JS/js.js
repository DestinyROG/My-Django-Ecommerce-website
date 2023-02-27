function increment(){
    var a=parseInt(document.getElementById(' qty-box').value)
    if(parseInt(document.getElementById('hid-qty').value)>a){
        document.getElementById(' qty-box').value=a+1
    }
}

function decrement(){
    var a=parseInt(document.getElementById(' qty-box').value)
    if(a>1){
        document.getElementById(' qty-box').value=a-1
    }
}

function addtocart(){
    var  a=parseInt(document.getElementById(' qty-box').value)
    document.getElementById('add-to-cart').href=`/addToCart/${document.getElementById('cate').value}/${document.getElementById('name').value}/${a}`
}

function incrementc(){
    a=document.activeElement.id;
    hidQty=parseInt(document.getElementById('hid-qty'+a).value);
    qty=parseInt(document.getElementById('qty'+a).value);
    prod_id=document.getElementById('prod_id'+a).value;
    token=document.getElementsByName('csrfmiddlewaretoken')[parseInt(a)+1].value;
    if(qty<hidQty){
        document.getElementById('qty'+a).value=qty+1
        data= new FormData()
        data.append('prod_id',prod_id)
        data.append('qty',qty+1)
        data.append('csrfmiddlewaretoken',token)
        fetch("/update-cart",{
            method: "POST",
            body: data,
        })
    }
}

function decrementc(){
    a=document.activeElement.id
    hidQty=parseInt(document.getElementById('hid-qty'+a).value);
    qty=parseInt(document.getElementById('qty'+a).value);
    prod_id=document.getElementById('prod_id'+a).value;
    token=document.getElementsByName('csrfmiddlewaretoken')[0].value;
    if(qty>1){
        document.getElementById('qty'+a).value=qty-1
        data= new FormData()
        data.append('qty',qty-1)
        data.append('prod_id',prod_id)
        data.append('csrfmiddlewaretoken',token)
        fetch('/update-cart',{
            method:'POST',
            body:data,
        })
    }
}


function remove() {
    a=document.activeElement.classList[2].slice(6,)
    prod_id=document.getElementById('prod_id'+a).value
    token=document.getElementsByName('csrfmiddlewaretoken')[0].value
    data= new FormData()
    data.append('prod_id',prod_id)
    data.append('csrfmiddlewaretoken',token)
    fetch('/remove',{
        method:"POST",
        body:data,
    })
    $('#mycart').load(location.href + ' #mycart')
}




function resistration(){
    first_name=document.getElementById('first_name').value
    last_name=document.getElementById('last_name').value
    username=document.getElementById('username').value
    email=document.getElementById('email').value
    password1=document.getElementById('password1').value
    password2=document.getElementById('password2').value
    token=document.getElementsByName('csrfmiddlewaretoken')[0].value 
    $.ajax({
        method:"POST",
        url:"/account/resister",
        data:{
            'csrfmiddlewaretoken':token,
            'password2':password2,
            'password1':password1,
            'email':email,
            'username':username,
            'last_name':last_name,
            'first_name':first_name,
        },
        success: function(response){
            alertify.set('notifier','position', 'top-left')
            alertify.success(response.Status)
        }
    })
    return false
}

function addtowishlist(){
    id=document.getElementById('id').value
    token= document.getElementsByName('csrfmiddlewaretoken')[0].value
    $.ajax({
        method: "POST",
        url:"/wishlist",
        data:{
            'csrfmiddlewaretoken':token,
            'id':id,
        },
        success: function(response){
            alertify.set('notifier','position', 'top-left')
            alertify.success(response.Status)
            check=response.checked
            if(check==0){
                $('#wishlisted').empty()
                $('#wishlisted').append(
                    `Wishlisted <i style="color: yellow;" class="fa fa-heart"></i>`
                    )
            }
            else{
                $('#wishlisted').empty()                   
                $('#wishlisted').append(
                    `Add to wishlist <i class="fa fa-heart"></i>`
                )
            }
        }
    })
    $('#wishlist-body').load(location.href + ' #wishlist-body')
}


function wishlistcolor(){
    category=document.getElementById('category').value
    nam=document.getElementById('name')
    fetch('/collections/category/name')
}

function removewishlist(){
    a=document.activeElement.id
    id=document.getElementById('id'+1).value
    token= document.getElementsByName('csrfmiddlewaretoken')[0].value
    $.ajax({
        method:"POST",
        url:'/removewishlist',
        data:{
            'id':id,
            'csrfmiddlewaretoken':token,
        }
    })
    $('#wishlist-body').load(location.href + ' #wishlist-body')
}